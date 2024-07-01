"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
Copyright (c) 2019-2022 Exabel AS. All rights reserved."""
import builtins
import collections.abc
from ..... import exabel
import google.protobuf.descriptor
import google.protobuf.field_mask_pb2
import google.protobuf.internal.containers
import google.protobuf.message
import typing
DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing.final
class ListEntityTypesRequest(google.protobuf.message.Message):
    """The request to list entity types."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    PAGE_SIZE_FIELD_NUMBER: builtins.int
    PAGE_TOKEN_FIELD_NUMBER: builtins.int
    page_size: builtins.int
    'Maximum number of results to return. Defaults to 1000, which is the maximum allowed value.'
    page_token: builtins.str
    'Token for a specific page of results, as returned from a previous list request with the same\n    query parameters.\n    '

    def __init__(self, *, page_size: builtins.int | None=..., page_token: builtins.str | None=...) -> None:
        ...

    def ClearField(self, field_name: typing.Literal['page_size', b'page_size', 'page_token', b'page_token']) -> None:
        ...
global___ListEntityTypesRequest = ListEntityTypesRequest

@typing.final
class ListEntityTypesResponse(google.protobuf.message.Message):
    """The response to list entity types. Returns all known entity types."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    ENTITY_TYPES_FIELD_NUMBER: builtins.int
    NEXT_PAGE_TOKEN_FIELD_NUMBER: builtins.int
    TOTAL_SIZE_FIELD_NUMBER: builtins.int
    next_page_token: builtins.str
    'Token for the next page of results, which can be sent to a subsequent query.'
    total_size: builtins.int
    'Total number of results, irrespective of paging.'

    @property
    def entity_types(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[exabel.api.data.v1.entity_messages_pb2.EntityType]:
        """List of entity types.
        The end of the list is reached when number of results is less than the page size
        (NOT when the token is empty).
        """

    def __init__(self, *, entity_types: collections.abc.Iterable[exabel.api.data.v1.entity_messages_pb2.EntityType] | None=..., next_page_token: builtins.str | None=..., total_size: builtins.int | None=...) -> None:
        ...

    def ClearField(self, field_name: typing.Literal['entity_types', b'entity_types', 'next_page_token', b'next_page_token', 'total_size', b'total_size']) -> None:
        ...
global___ListEntityTypesResponse = ListEntityTypesResponse

@typing.final
class GetEntityTypeRequest(google.protobuf.message.Message):
    """The request to get one entity type."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    NAME_FIELD_NUMBER: builtins.int
    name: builtins.str
    'The resource name of the requested entity type, for example `entityTypes/ns.type1`.'

    def __init__(self, *, name: builtins.str | None=...) -> None:
        ...

    def ClearField(self, field_name: typing.Literal['name', b'name']) -> None:
        ...
global___GetEntityTypeRequest = GetEntityTypeRequest

@typing.final
class CreateEntityTypeRequest(google.protobuf.message.Message):
    """The request to create one entity type."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    ENTITY_TYPE_FIELD_NUMBER: builtins.int

    @property
    def entity_type(self) -> exabel.api.data.v1.entity_messages_pb2.EntityType:
        """The entity type to create."""

    def __init__(self, *, entity_type: exabel.api.data.v1.entity_messages_pb2.EntityType | None=...) -> None:
        ...

    def HasField(self, field_name: typing.Literal['entity_type', b'entity_type']) -> builtins.bool:
        ...

    def ClearField(self, field_name: typing.Literal['entity_type', b'entity_type']) -> None:
        ...
global___CreateEntityTypeRequest = CreateEntityTypeRequest

@typing.final
class UpdateEntityTypeRequest(google.protobuf.message.Message):
    """The request to update one entity type."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    ENTITY_TYPE_FIELD_NUMBER: builtins.int
    UPDATE_MASK_FIELD_NUMBER: builtins.int
    ALLOW_MISSING_FIELD_NUMBER: builtins.int
    allow_missing: builtins.bool
    'If set to `true`, a new entity type will be created if it did not exist, and `update_mask` is\n    ignored.\n    '

    @property
    def entity_type(self) -> exabel.api.data.v1.entity_messages_pb2.EntityType:
        """The entity type to update."""

    @property
    def update_mask(self) -> google.protobuf.field_mask_pb2.FieldMask:
        """Use this to update only selected fields. For example, specify `display_name` to update only the
        display name. If `allow_missing` is set, this field is ignored.

        For REST requests, this is a comma-separated string.
        """

    def __init__(self, *, entity_type: exabel.api.data.v1.entity_messages_pb2.EntityType | None=..., update_mask: google.protobuf.field_mask_pb2.FieldMask | None=..., allow_missing: builtins.bool | None=...) -> None:
        ...

    def HasField(self, field_name: typing.Literal['entity_type', b'entity_type', 'update_mask', b'update_mask']) -> builtins.bool:
        ...

    def ClearField(self, field_name: typing.Literal['allow_missing', b'allow_missing', 'entity_type', b'entity_type', 'update_mask', b'update_mask']) -> None:
        ...
