from __future__ import annotations

import typing
from dataclasses import dataclass
from typing import Any, Mapping, Optional, Sequence, TypeVar

import pyarrow as pa
import pyarrow.compute as pc
from chalk.features._encoding.http import HttpResponse
from chalk.features._encoding.pyarrow import rich_to_pyarrow
from chalk.prompts import MultimodalPromptResponse, PromptResponse
from chalk.utils.json import TJSON, pyarrow_json_type

from chalkdf.libchalk.chalkfunction import (
    ArgumentType,
    CallbackType,
    DataFrameParameterType,
    VariadicType,
)
from chalkdf.libchalk.chalkfunction import (
    make_generic as generic,
)
from chalkdf.libchalk.udf import (
    BlockingCallChalkFunctionImpl,
    DirectChalkFunctionImpl,
    HttpRequestBlockingFunction,
)
from chalkdf.libchalk.udf import ChalkFunctionOverloadFailed as LibChalkFunctionOverloadFailed
from chalkdf.libchalk.udf import ChalkFunctionOverloadResolved as LibChalkFunctionOverloadResolved

from .__HACK__arrow_type_promotion import (
    datetime_type,
    duration_type,
    most_precise_numeric_type_from_arrow,
    pa_date_types,
    pa_float_types,
    pa_int_types,
)
from .__HACK__chalk_overload import (
    ChalkFunctionOverload,
    ChalkFunctionOverloadFailed,
    ChalkFunctionOverloadResolved,
    SagemakerPredictBlockingFunctionPlaceholder,
)
from .__HACK__maybe_named_collection import MaybeNamedCollection

T = TypeVar("T")
V = TypeVar("V")


VELOX_ZIP_ARITIES = tuple(range(2, 8))

PA_LIST_TYPES = (pa.list_, pa.large_list)
PA_LARGEST_NUM_TYPES = (pa.int64(), pa.float64())

PA_STRING_TYPES = (pa.string(), pa.large_string())
PA_BINARY_TYPES = (pa.binary(), pa.large_binary())
PA_INT_TYPES = tuple(pa_int_types.values())
PA_FLOAT_TYPES = tuple(pa_float_types.values())
PA_NUM_TYPES = PA_INT_TYPES + PA_FLOAT_TYPES
PA_TIMESTAMP_TYPES = (datetime_type,)
PA_DURATION_TYPES = (duration_type,)
PA_DATE_TYPES = tuple(pa_date_types.values())

PA_NUM_AND_TIME_TYPES = PA_NUM_TYPES + PA_TIMESTAMP_TYPES + PA_DURATION_TYPES + PA_DATE_TYPES
PA_ALL_TYPES = (
    PA_NUM_TYPES
    + PA_STRING_TYPES
    + PA_BINARY_TYPES
    + PA_TIMESTAMP_TYPES
    + PA_DURATION_TYPES
    + PA_DATE_TYPES
    + (pyarrow_json_type(),)
)

