from fastapi import FastAPI
from src.routers import user_router
from src.models import database

database.Base.metadata.create_all(bind=database.engine)

app = FastAPI()

app.include_router(user_router.router)

@app.get("/")
async def root():
    return {"message": "Core service!"}