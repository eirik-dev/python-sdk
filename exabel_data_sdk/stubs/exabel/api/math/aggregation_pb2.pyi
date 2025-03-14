"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
Copyright (c) 2019-2024 Exabel AS. All rights reserved."""
import builtins
import google.protobuf.descriptor
import google.protobuf.internal.enum_type_wrapper
import sys
import typing
if sys.version_info >= (3, 10):
    import typing as typing_extensions
else:
    import typing_extensions
DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class _Aggregation:
    ValueType = typing.NewType('ValueType', builtins.int)
    V: typing_extensions.TypeAlias = ValueType

class _AggregationEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_Aggregation.ValueType], builtins.type):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    AGGREGATION_INVALID: _Aggregation.ValueType
    'Aggregation is unspecified and invalid. Aggregation must be set.'
    MEAN: _Aggregation.ValueType
    'Takes the arithmetic mean of the data values. Example: 2, 1, 3, 5, 4 -> 3.'
    FIRST: _Aggregation.ValueType
    'Selects the first value. Example: 2, 1, 3, 5, 4 -> 2.'
    LAST: _Aggregation.ValueType
    'Selects the last value. Example: 2, 1, 3, 5, 4 -> 4.'
    SUM: _Aggregation.ValueType
    'Sums the data values. Example: 2, 1, 3, 5, 4 -> 15.'
    MIN: _Aggregation.ValueType
    'Selects the minimum value. Example: 2, 1, 3, 5, 4 -> 1.'
    MAX: _Aggregation.ValueType
    'Selects the maximum value. Example: 2, 1, 3, 5, 4 -> 5.'
    MEDIAN: _Aggregation.ValueType
    'Selects the median value. Example: 2, 1, 3, 5, 1000 -> 3.'

class Aggregation(_Aggregation, metaclass=_AggregationEnumTypeWrapper):
    """Aggregation methods."""
AGGREGATION_INVALID: Aggregation.ValueType
'Aggregation is unspecified and invalid. Aggregation must be set.'
MEAN: Aggregation.ValueType
'Takes the arithmetic mean of the data values. Example: 2, 1, 3, 5, 4 -> 3.'
FIRST: Aggregation.ValueType
'Selects the first value. Example: 2, 1, 3, 5, 4 -> 2.'
LAST: Aggregation.ValueType
'Selects the last value. Example: 2, 1, 3, 5, 4 -> 4.'
SUM: Aggregation.ValueType
'Sums the data values. Example: 2, 1, 3, 5, 4 -> 15.'
MIN: Aggregation.ValueType
'Selects the minimum value. Example: 2, 1, 3, 5, 4 -> 1.'
MAX: Aggregation.ValueType
'Selects the maximum value. Example: 2, 1, 3, 5, 4 -> 5.'
MEDIAN: Aggregation.ValueType
'Selects the median value. Example: 2, 1, 3, 5, 1000 -> 3.'
global___Aggregation = Aggregation