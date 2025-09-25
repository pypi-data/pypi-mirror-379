from itertools import islice

redis_alias_map = {
    # 'name': int(val),
}

redis_alias_map = dict(islice(redis_alias_map.items(), 16))
