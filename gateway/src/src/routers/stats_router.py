from datetime import datetime
import logging
import os
from fastapi import Depends, APIRouter, HTTPException, status
from dependencies import get_kafka_producer, get_stub_stats, get_stub, get_db
from src.protos.posts_pb2_grpc import PostServiceStub
from src.protos import posts_pb2
from src.protos import stats_pb2
from src.protos.stats_pb2_grpc import StatsServiceStub
import security
from sqlalchemy.orm import Session
from src.cruds import crud_credentials


router = APIRouter(
    prefix="/stats",
    tags=["stats"],)


@router.post("/like/{post_id}")
async def new_like(post_id: int, grpc_stub: PostServiceStub = Depends(get_stub), kafka_producer = Depends(get_kafka_producer), current_user_id: int = Depends(security.get_current_user_id)):
    response = grpc_stub.GetPostById(posts_pb2.GetPostByIdRequest(id=int(post_id)))
    if response.status != 0:
        raise HTTPException(status.HTTP_404_NOT_FOUND, "The post hasn't been found")
    owner = response.post.user_id
    logging.info(owner)
    await kafka_producer.send_message(os.getenv('KAFKA_TOPIC'), {"type_action": "like", 
                                                                 "post_id": post_id, 
                                                                 "current_user_id": current_user_id, 
                                                                 "time_stamp": datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                                                                 "post_owner": owner})


@router.post("/view/{post_id}")
async def new_view(post_id: str, grpc_stub: PostServiceStub = Depends(get_stub), kafka_producer = Depends(get_kafka_producer), current_user_id: int = Depends(security.get_current_user_id)):
    response = grpc_stub.GetPostById(posts_pb2.GetPostByIdRequest(id=int(post_id)))
    if response.status != 0:
        raise HTTPException(status.HTTP_404_NOT_FOUND, "The post hasn't been found")
    owner = response.post.user_id
    await kafka_producer.send_message(os.getenv('KAFKA_TOPIC'), {"type_action": "view", 
                                                                 "post_id": post_id, 
                                                                 "current_user_id": current_user_id, 
                                                                 "time_stamp": datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                                                                 "post_owner": owner})
    # todo: add background tasks

@router.get("/post/{post_id}")
def get_post_stats(post_id: int, grpc_stub: StatsServiceStub = Depends(get_stub_stats)):
    response = grpc_stub.GetPostStats(stats_pb2.GetPostStatsRequest(id=post_id))
    return {"likes": response.likes, "views": response.views}


@router.get("/popular_posts/{action_type}")
def get_popular_posts(action_type: str, grpc_stub: StatsServiceStub = Depends(get_stub_stats), db: Session = Depends(get_db)):
    response = grpc_stub.GetPopularPosts(stats_pb2.GetPopularPostsRequest(action_type=action_type, size=5))
    posts_list = list()
    for post in response.posts:
        posts_list.append(convert_to_post_dict(post, db))
    return posts_list


@router.get("/popular_users")
def get_popular_users(grpc_stub: StatsServiceStub = Depends(get_stub_stats), db: Session = Depends(get_db)):
    response = grpc_stub.GetPopularUsers(stats_pb2.GetPopularUsersRequest(count=3))
    users_list = list()
    for user in response.users:
        users_list.append(convert_to_user_dict(user, db))
    return users_list


def convert_to_post_dict(grpc_post, db) -> dict:
    login = crud_credentials.get_credentials_by_user_id(db, grpc_post.user_login)
    if login:
        login = login.login
    return {
        "post_id": grpc_post.id,
        "login": login,
        "count": grpc_post.count
    }
    
    
def convert_to_user_dict(grpc_user, db) -> dict:
    login = crud_credentials.get_credentials_by_user_id(db, int(grpc_user.login))
    if login:
        login = login.login
    return {"login": login, "likes": grpc_user.likes}