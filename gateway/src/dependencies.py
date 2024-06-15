import asyncio
from functools import lru_cache
import os
from dotenv import load_dotenv
import grpc
import logging

from common.kafka.producer_manager import KafkaProducer
from src.protos.stats_pb2_grpc import StatsServiceStub
from src.protos.posts_pb2_grpc import PostServiceStub
from src.models import database

# Get a database instance
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Get a grpc client stub instance
def get_stub():
    channel = grpc.insecure_channel("host.docker.internal:50052")
    return PostServiceStub(channel)

def get_stub_stats():
    channel = grpc.insecure_channel("statistics:1329")
    return StatsServiceStub(channel)

# Get a Kafka Producer instance

@lru_cache
def kafka_producer_config():
    kafka_host = os.getenv('KAFKA_HOST')
    kafka_port = os.getenv('KAFKA_PORT')
    config = {"bootstrap_servers": f"{kafka_host}:{kafka_port}", 
              "loop": loop}
    return config


def get_kafka_producer():
    return kafka_producer

load_dotenv()
loop = asyncio.get_event_loop()
kafka_producer = KafkaProducer(kafka_producer_config())
logging.basicConfig(level=logging.INFO)