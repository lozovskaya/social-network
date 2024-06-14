# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: posts.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0bposts.proto\x12\x0cpost_service\x1a\x1fgoogle/protobuf/timestamp.proto\"\xa2\x01\n\x04Post\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x0f\n\x07user_id\x18\x02 \x01(\x05\x12\r\n\x05title\x18\x03 \x01(\t\x12\x0f\n\x07\x63ontent\x18\x04 \x01(\t\x12.\n\ncreated_at\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12-\n\tedited_at\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"D\n\x11\x43reatePostRequest\x12\x0f\n\x07user_id\x18\x01 \x01(\x05\x12\r\n\x05title\x18\x02 \x01(\t\x12\x0f\n\x07\x63ontent\x18\x03 \x01(\t\" \n\x12\x43reatePostResponse\x12\n\n\x02id\x18\x01 \x01(\x05\"P\n\x11UpdatePostRequest\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x0f\n\x07user_id\x18\x02 \x01(\x05\x12\r\n\x05title\x18\x03 \x01(\t\x12\x0f\n\x07\x63ontent\x18\x04 \x01(\t\"0\n\x11\x44\x65letePostRequest\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x0f\n\x07user_id\x18\x02 \x01(\x05\" \n\x12GetPostByIdRequest\x12\n\n\x02id\x18\x01 \x01(\x05\"3\n\x10ListPostsRequest\x12\x0c\n\x04page\x18\x01 \x01(\x05\x12\x11\n\tpage_size\x18\x02 \x01(\x05\"6\n\x11ListPostsResponse\x12!\n\x05posts\x18\x01 \x03(\x0b\x32\x12.post_service.Post\"@\n\x0cPostResponse\x12 \n\x04post\x18\x01 \x01(\x0b\x32\x12.post_service.Post\x12\x0e\n\x06status\x18\x02 \x01(\x05\" \n\x0eStatusResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\"\x0f\n\rEmptyResponse2\x93\x03\n\x0bPostService\x12O\n\nCreatePost\x12\x1f.post_service.CreatePostRequest\x1a .post_service.CreatePostResponse\x12K\n\nUpdatePost\x12\x1f.post_service.UpdatePostRequest\x1a\x1c.post_service.StatusResponse\x12K\n\nDeletePost\x12\x1f.post_service.DeletePostRequest\x1a\x1c.post_service.StatusResponse\x12K\n\x0bGetPostById\x12 .post_service.GetPostByIdRequest\x1a\x1a.post_service.PostResponse\x12L\n\tListPosts\x12\x1e.post_service.ListPostsRequest\x1a\x1f.post_service.ListPostsResponseB\x04Z\x02./b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'posts_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z\002./'
  _globals['_POST']._serialized_start=63
  _globals['_POST']._serialized_end=225
  _globals['_CREATEPOSTREQUEST']._serialized_start=227
  _globals['_CREATEPOSTREQUEST']._serialized_end=295
  _globals['_CREATEPOSTRESPONSE']._serialized_start=297
  _globals['_CREATEPOSTRESPONSE']._serialized_end=329
  _globals['_UPDATEPOSTREQUEST']._serialized_start=331
  _globals['_UPDATEPOSTREQUEST']._serialized_end=411
  _globals['_DELETEPOSTREQUEST']._serialized_start=413
  _globals['_DELETEPOSTREQUEST']._serialized_end=461
  _globals['_GETPOSTBYIDREQUEST']._serialized_start=463
  _globals['_GETPOSTBYIDREQUEST']._serialized_end=495
  _globals['_LISTPOSTSREQUEST']._serialized_start=497
  _globals['_LISTPOSTSREQUEST']._serialized_end=548
  _globals['_LISTPOSTSRESPONSE']._serialized_start=550
  _globals['_LISTPOSTSRESPONSE']._serialized_end=604
  _globals['_POSTRESPONSE']._serialized_start=606
  _globals['_POSTRESPONSE']._serialized_end=670
  _globals['_STATUSRESPONSE']._serialized_start=672
  _globals['_STATUSRESPONSE']._serialized_end=704
  _globals['_EMPTYRESPONSE']._serialized_start=706
  _globals['_EMPTYRESPONSE']._serialized_end=721
  _globals['_POSTSERVICE']._serialized_start=724
  _globals['_POSTSERVICE']._serialized_end=1127
# @@protoc_insertion_point(module_scope)