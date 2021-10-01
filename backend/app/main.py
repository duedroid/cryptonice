from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api.api import api_router
from core.binance import binance_socket
from core.config import settings


app = FastAPI(title=settings.PROJECT_NAME)
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)
app.include_router(api_router, prefix=settings.API_V1_STR)


@app.get('/health')
async def home():
    return {'message': 'ok'}


@app.on_event('startup')
async def startup():
    print('startup !!!')
    await binance_socket.startup()