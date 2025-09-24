from __future__ import annotations

import dataclasses
from collections import defaultdict
from dataclasses import dataclass
from functools import reduce
from typing import Any, Callable, Mapping, Sequence, TypeVar

import pyarrow as pa
from chalk.utils.collections import OrderedSet

from chalkdf.libchalk.chalkfunction import (
    GENERIC_SIGIL,
    ArgumentType,
    CallbackType,
    ParameterType,
    UnassignedGenericType,
    UnorderableGenericType,
    VariadicType,
    default_arrow_type_promoter,
    format_type,
    replace_generic_types,
    unify_generic,
)
from chalkdf.libchalk.chalkfunction import (
    make_generic as generic,
)
from chalkdf.libchalk.udf import ChalkFunctionImplementation as LibChalkFunctionImplementation

from .__HACK__arrow_type_promotion import (
    can_promote_by_casting,
)
from .__HACK__maybe_named_collection import MaybeNamedCollection, MaybeNamedCollectionBuilder

TItem = TypeVar("TItem")
TOther = TypeVar("TOther")


class SagemakerPredictBlockingFunctionPlaceholder:
    # Placeholder to represent the SagemakerPredictBlockingFunction in pybind function, without explicitly instantiating
    # a whole BlockingFunction (non-trivial cost as it creates a Sagemaker client).
    def __init__(self):
        super().__init__()

    def get_name(self) -> str:
        return "sagemaker_predict"


TPybindFunction = LibChalkFunctionImplementation | str | None | SagemakerPredictBlockingFunctionPlaceholder


class _UnassignedGenericType(ValueError):
    """
    This error is raised when attempting to instantiate a generic type signature, and one or more
    generic types have no corresponding value.
    """

    def __init__(self, generic_name: str):
        self.generic_name = generic_name
        super().__init__(f"The generic type parameter '{generic_name}' could not be determined")


class _UnorderableGenericType(ValueError):
    """
    This error is raised when attempting to instantiate an orderable generic type, and the
    underlying type does not support comparison operators
    """

    def __init__(self, generic_name: str, assigned_type: pa.DataType):
        self.generic_name = generic_name
        super().__init__(
            f"The orderable generic type parameter '{GENERIC_SIGIL}{generic_name}' could not be mapped onto non-orderable type '{assigned_type}'"
        )


def _replace_generic_types(
    t: ArgumentType,
    *,
    mapping: Mapping[str, pa.DataType],
    fallback: Callable[[str], pa.DataType] | None,
) -> ArgumentType:
    """
    Wrapper around C++ version of this function, to convert return status to exception.

    This will go away when overload resolution moves into C++.
    """
    match result := replace_generic_types(t, mapping=mapping, fallback=fallback):
        case UnassignedGenericType(generic_name=generic_name):
            raise _UnassignedGenericType(generic_name=generic_name)
        case UnorderableGenericType(generic_name=generic_name, assigned_type=assigned_type):
            raise _UnorderableGenericType(generic_name=generic_name, assigned_type=assigned_type)
        case _:
            return result


