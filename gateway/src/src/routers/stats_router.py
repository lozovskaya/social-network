from datetime import datetime
import os
from fastapi import Depends, APIRouter
from dependencies import get_kafka_producer
import security

router = APIRouter(
    prefix="/stats",
    tags=["stats"],)


@router.post("/like/{post_id}")
async def new_like(post_id: int, kafka_producer = Depends(get_kafka_producer), current_user_id: int = Depends(security.get_current_user_id)):
    await kafka_producer.send_message(os.getenv('KAFKA_TOPIC'), {"type_action": "like", 
                                                                 "post_id": post_id, 
                                                                 "current_user_id": current_user_id, 
                                                                 "time_stamp": datetime.now().strftime('%Y-%m-%d %H:%M:%S')})


@router.post("/view/{post_id}")
async def new_view(post_id: str, kafka_producer = Depends(get_kafka_producer), current_user_id: int = Depends(security.get_current_user_id)):
    await kafka_producer.send_message(os.getenv('KAFKA_TOPIC'), {"type_action": "view", 
                                                                 "post_id": post_id, 
                                                                 "current_user_id": current_user_id, 
                                                                 "time_stamp": datetime.now().strftime('%Y-%m-%d %H:%M:%S')})