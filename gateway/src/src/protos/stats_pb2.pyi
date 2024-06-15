from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PostStatsByOneParameter(_message.Message):
    __slots__ = ("id", "user_login", "count")
    ID_FIELD_NUMBER: _ClassVar[int]
    USER_LOGIN_FIELD_NUMBER: _ClassVar[int]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    id: int
    user_login: str
    count: int
    def __init__(self, id: _Optional[int] = ..., user_login: _Optional[str] = ..., count: _Optional[int] = ...) -> None: ...

class GetPostStatsRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: int
    def __init__(self, id: _Optional[int] = ...) -> None: ...

class GetPostStatsResponse(_message.Message):
    __slots__ = ("likes", "views")
    LIKES_FIELD_NUMBER: _ClassVar[int]
    VIEWS_FIELD_NUMBER: _ClassVar[int]
    likes: int
    views: int
    def __init__(self, likes: _Optional[int] = ..., views: _Optional[int] = ...) -> None: ...

class GetPopularPostsRequest(_message.Message):
    __slots__ = ("action_type", "size")
    ACTION_TYPE_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    action_type: str
    size: int
    def __init__(self, action_type: _Optional[str] = ..., size: _Optional[int] = ...) -> None: ...

class GetPopularPostsResponse(_message.Message):
    __slots__ = ("posts",)
    POSTS_FIELD_NUMBER: _ClassVar[int]
    posts: _containers.RepeatedCompositeFieldContainer[PostStatsByOneParameter]
    def __init__(self, posts: _Optional[_Iterable[_Union[PostStatsByOneParameter, _Mapping]]] = ...) -> None: ...

class GetPopularUsersRequest(_message.Message):
    __slots__ = ("count",)
    COUNT_FIELD_NUMBER: _ClassVar[int]
    count: int
    def __init__(self, count: _Optional[int] = ...) -> None: ...

class UserInfo(_message.Message):
    __slots__ = ("login", "likes")
    LOGIN_FIELD_NUMBER: _ClassVar[int]
    LIKES_FIELD_NUMBER: _ClassVar[int]
    login: str
    likes: int
    def __init__(self, login: _Optional[str] = ..., likes: _Optional[int] = ...) -> None: ...

class GetPopularUsersResponse(_message.Message):
    __slots__ = ("users",)
    USERS_FIELD_NUMBER: _ClassVar[int]
    users: _containers.RepeatedCompositeFieldContainer[UserInfo]
    def __init__(self, users: _Optional[_Iterable[_Union[UserInfo, _Mapping]]] = ...) -> None: ...
