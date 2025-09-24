from typing import Any, Mapping

import pyarrow as pa
from chalk.features import Underscore
from chalk.features._encoding.pyarrow import rich_to_pyarrow
from chalk.features.underscore import UnderscoreAttr, UnderscoreCall, UnderscoreCast, UnderscoreFunction, UnderscoreRoot

from chalkdf.libchalk.chalkfunction import DataFrameParameterType
from chalkdf.libchalk.chalktable import AggExpr, AggregationFn, Expr
from chalkdf.libchalk.udf import BlockingCallChalkFunctionImpl, DirectChalkFunctionImpl

from .__HACK__arrow_type_promotion import cast_elements_to_arrow_type
from .__HACK__chalk_function_registry import get_chalk_function_registry_overload, is_aggregate_function
from .__HACK__chalk_overload import (
    ChalkFunctionOverloadFailed,
    ChalkFunctionOverloadResolved,
    SagemakerPredictBlockingFunctionPlaceholder,
)
from .__HACK__maybe_named_collection import MaybeNamedCollection


def convert_underscore_to_agg_expr(u: AggExpr | Underscore, schema: Mapping[str, pa.DataType]) -> AggExpr:
    if isinstance(u, AggExpr):
        return u

    if isinstance(u, UnderscoreCall):
        if isinstance(parent := u._chalk__parent, UnderscoreAttr):
            assert isinstance(parent, UnderscoreAttr), "pyright"
            fn_name = parent._chalk__attr

            # Special case - handle alias syntax
            if fn_name == "alias":
                parent_agg_expr = convert_underscore_to_agg_expr(parent._chalk__parent, schema)
                if len(u._chalk__args) != 1:
                    raise ValueError("alias() must be called with one argument")
                if not isinstance(alias := u._chalk__args[0], str):
                    raise ValueError("argument to alias() must be a string")
                return AggExpr.alias(parent_agg_expr, alias)

            if fn_name == "approx_percentile":
                parent_agg_expr = convert_underscore_to_expr(parent._chalk__parent, schema)
                if len(u._chalk__args) != 1 and "quantile" not in u._chalk__kwargs:
                    raise ValueError("approx_percentile must be called with the quantile argument")
                raw_kwargs = u._chalk__kwargs if len(u._chalk__args) == 0 else {"quantile": u._chalk__args[0]}
                return _resolve_agg_function(fn_name, converted_args=[parent_agg_expr], raw_kwargs=raw_kwargs)

            # Handle all aggregation functions
            if not is_aggregate_function(fn_name):
                raise ValueError(f"aggregation function '{fn_name}' does not exist")
            converted_args = [
                convert_underscore_to_expr(arg, schema) for arg in [parent._chalk__parent, *u._chalk__args]
            ]
            return _resolve_agg_function(fn_name, converted_args=converted_args, raw_kwargs=u._chalk__kwargs)
        else:
            raise ValueError(f"unexpected call signature: {u}")

    if isinstance(u, UnderscoreFunction):
        if not is_aggregate_function(u._chalk__function_name):
            raise ValueError(f"aggregation function '{u._chalk__function_name}' does not exist")
        converted_args: list[Expr] = [convert_underscore_to_expr(arg, schema) for arg in u._chalk__args]
        return _resolve_agg_function(u._chalk__function_name, converted_args=converted_args, raw_kwargs={})


