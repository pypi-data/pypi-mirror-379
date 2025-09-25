import pytest
from pyredis_manager.manager import RedisManager

@pytest.fixture
def redis_manager():
    return RedisManager(db_aliases={"default": 0})

def test_set_and_get(redis_manager):
    client = redis_manager.get("default")
    client.set("foo", "bar")
    value = client.get("foo")
    assert value == b"bar"

def test_alias_limit(redis_manager):
    assert len(redis_manager.aliases) <= 16
