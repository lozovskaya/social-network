from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Post(_message.Message):
    __slots__ = ("id", "user_id", "title", "content", "created_at", "edited_at")
    ID_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    EDITED_AT_FIELD_NUMBER: _ClassVar[int]
    id: int
    user_id: int
    title: str
    content: str
    created_at: _timestamp_pb2.Timestamp
    edited_at: _timestamp_pb2.Timestamp
    def __init__(self, id: _Optional[int] = ..., user_id: _Optional[int] = ..., title: _Optional[str] = ..., content: _Optional[str] = ..., created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., edited_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class CreatePostRequest(_message.Message):
    __slots__ = ("user_id", "title", "content")
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    user_id: int
    title: str
    content: str
    def __init__(self, user_id: _Optional[int] = ..., title: _Optional[str] = ..., content: _Optional[str] = ...) -> None: ...

class CreatePostResponse(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: int
    def __init__(self, id: _Optional[int] = ...) -> None: ...

class UpdatePostRequest(_message.Message):
    __slots__ = ("id", "user_id", "title", "content")
    ID_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    id: int
    user_id: int
    title: str
    content: str
    def __init__(self, id: _Optional[int] = ..., user_id: _Optional[int] = ..., title: _Optional[str] = ..., content: _Optional[str] = ...) -> None: ...

class DeletePostRequest(_message.Message):
    __slots__ = ("id", "user_id")
    ID_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    id: int
    user_id: int
    def __init__(self, id: _Optional[int] = ..., user_id: _Optional[int] = ...) -> None: ...

class GetPostByIdRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: int
    def __init__(self, id: _Optional[int] = ...) -> None: ...

class ListPostsRequest(_message.Message):
    __slots__ = ("page", "page_size")
    PAGE_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    page: int
    page_size: int
    def __init__(self, page: _Optional[int] = ..., page_size: _Optional[int] = ...) -> None: ...

class ListPostsResponse(_message.Message):
    __slots__ = ("posts",)
    POSTS_FIELD_NUMBER: _ClassVar[int]
    posts: _containers.RepeatedCompositeFieldContainer[Post]
    def __init__(self, posts: _Optional[_Iterable[_Union[Post, _Mapping]]] = ...) -> None: ...

class PostResponse(_message.Message):
    __slots__ = ("post", "status")
    POST_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    post: Post
    status: int
    def __init__(self, post: _Optional[_Union[Post, _Mapping]] = ..., status: _Optional[int] = ...) -> None: ...

class StatusResponse(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: int
    def __init__(self, status: _Optional[int] = ...) -> None: ...

class EmptyResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...