BASE_FUNCTIONS = {
    "+": [
        *(
            ChalkFunctionOverload(
                function_name="+",
                description="basic binary + operation",
                overload_generic_parameters=[typ, typ],
                overload_generic_return=typ,
                pybind_function="__add__",
                pybind_is_method=True,
                python_fallback=None,
            )
            for typ in PA_NUM_TYPES + PA_DURATION_TYPES + PA_BINARY_TYPES + PA_STRING_TYPES
        ),
        *(
            ChalkFunctionOverload(
                function_name="+",
                description="date + duration addition",
                overload_generic_parameters=order,
                overload_generic_return=date_typ,
                pybind_function="__add__",
                pybind_is_method=True,
                python_fallback=None,
            )
            for date_typ in PA_DATE_TYPES + PA_TIMESTAMP_TYPES
            for duration_typ in PA_DURATION_TYPES
            for order in ([date_typ, duration_typ], [duration_typ, date_typ])
        ),
    ],
    "-": [
        *(
            ChalkFunctionOverload(
                function_name="-",
                description="basic binary - operation",
                overload_generic_parameters=[typ, typ],
                overload_generic_return=typ,
                pybind_function="__sub__",
                pybind_is_method=True,
                python_fallback=None,
            )
            for typ in PA_NUM_TYPES + PA_DURATION_TYPES
        ),
        *(
            ChalkFunctionOverload(
                function_name="-",
                description="date - duration subtraction",
                overload_generic_parameters=[date_typ, duration_typ],
                overload_generic_return=date_typ,
                pybind_function="__sub__",
                pybind_is_method=True,
                python_fallback=None,
            )
            for date_typ in PA_DATE_TYPES + PA_TIMESTAMP_TYPES
            for duration_typ in PA_DURATION_TYPES
        ),
        *(
            ChalkFunctionOverload(
                function_name="-",
                description="date(time) subtraction",
                overload_generic_parameters=[date_typ, date_typ],
                overload_generic_return=pa.duration("us"),
                pybind_function="__sub__",
                pybind_is_method=True,
                python_fallback=None,
            )
            for date_typ in PA_DATE_TYPES + PA_TIMESTAMP_TYPES
        ),
    ],
    "*": [
        *(
            ChalkFunctionOverload(
                function_name="*",
                description="basic binary * operation",
                overload_generic_parameters=[typ, typ],
                overload_generic_return=typ,
                pybind_function="__mul__",
                pybind_is_method=True,
                python_fallback=None,
            )
            for typ in PA_NUM_TYPES
        ),
        *(
            ChalkFunctionOverload(
                function_name="*",
                description="num * duration multiplication",
                overload_generic_parameters=order,
                overload_generic_return=duration_typ,
                pybind_function="__mul__",
                pybind_is_method=True,
                python_fallback=None,
            )
            for num_type in PA_LARGEST_NUM_TYPES
            for duration_typ in PA_DURATION_TYPES
            for order in ([num_type, duration_typ], [duration_typ, num_type])
        ),
    ],
    "/": [
        *(
            ChalkFunctionOverload(
                function_name="/",
                description="basic binary / operation",
                overload_generic_parameters=[typ, typ],
                overload_generic_return=pa.float64(),
                pybind_function="__truediv__",
                pybind_is_method=True,
                python_fallback=None,
            )
            for typ in PA_NUM_TYPES
        ),
        *(
            ChalkFunctionOverload(
                function_name="/",
                description="duration / num division",
                overload_generic_parameters=[duration_typ, num_type],
                overload_generic_return=duration_typ,
                pybind_function="__truediv__",
                pybind_is_method=True,
                python_fallback=None,
            )
            for num_type in PA_LARGEST_NUM_TYPES
            for duration_typ in PA_DURATION_TYPES
        ),
    ],
    "**": [
        ChalkFunctionOverload(
            function_name="**",
            description="basic binary ** operation",
            overload_generic_parameters=[pa.float64(), pa.float64()],
            overload_generic_return=pa.float64(),
            pybind_function="__pow__",
            pybind_is_method=True,
            python_fallback=None,
        ),
    ],
    ">": [
        ChalkFunctionOverload(
            function_name=">",
            description="basic binary > operation",
            overload_generic_parameters=[generic("T_ord", orderable=True), generic("T_ord", orderable=True)],
            overload_generic_return=pa.bool_(),
            pybind_function="__gt__",
            pybind_is_method=True,
            python_fallback=None,
        ),
    ],
    ">=": [
        ChalkFunctionOverload(
            function_name=">=",
            description="basic binary >= operation",
            overload_generic_parameters=[generic("T_ord", orderable=True), generic("T_ord", orderable=True)],
            overload_generic_return=pa.bool_(),
            pybind_function="__ge__",
            pybind_is_method=True,
            python_fallback=None,
        ),
    ],
    "<": [
        ChalkFunctionOverload(
            function_name="<",
            description="basic binary < operation",
            overload_generic_parameters=[generic("T_ord", orderable=True), generic("T_ord", orderable=True)],
            overload_generic_return=pa.bool_(),
            pybind_function="__lt__",
            pybind_is_method=True,
            python_fallback=None,
        ),
    ],
    "<=": [
        ChalkFunctionOverload(
            function_name="<=",
            description="basic binary <= operation",
            overload_generic_parameters=[generic("T_ord", orderable=True), generic("T_ord", orderable=True)],
            overload_generic_return=pa.bool_(),
            pybind_function="__le__",
            pybind_is_method=True,
            python_fallback=None,
        ),
    ],
    "==": [
        ChalkFunctionOverload(
            function_name="==",
            description="basic binary == operation",
            overload_generic_parameters=[generic("T"), generic("T")],
            overload_generic_return=pa.bool_(),
            pybind_function="__eq__",
            pybind_is_method=True,
            python_fallback=None,
        ),
    ],
    "!=": [
        ChalkFunctionOverload(
            function_name="!=",
            description="basic binary != operation",
            overload_generic_parameters=[generic("T"), generic("T")],
            overload_generic_return=pa.bool_(),
            pybind_function="__ne__",
            pybind_is_method=True,
            python_fallback=None,
        ),
    ],
    "&": [
        ChalkFunctionOverload(
            function_name="&",
            description="boolean & operation",
            overload_generic_parameters=[pa.bool_(), pa.bool_()],
            overload_generic_return=pa.bool_(),
            pybind_function="__and__",
            pybind_is_method=True,
            python_fallback=None,
        ),
    ],
    "|": [
        ChalkFunctionOverload(
            function_name="|",
            description="boolean | operation",
            overload_generic_parameters=[pa.bool_(), pa.bool_()],
            overload_generic_return=pa.bool_(),
            pybind_function="__or__",
            pybind_is_method=True,
            python_fallback=None,
        ),
    ],
    "~": [
        ChalkFunctionOverload(
            function_name="~",
            description="boolean ~ operation",
            overload_generic_parameters=[pa.bool_()],
            overload_generic_return=pa.bool_(),
            pybind_function="__invert__",
            pybind_is_method=True,
            python_fallback=None,
        ),
    ],
    "secure_random": [
        ChalkFunctionOverload(
            function_name="secure_random",
            description="Generates a cryptographically secure random float between 0 and 1.",
            overload_generic_parameters=[],
            overload_generic_return=pa.float64(),
            pybind_function="secure_random",
            python_fallback=None,
        ),
        ChalkFunctionOverload(
            function_name="secure_random",
            description="Generates a cryptographically secure random int8 between the specified bounds.",
            overload_generic_parameters=[pa.int8(), pa.int8()],
            overload_generic_return=pa.int8(),
            pybind_function="secure_random",
            python_fallback=None,
        ),
        ChalkFunctionOverload(
            function_name="secure_random",
            description="Generates a cryptographically secure random int16 between the specified bounds.",
            overload_generic_parameters=[pa.int16(), pa.int16()],
            overload_generic_return=pa.int16(),
            pybind_function="secure_random",
            python_fallback=None,
        ),
        ChalkFunctionOverload(
            function_name="secure_random",
            description="Generates a cryptographically secure random int32 between the specified bounds.",
            overload_generic_parameters=[pa.int32(), pa.int32()],
            overload_generic_return=pa.int32(),
            pybind_function="secure_random",
            python_fallback=None,
        ),
        ChalkFunctionOverload(
            function_name="secure_random",
            description="Generates a cryptographically secure random int64 between the specified bounds.",
            overload_generic_parameters=[pa.int64(), pa.int64()],
            overload_generic_return=pa.int64(),
            pybind_function="secure_random",
            python_fallback=None,
        ),
        ChalkFunctionOverload(
            function_name="secure_random",
            description="Generates a cryptographically secure random float32 between the specified bounds.",
            overload_generic_parameters=[pa.float32(), pa.float32()],
            overload_generic_return=pa.float32(),
            pybind_function="secure_random",
            python_fallback=None,
        ),
        ChalkFunctionOverload(
            function_name="secure_random",
            description="Generates a cryptographically secure random float between the specified bounds.",
            overload_generic_parameters=[pa.float64(), pa.float64()],
            overload_generic_return=pa.float64(),
            pybind_function="secure_random",
            python_fallback=None,
        ),
    ],
    "random": [
        ChalkFunctionOverload(
            function_name="random",
            description="Generates a pseudo-random float between 0 and 1.",
            overload_generic_parameters=[],
            overload_generic_return=pa.float64(),
            pybind_function="random",
            python_fallback=None,
        ),
    ]
    + [
        ChalkFunctionOverload(
            function_name="random",
            description="Generates a pseudo-random integer within the bounds of the specified type.",
            overload_generic_parameters=[dt],
            overload_generic_return=dt,
            pybind_function="random",
            python_fallback=None,
        )
        for dt in (pa.int8(), pa.int16(), pa.int32(), pa.int64())
    ],
    "from_big_endian_64": [
        ChalkFunctionOverload(
            function_name="from_big_endian_64",
            description="Convert a 64-bit big-endian bytes value to an integer.",
            overload_generic_parameters=[pa.binary()],
            overload_generic_return=pa.int64(),
            pybind_function="from_big_endian_64",
            python_fallback=None,
        ),
        ChalkFunctionOverload(
            function_name="from_big_endian_64",
            description="Convert a 64-bit big-endian bytes value to an integer.",
            overload_generic_parameters=[pa.large_binary()],
            overload_generic_return=pa.int64(),
            pybind_function="from_big_endian_64",
            python_fallback=None,
        ),
    ],
    "from_big_endian_32": [
        ChalkFunctionOverload(
            function_name="from_big_endian_32",
            description="Convert a 32-bit big-endian bytes value to an integer.",
            overload_generic_parameters=[pa.binary()],
            overload_generic_return=pa.int32(),
            pybind_function="from_big_endian_32",
            python_fallback=None,
        ),
        ChalkFunctionOverload(
            function_name="from_big_endian_32",
            description="Convert a 32-bit big-endian bytes value to an integer.",
            overload_generic_parameters=[pa.large_binary()],
            overload_generic_return=pa.int32(),
            pybind_function="from_big_endian_32",
            python_fallback=None,
        ),
    ],
    "parse_datetime": [
        ChalkFunctionOverload(
            function_name="parse_datetime",
            description="Converts an ISO 8601 string into a datetime.",
            overload_generic_parameters=[pa.large_string(), pa.large_string()],
            overload_generic_return=pa.timestamp("us", tz="UTC"),
            pybind_function="parse_datetime",
        ),
    ],
    "to_iso8601": [
        ChalkFunctionOverload(
            function_name="to_iso8601",
            description="Converts a datetime to an ISO 8601 string format.",
            overload_generic_parameters=[pa.timestamp("us", tz="UTC")],
            overload_generic_return=pa.large_string(),
            pybind_function="to_iso8601",
        ),
    ],
    "strpos": [
        ChalkFunctionOverload(
            function_name="strpos",
            description="Returns the position of the first occurrence of a substring within a string.",
            overload_generic_parameters=[pa.large_string(), pa.large_string()],
            overload_generic_return=pa.int64(),
            pybind_function="strpos",
            python_fallback=None,
        ),
    ],
    "strrpos": [
        ChalkFunctionOverload(
            function_name="strrpos",
            description="Returns the position of the last occurrence of a substring within a string.",
            overload_generic_parameters=[pa.large_string(), pa.large_string()],
            overload_generic_return=pa.int64(),
            pybind_function="strrpos",
            python_fallback=None,
        ),
    ],
    "trim": [
        ChalkFunctionOverload(
            function_name="trim",
            description="Removes whitespace from both ends of a string.",
            overload_generic_parameters=[pa.large_string()],
            overload_generic_return=pa.large_string(),
            pybind_function="trim",
            python_fallback=None,
        ),
        ChalkFunctionOverload(
            function_name="trim",
            description="Removes specified characters from both ends of a string.",
            overload_generic_parameters=[pa.large_string(), pa.large_string()],
            overload_generic_return=pa.large_string(),
            pybind_function="trim",
            python_fallback=None,
        ),
    ],
    "rtrim": [
        ChalkFunctionOverload(
            function_name="rtrim",
            description="Removes whitespace from the right end of a string.",
            overload_generic_parameters=[pa.large_string()],
            overload_generic_return=pa.large_string(),
            pybind_function="rtrim",
            python_fallback=None,
        ),
        ChalkFunctionOverload(
            function_name="rtrim",
            description="Removes specified characters from the right end of a string.",
            overload_generic_parameters=[pa.large_string(), pa.large_string()],
            overload_generic_return=pa.large_string(),
            pybind_function="rtrim",
            python_fallback=None,
        ),
    ],
    "ltrim": [
        ChalkFunctionOverload(
            function_name="ltrim",
            description="Removes whitespace from the left end of a string.",
            overload_generic_parameters=[pa.large_string()],
            overload_generic_return=pa.large_string(),
            pybind_function="ltrim",
            python_fallback=None,
        ),
        ChalkFunctionOverload(
            function_name="ltrim",
            description="Removes specified characters from the left end of a string.",
            overload_generic_parameters=[pa.large_string(), pa.large_string()],
            overload_generic_return=pa.large_string(),
            pybind_function="ltrim",
            python_fallback=None,
        ),
    ],
    "upper": [
        ChalkFunctionOverload(
            function_name="upper",
            description="Converts a string to uppercase.",
            overload_generic_parameters=[pa.large_string()],
            overload_generic_return=pa.large_string(),
            pybind_function="upper",
            python_fallback=None,
        ),
    ],
    "lower": [
        ChalkFunctionOverload(
            function_name="lower",
            description="Converts a string to lowercase.",
            overload_generic_parameters=[pa.large_string()],
            overload_generic_return=pa.large_string(),
            pybind_function="lower",
            python_fallback=None,
        ),
    ],
    "chr": [
        ChalkFunctionOverload(
            function_name="chr",
            description="Converts an integer to its corresponding ASCII character.",
            overload_generic_parameters=[pa.int64()],
            overload_generic_return=pa.large_string(),
            pybind_function="chr",
            python_fallback=None,
        ),
    ],
    "levenshtein_distance": [
        ChalkFunctionOverload(
            function_name="levenshtein_distance",
            description="Calculates the Levenshtein distance between two strings.",
            overload_generic_parameters=[pa.large_string(), pa.large_string()],
            overload_generic_return=pa.int64(),
            pybind_function="levenshtein_distance",
            python_fallback=None,
        ),
    ],
    "lpad": [
        ChalkFunctionOverload(
            function_name="lpad",
            description="Pads a string with a specified padding string on the left to reach a target length.",
            overload_generic_parameters=[pa.large_string(), pa.int64(), pa.large_string()],
            overload_generic_return=pa.large_string(),
            pybind_function="lpad",
            python_fallback=None,
        ),
    ],
    "rpad": [
        ChalkFunctionOverload(
            function_name="rpad",
            description="Pads a string with a specified padding string on the right to reach a target length.",
            overload_generic_parameters=[pa.large_string(), pa.int64(), pa.large_string()],
            overload_generic_return=pa.large_string(),
            pybind_function="rpad",
            python_fallback=None,
        ),
    ],
    "split_part": [
        ChalkFunctionOverload(
            function_name="split_part",
            description="Splits a string by delimiter and returns the part at the specified index (1-based).",
            overload_generic_parameters=[pa.large_string(), pa.large_string(), pa.int64()],
            overload_generic_return=pa.large_string(),
            pybind_function="split_part",
            python_fallback=None,
        ),
    ],
    "word_stem": [
        ChalkFunctionOverload(
            function_name="word_stem",
            description="Returns the stem of a word using stemming algorithms.",
            overload_generic_parameters=[pa.large_string()],
            overload_generic_return=pa.large_string(),
            pybind_function="word_stem",
            python_fallback=None,
        ),
    ],
    "sequence_matcher_ratio": [
        ChalkFunctionOverload(
            function_name="sequence_matcher_ratio",
            description="Computes the similarity ratio between two strings using sequence matching.",
            overload_generic_parameters=[pa.large_string(), pa.large_string()],
            overload_generic_return=pa.float64(),
            pybind_function="sequence_matcher_ratio",
            python_fallback=None,
        )
    ],
    "from_iso8601_timestamp": [
        ChalkFunctionOverload(
            function_name="from_iso8601_timestamp",
            description="Parses an ISO 8601 timestamp string into a datetime object.",
            overload_generic_parameters=[pa.large_string()],
            overload_generic_return=pa.timestamp("us", tz="UTC"),
            pybind_function="from_iso8601_timestamp",
        ),
    ],
    "to_milliseconds": [
        ChalkFunctionOverload(
            function_name="to_milliseconds",
            description="Converts a duration to milliseconds.",
            overload_generic_parameters=[duration_type],
            overload_generic_return=pa.int64(),
            pybind_function="to_milliseconds",
        )
        for duration_type in PA_DURATION_TYPES
    ],
    "last_day_of_month": [
        ChalkFunctionOverload(
            function_name="last_day_of_month",
            description="Returns the last day of the month for a given date.",
            overload_generic_parameters=[pa.timestamp("us", tz="UTC")],
            overload_generic_return=pa.timestamp("us", tz="UTC"),
            pybind_function="last_day_of_month",
        ),
    ],
    "day_of_week": [
        ChalkFunctionOverload(
            function_name="day_of_week",
            description="Extracts the day of the week from a timestamp.",
            overload_generic_parameters=[date_or_timestamp],
            overload_generic_return=pa.int64(),
            pybind_function="day_of_week",
        )
        for date_or_timestamp in PA_DATE_TYPES + PA_TIMESTAMP_TYPES
    ],
    "day_of_month": [
        ChalkFunctionOverload(
            function_name="day_of_month",
            description="Extracts the day of the month from a timestamp.",
            overload_generic_parameters=[date_or_timestamp],
            overload_generic_return=pa.int64(),
            pybind_function="day_of_month",
        )
        for date_or_timestamp in PA_DATE_TYPES + PA_TIMESTAMP_TYPES
    ],
    "day_of_year": [
        ChalkFunctionOverload(
            function_name="day_of_year",
            description="Extracts the day of the month from a timestamp.",
            overload_generic_parameters=[date_or_timestamp],
            overload_generic_return=pa.int64(),
            pybind_function="day_of_year",
        )
        for date_or_timestamp in PA_DATE_TYPES + PA_TIMESTAMP_TYPES
    ],
    "week": [
        ChalkFunctionOverload(
            function_name="week",
            description="Extracts the week of the year from a timestamp.",
            overload_generic_parameters=[date_or_timestamp],
            overload_generic_return=pa.int64(),
            pybind_function="week",
        )
        for date_or_timestamp in PA_DATE_TYPES + PA_TIMESTAMP_TYPES
    ],
    "week_of_year": [
        ChalkFunctionOverload(
            function_name="week_of_year",
            description="Extracts the week of the year from a timestamp.",
            overload_generic_parameters=[date_or_timestamp],
            overload_generic_return=pa.int64(),
            pybind_function="week_of_year",
        )
        for date_or_timestamp in PA_DATE_TYPES + PA_TIMESTAMP_TYPES
    ],
    "year_of_week": [
        ChalkFunctionOverload(
            function_name="year_of_week",
            description="Extracts the year of the ISO week from a date.",
            overload_generic_parameters=[date_or_timestamp],
            overload_generic_return=pa.int64(),
            pybind_function="year_of_week",
        )
        for date_or_timestamp in PA_DATE_TYPES + PA_TIMESTAMP_TYPES
    ],
    "yow": [
        ChalkFunctionOverload(
            function_name="yow",
            description="Extracts the year of the ISO week from a date.",
            overload_generic_parameters=[date_or_timestamp],
            overload_generic_return=pa.int64(),
            pybind_function="yow",
        )
        for date_or_timestamp in PA_DATE_TYPES + PA_TIMESTAMP_TYPES
    ],
    "month": [
        ChalkFunctionOverload(
            function_name="month",
            description="Extracts the month from a timestamp.",
            overload_generic_parameters=[date_or_timestamp],
            overload_generic_return=pa.int64(),
            pybind_function="month",
        )
        for date_or_timestamp in PA_DATE_TYPES + PA_TIMESTAMP_TYPES
    ],
    "year": [
        ChalkFunctionOverload(
            function_name="year",
            description="Extracts the year from a timestamp.",
            overload_generic_parameters=[date_or_timestamp],
            overload_generic_return=pa.int64(),
            pybind_function="year",
        )
        for date_or_timestamp in PA_DATE_TYPES + PA_TIMESTAMP_TYPES
    ],
    "nan": [
        ChalkFunctionOverload(
            function_name="nan",
            description="Returns a floating point NaN (Not a Number) value.",
            overload_generic_parameters=[],
            overload_generic_return=pa.float64(),
            pybind_function="nan",
            python_fallback=None,
        ),
    ],
    "hour": [
        ChalkFunctionOverload(
            function_name="hour",
            description="Extracts the hour from a timestamp.",
            overload_generic_parameters=[pa.timestamp("us", tz="UTC")],
            overload_generic_return=pa.int64(),
            pybind_function="hour",
        ),
    ],
    "minute": [
        ChalkFunctionOverload(
            function_name="minute",
            description="Extracts the minute from a timestamp.",
            overload_generic_parameters=[pa.timestamp("us", tz="UTC")],
            overload_generic_return=pa.int64(),
            pybind_function="minute",
        ),
    ],
    "to_unixtime": [
        ChalkFunctionOverload(
            function_name="to_unixtime",
            description="Converts a timestamp to Unix timestamp (seconds since epoch).",
            overload_generic_parameters=[pa.timestamp("us", tz="UTC")],
            overload_generic_return=pa.float64(),
            pybind_function="to_unixtime",
        ),
    ],
    "second": [
        ChalkFunctionOverload(
            function_name="second",
            description="Extracts the second from a timestamp.",
            overload_generic_parameters=[pa.timestamp("us", tz="UTC")],
            overload_generic_return=pa.int64(),
            pybind_function="second",
        ),
    ],
    "millisecond": [
        ChalkFunctionOverload(
            function_name="millisecond",
            description="Extracts the millisecond from a timestamp.",
            overload_generic_parameters=[pa.timestamp("us", tz="UTC")],
            overload_generic_return=pa.int64(),
            pybind_function="millisecond",
        ),
    ],
    "quarter": [
        ChalkFunctionOverload(
            function_name="quarter",
            description="Extracts the quarter of the year from a timestamp.",
            overload_generic_parameters=[pa.timestamp("us", tz="UTC")],
            overload_generic_return=pa.int64(),
            pybind_function="quarter",
        ),
    ],
    "is_federal_holiday": [
        ChalkFunctionOverload(
            function_name="is_federal_holiday",
            description="Returns True if the given timestamp is a federal holiday.",
            overload_generic_parameters=[date_or_time],
            overload_generic_return=pa.bool_(),
            pybind_function="is_federal_holiday",
        )
        for date_or_time in PA_DATE_TYPES + PA_TIMESTAMP_TYPES
    ],
    "total_seconds": [
        ChalkFunctionOverload(
            function_name="total_seconds",
            description="Returns the length of the input duration in seconds.",
            overload_generic_parameters=[duration_type],
            overload_generic_return=pa.float64(),
            pybind_function="total_seconds",
            python_fallback=None,
        )
        for duration_type in PA_DURATION_TYPES
    ],
    "from_unix_seconds": [
        ChalkFunctionOverload(
            function_name="from_unixtime",
            description="Converts Unix timestamp (seconds since epoch) to a timestamp.",
            overload_generic_parameters=[pa.float64()],
            overload_generic_return=pa.timestamp("us", tz="UTC"),
            pybind_function="from_unixtime",
        ),
    ],
    "from_unixtime": [
        ChalkFunctionOverload(
            function_name="from_unixtime",
            description="Returns the UNIX timestamp unixtime as a timestamp with time zone using hours and minutes for the time zone offset.",
            overload_generic_parameters=[pa.float64(), pa.int64(), pa.int64()],
            overload_generic_return=pa.timestamp("us", tz="UTC"),
            pybind_function="from_unixtime",
        ),
        ChalkFunctionOverload(
            function_name="from_unixtime",
            description="Returns the UNIX timestamp unixtime as a timestamp with time zone.",
            overload_generic_parameters=[pa.float64()],
            overload_generic_return=pa.timestamp("us", tz="UTC"),
            pybind_function="from_unixtime",
        ),
    ],
    "array_join": [
        ChalkFunctionOverload(
            function_name="array_join",
            description="Joins elements of an array into a string using a separator.",
            overload_generic_parameters=[pa.list_(generic("K")), pa.large_string()],
            overload_generic_return=pa.large_string(),
            pybind_function="array_join",
            python_fallback=None,
        ),
        ChalkFunctionOverload(
            function_name="array_join",
            description="Joins elements of a large array into a string using a separator.",
            overload_generic_parameters=[
                pa.large_list(generic("K")),
                pa.large_string(),
            ],
            overload_generic_return=pa.large_string(),
            pybind_function="array_join",
            python_fallback=None,
        ),
    ],
    "from_base": [
        ChalkFunctionOverload(
            function_name="from_base",
            description="Converts a string representation of a number in a given base to an integer.",
            overload_generic_parameters=[pa.large_string(), pa.int64()],
            overload_generic_return=pa.int64(),
            pybind_function="from_base",
            python_fallback=None,
        ),
    ],
    "round": [
        ChalkFunctionOverload(
            function_name="round",
            description="Rounds a floating point number to the nearest integer.",
            overload_generic_parameters=[float_type],
            overload_generic_return=float_type,
            pybind_function="round",
            python_fallback=None,
        )
        for float_type in PA_FLOAT_TYPES
    ]
    + [
        ChalkFunctionOverload(
            function_name="round",
            description="Rounds a floating point number to the specified number of decimal places.",
            overload_generic_parameters=[float_type, pa.int64()],
            overload_generic_return=float_type,
            # Velox only supports 2-argument `round` on int32 numeric types, so we will cast the second
            # argument down to `int32` if it's actually int64.
            overload_force_cast_parameters=(float_type, pa.int32()),
            pybind_function="round",
            python_fallback=None,
        )
        for float_type in PA_FLOAT_TYPES
    ],
    "and": [
        ChalkFunctionOverload(
            function_name="and",
            description="Performs logical AND operation on two boolean values.",
            overload_generic_parameters=[pa.bool_(), pa.bool_()],
            overload_generic_return=pa.bool_(),
            pybind_function="and",
            python_fallback=None,
        )
    ],
    "lt": [
        ChalkFunctionOverload(
            function_name="lt",
            description="Compares if the first value is less than the second.",
            overload_generic_parameters=[t, t],
            overload_generic_return=pa.bool_(),
            pybind_function="lt",
            python_fallback=None,
        )
        for t in PA_NUM_TYPES
    ],
    "gt": [
        ChalkFunctionOverload(
            function_name="gt",
            description="Compares if the first value is greater than the second.",
            overload_generic_parameters=[t, t],
            overload_generic_return=pa.bool_(),
            pybind_function="gt",
            python_fallback=None,
        )
        for t in PA_NUM_TYPES
    ],
    "eq": [
        ChalkFunctionOverload(
            function_name="eq",
            description="Compares if two values are equal.",
            overload_generic_parameters=[t, t],
            overload_generic_return=pa.bool_(),
            pybind_function="eq",
            python_fallback=None,
        )
        for t in PA_ALL_TYPES
    ],
    "neq": [
        ChalkFunctionOverload(
            function_name="neq",
            description="Compares if two values are not equal.",
            overload_generic_parameters=[t, t],
            overload_generic_return=pa.bool_(),
            pybind_function="neq",
            python_fallback=None,
        )
        for t in PA_ALL_TYPES
    ],
    "lte": [
        ChalkFunctionOverload(
            function_name="lte",
            description="Compares if the first value is less than or equal to the second.",
            overload_generic_parameters=[t, t],
            overload_generic_return=pa.bool_(),
            pybind_function="lte",
            python_fallback=None,
        )
        for t in PA_NUM_TYPES
    ],
    "gte": [
        ChalkFunctionOverload(
            function_name="gte",
            description="Compares if the first value is greater than or equal to the second.",
            overload_generic_parameters=[t, t],
            overload_generic_return=pa.bool_(),
            pybind_function="gte",
            python_fallback=None,
        )
        for t in PA_NUM_TYPES
    ],
    "sin": [
        ChalkFunctionOverload(
            function_name="sin",
            description="Calculates the sine of an angle in radians.",
            overload_generic_parameters=[pa.float64()],
            overload_generic_return=pa.float64(),
            pybind_function="sin",
            python_fallback=None,
        ),
    ],
    "cos": [
        ChalkFunctionOverload(
            function_name="cos",
            description="Calculates the cosine of an angle in radians.",
            overload_generic_parameters=[pa.float64()],
            overload_generic_return=pa.float64(),
            pybind_function="cos",
            python_fallback=None,
        ),
    ],
    "tan": [
        ChalkFunctionOverload(
            function_name="tan",
            description="Calculates the tangent of an angle in radians.",
            overload_generic_parameters=[pa.float64()],
            overload_generic_return=pa.float64(),
            pybind_function="tan",
            python_fallback=None,
        ),
    ],
    "asin": [
        ChalkFunctionOverload(
            function_name="asin",
            description="Calculates the inverse sine in radians.",
            overload_generic_parameters=[pa.float64()],
            overload_generic_return=pa.float64(),
            pybind_function="asin",
            python_fallback=None,
        ),
    ],
    "acos": [
        ChalkFunctionOverload(
            function_name="acos",
            description="Calculates the inverse cosine in radians.",
            overload_generic_parameters=[pa.float64()],
            overload_generic_return=pa.float64(),
            pybind_function="acos",
            python_fallback=None,
        ),
    ],
    "sqrt": [
        ChalkFunctionOverload(
            function_name="sqrt",
            description="Calculates the square root of a number.",
            overload_generic_parameters=[pa.float64()],
            overload_generic_return=pa.float64(),
            pybind_function="sqrt",
            python_fallback=None,
        ),
    ],
    "exp": [
        ChalkFunctionOverload(
            function_name="exp",
            description="Calculates e raised to the power of a number.",
            overload_generic_parameters=[pa.float64()],
            overload_generic_return=pa.float64(),
            pybind_function="exp",
            python_fallback=None,
        ),
    ],
    "atan": [
        ChalkFunctionOverload(
            function_name="atan",
            description="Calculates the arctangent of a number in radians.",
            overload_generic_parameters=[pa.float64()],
            overload_generic_return=pa.float64(),
            pybind_function="atan",
            python_fallback=None,
        ),
    ],
    "atan2": [
        ChalkFunctionOverload(
            function_name="atan2",
            description="Calculates the arctangent of y/x in radians, handling quadrant correctly.",
            overload_generic_parameters=[pa.float64(), pa.float64()],
            overload_generic_return=pa.float64(),
            pybind_function="atan2",
            python_fallback=None,
        ),
    ],
    "cbrt": [
        ChalkFunctionOverload(
            function_name="cbrt",
            description="Calculates the cube root of a number.",
            overload_generic_parameters=[pa.float64()],
            overload_generic_return=pa.float64(),
            pybind_function="cbrt",
            python_fallback=None,
        ),
        ChalkFunctionOverload(
            function_name="cbrt",
            description="Calculates the cube root of an integer.",
            overload_generic_parameters=[pa.int64()],
            overload_generic_return=pa.float64(),
            pybind_function="cbrt",
            python_fallback=None,
        ),
    ],
    "cosh": [
        ChalkFunctionOverload(
            function_name="cosh",
            description="Calculates the hyperbolic cosine of a number.",
            overload_generic_parameters=[pa.float64()],
            overload_generic_return=pa.float64(),
            pybind_function="cosh",
            python_fallback=None,
        ),
    ],
    "degrees": [
        ChalkFunctionOverload(
            function_name="degrees",
            description="Converts radians to degrees.",
            overload_generic_parameters=[pa.float64()],
            overload_generic_return=pa.float64(),
            pybind_function="degrees",
            python_fallback=None,
        ),
    ],
    "tanh": [
        ChalkFunctionOverload(
            function_name="tanh",
            description="Calculates the hyperbolic tangent of a number.",
            overload_generic_parameters=[pa.float64()],
            overload_generic_return=pa.float64(),
            pybind_function="tanh",
            python_fallback=None,
        ),
    ],
    "sign": [
        ChalkFunctionOverload(
            function_name="sign",
            description="Returns the sign of a number (-1, 0, or 1).",
            overload_generic_parameters=[pa.float64()],
            overload_generic_return=pa.float64(),
            pybind_function="sign",
            python_fallback=None,
        ),
        ChalkFunctionOverload(
            function_name="sign",
            description="Returns the sign of an integer (-1, 0, or 1).",
            overload_generic_parameters=[pa.int64()],
            overload_generic_return=pa.int64(),
            pybind_function="sign",
            python_fallback=None,
        ),
    ],
    "log": [
        ChalkFunctionOverload(
            function_name="ln",
            description="Calculates the natural logarithm of a number.",
            overload_generic_parameters=[pa.float64()],
            overload_generic_return=pa.float64(),
            pybind_function="ln",
            python_fallback=None,
        ),
    ],
    "ln": [
        ChalkFunctionOverload(
            function_name="ln",
            description="Calculates the natural logarithm of a number.",
            overload_generic_parameters=[pa.float64()],
            overload_generic_return=pa.float64(),
            pybind_function="ln",
            python_fallback=None,
        ),
    ],
    "pow": [
        ChalkFunctionOverload(
            function_name="pow",
            description="Raises a number to the power of another number.",
            overload_generic_parameters=[pa.float64(), pa.float64()],
            overload_generic_return=pa.float64(),
            pybind_function="pow",
            python_fallback=None,
        ),
    ],
    "clamp": [
        ChalkFunctionOverload(
            function_name="clamp",
            description="Constrains a value between a minimum and maximum range.",
            overload_generic_parameters=[pa.float64(), pa.float64(), pa.float64()],
            overload_generic_return=pa.float64(),
            pybind_function="clamp",
            python_fallback=None,
        ),
        ChalkFunctionOverload(
            function_name="clamp",
            description="Constrains an integer value between a minimum and maximum range.",
            overload_generic_parameters=[pa.int64(), pa.int64(), pa.int64()],
            overload_generic_return=pa.int64(),
            pybind_function="clamp",
            python_fallback=None,
        ),
    ],
    "e": [
        ChalkFunctionOverload(
            function_name="e",
            description="Returns the mathematical constant e (Euler's number).",
            overload_generic_parameters=[],
            overload_generic_return=pa.float64(),
            pybind_function="e",
            python_fallback=None,
        ),
    ],
    "greatest": [
        ChalkFunctionOverload(
            function_name="greatest",
            description="Returns the maximum value from a list of float values.",
            overload_generic_parameters=[VariadicType(element_type=pa.float64())],
            overload_generic_return=pa.float64(),
            pybind_function="greatest",
            python_fallback=None,
        ),
        ChalkFunctionOverload(
            function_name="greatest",
            description="Returns the maximum value from a list of integer values.",
            overload_generic_parameters=[VariadicType(element_type=pa.int64())],
            overload_generic_return=pa.int64(),
            pybind_function="greatest",
            python_fallback=None,
        ),
    ],
    "least": [
        ChalkFunctionOverload(
            function_name="least",
            description="Returns the minimum value from a list of float values.",
            overload_generic_parameters=[VariadicType(element_type=pa.float64())],
            overload_generic_return=pa.float64(),
            pybind_function="least",
            python_fallback=None,
        ),
        ChalkFunctionOverload(
            function_name="least",
            description="Returns the minimum value from a list of integer values.",
            overload_generic_parameters=[VariadicType(element_type=pa.int64())],
            overload_generic_return=pa.int64(),
            pybind_function="least",
            python_fallback=None,
        ),
    ],
    "pi": [
        ChalkFunctionOverload(
            function_name="pi",
            description="Returns the mathematical constant π (pi).",
            overload_generic_parameters=[],
            overload_generic_return=pa.float64(),
            pybind_function="pi",
            python_fallback=None,
        ),
    ],
    "power": [
        ChalkFunctionOverload(
            function_name="power",
            description="Raises the first number to the power of the second number.",
            overload_generic_parameters=[pa.float64(), pa.float64()],
            overload_generic_return=pa.float64(),
            pybind_function="power",
            python_fallback=None,
        ),
    ],
    "radians": [
        ChalkFunctionOverload(
            function_name="radians",
            description="Converts degrees to radians.",
            overload_generic_parameters=[pa.float64()],
            overload_generic_return=pa.float64(),
            pybind_function="radians",
            python_fallback=None,
        ),
    ],
    "rand": [
        ChalkFunctionOverload(
            function_name="rand",
            description="Generates a random float between 0 and 1.",
            overload_generic_parameters=[],
            overload_generic_return=pa.float64(),
            pybind_function="rand",
            python_fallback=None,
        ),
    ],
    "to_base": [
        ChalkFunctionOverload(
            function_name="to_base",
            description="Converts an integer to its string representation in the specified base.",
            overload_generic_parameters=[pa.int64(), pa.int64()],
            overload_generic_return=pa.large_string(),
            pybind_function="to_base",
            python_fallback=None,
        ),
    ],
    "width_bucket": [
        ChalkFunctionOverload(
            function_name="width_bucket",
            description="Returns the bucket number for a value in a histogram with uniform bucket widths.",
            overload_generic_parameters=[pa.float64(), pa.float64(), pa.float64(), pa.int64()],
            overload_generic_return=pa.int64(),
            pybind_function="width_bucket",
            python_fallback=None,
        ),
    ],
    "bankers_round": [
        ChalkFunctionOverload(
            function_name="bankers_round",
            description="Rounds a number using banker's rounding (round half to even).",
            overload_generic_parameters=[float_type],
            overload_generic_return=float_type,
            pybind_function="bankers_round",
            python_fallback=None,
        )
        for float_type in PA_FLOAT_TYPES
    ]
    + [
        ChalkFunctionOverload(
            function_name="bankers_round",
            description="Rounds a number to specified decimal places using banker's rounding (round half to even).",
            overload_generic_parameters=[float_type, pa.int64()],
            overload_generic_return=float_type,
            # Velox only supports 2-argument `round` on int32 numeric types, so we will cast the second
            # argument down to `int32` if it's actually int64.
            overload_force_cast_parameters=(float_type, pa.int32()),
            pybind_function="bankers_round",
            python_fallback=None,
        )
        for float_type in PA_FLOAT_TYPES
    ],
    "beta_cdf": [
        ChalkFunctionOverload(
            function_name="beta_cdf",
            description="Compute the Beta cdf with given a, b parameters: P(N < value; a, b). The a, b parameters must be positive real numbers and value must be a real value (all of type DOUBLE). The value must lie on the interval [0, 1].",
            overload_generic_parameters=[pa.float64(), pa.float64(), pa.float64()],  # a, b, val
            overload_generic_return=pa.float64(),
            pybind_function="beta_cdf",
            python_fallback=None,
        ),
    ],
    "binomial_cdf": [
        ChalkFunctionOverload(
            function_name="binomial_cdf",
            description="Compute the Binomial cdf with given numberOfTrials and successProbability (for a single trial): P(N < value). The successProbability must be real value in [0, 1], numberOfTrials and value must be positive integers with numberOfTrials greater or equal to value.",
            overload_generic_parameters=[pa.int64(), pa.float64(), pa.int64()],  # num_trials, p_success, val
            overload_generic_return=pa.float64(),
            pybind_function="binomial_cdf",
            python_fallback=None,
        ),
    ],
    "cauchy_cdf": [
        ChalkFunctionOverload(
            function_name="cauchy_cdf",
            description="Compute the Cauchy cdf with given parameters median and scale (gamma): P(N; median, scale). The scale parameter must be a positive double. The value parameter must be a double on the interval [0, 1].",
            overload_generic_parameters=[pa.float64(), pa.float64(), pa.float64()],  # median, scale, val
            overload_generic_return=pa.float64(),
            pybind_function="cauchy_cdf",
            python_fallback=None,
        ),
    ],
    "chi_squared_cdf": [
        ChalkFunctionOverload(
            function_name="chi_squared_cdf",
            description="Compute the Chi-square cdf with given df (degrees of freedom) parameter: P(N < value; df). The df parameter must be a positive real number, and value must be a non-negative real value (both of type DOUBLE).",
            overload_generic_parameters=[pa.float64(), pa.float64()],  # df, val
            overload_generic_return=pa.float64(),
            pybind_function="chi_squared_cdf",
            python_fallback=None,
        ),
    ],
    "f_cdf": [
        ChalkFunctionOverload(
            function_name="f_cdf",
            description="Compute the F cdf with given df1 (numerator degrees of freedom) and df2 (denominator degrees of freedom) parameters: P(N < value; df1, df2). The numerator and denominator df parameters must be positive real numbers. The value must be a non-negative real number.",
            overload_generic_parameters=[pa.float64(), pa.float64(), pa.float64()],  # df1, df2, val
            overload_generic_return=pa.float64(),
            pybind_function="f_cdf",
            python_fallback=None,
        ),
    ],
    "gamma_cdf": [
        ChalkFunctionOverload(
            function_name="gamma_cdf",
            description="Compute the Gamma cdf with given shape and scale parameters: P(N < value; shape, scale). The shape and scale parameters must be positive real numbers. The value must be a non-negative real number.",
            overload_generic_parameters=[pa.float64(), pa.float64(), pa.float64()],  # shape, scale, val
            overload_generic_return=pa.float64(),
            pybind_function="gamma_cdf",
            python_fallback=None,
        ),
    ],
    "laplace_cdf": [
        ChalkFunctionOverload(
            function_name="laplace_cdf",
            description="Compute the Laplace cdf with given mean and scale parameters: P(N < value; mean, scale). The mean and value must be real values and the scale parameter must be a positive value (all of type DOUBLE).",
            overload_generic_parameters=[pa.float64(), pa.float64(), pa.float64()],  # mean, scale, val
            overload_generic_return=pa.float64(),
            pybind_function="laplace_cdf",
            python_fallback=None,
        ),
    ],
    "normal_cdf": [
        ChalkFunctionOverload(
            function_name="normal_cdf",
            description="Compute the Normal cdf with given mean and standard deviation (sd): P(N < value; mean, sd). The mean and value must be real values and the standard deviation must be a real and positive value (all of type DOUBLE).",
            overload_generic_parameters=[pa.float64(), pa.float64(), pa.float64()],  # mean, stddev, val
            overload_generic_return=pa.float64(),
            pybind_function="normal_cdf",
            python_fallback=None,
        ),
    ],
    "poisson_cdf": [
        ChalkFunctionOverload(
            function_name="poisson_cdf",
            description="Compute the Poisson cdf with given lambda (mean) parameter: P(N <= value; lambda). The lambda parameter must be a positive real number (of type DOUBLE) and value must be a non-negative integer.",
            overload_generic_parameters=[pa.float64(), pa.float64()],  # lambda, val
            overload_generic_return=pa.float64(),
            pybind_function="poisson_cdf",
            python_fallback=None,
        ),
    ],
    "weibull_cdf": [
        ChalkFunctionOverload(
            function_name="weibull_cdf",
            description="Compute the Weibull cdf with given parameters a, b: P(N <= value). The a and b parameters must be positive doubles and value must also be a double.",
            overload_generic_parameters=[pa.float64(), pa.float64(), pa.float64()],  # a, b, val
            overload_generic_return=pa.float64(),
            pybind_function="weibull_cdf",
            python_fallback=None,
        ),
    ],
    "inverse_beta_cdf": [
        ChalkFunctionOverload(
            function_name="inverse_beta_cdf",
            description="Compute the inverse of the Beta cdf with given a, b parameters for the cumulative probability (p): P(N < n). The a, b parameters must be positive double values. The probability p must lie on the interval [0, 1].",
            overload_generic_parameters=[pa.float64(), pa.float64(), pa.float64()],  # a, b, p
            overload_generic_return=pa.float64(),
            pybind_function="inverse_beta_cdf",
            python_fallback=None,
        ),
    ],
    "inverse_weibull_cdf": [
        ChalkFunctionOverload(
            function_name="inverse_weibull_cdf",
            description="Compute the inverse of the Weibull cdf with given parameters a, b for the probability p. The a, b parameters must be positive double values. The probability p must be a double on the interval [0, 1].",
            overload_generic_parameters=[pa.float64(), pa.float64(), pa.float64()],  # a, b, p
            overload_generic_return=pa.float64(),
            pybind_function="inverse_weibull_cdf",
            python_fallback=None,
        ),
    ],
    "inverse_cauchy_cdf": [
        ChalkFunctionOverload(
            function_name="inverse_cauchy_cdf",
            description="Compute the inverse of the Cauchy cdf with given parameters median and scale (gamma) for the probability p. The scale parameter must be a positive double. The probability p must be a double on the interval [0, 1].",
            overload_generic_parameters=[pa.float64(), pa.float64(), pa.float64()],  # median, scale, p
            overload_generic_return=pa.float64(),
            pybind_function="inverse_cauchy_cdf",
            python_fallback=None,
        ),
    ],
    "inverse_laplace_cdf": [
        ChalkFunctionOverload(
            function_name="inverse_laplace_cdf",
            description="Compute the inverse of the Laplace cdf with given mean and scale parameters for the cumulative probability (p): P(N < n). The mean must be a real value and the scale must be a positive real value (both of type DOUBLE). The probability p must lie on the interval [0, 1].",
            overload_generic_parameters=[pa.float64(), pa.float64(), pa.float64()],  # mean, scale, p
            overload_generic_return=pa.float64(),
            pybind_function="inverse_laplace_cdf",
            python_fallback=None,
        ),
    ],
    "inverse_f_cdf": [
        ChalkFunctionOverload(
            function_name="inverse_f_cdf",
            description="Compute the inverse of the Fisher F cdf with a given df1 (numerator degrees of freedom) and df2 (denominator degrees of freedom) parameters for the cumulative probability (p): P(N < n). The numerator and denominator df parameters must be positive real numbers. The probability p must lie on the interval [0, 1].",
            overload_generic_parameters=[pa.float64(), pa.float64(), pa.float64()],  # df1, df2, p
            overload_generic_return=pa.float64(),
            pybind_function="inverse_f_cdf",
            python_fallback=None,
        ),
    ],
    "inverse_normal_cdf": [
        ChalkFunctionOverload(
            function_name="inverse_normal_cdf",
            description="Compute the inverse of the Normal cdf with given mean and standard deviation (sd) for the cumulative probability (p): P(N < n). The mean must be a real value and the standard deviation must be a real and positive value (both of type DOUBLE). The probability p must lie on the interval (0, 1).",
            overload_generic_parameters=[pa.float64(), pa.float64(), pa.float64()],  # mean, stddev, p
            overload_generic_return=pa.float64(),
            pybind_function="inverse_normal_cdf",
            python_fallback=None,
        ),
    ],
    "inverse_gamma_cdf": [
        ChalkFunctionOverload(
            function_name="inverse_gamma_cdf",
            description="Compute the inverse of the Gamma cdf with given shape and scale parameters for the cumulative probability (p): P(N < n). The shape and scale parameters must be positive real values. The probability p must lie on the interval [0, 1].",
            overload_generic_parameters=[pa.float64(), pa.float64(), pa.float64()],  # shape, scale, p
            overload_generic_return=pa.float64(),
            pybind_function="inverse_gamma_cdf",
            python_fallback=None,
        ),
    ],
    "inverse_binomial_cdf": [
        ChalkFunctionOverload(
            function_name="inverse_binomial_cdf",
            description="Compute the inverse of the Binomial cdf with given numberOfTrials and successProbability (of a single trial) the cumulative probability (p): P(N <= n). The successProbability and p must be real values in [0, 1] and the numberOfTrials must be a positive integer.",
            overload_generic_parameters=[pa.int64(), pa.float64(), pa.float64()],  # num_trials, p_success, p
            overload_generic_return=pa.int64(),
            pybind_function="inverse_binomial_cdf",
            python_fallback=None,
        ),
    ],
    "inverse_poisson_cdf": [
        ChalkFunctionOverload(
            function_name="inverse_poisson_cdf",
            description="Compute the inverse of the Poisson cdf with given lambda (mean) parameter for the cumulative probability (p). It returns the value of n so that: P(N <= n; lambda) = p. The lambda parameter must be a positive real number (of type DOUBLE). The probability p must lie on the interval [0, 1).",
            overload_generic_parameters=[pa.float64(), pa.float64()],  # lambda, p
            overload_generic_return=pa.float64(),
            pybind_function="inverse_poisson_cdf",
            python_fallback=None,
        ),
    ],
    "inverse_chi_squared_cdf": [
        ChalkFunctionOverload(
            function_name="inverse_chi_squared_cdf",
            description="Compute the inverse of the Chi-square cdf with given df (degrees of freedom) parameter for the cumulative probability (p): P(N < n). The df parameter must be positive real values. The probability p must lie on the interval [0, 1].",
            overload_generic_parameters=[pa.float64(), pa.float64()],  # df, p
            overload_generic_return=pa.float64(),
            pybind_function="inverse_chi_squared_cdf",
            python_fallback=None,
        ),
    ],
    "wilson_interval_lower": [
        ChalkFunctionOverload(
            function_name="wilson_interval_lower",
            description="Returns the lower bound of the Wilson score interval of a Bernoulli trial process at a confidence specified by the z-score z.",
            overload_generic_parameters=[pa.int64(), pa.int64(), pa.float64()],  # successes, trials, z
            overload_generic_return=pa.float64(),
            pybind_function="wilson_interval_lower",
            python_fallback=None,
        ),
    ],
    "wilson_interval_upper": [
        ChalkFunctionOverload(
            function_name="wilson_interval_upper",
            description="Returns the upper bound of the Wilson score interval of a Bernoulli trial process at a confidence specified by the z-score z.",
            overload_generic_parameters=[pa.int64(), pa.int64(), pa.float64()],  # successes, trials, z
            overload_generic_return=pa.float64(),
            pybind_function="wilson_interval_upper",
            python_fallback=None,
        ),
    ],
    "length": [
        ChalkFunctionOverload(
            function_name="length",
            description="Returns the length of a string in characters.",
            overload_generic_parameters=[pa.large_string()],
            overload_generic_return=pa.int64(),
            pybind_function="length",
            python_fallback=None,
        ),
    ],
    "split": [
        ChalkFunctionOverload(
            function_name="split",
            description="Splits a string by a delimiter into a list of strings.",
            overload_generic_parameters=[pa.large_string(), pa.large_string()],
            overload_generic_return=pa.list_(pa.large_string()),
            pybind_function="split",
            python_fallback=None,
        ),
        ChalkFunctionOverload(
            function_name="split",
            description="Splits a string by a delimiter with a maximum number of splits.",
            overload_generic_parameters=[pa.large_string(), pa.large_string(), pa.int64()],
            overload_generic_return=pa.list_(pa.large_string()),
            pybind_function="split",
            python_fallback=None,
        ),
    ],
    "starts_with": [
        ChalkFunctionOverload(
            function_name="starts_with",
            description="Checks if a string starts with a specified prefix.",
            overload_generic_parameters=[pa.large_string(), pa.large_string()],
            overload_generic_return=pa.bool_(),
            pybind_function="starts_with",
            python_fallback=None,
        ),
    ],
    "ends_with": [
        ChalkFunctionOverload(
            function_name="ends_with",
            description="Checks if a string ends with a specified suffix.",
            overload_generic_parameters=[pa.large_string(), pa.large_string()],
            overload_generic_return=pa.bool_(),
            pybind_function="ends_with",
            python_fallback=None,
        ),
    ],
    "like": [
        ChalkFunctionOverload(
            function_name="like",
            description="Checks if a string matches a pattern using SQL LIKE syntax with wildcards.",
            overload_generic_parameters=[pa.large_string(), pa.large_string()],
            overload_generic_return=pa.bool_(),
            pybind_function="like",
            python_fallback=None,
        )
    ],
    "regexp_like": [
        ChalkFunctionOverload(
            function_name="regexp_like",
            description="Checks if a string matches a regular expression pattern.",
            overload_generic_parameters=[pa.large_string(), pa.large_string()],
            overload_generic_return=pa.bool_(),
            pybind_function="regexp_like",
            python_fallback=None,
        )
    ],
    "regexp_extract": [
        ChalkFunctionOverload(
            function_name="regexp_extract",
            description="Returns the first substring matched by the regular expression pattern in string.",
            overload_generic_parameters=[pa.large_string(), pa.large_string()],
            overload_generic_return=pa.large_string(),
            pybind_function="regexp_extract",
            python_fallback=None,
        )
    ]
    + [
        ChalkFunctionOverload(
            function_name="regexp_extract",
            description="Returns the first substring matched by the regular expression pattern in string and returns the capturing group number group.",
            overload_generic_parameters=[pa.large_string(), pa.large_string(), pa.int64()],
            overload_generic_return=pa.large_string(),
            pybind_function="regexp_extract",
            python_fallback=None,
        )
    ],
    "regexp_extract_all": [
        ChalkFunctionOverload(
            function_name="regexp_extract_all",
            description="Returns the substring(s) matched by the regular expression pattern in string.",
            overload_generic_parameters=[pa.large_string(), pa.large_string()],
            overload_generic_return=list_type(pa.large_string()),
            pybind_function="regexp_extract_all",
            python_fallback=None,
        )
        for list_type in PA_LIST_TYPES
    ]
    + [
        ChalkFunctionOverload(
            function_name="regexp_extract_all",
            description="Returns the substring(s) matched by the regular expression pattern in string and returns the capturing group number group.",
            overload_generic_parameters=[pa.large_string(), pa.large_string(), pa.int64()],
            overload_generic_return=list_type(pa.large_string()),
            pybind_function="regexp_extract_all",
            python_fallback=None,
        )
        for list_type in PA_LIST_TYPES
    ],
    "boost_regexp_findall": [
        ChalkFunctionOverload(
            function_name="boost_regexp_findall",
            description="Finds all matches of a regular expression pattern in a string and returns them as a list.",
            overload_generic_parameters=[pa.large_string(), pa.large_string()],
            overload_generic_return=pa.large_list(pa.large_string()),
            pybind_function="boost_regexp_findall",
            python_fallback=None,
        )
    ],
    "regexp_replace": [
        ChalkFunctionOverload(
            function_name="regexp_replace",
            description="Replaces all matches of a regular expression pattern with a replacement string.",
            overload_generic_parameters=[
                pa.large_string(),
                pa.large_string(),
                pa.large_string(),
            ],
            overload_generic_return=pa.large_string(),
            pybind_function="regexp_replace",
            python_fallback=None,
        ),
        ChalkFunctionOverload(
            function_name="regexp_replace",
            description="Removes all matches of a regular expression pattern from a string.",
            overload_generic_parameters=[
                pa.large_string(),
                pa.large_string(),
            ],
            overload_generic_return=pa.large_string(),
            pybind_function="regexp_replace",
            python_fallback=None,
        ),
    ],
    "replace": [
        ChalkFunctionOverload(
            function_name="replace",
            description="Replaces all occurrences of a substring with another string.",
            overload_generic_parameters=[
                pa.large_string(),
                pa.large_string(),
                pa.large_string(),
            ],
            overload_generic_return=pa.large_string(),
            pybind_function="replace",
            python_fallback=None,
        ),
    ],
    "jaccard_similarity": [
        ChalkFunctionOverload(
            function_name="jaccard_similarity",
            description="Calculates the Jaccard similarity coefficient between two strings based on character sets.",
            overload_generic_parameters=[
                pa.large_string(),
                pa.large_string(),
            ],
            overload_generic_return=pa.float64(),
            pybind_function="jaccard_similarity",
            python_fallback=None,
        ),
    ],
    "cardinality": [
        ChalkFunctionOverload(
            function_name="cardinality",
            description="Returns the number of elements in a list.",
            overload_generic_parameters=[list_type(generic("V"))],
            overload_generic_return=pa.int64(),
            pybind_function="cardinality",
            python_fallback=None,
        )
        for list_type in PA_LIST_TYPES
    ],
    "spooky_hash_v2_64": [
        ChalkFunctionOverload(
            function_name="spooky_hash_v2_64",
            description="Computes a 64-bit SpookyHash V2 hash of binary data.",
            overload_generic_parameters=[pa.large_binary()],
            overload_generic_return=pa.binary(),
            pybind_function="spooky_hash_v2_64",
        ),
    ],
    "spooky_hash_v2_32": [
        ChalkFunctionOverload(
            function_name="spooky_hash_v2_32",
            description="Computes a 32-bit SpookyHash V2 hash of binary data.",
            overload_generic_parameters=[pa.large_binary()],
            overload_generic_return=pa.binary(),
            pybind_function="spooky_hash_v2_32",
        ),
    ],
    "to_hex": [
        ChalkFunctionOverload(
            function_name="to_hex",
            description="Converts binary data to its hexadecimal string representation.",
            overload_generic_parameters=[pa.large_binary()],
            overload_generic_return=pa.large_string(),
            pybind_function="to_hex",
            # python_fallback=None,
        ),
    ],
    "from_utf8": [
        ChalkFunctionOverload(
            function_name="from_utf8",
            description="Decodes UTF-8 encoded binary data into a string.",
            overload_generic_parameters=[pa.large_binary()],
            overload_generic_return=pa.large_string(),
            pybind_function="from_utf8",
            python_fallback=None,
        ),
    ],
    "to_utf8": [
        ChalkFunctionOverload(
            function_name="to_utf8",
            description="Encodes a string to UTF-8 binary data.",
            overload_generic_parameters=[pa.large_string()],
            overload_generic_return=pa.large_binary(),
            pybind_function="to_utf8",
            python_fallback=None,
        ),
    ],
    "md5": [
        ChalkFunctionOverload(
            function_name="md5",
            description="Computes the MD5 hash of binary data.",
            overload_generic_parameters=[pa.large_binary()],
            overload_generic_return=pa.binary(),
            pybind_function="md5",
            python_fallback=None,
        ),
    ],
    "sha1": [
        ChalkFunctionOverload(
            function_name="sha1",
            description="Computes the SHA-1 hash of binary data.",
            overload_generic_parameters=[pa.large_binary()],
            overload_generic_return=pa.binary(),
            pybind_function="sha1",
            python_fallback=None,
        ),
    ],
    "sha256": [
        ChalkFunctionOverload(
            function_name="sha256",
            description="Computes the SHA-256 hash of binary data.",
            overload_generic_parameters=[pa.large_binary()],
            overload_generic_return=pa.binary(),
            pybind_function="sha256",
            python_fallback=None,
        ),
    ],
    "sha512": [
        ChalkFunctionOverload(
            function_name="sha512",
            description="Computes the SHA-512 hash of binary data.",
            overload_generic_parameters=[pa.large_binary()],
            overload_generic_return=pa.binary(),
            pybind_function="sha512",
            python_fallback=None,
        ),
    ],
    "gunzip": [
        ChalkFunctionOverload(
            function_name="gunzip",
            description="gunzip the input binary data.",
            overload_generic_parameters=[bin_type],
            overload_generic_return=bin_type,
            pybind_function="gunzip",
            python_fallback=None,
        )
        for bin_type in PA_BINARY_TYPES
    ],
    "hamming_distance": [
        ChalkFunctionOverload(
            function_name="hamming_distance",
            description="Returns the Hamming distance of string1 and string2, i.e. the number of positions at which the corresponding characters are different. Note that the two strings must have the same length.",
            overload_generic_parameters=[str_type, str_type],
            overload_generic_return=pa.int64(),
            pybind_function="hamming_distance",
            python_fallback=None,
        )
        for str_type in PA_STRING_TYPES
    ],
    "format_datetime": [
        ChalkFunctionOverload(
            function_name="format_datetime",
            description="Formats a datetime using a specified format string.",
            overload_generic_parameters=[
                pa.timestamp("us", tz="UTC"),
                pa.large_string(),
            ],
            overload_generic_return=pa.string(),
            pybind_function="format_datetime",
            python_fallback=None,
        ),
    ],
    "zi_split_part": [
        ChalkFunctionOverload(
            function_name="zi_split_part",
            description="Splits a string by delimiter and returns the part at the specified zero-based index.",
            overload_generic_parameters=[
                pa.large_string(),
                pa.large_string(),
                pa.int64(),
            ],
            overload_generic_return=pa.large_string(),
            pybind_function="zeroindex_split_part",
            python_fallback=None,
        )
    ],
    "scalar_min": [
        ChalkFunctionOverload(
            function_name="scalar_min",
            description="Returns the minimum of two scalar values.",
            overload_generic_parameters=[num, num],
            overload_generic_return=num,
            pybind_function="scalar_min",
            python_fallback=None,
        )
        for num in PA_NUM_AND_TIME_TYPES
    ],
    "scalar_max": [
        ChalkFunctionOverload(
            function_name="scalar_max",
            description="Returns the maximum of two scalar values.",
            overload_generic_parameters=[num, num],
            overload_generic_return=num,
            pybind_function="scalar_max",
            python_fallback=None,
        )
        for num in PA_NUM_AND_TIME_TYPES
    ],
    "%": [
        ChalkFunctionOverload(
            function_name="%",
            description="Calculates the modulo (remainder) of two integers.",
            overload_generic_parameters=[pa.int64(), pa.int64()],
            overload_generic_return=pa.int64(),
            pybind_function="mod",
            python_fallback=None,
        ),
        ChalkFunctionOverload(
            function_name="%",
            description="Calculates the modulo (remainder) of two floating-point numbers.",
            overload_generic_parameters=[pa.float64(), pa.float64()],
            overload_generic_return=pa.float64(),
            pybind_function="mod",
            python_fallback=None,
        ),
    ],
    "negate": [
        ChalkFunctionOverload(
            function_name="negate",
            description="Returns the negative value of a number.",
            overload_generic_parameters=[num_type],
            overload_generic_return=num_type,
            pybind_function="negate",
            python_fallback=None,
        )
        for num_type in PA_LARGEST_NUM_TYPES
    ],
    "is_nan": [
        ChalkFunctionOverload(
            function_name="is_nan",
            description="Checks if a floating-point number is NaN (Not a Number).",
            overload_generic_parameters=[pa.float64()],
            overload_generic_return=pa.bool_(),
            pybind_function="is_nan",
            python_fallback=None,
        ),
    ],
    "is_null": [
        ChalkFunctionOverload(
            function_name="is_null",
            description="Checks if the input is null.",
            overload_generic_parameters=[generic("T")],
            overload_generic_return=pa.bool_(),
            pybind_is_method=True,
            pybind_function="is_null",
            python_fallback=None,
        ),
    ],
    "element_at": [
        ChalkFunctionOverload(
            function_name="element_at",
            description="Returns the element at the specified index in a list.",
            overload_generic_parameters=[
                list_type(generic("E")),
                pa.int64(),
            ],
            overload_generic_return=generic("E"),
            # Velox calls this function 'element_at', and overloads it for both
            # arrays and maps.
            pybind_function="element_at",
            python_fallback=None,
        )
        for list_type in PA_LIST_TYPES
    ],
    "python_element_at": [
        ChalkFunctionOverload(
            function_name="python_element_at",
            description="Returns the element at the specified Python-style index in a list.",
            overload_generic_parameters=[
                list_type(generic("E")),
                pa.int64(),
            ],
            overload_generic_return=generic("E"),
            pybind_function="python_element_at",
            python_fallback=None,
        )
        for list_type in PA_LIST_TYPES
    ],
    "array_constructor": [
        ChalkFunctionOverload(
            function_name="array_constructor",
            description="Creates an array from a variable number of arguments.",
            overload_generic_parameters=[
                VariadicType(element_type=generic("T")),
            ],
            overload_generic_return=pa.list_(generic("T")),
            pybind_function="array_constructor",
            python_fallback=None,
        )
    ],
    "array_frequency": [
        ChalkFunctionOverload(
            function_name="array_frequency",
            description="Returns a map of elements to their frequency counts in an array.",
            overload_generic_parameters=[pa.large_list(generic("T"))],
            overload_generic_return=pa.map_(generic("T"), pa.int64()),
            pybind_function="array_frequency",
            python_fallback=None,
        ),
    ],
    "cosine_similarity_vector": [
        ChalkFunctionOverload(
            function_name="cosine_similarity_vector",
            description="Returns the cosine similarity between the vectors.",
            overload_generic_parameters=[list_type(float_type_1), list_type(float_type_2)],
            overload_generic_return=max(float_type_1, float_type_2, key=lambda float_type: float_type.byte_width),  # pyright: ignore[reportAttributeAccessIssue]
            pybind_function="cosine_similarity_vector",
            python_fallback=None,
        )
        for list_type in PA_LIST_TYPES
        for float_type_1 in (pa.float16(), pa.float32(), pa.float64())
        for float_type_2 in (pa.float16(), pa.float32(), pa.float64())
    ],
    "dot_product_vector": [
        ChalkFunctionOverload(
            function_name="dot_product_vector",
            description="Returns the dot product between the vectors.",
            overload_generic_parameters=[list_type(float_type_1), list_type(float_type_2)],
            overload_generic_return=max(float_type_1, float_type_2, key=lambda float_type: float_type.byte_width),  # pyright: ignore[reportAttributeAccessIssue]
            pybind_function="dot_product_vector",
            python_fallback=None,
        )
        for list_type in PA_LIST_TYPES
        for float_type_1 in (pa.float16(), pa.float32(), pa.float64())
        for float_type_2 in (pa.float16(), pa.float32(), pa.float64())
    ],
    "map_keys_by_top_n_values": [
        ChalkFunctionOverload(
            function_name="map_keys_by_top_n_values",
            description="Returns the keys of a map ordered by their top N highest values.",
            overload_generic_parameters=[pa.map_(generic("K"), generic("V")), pa.int64()],
            overload_generic_return=pa.list_(generic("K")),
            pybind_function="map_keys_by_top_n_values",
            python_fallback=None,
        ),
    ],
    "map_get": [
        ChalkFunctionOverload(
            function_name="map_get",
            description="Retrieves the value associated with a key from a map.",
            overload_generic_parameters=[
                pa.map_(generic("K"), generic("V")),
                generic("K"),
            ],
            overload_generic_return=generic("V"),
            # Velox calls this function 'element_at', and overloads it for both
            # arrays and maps.
            pybind_function="element_at",
            python_fallback=None,
        ),
        # This hack allows down-casting the lookup key. Without this overload, the customer needs
        # to manually cast the key to the smaller type.
        ChalkFunctionOverload(
            function_name="map_get",
            description="Retrieves the value associated with a string key from a map with automatic key type casting.",
            overload_generic_parameters=[
                pa.map_(pa.string(), generic("V")),
                pa.large_string(),
            ],
            overload_generic_return=generic("V"),
            # Velox calls this function 'element_at', and overloads it for both
            # arrays and maps.
            pybind_function="element_at",
            python_fallback=None,
        ),
    ],
    "slice": [
        ChalkFunctionOverload(
            function_name="slice",
            description="Returns a slice of a list starting at the given position for the specified length.",
            overload_generic_parameters=[
                list_type(generic("E")),
                pa.int64(),
                pa.int64(),
            ],
            overload_generic_return=list_type(generic("E")),
            pybind_function="slice",
            python_fallback=None,
        )
        for list_type in PA_LIST_TYPES
    ],
    "contains": [
        ChalkFunctionOverload(
            function_name="contains",
            description="Checks if a list contains a specific element.",
            overload_generic_parameters=[
                pa.large_list(generic("V")),
                generic("V"),
            ],
            overload_generic_return=pa.bool_(),
            pybind_function="contains",
            python_fallback=None,
        ),
    ],
    "map_contains": [
        ChalkFunctionOverload(
            function_name="map_contains",
            description="Checks if a map contains any keys that match a given condition.",
            overload_generic_parameters=[
                pa.map_(generic("K"), generic("V")),
                CallbackType(input_types=[generic("k")], output_type=pa.bool_()),
            ],
            overload_generic_return=pa.bool_(),
            pybind_function="any_keys_match",
            python_fallback=None,
        ),
    ],
    "date_trunc": [
        ChalkFunctionOverload(
            function_name="date_trunc",
            description="Truncates a timestamp to the specified time unit (e.g., day, month, year).",
            overload_generic_parameters=[
                pa.large_string(),
                pa.timestamp("us", tz="UTC"),
            ],
            overload_generic_return=pa.timestamp("us", tz="UTC"),
            pybind_function="date_trunc",
        ),
    ],
    "array_average": [
        ChalkFunctionOverload(
            function_name="array_average",
            description="Calculates the average of numeric values in an array.",
            overload_generic_parameters=[list_type(pa.float64())],
            overload_generic_return=pa.float64(),
            pybind_function="array_average",
            python_fallback=None,
        )
        for list_type in PA_LIST_TYPES
    ],
    "array_sort_desc": [
        ChalkFunctionOverload(
            function_name="array_sort_desc",
            description="Sorts an array in descending order.",
            overload_generic_parameters=[list_type(generic("T"))],
            overload_generic_return=list_type(generic("T")),
            pybind_function="array_sort_desc",
            python_fallback=None,
        )
        for list_type in PA_LIST_TYPES
    ],
    "array_filter": [
        ChalkFunctionOverload(
            function_name="array_filter",
            description="Filters an array using a callback function predicate.",
            overload_generic_parameters=[
                pa.large_list(generic("T")),
                CallbackType(input_types=[generic("T")], output_type=pa.bool_()),
            ],
            overload_generic_return=pa.large_list(generic("T")),
            pybind_function="filter",
            python_fallback=None,
        )
    ],
    "array_distinct": [
        ChalkFunctionOverload(
            function_name="array_distinct",
            description="Returns an array with duplicate elements removed, preserving order.",
            overload_generic_parameters=[list_type(generic("T"))],
            overload_generic_return=list_type(generic("T")),
            pybind_function="array_distinct",
            python_fallback=None,
        )
        for list_type in PA_LIST_TYPES
    ],
    "array_max": [
        ChalkFunctionOverload(
            function_name="array_max",
            description="Returns the maximum element in an array.",
            overload_generic_parameters=[list_type(generic("T"))],
            overload_generic_return=generic("T"),
            pybind_function="array_max",
            python_fallback=None,
        )
        for list_type in PA_LIST_TYPES
    ],
    "array_min": [
        ChalkFunctionOverload(
            function_name="array_min",
            description="Returns the minimum element in an array.",
            overload_generic_parameters=[list_type(generic("T"))],
            overload_generic_return=generic("T"),
            pybind_function="array_min",
            python_fallback=None,
        )
        for list_type in PA_LIST_TYPES
    ],
    "array_sort": [
        ChalkFunctionOverload(
            function_name="array_sort",
            description="Sorts an array in ascending order.",
            overload_generic_parameters=[list_type(generic("T"))],
            overload_generic_return=pa.list_(generic("T")),
            pybind_function="array_sort",
            python_fallback=None,
        )
        for list_type in PA_LIST_TYPES
    ],
    "array_stddev": [
        ChalkFunctionOverload(
            function_name="array_stddev",
            description="Calculates the standard deviation of numeric values in an array.",
            overload_generic_parameters=[list_type(pa.float64()), pa.bool_()],
            overload_generic_return=pa.float64(),
            pybind_function="array_stddev",
            python_fallback=None,
        )
        for list_type in PA_LIST_TYPES
    ],
    "array_median": [
        ChalkFunctionOverload(
            function_name="array_median",
            description="Calculates the median value of numeric elements in an array.",
            overload_generic_parameters=[list_type(pa.float64())],
            overload_generic_return=pa.float64(),
            pybind_function="array_median",
            python_fallback=None,
        )
        for list_type in PA_LIST_TYPES
    ],
    "array_mode": [
        *(
            ChalkFunctionOverload(
                function_name="array_mode",
                description="Returns the most frequently occurring element in an array.",
                overload_generic_parameters=[list_type(arg_type)],
                overload_generic_return=arg_type,
                pybind_function="array_mode",
                python_fallback=None,
            )
            for list_type in PA_LIST_TYPES
            for arg_type in (pa.int64(), pa.float64(), *PA_STRING_TYPES)
        ),
        *(
            ChalkFunctionOverload(
                function_name="array_mode",
                description="Returns the most frequently occurring element in an array with mode selection option.",
                overload_generic_parameters=[list_type(arg_type), pa.int64()],
                overload_generic_return=arg_type,
                pybind_function="array_mode",
                python_fallback=None,
            )
            for list_type in PA_LIST_TYPES
            for arg_type in (pa.int64(), pa.float64(), *PA_STRING_TYPES)
        ),
    ],
    "array_multimode": [
        *(
            ChalkFunctionOverload(
                function_name="array_multimode",
                description="Returns all most frequently occurring elements in an array.",
                overload_generic_parameters=[list_type(elem_type)],
                overload_generic_return=list_type(elem_type),
                pybind_function="array_multimode",
                python_fallback=None,
            )
            for list_type in PA_LIST_TYPES
            for elem_type in (pa.int64(), pa.float64(), *PA_STRING_TYPES)
        ),
    ],
    "array_sum": [
        ChalkFunctionOverload(
            function_name="array_sum",
            description="Calculates the sum of numeric values in an array.",
            overload_generic_parameters=[list_type(num_type)],
            overload_generic_return=num_type,
            pybind_function="array_sum",
            python_fallback=None,
        )
        for list_type in PA_LIST_TYPES
        for num_type in PA_LARGEST_NUM_TYPES
    ],
    "h3_lat_lon_to_cell": [
        ChalkFunctionOverload(
            function_name="h3_lat_lon_to_cell",
            description="Calculates the h3 cell for a given lat-lon.",
            overload_generic_parameters=[
                ft,
                ft,
                dt,
            ],
            overload_generic_return=pa.large_string(),
            pybind_function="h3_lat_lon_to_cell",
        )
        for dt in PA_INT_TYPES
        for ft in PA_NUM_TYPES
    ],
    "h3_cell_to_lat_lon_radians": [
        ChalkFunctionOverload(
            function_name="h3_cell_to_lat_lon_radians",
            description="Calculates the lat-lon for a given h3 cell.",
            overload_generic_parameters=[pa.large_string()],
            overload_generic_return=pa.struct(
                {
                    "lat_radians": pa.float64(),
                    "lon_radians": pa.float64(),
                }
            ),
            pybind_function="h3_cell_to_lat_lon_radians",
        )
    ],
    "h3_cell_to_lat_lon_degrees": [
        ChalkFunctionOverload(
            function_name="h3_cell_to_lat_lon_degrees",
            description="Calculates the lat-lon in degrees for a given h3 cell.",
            overload_generic_parameters=[pa.large_string()],
            overload_generic_return=pa.struct(
                {
                    "lat": pa.float64(),
                    "lon": pa.float64(),
                }
            ),
            pybind_function="h3_cell_to_lat_lon_degrees",
        )
    ],
    "jaro_winkler_distance": [
        ChalkFunctionOverload(
            function_name="jaro_winkler_distance",
            description="Calculates the Jaro-Winkler distance between two strings.",
            overload_generic_parameters=[
                pa.large_string(),
                pa.large_string(),
                pa.float64(),
            ],
            overload_generic_return=pa.float64(),
            pybind_function="jaro_winkler_distance",
        )
    ],
    "partial_ratio": [
        ChalkFunctionOverload(
            function_name="partial_ratio",
            description="Calculates the partial ratio similarity between two strings using fuzzy matching.",
            overload_generic_parameters=[pa.large_string(), pa.large_string()],
            overload_generic_return=pa.float64(),
            pybind_function="partial_ratio",
        )
    ],
    "token_set_ratio": [
        ChalkFunctionOverload(
            function_name="token_set_ratio",
            description="Calculates the token set ratio similarity between two strings using fuzzy matching.",
            overload_generic_parameters=[pa.large_string(), pa.large_string()],
            overload_generic_return=pa.float64(),
            pybind_function="token_set_ratio",
        )
    ],
    "token_sort_ratio": [
        ChalkFunctionOverload(
            function_name="token_sort_ratio",
            description="Calculates the token sort ratio similarity between two strings using fuzzy matching.",
            overload_generic_parameters=[pa.large_string(), pa.large_string()],
            overload_generic_return=pa.float64(),
            pybind_function="token_sort_ratio",
        )
    ],
    "unidecode_normalize": [
        ChalkFunctionOverload(
            function_name="unidecode_normalize",
            description="Normalizes Unicode characters to their closest ASCII equivalents with whitespace normalization.",
            overload_generic_parameters=[pa.large_string()],
            overload_generic_return=pa.large_string(),
            pybind_function="unidecode_normalize",
        )
    ],
    "unidecode_to_ascii": [
        ChalkFunctionOverload(
            function_name="unidecode_to_ascii",
            description="Converts Unicode characters to their closest ASCII equivalents.",
            overload_generic_parameters=[pa.large_string()],
            overload_generic_return=pa.large_string(),
            pybind_function="unidecode_to_ascii",
        )
    ],
    "codepoint": [
        ChalkFunctionOverload(
            function_name="codepoint",
            description="Returns the Unicode code point of the only character of the string.",
            overload_generic_parameters=[str_type],
            overload_generic_return=pa.int32(),
            pybind_function="codepoint",
        )
        for str_type in PA_STRING_TYPES
    ],
    "concat": [
        ChalkFunctionOverload(
            function_name="concat",
            description="Concatenates two or more strings together.",
            overload_generic_parameters=[
                pa.large_string(),
                pa.large_string(),
                VariadicType(element_type=pa.large_string()),
            ],
            overload_generic_return=pa.large_string(),
            pybind_function="concat",
            python_fallback=None,
        ),
        *[
            ChalkFunctionOverload(
                function_name="concat",
                description="Concatenates two or more lists together.",
                overload_generic_parameters=[
                    list_type(generic("T")),
                    VariadicType(element_type=list_type(generic("T"))),
                ],
                overload_generic_return=list_type(generic("T")),
                pybind_function="concat",
                python_fallback=None,
            )
            for list_type in PA_LIST_TYPES
        ],
    ],
    "current_date": [
        ChalkFunctionOverload(
            function_name="current_date",
            description="Returns the current date.",
            overload_generic_parameters=[],
            overload_generic_return=pa.date32(),
            pybind_function="current_date",
            python_fallback=None,
        ),
    ],
    "log2": [
        ChalkFunctionOverload(
            function_name="log2",
            description="Calculates the base-2 logarithm of a number.",
            overload_generic_parameters=[pa.float64()],
            overload_generic_return=pa.float64(),
            pybind_function="log2",
            python_fallback=None,
        ),
    ],
    "log10": [
        ChalkFunctionOverload(
            function_name="log10",
            description="Calculates the base-10 logarithm of a number.",
            overload_generic_parameters=[pa.float64()],
            overload_generic_return=pa.float64(),
            pybind_function="log10",
            python_fallback=None,
        ),
    ],
    "abs": [
        ChalkFunctionOverload(
            function_name="abs",
            description="Returns the absolute value of a number.",
            overload_generic_parameters=[num_type],
            overload_generic_return=num_type,
            pybind_function="abs",
            python_fallback=None,
        )
        for num_type in PA_LARGEST_NUM_TYPES
    ],
    "truncate": [
        ChalkFunctionOverload(
            function_name="truncate",
            description="Truncates a floating-point number to remove the decimal part.",
            overload_generic_parameters=[pa.float64()],
            overload_generic_return=pa.float64(),
            pybind_function="truncate",
            python_fallback=None,
        ),
    ],
    "floor": [
        ChalkFunctionOverload(
            function_name="floor",
            description="Returns the largest integer less than or equal to the given number.",
            overload_generic_parameters=[float_type],
            overload_generic_return=float_type,
            pybind_function="floor",
            python_fallback=None,
        )
        for float_type in PA_FLOAT_TYPES
    ],
    "ceiling": [
        ChalkFunctionOverload(
            function_name="ceiling",
            description="Returns the smallest integer greater than or equal to the given number.",
            overload_generic_parameters=[float_type],
            overload_generic_return=float_type,
            pybind_function="ceiling",
            python_fallback=None,
        )
        for float_type in PA_FLOAT_TYPES
    ],
    "ceil": [
        ChalkFunctionOverload(
            function_name="ceiling",
            description="Returns the smallest integer greater than or equal to the given number.",
            overload_generic_parameters=[float_type],
            overload_generic_return=float_type,
            pybind_function="ceiling",
            python_fallback=None,
        )
        for float_type in PA_FLOAT_TYPES
    ],
    "reverse": [
        ChalkFunctionOverload(
            function_name="reverse",
            description="Reverses the characters in a string.",
            overload_generic_parameters=[string],
            overload_generic_return=string,
            pybind_function="reverse",
            python_fallback=None,
        )
        for string in PA_STRING_TYPES
    ],
    "trail": [
        ChalkFunctionOverload(
            function_name="trail",
            description="Returns the last N characters of the input string up to at most the length of string.",
            overload_generic_parameters=[s, pa.int64()],
            overload_generic_return=s,
            pybind_function="trail",
            python_fallback=None,
        )
        for s in (pa.string(), pa.large_string(), pa.binary(), pa.large_binary())
    ],
    "substr": [
        ChalkFunctionOverload(
            function_name="substr",
            description="Returns a substring starting at the specified position.",
            overload_generic_parameters=[s, pa.int64()],
            overload_generic_return=s,
            pybind_function="substr",
            # you can't be passed a slice in python
            python_fallback=None,
        )
        for s in (pa.string(), pa.large_string(), pa.binary(), pa.large_binary())
    ]
    + [
        ChalkFunctionOverload(
            function_name="substr",
            description="Returns a substring starting at the specified position with the given length.",
            overload_generic_parameters=[s, pa.int64(), pa.int64()],
            overload_generic_return=s,
            pybind_function="substr",
            # you can't be passed a slice in python
            python_fallback=None,
        )
        for s in (pa.string(), pa.large_string(), pa.binary(), pa.large_binary())
    ],
    "fail": [
        ChalkFunctionOverload(
            function_name="fail",
            description="Raises an error with the specified error message.",
            overload_generic_parameters=[s],
            overload_generic_return=pa.null(),
            pybind_function="fail",
            python_fallback=None,
        )
        for s in (pa.string(), pa.large_string())
    ],
    "try_": [
        ChalkFunctionOverload(
            function_name="try_",
            description="Attempts to execute an expression and handles any errors gracefully.",
            overload_generic_parameters=[generic("T")],
            overload_generic_return=generic("T"),
            pybind_function="try_",
            python_fallback=None,
        )
    ],
    "python_range": [
        ChalkFunctionOverload(
            function_name="python_range",
            description="Creates a range of integers with Python-like semantics.",
            overload_generic_parameters=[pa.int64()] * i,
            overload_generic_return=pa.large_list(pa.int64()),
            pybind_function="python_range",
            python_fallback=None,
        )
        for i in range(1, 4)
    ],
    "get_json_value": [
        ChalkFunctionOverload(
            function_name="json_extract",
            description="Extracts a value from JSON using a path expression.",
            overload_generic_parameters=[pyarrow_json_type(), pa.large_string()],
            overload_generic_return=pyarrow_json_type(),
            pybind_function="json_extract",
            python_fallback=None,
        ),
        ChalkFunctionOverload(
            function_name="json_extract",
            description="Extracts a value from JSON string using a path expression.",
            overload_generic_parameters=[pa.large_string(), pa.large_string()],
            overload_generic_return=pyarrow_json_type(),
            pybind_function="json_extract",
            python_fallback=None,
        ),
    ],
    "json_extract_array": [
        ChalkFunctionOverload(
            function_name="json_extract_array",
            description="Extracts an array from JSON string using a path expression.",
            overload_generic_parameters=[pa.large_string(), pa.large_string()],
            overload_generic_return=pa.large_list(pyarrow_json_type()),
            pybind_function="json_extract_array",
            python_fallback=None,
        ),
        ChalkFunctionOverload(
            function_name="json_extract_array",
            description="Extracts an array from JSON string using a path expression.",
            overload_generic_parameters=[pyarrow_json_type(), pa.large_string()],
            overload_generic_return=pa.large_list(pyarrow_json_type()),
            pybind_function="json_extract_array",
            python_fallback=None,
        ),
    ],
    "jsonify": [
        ChalkFunctionOverload(
            function_name="jsonify",
            description="Converts an arbitrary value into a JSON string",
            overload_generic_parameters=[generic("T")],
            overload_generic_return=pa.large_string(),
            pybind_function="jsonify",
            python_fallback=None,
        ),
    ],
    "coalesce": [
        ChalkFunctionOverload(
            function_name="coalesce",
            description="Returns the first non-null value from a list of arguments.",
            overload_generic_parameters=[VariadicType(element_type=generic("T"))],
            overload_generic_return=generic("T"),
            pybind_function="coalesce",
            pybind_is_method=True,
            pybind_method_pack_arguments=True,
            python_fallback=None,
        )
    ],
    "recover": [
        ChalkFunctionOverload(
            function_name="coalesce",
            description="Return the first valid entry. Functions like coalesce, but allows recovering from an upstream failure",
            overload_generic_parameters=[VariadicType(element_type=generic("T"))],
            overload_generic_return=generic("T"),
            pybind_function="coalesce",
            pybind_is_method=True,
            pybind_method_pack_arguments=True,
            python_fallback=None,
            convert_input_errors_to_none=True,
        )
    ],
    "between": [
        ChalkFunctionOverload(
            function_name="between",
            description="Checks if a floating-point value is between two bounds (inclusive).",
            overload_generic_parameters=[pa.float64(), pa.float64(), pa.float64()],
            overload_generic_return=pa.bool_(),
            pybind_function="between",
            python_fallback=None,
        ),
        ChalkFunctionOverload(
            function_name="between",
            description="Checks if an integer value is between two bounds (inclusive).",
            overload_generic_parameters=[pa.int64(), pa.int64(), pa.int64()],
            overload_generic_return=pa.bool_(),
            pybind_function="between",
            python_fallback=None,
        ),
    ],
    "distinct_from": [
        ChalkFunctionOverload(
            function_name="distinct_from",
            description="Checks if two values are distinct, treating NULL values as different from non-NULL values.",
            overload_generic_parameters=[generic("T"), generic("T")],
            overload_generic_return=pa.bool_(),
            pybind_function="distinct_from",
            python_fallback=None,
        )
    ],
    "proto_to_struct": [
        ChalkFunctionOverload(
            function_name="proto_to_struct",
            description="Converts protobuf binary data to a structured format.",
            overload_generic_parameters=[pa.large_binary(), pa.large_string(), generic("T"), pa.large_binary()],
            overload_generic_return=generic("T"),
            pybind_function="proto_to_struct",
            python_fallback=None,
        )
    ],
    "struct_to_proto": [
        ChalkFunctionOverload(
            function_name="struct_to_proto",
            description="Converts structured data to protobuf binary format.",
            overload_generic_parameters=[pa.large_binary(), pa.large_string(), generic("T")],
            overload_generic_return=pa.large_binary(),
            pybind_function="struct_to_proto",
            python_fallback=None,
        )
    ],
    "bytes_to_string_base64": [
        ChalkFunctionOverload(
            function_name="to_base64",
            description="Encodes binary into a base64 string representation.",
            overload_generic_parameters=[pa.large_binary()],
            overload_generic_return=pa.large_string(),
            pybind_function="to_base64",
            python_fallback=None,
        )
    ],
    "string_to_bytes_base64": [
        ChalkFunctionOverload(
            function_name="from_base64",
            description="Decodes a Base64-encoded string back into its original binary form. This function is capable of handling both fully padded and non-padded Base64 encoded strings. Partially padded Base64 strings are not supported and will result in a “UserError” status being returned.",
            overload_generic_parameters=[pa.large_string()],
            overload_generic_return=pa.large_binary(),
            pybind_function="from_base64",
            python_fallback=None,
        )
    ],
    "bytes_to_string_hex": [
        ChalkFunctionOverload(
            function_name="to_hex",  # NOTE - special case in compute_underscore to handle this case
            description="Encodes binary into a base64 string representation.",
            overload_generic_parameters=[pa.large_binary()],
            overload_generic_return=pa.large_string(),
            pybind_function="to_hex",
            python_fallback=None,
        )
    ],
    "string_to_bytes_hex": [
        ChalkFunctionOverload(
            function_name="from_hex",
            description="Decodes binary data from the hex encoded string.",
            overload_generic_parameters=[pa.large_string()],
            overload_generic_return=pa.large_binary(),
            pybind_function="from_hex",
            python_fallback=None,
        )
    ],
    "bytes_to_string_utf8": [
        ChalkFunctionOverload(
            function_name="from_utf8",  # NOT A TYPO
            description="Encodes binary into a base64 string representation.",
            overload_generic_parameters=[pa.large_binary()],
            overload_generic_return=pa.large_string(),
            pybind_function="from_utf8",
            python_fallback=None,
        )
    ],
    "string_to_bytes_utf8": [
        ChalkFunctionOverload(
            function_name="to_utf8",  # NOT A TYPO
            description="Encodes string into a UTF-8 varbinary representation.",
            overload_generic_parameters=[pa.large_string()],
            overload_generic_return=pa.large_binary(),
            pybind_function="to_utf8",
            python_fallback=None,
        )
    ],
    "if_else": [
        ChalkFunctionOverload(
            function_name="if_else",
            description="Returns the second argument if the condition is true, otherwise returns the third argument.",
            overload_generic_parameters=[pa.bool_(), generic("T"), generic("T")],
            overload_generic_return=generic("T"),
            pybind_function="if_else",
            python_fallback=None,
        )
    ],
    "zip": [
        ChalkFunctionOverload(
            function_name="zip",
            description="Combines two lists element-wise into a list of paired structures.",
            overload_generic_parameters=[pa.large_list(generic("T")), pa.large_list(generic("U"))],
            overload_generic_return=pa.large_list(
                pa.struct(
                    [
                        pa.field("f1", generic("T")),
                        pa.field("f2", generic("U")),
                    ]
                )
            ),
            pybind_function="zip",
            python_fallback=None,
        ),
    ],
    "python_zip": [
        ChalkFunctionOverload(
            function_name="python_zip",
            description="Combines multiple lists element-wise into a list of paired structures with Python semantics.",
            overload_generic_parameters=[pa.large_list(generic(chr(65 + j))) for j in range(i)],
            overload_generic_return=pa.large_list(
                pa.struct([pa.field(f"f{j}", generic(chr(65 + j))) for j in range(i)])
            ),
            pybind_function="python_zip",
            python_fallback=None,
        )
        for i in VELOX_ZIP_ARITIES
    ],
    "zip_with": [
        ChalkFunctionOverload(
            function_name="zip_with",
            description="Combines two lists element-wise using a callback function to transform paired elements.",
            overload_generic_parameters=[
                pa.large_list(generic("T")),
                pa.large_list(generic("U")),
                CallbackType(input_types=[generic("T"), generic("U")], output_type=generic("R")),
            ],
            overload_generic_return=pa.large_list(generic("R")),
            pybind_function="zip_with",
            python_fallback=None,
        )
    ],
    "url_decode": [
        ChalkFunctionOverload(
            function_name="url_decode",
            description="Decodes URL-encoded characters in a string.",
            overload_generic_parameters=[pa.large_string()],
            overload_generic_return=pa.large_string(),
            pybind_function="url_decode",
            python_fallback=None,
        ),
    ],
    "url_encode": [
        ChalkFunctionOverload(
            function_name="url_encode",
            description="URL-encodes special characters in a string.",
            overload_generic_parameters=[pa.large_string()],
            overload_generic_return=pa.large_string(),
            pybind_function="url_encode",
            python_fallback=None,
        ),
    ],
    "url_extract_fragment": [
        ChalkFunctionOverload(
            function_name="url_extract_fragment",
            description="Extracts the fragment portion (after #) from a URL.",
            overload_generic_parameters=[pa.large_string()],
            overload_generic_return=pa.large_string(),
            pybind_function="url_extract_fragment",
            python_fallback=None,
        ),
    ],
    "url_extract_host": [
        ChalkFunctionOverload(
            function_name="url_extract_host",
            description="Returns the host from a URL.",
            overload_generic_parameters=[pa.large_string()],
            overload_generic_return=pa.large_string(),
            pybind_function="url_extract_host",
            python_fallback=None,
        ),
    ],
    "url_extract_parameter": [
        ChalkFunctionOverload(
            function_name="url_extract_parameter",
            description="Extracts the value of a specific query parameter from a URL.",
            overload_generic_parameters=[pa.large_string(), pa.large_string()],
            overload_generic_return=pa.large_string(),
            pybind_function="url_extract_parameter",
            python_fallback=None,
        ),
    ],
    "url_extract_path": [
        ChalkFunctionOverload(
            function_name="url_extract_path",
            description="Returns the path from a URL.",
            overload_generic_parameters=[pa.large_string()],
            overload_generic_return=pa.large_string(),
            pybind_function="url_extract_path",
            python_fallback=None,
        ),
    ],
    "url_extract_port": [
        ChalkFunctionOverload(
            function_name="url_extract_port",
            description="Extracts the port number from a URL.",
            overload_generic_parameters=[pa.large_string()],
            overload_generic_return=pa.int64(),
            pybind_function="url_extract_port",
            python_fallback=None,
        ),
    ],
    "url_extract_protocol": [
        ChalkFunctionOverload(
            function_name="url_extract_protocol",
            description="Returns the protocol from a URL.",
            overload_generic_parameters=[pa.large_string()],
            overload_generic_return=pa.large_string(),
            pybind_function="url_extract_protocol",
            python_fallback=None,
        ),
    ],
    "url_extract_query": [
        ChalkFunctionOverload(
            function_name="url_extract_query",
            description="Extracts the query string portion (after ?) from a URL.",
            overload_generic_parameters=[pa.large_string()],
            overload_generic_return=pa.large_string(),
            pybind_function="url_extract_query",
            python_fallback=None,
        ),
    ],
    "crc32": [
        ChalkFunctionOverload(
            function_name="crc32",
            description="Calculates the CRC32 checksum of binary data.",
            overload_generic_parameters=[pa.large_binary()],
            overload_generic_return=pa.int64(),
            pybind_function="crc32",
            python_fallback=None,
        ),
    ],
    "from_base64": [
        ChalkFunctionOverload(
            function_name="from_base64",
            description="Decodes a Base64-encoded string to binary data.",
            overload_generic_parameters=[pa.large_string()],
            overload_generic_return=pa.large_binary(),
            pybind_function="from_base64",
            python_fallback=None,
        ),
    ],
    "from_base64url": [
        ChalkFunctionOverload(
            function_name="from_base64url",
            description="Decodes a Base64url-encoded string to binary data.",
            overload_generic_parameters=[pa.large_string()],
            overload_generic_return=pa.large_binary(),
            pybind_function="from_base64url",
            python_fallback=None,
        ),
    ],
    "from_hex": [
        ChalkFunctionOverload(
            function_name="from_hex",
            description="Converts a hexadecimal string to binary data.",
            overload_generic_parameters=[pa.large_string()],
            overload_generic_return=pa.large_binary(),
            pybind_function="from_hex",
            python_fallback=None,
        ),
    ],
    "hmac_md5": [
        ChalkFunctionOverload(
            function_name="hmac_md5",
            description="Computes HMAC-MD5 authentication code for data using a secret key.",
            overload_generic_parameters=[pa.large_binary(), pa.large_binary()],
            overload_generic_return=pa.large_binary(),
            pybind_function="hmac_md5",
            python_fallback=None,
        ),
    ],
    "hmac_sha1": [
        ChalkFunctionOverload(
            function_name="hmac_sha1",
            description="Computes HMAC-SHA1 authentication code for data using a secret key.",
            overload_generic_parameters=[pa.large_binary(), pa.large_binary()],
            overload_generic_return=pa.large_binary(),
            pybind_function="hmac_sha1",
            python_fallback=None,
        ),
    ],
    "hmac_sha256": [
        ChalkFunctionOverload(
            function_name="hmac_sha256",
            description="Computes HMAC-SHA256 authentication code for data using a secret key.",
            overload_generic_parameters=[pa.large_binary(), pa.large_binary()],
            overload_generic_return=pa.large_binary(),
            pybind_function="hmac_sha256",
            python_fallback=None,
        ),
    ],
    "hmac_sha512": [
        ChalkFunctionOverload(
            function_name="hmac_sha512",
            description="Computes HMAC-SHA512 authentication code for data using a secret key.",
            overload_generic_parameters=[pa.large_binary(), pa.large_binary()],
            overload_generic_return=pa.large_binary(),
            pybind_function="hmac_sha512",
            python_fallback=None,
        ),
    ],
    "to_base64": [
        ChalkFunctionOverload(
            function_name="to_base64",
            description="Encodes binary data to a Base64 string.",
            overload_generic_parameters=[pa.large_binary()],
            overload_generic_return=pa.large_string(),
            pybind_function="to_base64",
            python_fallback=None,
        ),
    ],
    "to_base64url": [
        ChalkFunctionOverload(
            function_name="to_base64url",
            description="Encodes binary data to a Base64url string.",
            overload_generic_parameters=[pa.large_binary()],
            overload_generic_return=pa.large_string(),
            pybind_function="to_base64url",
            python_fallback=None,
        ),
    ],
    "xxhash64": [
        ChalkFunctionOverload(
            function_name="xxhash64",
            description="Computes a 64-bit XXHash of binary data.",
            overload_generic_parameters=[pa.large_binary()],
            overload_generic_return=pa.int64(),
            pybind_function="xxhash64",
            python_fallback=None,
        ),
    ],
    "bitwise_and": [
        ChalkFunctionOverload(
            function_name="bitwise_and",
            description="Performs bitwise AND operation on two integer values.",
            overload_generic_parameters=[dt, dt],
            overload_generic_return=dt,
            pybind_function="bitwise_and",
            python_fallback=None,
        )
        for dt in PA_INT_TYPES
    ],
    "bitwise_not": [
        ChalkFunctionOverload(
            function_name="bitwise_not",
            description="Performs bitwise NOT operation (complement) on an integer value.",
            overload_generic_parameters=[dt],
            overload_generic_return=dt,
            pybind_function="bitwise_not",
            python_fallback=None,
        )
        for dt in PA_INT_TYPES
    ],
    "bitwise_or": [
        ChalkFunctionOverload(
            function_name="bitwise_or",
            description="Performs bitwise OR operation on two integer values.",
            overload_generic_parameters=[dt, dt],
            overload_generic_return=dt,
            pybind_function="bitwise_or",
            python_fallback=None,
        )
        for dt in PA_INT_TYPES
    ],
    "bitwise_xor": [
        ChalkFunctionOverload(
            function_name="bitwise_xor",
            description="Performs bitwise XOR operation on two integer values.",
            overload_generic_parameters=[dt, dt],
            overload_generic_return=dt,
            pybind_function="bitwise_xor",
            python_fallback=None,
        )
        for dt in PA_INT_TYPES
    ],
    "bitwise_arithmetic_shift_right": [
        ChalkFunctionOverload(
            function_name="bitwise_arithmetic_shift_right",
            description="Returns the arithmetic right shift operation on x in 2’s complement representation. shift must not be negative.",
            overload_generic_parameters=[dt, dt],
            overload_generic_return=dt,
            pybind_function="bitwise_arithmetic_shift_right",
            python_fallback=None,
        )
        for dt in (pa.int64(),)
    ],
    "bitwise_logical_shift_right": [
        ChalkFunctionOverload(
            function_name="bitwise_logical_shift_right",
            description="Returns the logical right shift operation on x (treated as bits-bit integer) shifted by shift. shift must not be negative.",
            overload_generic_parameters=[dt, dt, dt],  # x, shift, bits
            overload_generic_return=dt,
            pybind_function="bitwise_logical_shift_right",
            python_fallback=None,
        )
        for dt in (pa.int64(),)
    ],
    "bitwise_left_shift": [
        ChalkFunctionOverload(
            function_name="bitwise_left_shift",
            description="Returns the left shifted value of x.",
            overload_generic_parameters=[dt, dt],
            overload_generic_return=dt,
            pybind_function="bitwise_left_shift",
            python_fallback=None,
        )
        for dt in (pa.int64(),)
    ],
    "bitwise_right_shift": [
        ChalkFunctionOverload(
            function_name="bitwise_right_shift",
            description="Returns the logical right shifted value of x.",
            overload_generic_parameters=[dt, dt],
            overload_generic_return=dt,
            pybind_function="bitwise_right_shift",
            python_fallback=None,
        )
        for dt in (pa.int64(),)
    ],
    "bitwise_right_shift_arithmetic": [
        ChalkFunctionOverload(
            function_name="bitwise_right_shift_arithmetic",
            description="Returns the arithmetic right shift value of x.",
            overload_generic_parameters=[dt, dt],
            overload_generic_return=dt,
            pybind_function="bitwise_right_shift_arithmetic",
            python_fallback=None,
        )
        for dt in (pa.int64(),)
    ],
    "bitwise_shift_left": [
        ChalkFunctionOverload(
            function_name="bitwise_shift_left",
            description="Returns the left shift operation on x (treated as bits-bit integer) shifted by shift. shift must not be negative.",
            overload_generic_parameters=[dt, dt],
            overload_generic_return=dt,
            pybind_function="bitwise_shift_left",
            python_fallback=None,
        )
        for dt in (pa.int64(),)
    ],
    "array_cum_sum": [
        ChalkFunctionOverload(
            function_name="array_cum_sum",
            description="Calculates the cumulative sum of numeric values in an array.",
            overload_generic_parameters=[list_type(num_type)],
            overload_generic_return=list_type(num_type),
            pybind_function="array_cum_sum",
            python_fallback=None,
        )
        for list_type in PA_LIST_TYPES
        for num_type in PA_LARGEST_NUM_TYPES
    ],
    "array_duplicates": [
        ChalkFunctionOverload(
            function_name="array_duplicates",
            description="Returns an array containing only the duplicate elements from the input array.",
            overload_generic_parameters=[list_type(generic("T"))],
            overload_generic_return=list_type(generic("T")),
            pybind_function="array_duplicates",
            python_fallback=None,
        )
        for list_type in PA_LIST_TYPES
    ],
    "array_except": [
        ChalkFunctionOverload(
            function_name="array_except",
            description="Returns elements from the first array that are not present in the second array.",
            overload_generic_parameters=[list_type(generic("T")), list_type(generic("T"))],
            overload_generic_return=list_type(generic("T")),
            pybind_function="array_except",
            python_fallback=None,
        )
        for list_type in PA_LIST_TYPES
    ],
    "array_has_duplicates": [
        ChalkFunctionOverload(
            function_name="array_has_duplicates",
            description="Checks if an array contains duplicate elements.",
            overload_generic_parameters=[list_type(generic("T"))],
            overload_generic_return=pa.bool_(),
            pybind_function="array_has_duplicates",
            python_fallback=None,
        )
        for list_type in PA_LIST_TYPES
    ],
    "array_intersect": [
        ChalkFunctionOverload(
            function_name="array_intersect",
            description="Returns the intersection of two arrays (elements present in both arrays).",
            overload_generic_parameters=[list_type(generic("T")), list_type(generic("T"))],
            overload_generic_return=list_type(generic("T")),
            pybind_function="array_intersect",
            python_fallback=None,
        )
        for list_type in PA_LIST_TYPES
    ],
    "array_normalize": [
        ChalkFunctionOverload(
            function_name="array_normalize",
            description="Computes the L_p normalization of a Vector.",
            overload_generic_parameters=[list_type(float_type_1), float_type_2],
            overload_generic_return=list_type(float_type_1),
            pybind_function="array_normalize",
            python_fallback=None,
        )
        for list_type in PA_LIST_TYPES
        for float_type_1 in (pa.float16(), pa.float32(), pa.float64())
        for float_type_2 in (pa.float16(), pa.float32(), pa.float64())
    ],
    "array_position": [
        ChalkFunctionOverload(
            function_name="array_position",
            description="Returns the 1-based position of the first occurrence of an element in an array.",
            overload_generic_parameters=[list_type(generic("T")), generic("T")],
            overload_generic_return=pa.int64(),
            pybind_function="array_position",
            python_fallback=None,
        )
        for list_type in PA_LIST_TYPES
    ],
    "array_remove": [
        ChalkFunctionOverload(
            function_name="array_remove",
            description="Removes all occurrences of a specified element from an array.",
            overload_generic_parameters=[list_type(generic("T")), generic("T")],
            overload_generic_return=list_type(generic("T")),
            pybind_function="array_remove",
            python_fallback=None,
        )
        for list_type in PA_LIST_TYPES
    ],
    "arrays_overlap": [
        ChalkFunctionOverload(
            function_name="arrays_overlap",
            description="Checks if two arrays have any elements in common.",
            overload_generic_parameters=[list_type(generic("T")), list_type(generic("T"))],
            overload_generic_return=pa.bool_(),
            pybind_function="arrays_overlap",
            python_fallback=None,
        )
        for list_type in PA_LIST_TYPES
    ],
    "find_first": [
        ChalkFunctionOverload(
            function_name="find_first",
            description="Returns the first element in an array that matches the given predicate function.",
            overload_generic_parameters=[
                list_type(generic("T")),
                CallbackType(input_types=[generic("T")], output_type=pa.bool_()),
            ],
            overload_generic_return=generic("T"),
            pybind_function="find_first",
            python_fallback=None,
        )
        for list_type in PA_LIST_TYPES
    ],
    "find_first_index": [
        ChalkFunctionOverload(
            function_name="find_first_index",
            description="Returns the 1-based index of the first element in an array that matches the given predicate function.",
            overload_generic_parameters=[
                list_type(generic("T")),
                CallbackType(input_types=[generic("T")], output_type=pa.bool_()),
            ],
            overload_generic_return=pa.int64(),
            pybind_function="find_first_index",
            python_fallback=None,
        )
        for list_type in PA_LIST_TYPES
    ],
    "flatten": [
        ChalkFunctionOverload(
            function_name="flatten",
            description="Flattens a nested array by one level, combining all sub-arrays into a single array.",
            overload_generic_parameters=[list_type(list_type(generic("T")))],
            overload_generic_return=list_type(generic("T")),
            pybind_function="flatten",
            python_fallback=None,
        )
        for list_type in PA_LIST_TYPES
    ],
    "remove_nulls": [
        ChalkFunctionOverload(
            function_name="remove_nulls",
            description="Removes all null values from an array.",
            overload_generic_parameters=[list_type(generic("T"))],
            overload_generic_return=list_type(generic("T")),
            pybind_function="remove_nulls",
            python_fallback=None,
        )
        for list_type in PA_LIST_TYPES
    ],
    "sequence": [
        ChalkFunctionOverload(
            function_name="sequence",
            description="Generates a sequence of integers from start to stop (inclusive).",
            overload_generic_parameters=[pa.int64(), pa.int64()],
            overload_generic_return=pa.list_(pa.int64()),
            pybind_function="sequence",
            python_fallback=None,
        ),
        ChalkFunctionOverload(
            function_name="sequence",
            description="Generates a sequence of integers from start to stop (inclusive) with a specified step.",
            overload_generic_parameters=[pa.int64(), pa.int64(), pa.int64()],
            overload_generic_return=pa.list_(pa.int64()),
            pybind_function="sequence",
            python_fallback=None,
        ),
    ],
    "shuffle": [
        ChalkFunctionOverload(
            function_name="shuffle",
            description="Randomly shuffles the elements of an array.",
            overload_generic_parameters=[list_type(generic("T"))],
            overload_generic_return=list_type(generic("T")),
            pybind_function="shuffle",
            python_fallback=None,
        )
        for list_type in PA_LIST_TYPES
    ],
    "transform": [
        ChalkFunctionOverload(
            function_name="transform",
            description="Applies a transformation function to each element in an array and returns a new array.",
            overload_generic_parameters=[
                list_type(generic("T")),
                CallbackType(input_types=[generic("T")], output_type=generic("U")),
            ],
            overload_generic_return=list_type(generic("U")),
            pybind_function="transform",
            python_fallback=None,
        )
        for list_type in PA_LIST_TYPES
    ],
}

