import pytest
from pyredis_manager.async_manager import AsyncRedisManager

@pytest.fixture
def async_redis_manager():
    return AsyncRedisManager(db_aliases={"default": 0})

@pytest.mark.asyncio
async def test_async_set_and_get(async_redis_manager):
    client = async_redis_manager.get("default")
    await client.set("foo", "bar")
    value = await client.get("foo")
    assert value == b"bar"

@pytest.mark.asyncio
async def test_async_alias_limit(async_redis_manager):
    assert len(async_redis_manager.aliases) <= 16
