from redis.asyncio import from_url

from src.core.credentails import settings

redis = from_url(settings.REDIS_URL.unicode_string())