MultimodalContentItem = Mapping[str, str | None]
MultimodalMessageContents = list[MultimodalContentItem]


def _transform_content(content: MultimodalContentItem) -> Mapping[str, Any]:
    content_type = content.get("type")
    if content_type == "text" or content_type == "input_text":
        return {"type": "text", "text": content["text"]}
    elif content_type == "image_url" or content_type == "input_image":
        image_url_obj = {"url": content["image_url"]}
        if content.get("detail") is not None:
            image_url_obj["detail"] = content["detail"]
        return {"type": "image_url", "image_url": image_url_obj}
    else:
        raise ValueError(f"Unknown content type: {content_type}")


def _transform_messages(
    messages: list[Mapping[str, MultimodalMessageContents]],
) -> list[Mapping[str, list[Mapping[str, Any]]]]:
    return [
        {
            "role": message["role"],
            "content": [_transform_content(content) for content in message["content"]],
        }
        for message in messages
    ]


def _is_multimodal_messages(messages: list[Mapping[str, str | MultimodalMessageContents]]) -> bool:
    if not messages:
        return False
    return isinstance(messages[0].get("content"), list)


def _sanitize_contents(contents: MultimodalMessageContents) -> list[Mapping[str, str]]:
    return [{k: v for k, v in content.items() if v is not None} for content in contents]