def convert_underscore_to_expr(u: Any, schema: Mapping[str, pa.DataType]) -> Expr:
    if isinstance(u, Expr):
        # Allow for mixing of expressions and underscores
        return u

    if not isinstance(u, Underscore):
        return Expr.lit(_infer_pa_scalar(u))

    if isinstance(u, UnderscoreCast):
        value_expr = convert_underscore_to_expr(u._chalk__value, schema)
        return Expr.cast(value_expr, u._chalk__to_type)

    if isinstance(u, UnderscoreAttr):
        parent = u._chalk__parent
        attr = u._chalk__attr
        if isinstance(parent, UnderscoreRoot):
            if attr not in schema:
                raise ValueError(f"no column '{attr}' found in table with columns '{list(schema.keys())}'")
            return Expr.column(attr, schema[attr])

        # Struct subfield
        parent_expr = convert_underscore_to_expr(parent, schema)
        if not isinstance(parent_expr.dtype, pa.StructType):
            raise ValueError(f"cannot get struct field '{attr}' from non-struct expression '{parent}'")
        if attr not in [field.name for field in parent_expr.dtype]:
            raise ValueError(f"field '{attr}' does not exist on struct with type {parent_expr.dtype}")
        return parent_expr.get_struct_subfield(attr)

    if isinstance(u, UnderscoreCall):
        raise ValueError(f"unexpected aggregation expression '{u}'")

    if isinstance(u, UnderscoreFunction):
        if is_aggregate_function(u._chalk__function_name):
            raise ValueError(f"unexpected aggregation function '{u._chalk__function_name}'")
        converted_args: list[Expr] = [convert_underscore_to_expr(arg, schema) for arg in u._chalk__args]
        converted_kwargs: Mapping[str, Expr] = {
            name: convert_underscore_to_expr(kwarg, schema) for name, kwarg in u._chalk__kwargs.items()
        }

        if u._chalk__function_name == "struct_pack":
            if len(u._chalk__args) == 0:
                raise ValueError("invalid call to F.struct_pack: no arguments provided")
            struct_names = u._chalk__args[0]
            struct_values = converted_args[1:]
            struct_names_typed = [name for name in struct_names if isinstance(name, str)]  # pyright: ignore[reportUnknownVariableType]
            if len(struct_names_typed) != len(struct_names):  # pyright: ignore[reportUnknownArgumentType]
                raise ValueError("All field names in struct_pack must be constant strings")
            if len(struct_names_typed) != len(struct_values):
                raise ValueError("The number of field names in struct_pack must match the number of values")
            return Expr.struct_pack(struct_names_typed, struct_values)

        return _resolve_scalar_function(
            u._chalk__function_name, converted_args=converted_args, converted_kwargs=converted_kwargs
        )

    raise NotImplementedError(f"{type(u)} is not yet supported for chalkdf")


# Helpers
def _bind_agg_fn(
    libchalk_fn_name: str, chalk_fn_name: str, promoted_operands: list[Expr], agg_options: dict[str, Any]
) -> AggExpr:
    if (
        len(promoted_operands) == 1
        and len(agg_options) == 0
        and (agg_fn := getattr(AggregationFn, libchalk_fn_name.upper(), None))
    ):
        # this handles any simple aggs that aren't explicity exposed in the pybind
        return promoted_operands[0].agg(agg_fn)
    elif len(promoted_operands) != 0:
        bound_agg = getattr(promoted_operands[0], libchalk_fn_name, None)
        if bound_agg is None:
            raise ValueError(
                f"There is no Velox aggregation registered with name '{libchalk_fn_name}' for the Chalk operation '{chalk_fn_name}'"
            )
        return bound_agg(*promoted_operands[1:], **agg_options)
    raise ValueError("Aggregation function must be called on a column")


def _bind_scalar_fn(
    libchalk_fn_name: str,
    chalk_fn_name: str,
    promoted_operands: list[Expr],
    promoted_kwargs: dict[str, Expr],
    resolved_overload: ChalkFunctionOverloadResolved,
) -> Expr:
    if len(promoted_operands) > 0:
        bound_function = getattr(promoted_operands[0], libchalk_fn_name, None)
        if bound_function is None:
            raise ValueError(
                f"There is no Velox function registered with name '{libchalk_fn_name}' for the Chalk operation '{chalk_fn_name}'"
            )

        called_with = (
            [promoted_operands[1:]]
            if resolved_overload.pybind_method_pack_arguments
            else promoted_operands[1:]
            if resolved_overload.pybind_is_method
            else promoted_operands
        )
        call_expression = bound_function(*called_with, **promoted_kwargs)

        # HACK HACK HACK - bytes-to-string (hex) needs to be lowercased
        if libchalk_fn_name == "to_hex":
            call_expression = call_expression.result.lower(call_expression.result)
        return call_expression
    else:
        bound_function = getattr(Expr, chalk_fn_name, None)
        if bound_function is None:
            raise ValueError(
                f"There is no Velox function registered with name '{libchalk_fn_name}' for the Chalk operation '{chalk_fn_name}'"
            )
        return bound_function(*promoted_operands)


