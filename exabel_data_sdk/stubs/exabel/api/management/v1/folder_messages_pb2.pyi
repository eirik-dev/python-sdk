"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
Copyright (c) 2022 Exabel AS. All rights reserved."""
import builtins
import collections.abc
from ..... import exabel
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import google.protobuf.timestamp_pb2
import sys
import typing
if sys.version_info >= (3, 10):
    import typing as typing_extensions
else:
    import typing_extensions
DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class _FolderItemType:
    ValueType = typing.NewType('ValueType', builtins.int)
    V: typing_extensions.TypeAlias = ValueType

class _FolderItemTypeEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_FolderItemType.ValueType], builtins.type):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    FOLDER_ITEM_TYPE_INVALID: _FolderItemType.ValueType
    'Invalid item type.'
    DERIVED_SIGNAL: _FolderItemType.ValueType
    'Derived signal.'
    PREDICTION_MODEL: _FolderItemType.ValueType
    'Prediction model.'
    PORTFOLIO_STRATEGY: _FolderItemType.ValueType
    'Portfolio strategy.'
    DASHBOARD: _FolderItemType.ValueType
    'Dashboard.'
    DRILL_DOWN: _FolderItemType.ValueType
    'Company or entity drill down view.'
    TAG: _FolderItemType.ValueType
    'Static tag.'
    SCREEN: _FolderItemType.ValueType
    'Screen.'
    FINANCIAL_MODEL: _FolderItemType.ValueType
    'Financial model.'
    CHART: _FolderItemType.ValueType
    'Chart.'
    KPI_MAPPING: _FolderItemType.ValueType
    'KPI mapping.'

class FolderItemType(_FolderItemType, metaclass=_FolderItemTypeEnumTypeWrapper):
    """An enum representing the type of a folder item."""
FOLDER_ITEM_TYPE_INVALID: FolderItemType.ValueType
'Invalid item type.'
DERIVED_SIGNAL: FolderItemType.ValueType
'Derived signal.'
PREDICTION_MODEL: FolderItemType.ValueType
'Prediction model.'
PORTFOLIO_STRATEGY: FolderItemType.ValueType
'Portfolio strategy.'
DASHBOARD: FolderItemType.ValueType
'Dashboard.'
DRILL_DOWN: FolderItemType.ValueType
'Company or entity drill down view.'
TAG: FolderItemType.ValueType
'Static tag.'
SCREEN: FolderItemType.ValueType
'Screen.'
FINANCIAL_MODEL: FolderItemType.ValueType
'Financial model.'
CHART: FolderItemType.ValueType
'Chart.'
KPI_MAPPING: FolderItemType.ValueType
'KPI mapping.'
global___FolderItemType = FolderItemType

@typing_extensions.final
class Folder(google.protobuf.message.Message):
    """A folder."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    NAME_FIELD_NUMBER: builtins.int
    DISPLAY_NAME_FIELD_NUMBER: builtins.int
    DESCRIPTION_FIELD_NUMBER: builtins.int
    WRITE_FIELD_NUMBER: builtins.int
    ITEMS_FIELD_NUMBER: builtins.int
    name: builtins.str
    'Unique resource name of the folder, e.g. `folders/123`. In the "Create folder" method, this is\n    ignored and may be left empty.\n    '
    display_name: builtins.str
    'Appears in the Exabel Library in the list of folders.'
    description: builtins.str
    'The description of the folder.'
    write: builtins.bool
    'Whether the API caller has write access to the folder.'

    @property
    def items(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___FolderItem]:
        """List of items in the folder. To add or remove folder items, use the "Move folder items" method."""

    def __init__(self, *, name: builtins.str | None=..., display_name: builtins.str | None=..., description: builtins.str | None=..., write: builtins.bool | None=..., items: collections.abc.Iterable[global___FolderItem] | None=...) -> None:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['description', b'description', 'display_name', b'display_name', 'items', b'items', 'name', b'name', 'write', b'write']) -> None:
        ...
global___Folder = Folder

@typing_extensions.final
class FolderItem(google.protobuf.message.Message):
    """An item in a folder."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    PARENT_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    DISPLAY_NAME_FIELD_NUMBER: builtins.int
    DESCRIPTION_FIELD_NUMBER: builtins.int
    ITEM_TYPE_FIELD_NUMBER: builtins.int
    CREATE_TIME_FIELD_NUMBER: builtins.int
    UPDATE_TIME_FIELD_NUMBER: builtins.int
    CREATED_BY_FIELD_NUMBER: builtins.int
    UPDATED_BY_FIELD_NUMBER: builtins.int
    parent: builtins.str
    'Resource name of the parent folder, e.g. `folders/123`.'
    name: builtins.str
    'Resource name of the item, e.g. `derivedSignals/123` or `models/987`.'
    display_name: builtins.str
    'Appears in the Exabel Library when viewing items in a folder, and also when the item is opened.'
    description: builtins.str
    'Appears in the Exabel Library under each item, and when the item is opened.'
    item_type: global___FolderItemType.ValueType
    'Item type.'

    @property
    def create_time(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """When the item was created."""

    @property
    def update_time(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """When the item was last updated."""
    created_by: builtins.str
    'Resource name of the user who created the item.'
    updated_by: builtins.str
    'Resource name of the user who last updated the item.'

    def __init__(self, *, parent: builtins.str | None=..., name: builtins.str | None=..., display_name: builtins.str | None=..., description: builtins.str | None=..., item_type: global___FolderItemType.ValueType | None=..., create_time: google.protobuf.timestamp_pb2.Timestamp | None=..., update_time: google.protobuf.timestamp_pb2.Timestamp | None=..., created_by: builtins.str | None=..., updated_by: builtins.str | None=...) -> None:
        ...

    def HasField(self, field_name: typing_extensions.Literal['create_time', b'create_time', 'update_time', b'update_time']) -> builtins.bool:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['create_time', b'create_time', 'created_by', b'created_by', 'description', b'description', 'display_name', b'display_name', 'item_type', b'item_type', 'name', b'name', 'parent', b'parent', 'update_time', b'update_time', 'updated_by', b'updated_by']) -> None:
        ...
global___FolderItem = FolderItem

@typing_extensions.final
class FolderAccessor(google.protobuf.message.Message):
    """An accessor of a folder."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    GROUP_FIELD_NUMBER: builtins.int
    WRITE_FIELD_NUMBER: builtins.int

    @property
    def group(self) -> exabel.api.management.v1.user_messages_pb2.Group:
        """User group that has access to the folder."""
    write: builtins.bool
    'Whether the user group has write access. Read access is implied.'

    def __init__(self, *, group: exabel.api.management.v1.user_messages_pb2.Group | None=..., write: builtins.bool | None=...) -> None:
        ...

    def HasField(self, field_name: typing_extensions.Literal['group', b'group']) -> builtins.bool:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['group', b'group', 'write', b'write']) -> None:
        ...
global___FolderAccessor = FolderAccessor

@typing_extensions.final
class SearchResult(google.protobuf.message.Message):
    """A search result."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    ITEM_FIELD_NUMBER: builtins.int

    @property
    def item(self) -> global___FolderItem:
        """The folder item."""

    def __init__(self, *, item: global___FolderItem | None=...) -> None:
        ...

    def HasField(self, field_name: typing_extensions.Literal['item', b'item']) -> builtins.bool:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['item', b'item']) -> None:
        ...
global___SearchResult = SearchResult