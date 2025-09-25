from itertools import islice
from typing import Dict, Optional
from redis.asyncio.client import Redis as AsyncRedis

try:
    from .map import redis_alias_map
except ImportError:
    redis_alias_map = {}


class AsyncRedisManager:
    def __init__(
        self,
        host: str = "localhost",
        port: int = 6379,
        db_aliases: dict = None,
        **kwargs
    ) -> None:
        self.clients: Dict[str, AsyncRedis] = {}
        self.host = host
        self.port = port

        if db_aliases is None: 
            db_aliases = dict(islice(redis_alias_map.items(), 16))
        else:
            db_aliases = dict(islice(db_aliases.items(), 16))
        self.aliases = db_aliases

        # init clients
        for alias, db_num in self.aliases.items():
            self.clients[alias] = AsyncRedis(host=host, port=port, db=db_num, **kwargs)

    def get(self, alias: str) -> Optional[AsyncRedis]:
        return self.clients.get(alias)

    def set_alias(self, alias: str, db_num: int) -> None:
        self.clients[alias] = AsyncRedis(host=self.host, port=self.port, db=db_num)
        self.aliases[alias] = db_num


async_redis_manager: AsyncRedisManager = AsyncRedisManager()