def _convert_pydantic_to_langchain(
    schema: dict[str, TJSON],
) -> TJSON:
    # reimplementation of langchain's convert_pydantic_to_openai_function so that it accepts a dict
    # rather than the pydantic basemodel class
    schema.pop("definitions", None)
    name = schema.pop("title", "")
    description = schema.pop("description", "")
    return {
        "name": name,
        "description": description,
        "parameters": schema,
    }


@dataclass
class UsageCounter:
    input_tokens: int = 0
    output_tokens: int = 0
    total_tokens: int = 0

    def add(self, input_tokens: int, output_tokens: int, total_tokens: int):
        self.input_tokens += input_tokens
        self.output_tokens += output_tokens
        self.total_tokens += total_tokens


def _completion_op(
    model: str,
    messages: list[Mapping[str, str | MultimodalMessageContents]],
    timeout_seconds: float | None,
    output_structure: str | None,
    temperature: Optional[float],
    top_p: Optional[float],
    max_completion_tokens: Optional[int],
    max_tokens: Optional[int],
    stop: Optional[list[str]],
    presence_penalty: Optional[float],
    frequency_penalty: Optional[float],
    logit_bias: Optional[dict[int, float]],
    seed: Optional[int],
    user: Optional[str],
    model_provider: Optional[str],
    base_url: Optional[str],
    api_key: Optional[str],
    num_retries: Optional[int],
) -> Any:
    import json

    from chalk.prompts import (
        Message,
        MultimodalMessage,
        MultimodalPrompt,
        MultimodalPromptResponse,
        Prompt,
        PromptResponse,
        RuntimeStats,
        Usage,
    )
    from chalk.utils.tracing import PerfTimer
    from langchain.chat_models import init_chat_model
    from tenacity import (
        RetryError,
        Retrying,
        retry_if_exception_message,
        retry_if_not_exception_message,
        retry_if_not_exception_type,
        stop_after_attempt,
        stop_after_delay,
        wait_exponential_jitter,
    )

    with PerfTimer() as overall_pt:
        is_multimodal_prompt = _is_multimodal_messages(messages)
        if is_multimodal_prompt:
            # guaranteed by _is_multimodal_messages check
            multimodal_messages = typing.cast(list[Mapping[str, MultimodalMessageContents]], messages)
            transformed_messages = _transform_messages(multimodal_messages)
        else:
            transformed_messages = messages

        # pyright does not understand langchain
        model_obj = init_chat_model(  # pyright: ignore[reportCallIssue]
            model=model,
            timeout=timeout_seconds,
            top_p=top_p,
            max_completion_tokens=max_completion_tokens,
            max_tokens=max_tokens,
            stop=stop,
            presence_penalty=presence_penalty,
            frequency_penalty=frequency_penalty,
            logit_bias=logit_bias,
            seed=seed,
            model_provider=model_provider,
            base_url=base_url,
            api_key=api_key,
            max_retries=0,  # custom retry logic below
            user=user,  # pyright: ignore[reportArgumentType]
            **({"temperature": temperature} if temperature is not None else {}),  # pyright: ignore[reportArgumentType]
        )
        if output_structure is not None:
            try:
                output_structure_langchain = _convert_pydantic_to_langchain(json.loads(output_structure))
                model_obj = model_obj.with_structured_output(output_structure_langchain, include_raw=True)
            except Exception as e:
                raise ValueError(
                    f"Prompt requested output structure `{output_structure}`, which is not a valid JSON representation of a Pydantic model."
                    + "Use Model.model_json_schema() (Pydantic V2) or Model.schema_json() (Pydantic V1) to get the JSON representatino of a model."
                    + f"Error details: {e}"
                )

        response = None
        raw: Any = None
        total_tries = 0
        general_tries = 0
        last_try_latency: float | None = None
        usage_counter = UsageCounter()

        general_stop = stop_after_attempt(1 if num_retries is None else num_retries + 1)
        if timeout_seconds is not None:
            general_stop |= stop_after_delay(timeout_seconds)
        for general_attempt in Retrying(
            retry=retry_if_not_exception_type(RetryError) & retry_if_not_exception_message(match=r".*429.*"),
            wait=wait_exponential_jitter(),
            stop=general_stop,
            reraise=True,
        ):
            general_tries += 1
            with general_attempt:
                output: Any = None
                stop_429 = stop_after_attempt(10)
                if timeout_seconds is not None:
                    stop_429 |= stop_after_delay(timeout_seconds)
                for attempt_429 in Retrying(
                    retry=retry_if_exception_message(match=r".*429.*"),
                    wait=wait_exponential_jitter(),
                    stop=stop_429,
                    reraise=True,
                ):
                    total_tries += 1
                    with attempt_429:
                        with PerfTimer() as last_try_pt:
                            output = model_obj.invoke(transformed_messages)
                        last_try_latency = last_try_pt.duration_seconds

                if output_structure is not None:
                    raw = output["raw"]
                else:
                    raw = output
                usage_counter.add(
                    input_tokens=raw.usage_metadata["input_tokens"],
                    output_tokens=raw.usage_metadata["output_tokens"],
                    total_tokens=raw.usage_metadata["total_tokens"],
                )
                if output_structure is not None:
                    if output["parsing_error"] is not None:
                        raise ValueError(output["parsing_error"])
                    response = json.dumps(output["parsed"]) if output["parsed"] is not None else None
                else:
                    response = output.content

    usage = Usage(
        input_tokens=usage_counter.input_tokens,
        output_tokens=usage_counter.output_tokens,
        total_tokens=usage_counter.total_tokens,
    )
    runtime_stats = RuntimeStats(
        total_latency=overall_pt.duration_seconds,
        last_try_latency=last_try_latency,
        total_retries=total_tries - 1,
        rate_limit_retries=total_tries - general_tries,
    )
    if is_multimodal_prompt:
        return MultimodalPromptResponse(
            response=response,
            prompt=MultimodalPrompt(
                model=model,
                messages=[
                    MultimodalMessage(
                        role=typing.cast(str, message["role"]),
                        content=_sanitize_contents(typing.cast(MultimodalMessageContents, message["content"])),
                    )
                    for message in messages
                ],
                output_structure=output_structure,
                timeout_seconds=timeout_seconds,
                temperature=temperature,
                top_p=top_p,
                max_completion_tokens=max_completion_tokens,
                max_tokens=max_tokens,
                stop=stop,
                presence_penalty=presence_penalty,
                frequency_penalty=frequency_penalty,
                logit_bias=logit_bias,
                seed=seed,
                user=user,
                model_provider=model_provider,
                base_url=base_url,
                num_retries=num_retries,
            ),
            usage=usage,
            runtime_stats=runtime_stats,
        ).dict()
    else:
        return PromptResponse(
            response=response,
            prompt=Prompt(
                model=model,
                messages=[
                    Message(
                        role=typing.cast(str, message["role"]),
                        content=typing.cast(str, message["content"]),
                    )
                    for message in messages
                ],
                output_structure=output_structure,
                timeout_seconds=timeout_seconds,
                temperature=temperature,
                top_p=top_p,
                max_completion_tokens=max_completion_tokens,
                max_tokens=max_tokens,
                stop=stop,
                presence_penalty=presence_penalty,
                frequency_penalty=frequency_penalty,
                logit_bias=logit_bias,
                seed=seed,
                user=user,
                model_provider=model_provider,
                base_url=base_url,
                num_retries=num_retries,
            ),
            usage=usage,
            runtime_stats=runtime_stats,
        ).dict()


