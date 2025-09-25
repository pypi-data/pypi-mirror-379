"""
==============
PyRedisManager
==============
A lightweight, standalone Redis client manager supporting both synchronous and asynchronous operations, multi-alias management, and module-level singleton design.
Only depends on the official redis / redis.asyncio library—no Flask, Django, or other frameworks required.
"""

from .manager import RedisManager, redis_manager
from .async_manager import AsyncRedisManager, async_redis_manager

__all__ = ["RedisManager", "redis_manager", "AsyncRedisManager", "async_redis_manager"]
__version__ = "0.1.4"