global___UpdateEntityTypeRequest = UpdateEntityTypeRequest

@typing.final
class DeleteEntityTypeRequest(google.protobuf.message.Message):
    """The request to delete one entity type."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    NAME_FIELD_NUMBER: builtins.int
    name: builtins.str
    'The resource name of the entity type to delete, for example `entityTypes/ns.type1`.'

    def __init__(self, *, name: builtins.str | None=...) -> None:
        ...

    def ClearField(self, field_name: typing.Literal['name', b'name']) -> None:
        ...
global___DeleteEntityTypeRequest = DeleteEntityTypeRequest

@typing.final
class ListEntitiesRequest(google.protobuf.message.Message):
    """The request to list entities."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    PARENT_FIELD_NUMBER: builtins.int
    PAGE_SIZE_FIELD_NUMBER: builtins.int
    PAGE_TOKEN_FIELD_NUMBER: builtins.int
    parent: builtins.str
    'The parent entity type of the entities to list, for example `entityTypes/ns.type1`.'
    page_size: builtins.int
    'Maximum number of results to return. Defaults to 1000, which is the maximum allowed value.'
    page_token: builtins.str
    'Token for a specific page of results, as returned from a previous list request with the\n    same query parameters.\n    '

    def __init__(self, *, parent: builtins.str | None=..., page_size: builtins.int | None=..., page_token: builtins.str | None=...) -> None:
        ...

    def ClearField(self, field_name: typing.Literal['page_size', b'page_size', 'page_token', b'page_token', 'parent', b'parent']) -> None:
        ...
global___ListEntitiesRequest = ListEntitiesRequest

@typing.final
class ListEntitiesResponse(google.protobuf.message.Message):
    """The response to list entities. Returns all entities of a given entity type, with only name set."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    ENTITIES_FIELD_NUMBER: builtins.int
    NEXT_PAGE_TOKEN_FIELD_NUMBER: builtins.int
    TOTAL_SIZE_FIELD_NUMBER: builtins.int
    next_page_token: builtins.str
    'Token for the next page of results, which can be sent to a subsequent query.\n    The end of the list is reached when the number of results is less than the page size\n    (NOT when the token is empty).\n    '
    total_size: builtins.int
    'Total number of results, irrespective of paging.'

    @property
    def entities(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[exabel.api.data.v1.entity_messages_pb2.Entity]:
        """List of entities."""

    def __init__(self, *, entities: collections.abc.Iterable[exabel.api.data.v1.entity_messages_pb2.Entity] | None=..., next_page_token: builtins.str | None=..., total_size: builtins.int | None=...) -> None:
        ...

    def ClearField(self, field_name: typing.Literal['entities', b'entities', 'next_page_token', b'next_page_token', 'total_size', b'total_size']) -> None:
        ...
global___ListEntitiesResponse = ListEntitiesResponse

@typing.final
class DeleteEntitiesRequest(google.protobuf.message.Message):
    """The request to delete all entities of a given entity type."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    PARENT_FIELD_NUMBER: builtins.int
    CONFIRM_FIELD_NUMBER: builtins.int
    parent: builtins.str
    'The parent entity type of the entities to delete, for example `entityTypes/ns.type1`.'
    confirm: builtins.bool
    'Safeguard against accidental deletion. Must be set to `true` for deletion to take place.'

    def __init__(self, *, parent: builtins.str | None=..., confirm: builtins.bool | None=...) -> None:
        ...

    def ClearField(self, field_name: typing.Literal['confirm', b'confirm', 'parent', b'parent']) -> None:
        ...