def _jinja_op(template: str, context: dict[str, Any]) -> str:
    try:
        import jinja2

        return jinja2.Environment().from_string(template).render(context)
    except:
        return ""


LLM_FUNCTIONS = {
    "completion": [
        ChalkFunctionOverload(
            function_name="completion",
            description="Generates text completions using a language model with string-based message content.",
            overload_generic_parameters=[],
            overload_generic_named_parameters=[
                ("model", pa.large_string()),
                (
                    "messages",
                    pa.large_list(
                        pa.struct(
                            {
                                "role": pa.large_string(),
                                "content": pa.large_string(),
                            }
                        )
                    ),
                ),
                ("timeout_seconds", pa.float64()),
                ("output_structure", pa.large_string()),
                ("temperature", pa.float64()),
                ("top_p", pa.float64()),
                ("max_completion_tokens", pa.int64()),
                ("max_tokens", pa.int64()),
                ("stop", pa.large_list(pa.large_string())),
                ("presence_penalty", pa.float64()),
                ("frequency_penalty", pa.float64()),
                ("logit_bias", pa.map_(pa.int64(), pa.float64())),
                ("seed", pa.int64()),
                ("user", pa.large_string()),
                ("model_provider", pa.large_string()),
                ("base_url", pa.large_string()),
                ("api_key", pa.large_string()),
                ("num_retries", pa.int64()),
            ],
            overload_generic_return=rich_to_pyarrow(PromptResponse, name="PromptResponse"),
            pybind_function=None,
            python_fallback=None,
        ),
        ChalkFunctionOverload(
            function_name="completion",
            description="Generates text completions using a language model with multimodal message content (text and images).",
            overload_generic_parameters=[],
            overload_generic_named_parameters=[
                ("model", pa.large_string()),
                (
                    "messages",
                    pa.large_list(
                        pa.struct(
                            {
                                "role": pa.large_string(),
                                "content": pa.large_list(
                                    pa.struct(
                                        {
                                            "type": pa.large_string(),
                                            "text": pa.large_string(),
                                            "image_url": pa.large_string(),
                                            "detail": pa.large_string(),
                                        }
                                    )
                                ),
                            }
                        )
                    ),
                ),
                ("timeout_seconds", pa.float64()),
                ("output_structure", pa.large_string()),
                ("temperature", pa.float64()),
                ("top_p", pa.float64()),
                ("max_completion_tokens", pa.int64()),
                ("max_tokens", pa.int64()),
                ("stop", pa.large_list(pa.large_string())),
                ("presence_penalty", pa.float64()),
                ("frequency_penalty", pa.float64()),
                ("logit_bias", pa.map_(pa.int64(), pa.float64())),
                ("seed", pa.int64()),
                ("user", pa.large_string()),
                ("model_provider", pa.large_string()),
                ("base_url", pa.large_string()),
                ("api_key", pa.large_string()),
                ("num_retries", pa.int64()),
            ],
            overload_generic_return=rich_to_pyarrow(MultimodalPromptResponse, name="MultimodalPromptResponse"),
            pybind_function=None,
            python_fallback=None,
        ),
    ],
    "jinja": [
        ChalkFunctionOverload(
            function_name="jinja",
            description="Renders a Jinja2 template string with provided context variables.",
            overload_generic_parameters=[pa.large_string(), generic("T")],
            overload_generic_return=pa.large_string(),
            pybind_function=None,
            python_fallback=None,
        )
    ],
    "run_prompt": [
        ChalkFunctionOverload(
            function_name="run_prompt",
            description="Executes a named prompt template and returns the generated response.",
            overload_generic_parameters=[],
            overload_generic_named_parameters=[
                ("prompt_name", pa.large_string()),
            ],
            overload_generic_return=rich_to_pyarrow(PromptResponse, name="PromptResponse"),
            pybind_function=None,
            python_fallback=None,
        ),
        ChalkFunctionOverload(
            function_name="run_prompt",
            description="Executes a prompt template by its ID and returns the response.",
            overload_generic_parameters=[],
            overload_generic_named_parameters=[
                ("propmt_id", pa.int64()),
            ],
            overload_generic_return=rich_to_pyarrow(PromptResponse, name="PromptResponse"),
            pybind_function=None,
            python_fallback=None,
        ),
    ],
}

