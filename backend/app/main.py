from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api.api import api_router
from core.redis import redis_dependency
from core.config import settings
from db.database import database


app = FastAPI(title='Midas Bot API')
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)
app.include_router(api_router, prefix=settings.API_V1_STR)


@app.on_event('startup')
async def startup():
    print('startup')
    await redis_dependency.init()
    await database.connect()


@app.on_event('shutdown')
async def shutdown():
    await database.disconnect()


@app.get('/health')
async def home():
    return {'message': 'ok'}