from typing import Any, Optional

from aioredis import Redis, from_url

from .config import settings


class RedisBackend:
    redis: Redis
    
    @staticmethod
    async def init():
        self = RedisBackend()
        self.redis = await from_url(settings.REDIS_URL, decode_responses=True)
        return self

    async def set(self, key: str, value: Any, ttl: int):
        return await self.redis.set(key, value, ttl)
    
    async def get(self, key: str):
        return await self.redis.get(key)
    
    async def delete(self, key: str):
        return await self.redis.delete(key)


class RedisDependency:
    redis: Optional[RedisBackend] = None

    async def __call__(self):
        return self.redis

    async def init(self):
        self.redis = await RedisBackend.init()


redis_dependency: RedisDependency = RedisDependency()