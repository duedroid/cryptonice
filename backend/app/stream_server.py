from typing import Optional

from fastapi import BackgroundTasks, FastAPI, Header, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from core.binance_stream import binance_stream
from core.config import settings


app = FastAPI(title='Cryptonice Stream API')
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)


@app.get('/health')
async def home():
    return {'message': 'ok'}


class Symbol(BaseModel):
    symbol: str


@app.post('/listener/ticker/start')
async def start_listener(
    data: Symbol,
    background_tasks: BackgroundTasks,
    authorization: Optional[str] = Header(None),
):
    if authorization != 'Bearer ' + settings.STREAM_SERVER_TOKEN:
        raise HTTPException(401)

    background_tasks.add_task(binance_stream.start_ticker_listener, data.symbol)
    return {}


@app.post('/listener/ticker/stop')
async def stop_listener(data: Symbol, authorization: Optional[str] = Header(None),):
    if authorization != 'Bearer ' + settings.STREAM_SERVER_TOKEN:
        raise HTTPException(401)

    await binance_stream.stop_ticker_listener(data.symbol)
    return {}


@app.get('/symbols/active')
async def active_symbols():
    return {'symbols': binance_stream.active_symbols}


@app.on_event('startup')
async def startup():
    print('startup !!!')
    await binance_stream.startup()