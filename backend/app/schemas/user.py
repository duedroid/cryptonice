from enum import Enum

from fastapi import HTTPException
from pydantic import BaseModel, root_validator

from core.exchange import Exchange


class BridgeEnum(str, Enum):
    USDT = 'USDT'
    BUSD = 'BUSD'
    BTC = 'BTC'


class UserRegister(BaseModel):
    username: str
    password: str
    bridge: BridgeEnum = BridgeEnum.USDT
    api_key: str
    api_secret: str

    @root_validator
    def check_api_key(cls, values):
        exchange = Exchange(values.get('api_key'), values.get('api_secret'))
        auth = exchange.check_auth()
        if not auth:
            raise HTTPException(status_code=400, detail='API Key is invalid')
        
        return values
        