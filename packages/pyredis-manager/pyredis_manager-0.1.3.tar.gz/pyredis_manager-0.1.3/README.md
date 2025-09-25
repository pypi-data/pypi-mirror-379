# PyRedisManager

A lightweight, standalone Redis client manager supporting both synchronous and asynchronous operations, multi-alias management, and module-level singleton design.
Only depends on the official redis / redis.asyncio library—no Flask, Django, or other frameworks required.


## install

```bash
pip install pyredis-manager
```

Synchronous Example:

```python
from pyredis_manager import redis_manager


redis_manager.set_alias('default', 0)
default = redis_manager.get('default')
default.set(name='foo', value='bar', ex=300)
val = default.get('foo')
print(val)
```

Asynchronous Example:

```python
import asyncio

from pyredis_manager import async_redis_manager


async def main():
    async_redis_manager.set_alias("default", 0)
    default = async_redis_manager.get("default")
    await default.set(name="fooo", value="barr", ex=300)
    val = await default.get("fooo")
    print(val)


asyncio.run(main())
```

## Features

- Module-level singleton for a globally unique instance

- Multi-alias management, each alias maps to an independent Redis DB

- Supports synchronous and asynchronous Redis clients

- Simple, type-hinted, IDE-friendly API

- Framework-agnostic
