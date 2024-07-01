"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
Copyright (c) 2022 Exabel AS. All rights reserved."""
import builtins
import collections.abc
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import typing
DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing.final
class User(google.protobuf.message.Message):
    """A user."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    NAME_FIELD_NUMBER: builtins.int
    EMAIL_FIELD_NUMBER: builtins.int
    BLOCKED_FIELD_NUMBER: builtins.int
    name: builtins.str
    'Unique resource name of the user, e.g. `users/123`.'
    email: builtins.str
    "User's email."
    blocked: builtins.bool
    'Whether the user is blocked from accessing the system.'

    def __init__(self, *, name: builtins.str | None=..., email: builtins.str | None=..., blocked: builtins.bool | None=...) -> None:
        ...

    def ClearField(self, field_name: typing.Literal['blocked', b'blocked', 'email', b'email', 'name', b'name']) -> None:
        ...
global___User = User

@typing.final
class Group(google.protobuf.message.Message):
    """A group."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    NAME_FIELD_NUMBER: builtins.int
    DISPLAY_NAME_FIELD_NUMBER: builtins.int
    USERS_FIELD_NUMBER: builtins.int
    name: builtins.str
    'Unique resource name of the user group, e.g. `groups/123`.'
    display_name: builtins.str
    'Display name of the user group, shown in the Library when sharing a folder with any of the\n    customer user groups.\n    '

    @property
    def users(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___User]:
        """List of users in this user group. Only populated for some responses (refer to documentation for
        each method).
        """

    def __init__(self, *, name: builtins.str | None=..., display_name: builtins.str | None=..., users: collections.abc.Iterable[global___User] | None=...) -> None:
        ...

    def ClearField(self, field_name: typing.Literal['display_name', b'display_name', 'name', b'name', 'users', b'users']) -> None:
        ...
global___Group = Group