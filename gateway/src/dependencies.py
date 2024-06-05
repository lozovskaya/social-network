import grpc

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