### Fastapi cache

```python
from fastapi_tools.cache import RedisConfig, RedisFactory


config = RedisConfig(...)
redis_factory = RedisFactory(config)
redis_client = redis_factory.get_async()
```