UDF_BASED_FUNCTIONS = {
    "http_request": [
        # ChalkFunctionOverload(
        #     function_name="http_request",
        #     overload_generic_parameters=[
        #         pa.large_string(),
        #         pa.large_string(),
        #         pa.map_(pa.large_string(), pa.large_string()),
        #         pa.large_string(),
        #         pa.bool_(),
        #         pa.int64(),
        #     ],
        #     overload_generic_return=rich_to_pyarrow(HttpResponse[str], name="HttpResponse[str]"),
        #     pybind_function=make_http_udf_chalk_function(),
        #     python_fallback=None,
        # ),
        # ChalkFunctionOverload(
        #     function_name="http_request",
        #     overload_generic_parameters=[
        #         pa.large_string(),
        #         pa.large_string(),
        #         pa.map_(pa.large_string(), pa.large_string()),
        #         pa.large_binary(),
        #         pa.bool_(),
        #         pa.int64(),
        #     ],
        #     overload_generic_return=rich_to_pyarrow(HttpResponse[str], name="HttpResponse[str]"),
        #     pybind_function=make_http_udf_chalk_function(),
        #     python_fallback=None,
        # ),
        ChalkFunctionOverload(
            function_name="http_request",
            description="Makes an HTTP request with string body and returns the response as bytes.",
            overload_generic_parameters=[
                pa.large_string(),
                pa.large_string(),
                pa.map_(pa.large_string(), pa.large_string()),
                pa.large_string(),
                pa.bool_(),
                pa.int64(),
            ],
            overload_generic_return=rich_to_pyarrow(HttpResponse[bytes], name="HttpResponse[bytes]"),
            pybind_function=BlockingCallChalkFunctionImpl(HttpRequestBlockingFunction()),
            python_fallback=None,
        ),
        ChalkFunctionOverload(
            function_name="http_request",
            description="Makes an HTTP request with binary body and returns the response as bytes.",
            overload_generic_parameters=[
                pa.large_string(),
                pa.large_string(),
                pa.map_(pa.large_string(), pa.large_string()),
                pa.large_binary(),
                pa.bool_(),
                pa.int64(),
            ],
            overload_generic_return=rich_to_pyarrow(HttpResponse[bytes], name="HttpResponse[bytes]"),
            pybind_function=BlockingCallChalkFunctionImpl(HttpRequestBlockingFunction()),
            python_fallback=None,
        ),
    ],
    "onnx_run_embedding": [
        ChalkFunctionOverload(
            function_name="onnx_run_embedding",
            description="Generates embeddings from text using the specified ONNX model.",
            overload_generic_parameters=[
                pa.large_string(),
            ],
            overload_generic_return=pa.large_list(pa.float32()),
            overload_generic_named_parameters=[
                ("model_name", pa.large_string()),
            ],
            pybind_function="onnx_run_embedding",
            python_fallback=None,
        ),
    ],
    "sagemaker_predict": [
        ChalkFunctionOverload(
            function_name="sagemaker_predict",
            description="Invokes an AWS SageMaker endpoint for inference with the provided binary input and returns the binary output.",
            overload_generic_parameters=[bin_type],
            overload_generic_named_parameters=[
                ("endpoint", str_type),
                ("content_type", str_type),
                ("target_model", str_type),
                ("target_variant", str_type),
                ("aws_access_key_id_override", str_type),
                ("aws_secret_access_key_override", str_type),
                ("aws_session_token_override", str_type),
                ("aws_role_arn_override", str_type),
                ("aws_region_override", str_type),
                ("aws_profile_name_override", str_type),
                ("inference_component", str_type),
            ],
            overload_generic_return=bin_type,
            pybind_function=SagemakerPredictBlockingFunctionPlaceholder(),
            python_fallback=None,
        )
        for bin_type, str_type in zip(PA_BINARY_TYPES, PA_STRING_TYPES)
    ],
}

