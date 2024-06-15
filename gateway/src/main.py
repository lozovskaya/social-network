from contextlib import asynccontextmanager
from fastapi import FastAPI
from src.routers import user_router, posts_router, stats_router
from src.models import database
from dependencies import kafka_producer

database.Base.metadata.create_all(bind=database.engine)

@asynccontextmanager
async def lifespan(_ : FastAPI):
    await kafka_producer.create()
    await kafka_producer.start()
    yield
    await kafka_producer.stop()


app = FastAPI(lifespan=lifespan)

app.include_router(user_router.router)
app.include_router(posts_router.router)
app.include_router(stats_router.router)

@app.get("/")
async def root():
    return {"message": "Core service!"}