global___DeleteEntitiesRequest = DeleteEntitiesRequest

@typing.final
class GetEntityRequest(google.protobuf.message.Message):
    """The request to get one entity."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    NAME_FIELD_NUMBER: builtins.int
    name: builtins.str
    'The resource name of the requested entity, for example `entityTypes/ns.type1/entities/ns.entity1`.'

    def __init__(self, *, name: builtins.str | None=...) -> None:
        ...

    def ClearField(self, field_name: typing.Literal['name', b'name']) -> None:
        ...
global___GetEntityRequest = GetEntityRequest

@typing.final
class CreateEntityRequest(google.protobuf.message.Message):
    """The response to create one entity."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    PARENT_FIELD_NUMBER: builtins.int
    ENTITY_FIELD_NUMBER: builtins.int
    parent: builtins.str
    'The parent entity type of the created entity, for example `entityTypes/ns.type1`.'

    @property
    def entity(self) -> exabel.api.data.v1.entity_messages_pb2.Entity:
        """The entity to create."""

    def __init__(self, *, parent: builtins.str | None=..., entity: exabel.api.data.v1.entity_messages_pb2.Entity | None=...) -> None:
        ...

    def HasField(self, field_name: typing.Literal['entity', b'entity']) -> builtins.bool:
        ...

    def ClearField(self, field_name: typing.Literal['entity', b'entity', 'parent', b'parent']) -> None:
        ...
global___CreateEntityRequest = CreateEntityRequest

@typing.final
class UpdateEntityRequest(google.protobuf.message.Message):
    """The request to update one entity."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    ENTITY_FIELD_NUMBER: builtins.int
    UPDATE_MASK_FIELD_NUMBER: builtins.int
    ALLOW_MISSING_FIELD_NUMBER: builtins.int
    allow_missing: builtins.bool
    'If set to `true`, a new entity will be created if it did not exist, and `update_mask` is\n    ignored.\n    '

    @property
    def entity(self) -> exabel.api.data.v1.entity_messages_pb2.Entity:
        """The entity to update."""

    @property
    def update_mask(self) -> google.protobuf.field_mask_pb2.FieldMask:
        """Use this to update only selected fields. For example, specify `display_name` to update only the
        display name. If `allow_missing` is set, this field is ignored.

        For REST requests, this is a comma-separated string.
        """

    def __init__(self, *, entity: exabel.api.data.v1.entity_messages_pb2.Entity | None=..., update_mask: google.protobuf.field_mask_pb2.FieldMask | None=..., allow_missing: builtins.bool | None=...) -> None:
        ...

    def HasField(self, field_name: typing.Literal['entity', b'entity', 'update_mask', b'update_mask']) -> builtins.bool:
        ...

    def ClearField(self, field_name: typing.Literal['allow_missing', b'allow_missing', 'entity', b'entity', 'update_mask', b'update_mask']) -> None:
        ...
global___UpdateEntityRequest = UpdateEntityRequest

@typing.final
class DeleteEntityRequest(google.protobuf.message.Message):
    """The request to delete one entity."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    NAME_FIELD_NUMBER: builtins.int
    name: builtins.str
    'The resource name of the entity to delete, for example `entityTypes/ns.type1/entities/ns.entity1`.'

    def __init__(self, *, name: builtins.str | None=...) -> None:
        ...

    def ClearField(self, field_name: typing.Literal['name', b'name']) -> None:
        ...
global___DeleteEntityRequest = DeleteEntityRequest

