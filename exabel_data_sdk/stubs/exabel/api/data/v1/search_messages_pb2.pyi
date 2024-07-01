"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
Copyright (c) 2019-2022 Exabel AS. All rights reserved."""
import builtins
import google.protobuf.descriptor
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import sys
import typing
if sys.version_info >= (3, 10):
    import typing as typing_extensions
else:
    import typing_extensions
DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class _SearchUniverse:
    ValueType = typing.NewType('ValueType', builtins.int)
    V: typing_extensions.TypeAlias = ValueType

class _SearchUniverseEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_SearchUniverse.ValueType], builtins.type):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    SEARCH_UNIVERSE_UNSPECIFIED: _SearchUniverse.ValueType
    'No search universe specified. This is the default behaviour.\n    For text search for entityTypes/company, this searches the Exabel company universe.\n    '
    EXABEL_COMPANIES: _SearchUniverse.ValueType
    'Search all companies in the Exabel company universe. This includes all companies with\n    price data or a directly connected time series. Only supported for text search for\n    entityTypes/company.\n    '
    ALL_COMPANIES: _SearchUniverse.ValueType
    "Search all companies, including companies not in the Exabel company universe. This includes all\n    FactSet companies of type 'SUB' and 'PVT'. Only supported for text search for entityTypes/company.\n    "

class SearchUniverse(_SearchUniverse, metaclass=_SearchUniverseEnumTypeWrapper):
    """Enum to select search universe."""
SEARCH_UNIVERSE_UNSPECIFIED: SearchUniverse.ValueType
'No search universe specified. This is the default behaviour.\nFor text search for entityTypes/company, this searches the Exabel company universe.\n'
EXABEL_COMPANIES: SearchUniverse.ValueType
'Search all companies in the Exabel company universe. This includes all companies with\nprice data or a directly connected time series. Only supported for text search for\nentityTypes/company.\n'
ALL_COMPANIES: SearchUniverse.ValueType
"Search all companies, including companies not in the Exabel company universe. This includes all\nFactSet companies of type 'SUB' and 'PVT'. Only supported for text search for entityTypes/company.\n"
global___SearchUniverse = SearchUniverse

@typing.final
class SearchTerm(google.protobuf.message.Message):
    """A single search term in a search request."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    FIELD_FIELD_NUMBER: builtins.int
    QUERY_FIELD_NUMBER: builtins.int
    field: builtins.str
    'The name of the field that should be matched. Field names are\n    case-insensitive.\n    '
    query: builtins.str
    'The query against which the field is matched.'

    def __init__(self, *, field: builtins.str | None=..., query: builtins.str | None=...) -> None:
        ...

    def ClearField(self, field_name: typing.Literal['field', b'field', 'query', b'query']) -> None:
        ...
global___SearchTerm = SearchTerm

@typing.final
class SearchOptions(google.protobuf.message.Message):
    """Options on how the search should be performed."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    UNIVERSE_FIELD_NUMBER: builtins.int
    universe: global___SearchUniverse.ValueType
    "The entity universe to search. Currently only supported for 'text' search for entityType/company."

    def __init__(self, *, universe: global___SearchUniverse.ValueType | None=...) -> None:
        ...

    def ClearField(self, field_name: typing.Literal['universe', b'universe']) -> None:
        ...
global___SearchOptions = SearchOptions