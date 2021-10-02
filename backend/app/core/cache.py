from typing import Any

import aioredis

from .config import settings


class Cache:
    price_prefix = 'price_'

    def __init__(self):
        self.redis = aioredis.from_url(settings.REDIS_URL, decode_responses=True)
    
    async def set_value(self, key: str, value: Any, ttl: int = 60):
        await self.redis.set(self.price_prefix + key, value, ttl)
    
    async def get_value(self, key: str):
        await self.redis.get(self.price_prefix + key)
    
    async def delete_value(self, key: str):
        await self.redis.delete(self.price_prefix + key)


cache = Cache()