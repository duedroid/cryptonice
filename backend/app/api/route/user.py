import ujson

from aioredis import Redis
from fastapi import APIRouter, BackgroundTasks, Depends

from core.auth import get_current_user
from core.exchange import Exchange
from core.redis import redis_dependency
from models.user import User


router = APIRouter()


async def get_balances(api_key: str, api_secret: str):
    user_exchange = Exchange(api_key, api_secret)
    total_balance = user_exchange.get_balance()
    balances = []
    for balance in total_balance['balances']:
        amount = float(balance['free']) + float(balance['locked'])
        if amount == 0:
            continue

        asset = balance['asset']
        balances.append({
            'asset': asset,
            'amount': amount
        })

    return balances


@router.get('/balance')
async def get_balance(
    background_tasks: BackgroundTasks,
    current_user: User = Depends(get_current_user),
    redis: Redis = Depends(redis_dependency),
):
    key = f'balance_{current_user.id}'
    response = await redis.get(key)
    if response is None:
        balances = await get_balances(current_user.api_key, current_user.api_secret)
        response = {
            'bridge': current_user.bridge,
            'balances': balances
        }
        background_tasks.add_task(redis.set, key=key, value=ujson.dumps(response), ttl=10)
        return response
    
    return ujson.loads(response)