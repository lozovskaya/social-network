import datetime
from typing import List
from fastapi import Depends, APIRouter, HTTPException, status
from dependencies import get_stub
from src.protos import posts_pb2
from src.protos.posts_pb2_grpc import PostServiceStub
from src.models.schemas import FullInfoPost, Post, UserModel
import security

router = APIRouter(
    prefix="/posts",
    tags=["posts"],)


@router.post("/create", response_model=int)
def new_post(new_post: Post, grpc_stub: PostServiceStub = Depends(get_stub), current_user_id: int = Depends(security.get_current_user_id)):
    response = grpc_stub.CreatePost(posts_pb2.CreatePostRequest(user_id=current_user_id, title=new_post.title, content=new_post.content))

    return response.id


@router.put("/update", response_model=None)
def update_post(post_id: int, updated_post: Post, grpc_stub: PostServiceStub = Depends(get_stub), current_user_id: int = Depends(security.get_current_user_id)):
    response = grpc_stub.UpdatePost(posts_pb2.UpdatePostRequest(id=int(post_id), user_id=current_user_id, title=updated_post.title, content=updated_post.content))

    if int(response.status) != 0:
        raise HTTPException(status.HTTP_404_NOT_FOUND, "The post hasn't been found")

    return 


@router.delete("/delete", response_model=None)
def delete_post(post_id: int, grpc_stub: PostServiceStub = Depends(get_stub), current_user_id: int = Depends(security.get_current_user_id)):
    response = grpc_stub.DeletePost(posts_pb2.DeletePostRequest(id=int(post_id), user_id=current_user_id))
    return 


@router.get("/", response_model=FullInfoPost)
def get_post(post_id: int, grpc_stub: PostServiceStub = Depends(get_stub)):
    response = grpc_stub.GetPostById(posts_pb2.GetPostByIdRequest(id=int(post_id)))

    if response.status != 0:
        raise HTTPException(status.HTTP_404_NOT_FOUND, "The post hasn't been found")

    return convert_to_post_model(response.post)


@router.get("/list", response_model=List[FullInfoPost])
async def get_all_posts(page_number : int, page_size : int, grpc_stub: PostServiceStub = Depends(get_stub)):
    response = grpc_stub.ListPosts(posts_pb2.ListPostsRequest(page=page_number, page_size=page_size))

    posts_list = list()
    for post in response.posts:
        posts_list.append(convert_to_post_model(post))
    return posts_list


def convert_to_post_model(grpc_post) -> FullInfoPost:
    time_seconds_created = grpc_post.created_at.seconds + grpc_post.created_at.nanos / 1e9
    time_seconds_edited = grpc_post.edited_at.seconds + grpc_post.edited_at.nanos / 1e9

    return FullInfoPost(
        post_id=grpc_post.id,
        user_id=grpc_post.user_id,
        title=grpc_post.title,
        content=grpc_post.content,
        created_at=datetime.datetime.fromtimestamp(time_seconds_created),
        edited_at=datetime.datetime.fromtimestamp(time_seconds_edited)
    )