from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api import v1_router
from app.config import logger
from app.database import MongoManager, RedisManager

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['http://localhost:8000/', 'https://auth-and-login-app.herokuapp.com'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
async def on_startup():
    await MongoManager.connect()
    await RedisManager.connect()
    logger.info('Startup event - connecting to the database')


app.include_router(v1_router)