@dataclass(kw_only=True, frozen=True)
class ChalkFunctionOverloadResolved:
    function_name: str
    """
    Original chalk function name
    """

    output_type: pa.DataType
    """
    The (scalar) output type of this overload.
    """

    input_promotion_target_types: MaybeNamedCollection[ArgumentType]
    """
    The (scalar) input types for this overload.
    Note that these might be different from the original `input_types` provided
    by the caller of `get_resolved_overload()`: if they are different, the caller
    is responsible for promoting each argument to the corresponding provided type
    before calling this function.

    For example, (+) may have an overload `float64 * float64 -> float64`.
    If the caller provides `(int32, float64)`, then the promotion types for this
    overload would be `(float64, float64)` and the caller would be required to
    promote the left argument from `int32` to `float64`.
    """

    python_fallback: Callable[..., Any] | None

    pybind_function: TPybindFunction
    """
    The name of the Velox function to call when statically compiled.
    This can be different from the original Chalk function name.
    """

    pybind_is_method: bool
    pybind_method_pack_arguments: bool

    cast_input_types_before_executing: tuple[pa.DataType, ...] | None
    """
    If `cast_input_types_before_executing` is present, then each input argument must be cast to the
    corresponding target type before the function is called.

    This is because the underlying function registration only supports the cast target as a value,
    instead of the original type.

    For example, Velox has an overload `round(float64, int32) -> float64`, but we want to support
    the call `round(float64, int64)`, so this overload specifies
    ```
    cast_input_types_before_executing = [pa.float64(), pa.int32()]
    ```
    for this overload, which casts the second parameter from `int64` to `int32`.
    """

    cast_output_type_from: pa.DataType | None
    """
    If `cast_output_type_from` is present, then the underlying Velox function actually returns a
    value of type `cast_output_type_from`, which must be cast to the declared `output_type`.

    For example, if Velox had a function `round_to_int: float32 -> int64` but we wanted to alter
    the return type to be `float32 -> float32`, then we could define the overload as `float32 -> float32`
    with `cast_output_type_from = int64()`.
    """

    description: str | None
    """
    A brief description of what this function overload does.
    """

    convert_input_errors_to_none: bool
    """
    Used only in the `recover` function to recover from an upstream failure
    """


@dataclass(kw_only=True, frozen=True)
class ChalkFunctionOverloadFailed:
    failure_priority: int
    """
    If `failure_priority` is higher, then this erorr is more likely to be chosen when deciding
    which of the overloads to present to the user when erroring.
    """

    failure_message: str
    """
    A description of why the overload will not work.
    """


def _plural(
    count: int,
    item: str,
    *,
    irregular_plural: str | None = None,
) -> str:
    """
    Basic pluralization helper for error messages.
    """
    if count == 1:
        return item
    if irregular_plural:
        return irregular_plural
    return item + "s"


def _ordinal(index: int) -> str:
    index += 1
    if index % 10 == 1:
        return f"{index}st"
    if index % 10 == 2:
        return f"{index}nd"
    if index % 10 == 3:
        return f"{index}rd"
    return f"{index}th"