"""
The order of resolution is based on the order that they appear in the list. So we attempt to resolve against
CHALK_SQL_FUNCTIONS.get(name)[0], then CHALK_SQL_FUNCTIONS.get(name)[1], etc.

These functions are those that aren't given special treatment by DuckDB. That is, if I say SELECT 1 + 2, DuckDB parses
this as "+"(1,2), instead of a special class of ExpressionNode.
"""
CHALK_SQL_FUNCTIONS: dict[str, list[ChalkFunctionOverload]] = {
    "+": [
        # Velox plus() states that x and y must be the same types
        *[
            ChalkFunctionOverload(
                function_name="+",
                description="Adds two numbers together.",
                overload_generic_parameters=[t, t],
                overload_generic_return=t,
                pybind_function="plus",
                python_fallback=None,
            )
            for t in PA_NUM_TYPES
        ],
    ],
    "-": [
        ChalkFunctionOverload(
            function_name="-",
            description="Subtracts the second number from the first.",
            overload_generic_parameters=[t, t],
            overload_generic_return=t,
            pybind_function="minus",
            python_fallback=None,
        )
        for t in PA_NUM_TYPES
    ],
    "*": [
        ChalkFunctionOverload(
            function_name="*",
            description="Multiplies two numbers together.",
            overload_generic_parameters=[t, t],
            overload_generic_return=t,
            pybind_function="multiply",
            python_fallback=None,
        )
        for t in PA_NUM_TYPES
    ],
}