@typing.final
class SearchEntitiesRequest(google.protobuf.message.Message):
    """The request to search for one or more entities."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    PARENT_FIELD_NUMBER: builtins.int
    TERMS_FIELD_NUMBER: builtins.int
    OPTIONS_FIELD_NUMBER: builtins.int
    PAGE_SIZE_FIELD_NUMBER: builtins.int
    PAGE_TOKEN_FIELD_NUMBER: builtins.int
    parent: builtins.str
    'The parent entity type of the entities to list, for example `entityTypes/ns.type1`.'
    page_size: builtins.int
    'The maximum number of results to return. Defaults to 1000, which is also the maximum value\n    of this field. (Not implemented yet.)\n    '
    page_token: builtins.str
    'The page token to resume the results from, as returned from a previous request to this method\n    with the same query parameters. (Not implemented yet.)\n    '

    @property
    def terms(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[exabel.api.data.v1.search_messages_pb2.SearchTerm]:
        """Search terms."""

    @property
    def options(self) -> exabel.api.data.v1.search_messages_pb2.SearchOptions:
        """Options on how the search should be performed. Currently only affects company search using
        field 'text'.
        """

    def __init__(self, *, parent: builtins.str | None=..., terms: collections.abc.Iterable[exabel.api.data.v1.search_messages_pb2.SearchTerm] | None=..., options: exabel.api.data.v1.search_messages_pb2.SearchOptions | None=..., page_size: builtins.int | None=..., page_token: builtins.str | None=...) -> None:
        ...

    def HasField(self, field_name: typing.Literal['options', b'options']) -> builtins.bool:
        ...

    def ClearField(self, field_name: typing.Literal['options', b'options', 'page_size', b'page_size', 'page_token', b'page_token', 'parent', b'parent', 'terms', b'terms']) -> None:
        ...
global___SearchEntitiesRequest = SearchEntitiesRequest

@typing.final
class SearchEntitiesResponse(google.protobuf.message.Message):
    """The response to searching for entities. Returns all entities matching the search parameters."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    @typing.final
    class SearchResult(google.protobuf.message.Message):
        """The result of one search."""
        DESCRIPTOR: google.protobuf.descriptor.Descriptor
        TERMS_FIELD_NUMBER: builtins.int
        ENTITIES_FIELD_NUMBER: builtins.int

        @property
        def terms(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[exabel.api.data.v1.search_messages_pb2.SearchTerm]:
            """The terms used for this search."""

        @property
        def entities(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[exabel.api.data.v1.entity_messages_pb2.Entity]:
            """All entities matching one search, possibly empty if no entities matched this search."""

        def __init__(self, *, terms: collections.abc.Iterable[exabel.api.data.v1.search_messages_pb2.SearchTerm] | None=..., entities: collections.abc.Iterable[exabel.api.data.v1.entity_messages_pb2.Entity] | None=...) -> None:
            ...

        def ClearField(self, field_name: typing.Literal['entities', b'entities', 'terms', b'terms']) -> None:
            ...
    RESULTS_FIELD_NUMBER: builtins.int
    NEXT_PAGE_TOKEN_FIELD_NUMBER: builtins.int
    ENTITIES_FIELD_NUMBER: builtins.int
    next_page_token: builtins.str
    'The page token where the search continues. Can be sent to a subsequent query. (Not implemented\n    yet.)\n    '

    @property
    def results(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___SearchEntitiesResponse.SearchResult]:
        """The results of each search, in the request order. Note that some consecutive terms are defined
        as belonging to one search query, and in these cases the number of results will be less than
        the number of search terms.
        """

    @property
    def entities(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[exabel.api.data.v1.entity_messages_pb2.Entity]:
        """The resulting entities, concatenated from multiple search terms. (Kept for backwards
        compatibility.)
        """

    def __init__(self, *, results: collections.abc.Iterable[global___SearchEntitiesResponse.SearchResult] | None=..., next_page_token: builtins.str | None=..., entities: collections.abc.Iterable[exabel.api.data.v1.entity_messages_pb2.Entity] | None=...) -> None:
        ...

    def ClearField(self, field_name: typing.Literal['entities', b'entities', 'next_page_token', b'next_page_token', 'results', b'results']) -> None:
        ...
global___SearchEntitiesResponse = SearchEntitiesResponse