def _resolve_agg_function(function_name: str, *, converted_args: list[Expr], raw_kwargs: dict[str, Any]) -> AggExpr:
    positional_items = [expr.dtype for expr in converted_args]
    positional_items[0] = DataFrameParameterType(columns={"series": positional_items[0]})
    overload = get_chalk_function_registry_overload(
        function_name=function_name,
        input_types=MaybeNamedCollection(
            positional_items=positional_items,
            named_items={},  # Aggregates like approx_top_k and approx_percentile don't use these named_items. I DON'T LIKE THIS AT ALL
        ),
    )
    if overload is None:
        raise ValueError(f"unknown chalk aggregation function '{function_name}'")
    if isinstance(overload, ChalkFunctionOverloadFailed):
        raise ValueError(overload.failure_message)

    argument_target_types = overload.input_promotion_target_types.positional_items
    if overload.cast_input_types_before_executing is not None:
        argument_target_types = overload.cast_input_types_before_executing

    promoted_operands = cast_elements_to_arrow_type(
        types=converted_args,
        target_types=argument_target_types,
        cast_fn=Expr.cast,
        extract_dtype=lambda e: e.dtype,
        lit=lambda val, typ: Expr.lit(pa.scalar(val, typ)),
    )

    if not isinstance(overload.pybind_function, str):
        raise NotImplementedError(f"{overload.pybind_function} not supported")

    return _bind_agg_fn(overload.pybind_function, function_name, promoted_operands, agg_options=raw_kwargs)


def _resolve_scalar_function(function_name: str, *, converted_args: list[Expr], converted_kwargs: Mapping[str, Expr]):
    positional_items = [expr.dtype for expr in converted_args]
    overload = get_chalk_function_registry_overload(
        function_name=function_name,
        input_types=MaybeNamedCollection(
            positional_items=positional_items,
            named_items={name: expr.dtype for name, expr in converted_kwargs.items()},
        ),
    )
    if overload is None:
        raise ValueError(f"unknown chalk function '{function_name}'")
    if isinstance(overload, ChalkFunctionOverloadFailed):
        raise ValueError(overload.failure_message)

    argument_target_types = overload.input_promotion_target_types.positional_items
    if overload.cast_input_types_before_executing is not None:
        argument_target_types = overload.cast_input_types_before_executing

    promoted_operands = cast_elements_to_arrow_type(
        types=converted_args,
        target_types=argument_target_types,
        cast_fn=Expr.cast,
        extract_dtype=lambda e: e.dtype,
        lit=lambda val, typ: Expr.lit(pa.scalar(val, typ)),
    )
    named_target_types = overload.input_promotion_target_types.named_items
    promoted_kwargs = dict(
        zip(
            named_target_types.keys(),
            cast_elements_to_arrow_type(
                types=[converted_kwargs[name] for name in named_target_types],
                target_types=[overload.input_promotion_target_types.named_items[name] for name in named_target_types],
                cast_fn=Expr.cast,
                extract_dtype=lambda e: e.dtype,
                lit=lambda val, typ: Expr.lit(pa.scalar(val, typ)),
            ),
        )
    )

    if isinstance(overload.pybind_function, str):
        libchalk_fn_name = overload.pybind_function
    elif isinstance(
        overload.pybind_function,
        (DirectChalkFunctionImpl, BlockingCallChalkFunctionImpl, SagemakerPredictBlockingFunctionPlaceholder),
    ):
        libchalk_fn_name = overload.pybind_function.get_name()
    else:
        raise NotImplementedError(f"{overload.pybind_function} not supported")

    return _bind_scalar_fn(libchalk_fn_name, function_name, promoted_operands, promoted_kwargs, overload)


# Copied from `convert_chalkpy_underscore.py`
def _infer_pa_scalar(obj: object) -> pa.Scalar:
    """
    Construct a pyarrow scalar from a Python value.
    Manual conversion here because:
    (1) when obj is a dict, pa.scalar(obj) returns a struct by default instead of a map
    (2) Chalk function registry has preferences defined by rich_to_pyarrow
    """
    try:
        if isinstance(obj, dict):
            key_val = rich_to_pyarrow(type(next(iter(obj))), "key")
            for v in obj.values():
                if v is not None:
                    value_type = _infer_pa_scalar(v).type
                    return pa.scalar(obj, type=pa.map_(key_val, value_type))
            return pa.scalar(obj, type=pa.map_(key_val, pa.null()))
        elif isinstance(obj, (list, set, frozenset, tuple)):
            for v in obj:
                if v is not None:
                    value_type = _infer_pa_scalar(v).type
                    return pa.scalar(obj, type=pa.large_list(value_type))
            return pa.scalar(obj, type=pa.large_list(pa.null()))
        else:
            return pa.scalar(obj, type=rich_to_pyarrow(type(obj), "python_type"))
    except Exception:
        return pa.scalar(obj)