def _velox_only_agg(fn_name: str):
    def _inner(*args: Any):
        raise NotImplementedError(f"aggregate function {fn_name} is only supported on Velox")

    return _inner


def _exact_count_distinct_fn_from_func_name(func_name: str):
    def _exact_count_distinct_fn(input: Any):
        if not isinstance(input, (pa.Array, pa.ChunkedArray)):
            raise ValueError(f"Cannot run `.{func_name}()` on non-array input of type '{type(input)}'")

        return pc.count_distinct(input).as_py()

    return _exact_count_distinct_fn


def _approx_percentile_fn(input: Any, quantile: float):
    if not isinstance(input, (pa.Array, pa.ChunkedArray)):
        raise ValueError(f"Cannot run `.approx_percentile()` on non-array input of type '{type(input)}'")

    try:
        quantile = float(quantile)
    except:
        raise TypeError(
            f"The quantile value must be float in the range [0, 1], but got {repr(quantile)} with type '{type(quantile)}'"
        )

    if not (0 <= quantile <= 1):
        raise ValueError(
            f"Cannot run `.approx_percentile()` with quantile value '{repr(quantile)}' outside of the legal range [0, 1]"
        )

    return pc.quantile(input, q=quantile)[0].as_py()


AGGREGATE_FUNCTIONS: dict[str, list[ChalkFunctionOverload]] = {
    "sum": [
        *(
            ChalkFunctionOverload(
                function_name="sum",
                description="Returns the sum of a df column",
                overload_generic_parameters=[DataFrameParameterType(columns={"series": num_type})],
                overload_generic_return=num_type,
                pybind_function="sum",
                python_fallback=None,
            )
            for num_type in PA_NUM_TYPES
        ),
        *(
            ChalkFunctionOverload(
                function_name="vector_sum",
                description="Returns the vectorized sum of a df column",
                overload_generic_parameters=[DataFrameParameterType(columns={"series": list_type(num_type)})],
                overload_generic_return=list_type(num_type),
                pybind_function="vector_sum",
                python_fallback=None,
            )
            for num_type in PA_NUM_TYPES
            for list_type in PA_LIST_TYPES
        ),
    ],
    "min": [
        ChalkFunctionOverload(
            function_name="min",
            description="Returns the min value of a df column",
            overload_generic_parameters=[DataFrameParameterType(columns={"series": num_type})],
            overload_generic_return=num_type,
            pybind_function="min",
            python_fallback=None,
        )
        for num_type in PA_NUM_AND_TIME_TYPES
    ],
    "max": [
        ChalkFunctionOverload(
            function_name="max",
            description="Returns the max value of a df column",
            overload_generic_parameters=[DataFrameParameterType(columns={"series": sortable_type})],
            overload_generic_return=sortable_type,
            pybind_function="max",
            python_fallback=None,
        )
        for sortable_type in PA_NUM_AND_TIME_TYPES
    ],
    "mean": [
        ChalkFunctionOverload(
            function_name="mean",
            description="Returns the mean value of a df column",
            overload_generic_parameters=[DataFrameParameterType(columns={"series": num_type})],
            overload_generic_return=most_precise_numeric_type_from_arrow(types=[num_type], minimum_type=pa.float16()),
            pybind_function="mean",
            python_fallback=None,
        )
        for num_type in PA_NUM_TYPES
    ],
    "mode": [
        ChalkFunctionOverload(
            function_name="mode",
            description="Returns the mode value of a df column",
            overload_generic_parameters=[DataFrameParameterType(columns={"series": num_type})],
            overload_generic_return=num_type,
            pybind_function="mode",
            python_fallback=None,  # type: ignore
        )
        for num_type in PA_NUM_TYPES
    ],
    "count": [
        ChalkFunctionOverload(
            function_name="count_all",
            description="Returns the number of entries in a df",
            overload_generic_parameters=[DataFrameParameterType(columns={"series": generic("T")})],
            overload_generic_return=pa.int64(),
            pybind_function="count_all",
            python_fallback=None,
        )
    ],
    "any": [
        ChalkFunctionOverload(
            function_name="any",
            description="Returns True if any of the entries in a df column are True",
            overload_generic_parameters=[DataFrameParameterType(columns={"series": pa.bool_()})],
            overload_generic_return=pa.bool_(),
            pybind_function="any",
            python_fallback=None,
        )
    ],
    "all": [
        ChalkFunctionOverload(
            function_name="all",
            description="Returns True if all of the entries in a df column are True",
            overload_generic_parameters=[DataFrameParameterType(columns={"series": pa.bool_()})],
            overload_generic_return=pa.bool_(),
            pybind_function="all",
            python_fallback=None,
        )
    ],
    **{
        stddev_alias: [
            ChalkFunctionOverload(
                function_name="stddev_sample",
                description="Returns the sample standard deviation of a df column",
                overload_generic_parameters=[DataFrameParameterType(columns={"series": num_type})],
                overload_generic_return=pa.float64(),
                pybind_function="stddev_sample",
                python_fallback=None,
            )
            for num_type in PA_NUM_TYPES
        ]
        for stddev_alias in ("std", "stddev", "std_sample", "stddev_sample")
    },
    **{
        var_alias: [
            ChalkFunctionOverload(
                function_name="variance_sample",
                description="Returns the sample variance of a df column",
                overload_generic_parameters=[DataFrameParameterType(columns={"series": num_type})],
                overload_generic_return=pa.float64(),
                pybind_function="variance_sample",
                python_fallback=None,
            )
            for num_type in PA_NUM_TYPES
        ]
        for var_alias in ("var", "var_sample")
    },
    "approx_count_distinct": [
        ChalkFunctionOverload(
            function_name="approx_count_distinct",
            description="Returns an approximate number of distinct entries in a df column",
            overload_generic_parameters=[DataFrameParameterType(columns={"series": generic("T")})],
            overload_generic_return=pa.int64(),
            pybind_function="approx_count_distinct",
            python_fallback=None,
        )
    ],
    "max_by": [
        ChalkFunctionOverload(
            function_name="max_by",
            description="Return the maximum value of a df column, sorted by the sort column.",
            overload_generic_parameters=[DataFrameParameterType(columns={"series": generic("V")}), generic("S")],
            overload_generic_return=generic("V"),
            pybind_function="max_by",
        )
    ],
    "max_by_n": [
        ChalkFunctionOverload(
            function_name="max_by_n",
            description="Return the maximum n values of a df column, sorted by the sort column.",
            overload_generic_parameters=[
                DataFrameParameterType(columns={"series": generic("V")}),
                generic("S"),
                pa.int64(),
            ],
            overload_generic_return=list_type(generic("V")),
            pybind_function="max_by_n",
        )
        for list_type in PA_LIST_TYPES
    ],
    "min_by": [
        ChalkFunctionOverload(
            function_name="min_by",
            description="Return the minimum value of a df column, sorted by the sort column.",
            overload_generic_parameters=[DataFrameParameterType(columns={"series": generic("V")}), generic("S")],
            overload_generic_return=generic("V"),
            pybind_function="min_by",
        )
    ],
    "min_by_n": [
        ChalkFunctionOverload(
            function_name="min_by_n",
            description="Return the minimum n values of a df column, sorted by the sort column.",
            overload_generic_parameters=[
                DataFrameParameterType(columns={"series": generic("V")}),
                generic("S"),
                pa.int64(),
            ],
            overload_generic_return=list_type(generic("V")),
            pybind_function="min_by_n",
        )
        for list_type in PA_LIST_TYPES
    ],
    "count_distinct": [
        ChalkFunctionOverload(
            function_name="count_distinct",
            description="Returns the number of distinct entries in a df column",
            overload_generic_parameters=[DataFrameParameterType(columns={"series": generic("T")})],
            overload_generic_return=pa.int64(),
            pybind_function="count_distinct",
            python_fallback=None,
        )
    ],
    "array_agg": [
        ChalkFunctionOverload(
            function_name="array_agg",
            description="Returns a scalar array of a df column",
            overload_generic_parameters=[DataFrameParameterType(columns={"series": generic("T")})],
            overload_generic_return=list_type(generic("T")),
            pybind_function="array_agg",
            python_fallback=None,
        )
        for list_type in PA_LIST_TYPES
    ],
    "approx_percentile": [
        ChalkFunctionOverload(
            function_name="approx_percentile",
            description="Returns the approximate percentile value of the df column",
            overload_generic_parameters=[
                DataFrameParameterType(columns={"series": num_type})
            ],  # FIXME - Dominic - this agg actually takes in another parameter, "quartile", that's handled differently from all other aggregations
            overload_generic_return=pa.float64(),
            pybind_function="approx_percentile",
            python_fallback=None,
        )
        for num_type in PA_NUM_TYPES
    ],
    "approx_top_k": [
        ChalkFunctionOverload(
            function_name="approx_top_k",
            description="Returns the approximate k-most frequent values of the df column",
            overload_generic_parameters=[
                DataFrameParameterType(columns={"series": generic("T")}),
            ],  # FIXME - Dominic - this agg actually takes in other parameters, "k" and "output_type", that are handled differently from all other aggregations
            overload_generic_return=pa.large_list(generic("T")),
            pybind_function="approx_top_k",
        )
    ],
}

AGGREGATE_FUNCTION_NULL_FILLING_DETAILS: Mapping[str, int | None | bool] = {
    **{fn_name: 0 for fn_name in ("sum", "count_all", "approx_count_distinct", "count_distinct")},
    **{fn_name: False for fn_name in ("any",)},
    **{fn_name: True for fn_name in ("all",)},
    **{
        fn_name: None
        for fn_name in (
            "vector_sum",
            "min",
            "max",
            "mean",
            "mode",
            "stddev_sample",
            "variance_sample",
            "array_agg",
            "approx_percentile",
            "approx_top_k",
            "min_by_n",
            "max_by_n",
            "min_by",
            "max_by",
        )
    },
}

assert all(
    overload.function_name in AGGREGATE_FUNCTION_NULL_FILLING_DETAILS
    for overloads in AGGREGATE_FUNCTIONS.values()
    for overload in overloads
)

CHALK_FUNCTION_REGISTRY: Mapping[str, list[ChalkFunctionOverload]] = (
    BASE_FUNCTIONS | LLM_FUNCTIONS | UDF_BASED_FUNCTIONS | AGGREGATE_FUNCTIONS
)

CHALK_SQL_FUNCTION_REGISTRY: Mapping[str, list[ChalkFunctionOverload]] = CHALK_FUNCTION_REGISTRY | CHALK_SQL_FUNCTIONS

"""
The `CHALK_FUNCTION_REGISTRY` lists explicit overloads for a subset of (scalar) Chalk functions.
Each function can have multiple overloads, with different number or types of input parameters.

Overloads are considered in the listed order - the first matching overload is selected.
This means that for e.g. numeric functions which support multiple precisions, list the most-specific overloads first.

The backend function name may be different from the Chalk function name.

This registry should be preferred, because it is used by chalkpy->UnderscoreValue,
UnderscoreValue->libchalk/velox, and ast.AST->SymbolicValue conversion logic,
which ensures that the overloads do not get out-of-sync.
"""


def attempt_to_resolve_overloads(
    *,
    function_name: str,
    candidate_overloads: Sequence[ChalkFunctionOverload],
    input_types: MaybeNamedCollection[ArgumentType],
) -> ChalkFunctionOverloadResolved | ChalkFunctionOverloadFailed:
    """
    Note: the `function_name` in this function is ONLY used for error reporting.
    This function does NOT read from the registry.

    Attempts to resolve the provided inputs against each of the provided overloads.
    Returns the first resolved overload.

    If none of the overloads match, returns a descriptive error describing the heuristically-best error.
    """

    # Attempt each overload in sequence. Return the first matching overload.

    # This is the fallback error for the overload. It should never be returned,
    # since there is always at least one overload.
    best_overload_failure = ChalkFunctionOverloadFailed(
        failure_priority=-1000,
        failure_message=f"no matching overload for function '{function_name}'",
    )

    for overload_candidate in candidate_overloads:
        # Try to resolve against this overload.
        candidate_result = overload_candidate.get_resolved_overload(input_types)
        if isinstance(candidate_result, ChalkFunctionOverloadResolved):
            # Return the successful resolved overload.
            return candidate_result

        # If the latest error is more helpful than the previous best one, then replace it.
        if candidate_result.failure_priority > best_overload_failure.failure_priority:
            best_overload_failure = candidate_result

    available_signatures_string = "".join(f"\n- {candidate.formatted_overload()}" for candidate in candidate_overloads)
    return ChalkFunctionOverloadFailed(
        failure_priority=best_overload_failure.failure_priority,
        failure_message=f"{best_overload_failure.failure_message}\nThe following candidate function overloads are available:{available_signatures_string}",
    )


def is_aggregate_function(fn_name: str):
    return fn_name in AGGREGATE_FUNCTION_NULL_FILLING_DETAILS


def get_chalk_function_registry_overload(
    *,
    function_name: str,
    input_types: MaybeNamedCollection[ArgumentType],
) -> None | ChalkFunctionOverloadResolved | ChalkFunctionOverloadFailed:
    """
    If no matching function exists in the registry, returns `None`.

    Otherwise, attempts to resolve the provided input types against the overloads
    in the registry.

    If there is a Chalk function registered with the provided name, then returns
    either a `ChalkFunctionOverloadResolved` with the resolved input/output types,
    or else returns an `ChalkFunctionOverloadFailed` with information about the attempted overloads.
    """

    overloads = CHALK_FUNCTION_REGISTRY.get(function_name, None)

    if overloads is None or len(overloads) == 0:
        return None

    return attempt_to_resolve_overloads(
        function_name=function_name,
        input_types=input_types,
        candidate_overloads=overloads,
    )


def get_libchalk_fn_overload_from_py(
    name: str,
    overload: ChalkFunctionOverloadResolved,
) -> LibChalkFunctionOverloadResolved | LibChalkFunctionOverloadFailed:
    if overload.pybind_function is None:
        return LibChalkFunctionOverloadFailed(
            failure_message="No Velox function found for function {}".format(name),
            failure_priority=0,
        )
    new_pybind_function = overload.pybind_function
    if isinstance(new_pybind_function, str):
        # If the overload is a direct implementation, we need to convert it to a pybind function.
        new_pybind_function = DirectChalkFunctionImpl(new_pybind_function)
    overload_input_types = overload.input_promotion_target_types
    if len(overload_input_types.named_items) > 0:
        return LibChalkFunctionOverloadFailed(
            failure_message="Named input parameters are not supported for function {}".format(name),
            failure_priority=0,
        )
    type_checked_overload_input_types = [x for x in overload_input_types.positional_items if isinstance(x, pa.DataType)]
    if len(type_checked_overload_input_types) != len(overload_input_types.positional_items):
        return LibChalkFunctionOverloadFailed(
            failure_message="Non-arrow input types for function {}".format(name),
            failure_priority=0,
        )
    return LibChalkFunctionOverloadResolved(
        input_types=type_checked_overload_input_types,
        output_type=overload.output_type,
        libchalk_function=new_pybind_function,
        impl_input_types=overload.cast_input_types_before_executing,
        impl_output_type=overload.cast_output_type_from,
        description=overload.description,
    )