@dataclass(kw_only=True, frozen=True, slots=True)
class ChalkFunctionOverload:
    function_name: str
    """
    The name of the Chalk function.
    """

    description: str | None = None
    """
    A brief description of what this function overload does.
    """

    overload_generic_parameters: Sequence[ParameterType]
    """
    This is the exact type which this overload expects - in order to call this overload, all
    arguments must be promoted to exactly match these types.

    This type signature may also include generics and other special features, which means
    that callers MUST call `get_resolved_overload` in order to get correct types to promote.
    """

    overload_generic_return: pa.DataType
    """
    The is the (possibly-generic) output type for this overload.
    Do not access this directly - call `get_resolved_overload` instead.
    """

    overload_generic_named_parameters: Sequence[tuple[str, pa.DataType | CallbackType]] = dataclasses.field(
        default_factory=tuple
    )
    """
    These parameters MUST be matched to keyword arguments.
    """

    overload_force_cast_parameters: tuple[pa.DataType, ...] | None = None
    """
    If specified, forces argument values to be cast to this sequence before the function is called.
    Not available for variadic functions; cannot be generic.
    """

    overload_force_cast_output_from_velox_type: pa.DataType | None = None
    """
    If specified, then the *actual* result type of the function call with the (force-cast) parameters
    will be this type, which the caller should cast to the `overload_generic_return`.
    """

    pybind_function: TPybindFunction
    """
    This is how the function is exposed in the libchalk pybind layer.
    If `None`, the python planner won't know how to run this function using libchalk.
    It will run the python fallback instead for this function.
    """

    """
    By default, we'll assume the function is a static method
    E.g. Expr.function(arg0, arg1, ...)
    """
    pybind_is_method: bool = False
    """
    If `True`, then the Velox function is a method on the first argument,
    and the first argument should not be passed as a separate argument.
    E.g. arg0.function(arg1, arg2, ...).
    """
    pybind_method_pack_arguments: bool = False
    """
    If `True`, then the Velox function is a method on the first argument,
    the other arguments should be passed as a list.
    E.g. arg0.function([arg1, arg2, ...]).
    """

    convert_input_errors_to_none: bool = False
    """
    Used only in the `recover` function to recover from an upstream failure
    """

    variadic_parameter: VariadicType | None = dataclasses.field(init=False, default=None)
    python_fallback: Callable[..., Any] | None = None

    def __post_init__(self):
        last_index = len(self.overload_generic_parameters) - 1
        for index, overload_parameter in enumerate(self.overload_generic_parameters):
            if isinstance(overload_parameter, VariadicType):
                if index != last_index:
                    raise ValueError(f"VariadicType must be the last parameter in the overload signature: {self}")
                object.__setattr__(self, "variadic_parameter", overload_parameter)

    def formatted_overload(self) -> str:
        parameters_str = ", ".join(format_type(p) for p in self.overload_generic_parameters)
        return_str = format_type(self.overload_generic_return)
        return f"{self.function_name}({parameters_str}) -> {return_str}"

    def get_resolved_overload(
        self,
        input_types: MaybeNamedCollection[ArgumentType],
    ) -> ChalkFunctionOverloadResolved | ChalkFunctionOverloadFailed:
        """
        Returns `ChalkFunctionOverloadFailed` if the overload does not match, with an error message explaining why.
        The object includes a priority, which can be used to choose the closest-matching overload when deciding
        which error to show to the user.

        If this function is concrete (i.e. non-generic) then checks that:
        (1) The number of provided `input_types` matches the expected number of inputs. If the function
            is variadic, the last input type is repeated to match the number of provided inputs.
        (2) Checks that each input type can be promoted to the corresponding parameter type
        (3) Returns the overload

        If the overload is generic, then additional steps are required:
        (1.1) Attempt to unify the generic parameter types with the provided input types.
        - If two complex types match, recursively compare their parts (e.g. compare `list[A]` against `list[B]`
          by comparing `A` against `B`).
        - When comparing a generic parameter type `$T` against any input type `X`, add `$T = X` as a possible
          constraint.
        - When types with invalid structures appear, like passing a `list[T]` where a `map[K, V]` is expected,
          no error occurs in this step in order to try to infer as many of the generic types as possible. This
          makes the error message much clearer.
        (1.2) For each generic type `$T`, check all the constraint types - exactly one of them must be a
              legal promotion target from all the other constraints found. If not, raise an error.
        (3.1) Replace any generic parameter types in the input/output overload before returning it.
        """

        # Replace the variadic types up-front with the elem type to line up with the number of input_types
        non_variadic_parameters = [p for p in self.overload_generic_parameters if not isinstance(p, VariadicType)]

        if len(input_types.positional_items) == len(non_variadic_parameters):
            # Variadic parameters are 0 or more, so they can be skipped.
            overload_generic_parameters = non_variadic_parameters
        elif self.variadic_parameter and len(input_types.positional_items) > len(non_variadic_parameters):
            # There are more input types than parameters, so the last parameter is variadic,
            # and should be repeated to match the number of input types.
            overload_generic_parameters = non_variadic_parameters + [self.variadic_parameter.element_type] * (
                len(input_types.positional_items) - len(non_variadic_parameters)
            )
        else:
            return ChalkFunctionOverloadFailed(
                failure_priority=100,
                failure_message=(
                    f"wrong number of inputs to function '{self.function_name}': "
                    f"the function is called with {len(input_types.positional_items)} {_plural(len(input_types.positional_items), 'input')} "
                    f"but we wanted {len(self.overload_generic_parameters)} {_plural(len(self.overload_generic_parameters), 'input')}"
                ),
            )
        # overload_generic_parameters = list(map(lambda p: p.element_type if isinstance(p, HasManyColumnType) else p, overload_generic_parameters))

        if set(input_types.named_items) != set(name for name, _ in self.overload_generic_named_parameters):
            return ChalkFunctionOverloadFailed(
                failure_priority=100,
                failure_message=(
                    f"Wrong keyword arguments to function '{self.function_name}': "
                    f"the function is called with named inputs '{', '.join(input_types.named_items)}' "
                    f"but we wanted '{', '.join(name for name, _ in self.overload_generic_named_parameters)}'"
                ),
            )
        overload_generic_parameter_collection = MaybeNamedCollection(
            positional_items=overload_generic_parameters,
            named_items=dict(self.overload_generic_named_parameters),
        )

        # First, if any of the input parameter types are generic, then we need to infer the generic parameters.
        generic_parameter_constraints = defaultdict[str, OrderedSet[pa.DataType]](OrderedSet[pa.DataType])

        for _, (generic_param_type, input_type) in overload_generic_parameter_collection.zip(input_types).enumerate():
            unified = unify_generic(generic_type=generic_param_type, input_type=input_type)
            for generic_name, generic_constraint in unified:
                generic_parameter_constraints[generic_name].add(generic_constraint)

        # Attempt to assign a value to each generic parameter.
        # TODO: enforce that there must be a unique "maximal" constraint type for each variable, otherwise it is ambiguous or invalid.
        # Currently, there are no ambiguous constraint types, but the `lca_promoting_type` does not let us know if there exist
        # multiple data types that are least common ancestors
        generic_assignments: dict[str, pa.DataType] = {}
        for generic_name, constraint_types in generic_parameter_constraints.items():
            if len(constraint_types) == 0:
                generic_lca_type = None
            else:
                generic_lca_type = reduce(
                    lambda t1, t2: None
                    if (t1 is None or t2 is None)
                    else default_arrow_type_promoter.lca_promoting_type(t1, t2),
                    constraint_types,
                )

            if generic_lca_type is None:
                # This generic parameter is unknown, because it has no candidates or too many.
                # We cannot determine the value for this parameter, because none of the types can be converted to
                # the other values.

                if self.function_name.upper() == self.function_name.lower():
                    # This is an operator, like "+" or "==".
                    display_function_name: str = f"operator '{self.function_name}'"
                else:
                    display_function_name = f"function '{self.function_name}'"

                display_input_types: str = input_types.map(format_type).pprint()
                display_expected_input_types: str = overload_generic_parameter_collection.map(format_type).pprint()

                if len(constraint_types) == 0:
                    display_generic_complaint = (
                        f"The generic type '{GENERIC_SIGIL}{generic_name}' could not be determined."
                    )
                else:
                    # There are 2 or more candidates.
                    # target_constraint_types
                    display_candidates = " or ".join(f"'{format_type(t)}'" for t in constraint_types)
                    display_generic_complaint = (
                        f"The generic type '{GENERIC_SIGIL}{generic_name}' could not be determined.\n"
                        f"{GENERIC_SIGIL}{generic_name} could be any of {display_candidates}\n"
                        "but these types are not compatible with each other."
                    )

                return ChalkFunctionOverloadFailed(
                    failure_priority=250,
                    failure_message=(
                        f"Generic {display_function_name} cannot be called with input types {display_input_types}.\n"
                        f"Generic {display_function_name} expects input types {display_expected_input_types} where '{GENERIC_SIGIL}{generic_name}' is a generic type.\n"
                        f"{display_generic_complaint}\n"
                    ),
                )

            # There is only one target value, so use it for the assignment.
            generic_assignments[generic_name] = generic_lca_type

        failed_argument: tuple[int | str, ParameterType, ParameterType] | None = None
        matching_arguments = 0
        expected_arguments: MaybeNamedCollection[ArgumentType] = MaybeNamedCollectionBuilder()
        for param_identifier, (expect_generic_type, given_type) in overload_generic_parameter_collection.zip(
            input_types
        ).enumerate():
            # First, attempt to convert the generic type into a concrete type.
            try:
                expect_type = _replace_generic_types(
                    expect_generic_type,
                    mapping=generic_assignments,
                    fallback=None,
                )
            except _UnassignedGenericType:
                # This type could not be converted, because the generic type was not known.
                # Create a partially-instantiated placeholder to replace it.
                partially_instantiated_expect_type = _replace_generic_types(
                    expect_generic_type,
                    mapping=generic_assignments,
                    fallback=lambda name: generic(name),
                )

                if failed_argument is None:
                    failed_argument = (
                        param_identifier,
                        partially_instantiated_expect_type,
                        given_type,
                    )

                expected_arguments.add(param_identifier, partially_instantiated_expect_type)
                continue
            except _UnorderableGenericType as _unorderable_exc:
                failure_message = f"invalid inputs to function '{self.function_name}':\n{_unorderable_exc}"
                return ChalkFunctionOverloadFailed(
                    # If more arguments match, give a slightly higher score.
                    # This caps out at 10 because most functions don't have that many arguments,
                    # and we want to reserve the rest of the space for other priorities.
                    failure_priority=200,
                    failure_message=failure_message,
                )

            expected_arguments.add(param_identifier, expect_type)

            if can_promote_by_casting(src=given_type, target=expect_type):
                # Count the number of matching arguments in order to try to pick the right overload.
                matching_arguments += 1
            elif failed_argument is None:
                # Track the first failed argument.
                failed_argument = (param_identifier, expect_type, given_type)

        if failed_argument is not None:
            # The type does not match!
            param_identifier, expect_type, given_type = failed_argument
            if generic_assignments:
                failure_message = f"Generic overload '{self.formatted_overload()}' failed. "
            else:
                failure_message = f"Overload '{self.formatted_overload()}' failed. "

            if isinstance(param_identifier, int):
                input_type_description = f"The {_ordinal(param_identifier)} input type"
            else:
                input_type_description = f"The input type '{param_identifier}'"
            failure_message += (
                f"{input_type_description} is '{format_type(given_type)}'; expected '{format_type(expect_type)}'.\n"
                f"- received: '{input_types.map(format_type).pprint()}'\n"
                f"- expected: '{expected_arguments.map(format_type).pprint()}'"
            )

            return ChalkFunctionOverloadFailed(
                # If more arguments match, give a slightly higher score.
                # This caps out at 10 because most functions don't have that many arguments,
                # and we want to reserve the rest of the space for other priorities.
                failure_priority=200 + min(matching_arguments, 10),
                failure_message=failure_message,
            )

        try:
            overload_return = _replace_generic_types(
                self.overload_generic_return,
                mapping=generic_assignments,
                fallback=None,
            )
            if not isinstance(overload_return, pa.DataType):
                raise AssertionError("Expected _replace_generic_types to preserve types")
        except _UnassignedGenericType:
            failure_message = (
                f"mismatched inputs to function '{self.function_name}':\n"
                f"- received: '({input_types.map(format_type).pprint()})'\n"
                f"- expected: '({self.formatted_overload()})'"
            )
            return ChalkFunctionOverloadFailed(
                failure_priority=160,
                failure_message=failure_message,
            )

        # Every type matched or could be promoted to the corresponding target type, so return this overload.
        return ChalkFunctionOverloadResolved(
            function_name=self.function_name,
            input_promotion_target_types=expected_arguments,
            output_type=overload_return,
            python_fallback=self.python_fallback,
            pybind_function=self.pybind_function,
            pybind_is_method=self.pybind_is_method,
            cast_input_types_before_executing=self.overload_force_cast_parameters,
            cast_output_type_from=self.overload_force_cast_output_from_velox_type,
            pybind_method_pack_arguments=self.pybind_method_pack_arguments,
            description=self.description,
            convert_input_errors_to_none=self.convert_input_errors_to_none,
        )
