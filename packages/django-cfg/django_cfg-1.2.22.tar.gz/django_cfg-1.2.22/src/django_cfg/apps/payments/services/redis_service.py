"""
Redis service for universal payments with circuit breaker.
"""

import logging
import redis
import json
import time
from typing import Optional, Any, Dict, List
from django_cfg.modules import BaseCfgModule
from django.core.cache import cache
from django.db import transaction

logger = logging.getLogger(__name__)


class RedisCircuitBreaker:
    """Circuit breaker for Redis operations with database fallback."""
    
    def __init__(self, failure_threshold: int = 5, recovery_timeout: int = 60):
        self.failure_threshold = failure_threshold
        self.recovery_timeout = recovery_timeout
        self.failure_count = 0
        self.last_failure_time = None
        self.state = "CLOSED"  # CLOSED, OPEN, HALF_OPEN
    
    def call(self, redis_func, fallback_func, *args, **kwargs):
        """Execute function with circuit breaker pattern."""
        if self.state == "OPEN":
            if self._should_attempt_reset():
                self.state = "HALF_OPEN"
            else:
                logger.warning("Circuit breaker OPEN, using fallback")
                return fallback_func(*args, **kwargs)
        
        try:
            result = redis_func(*args, **kwargs)
            self._on_success()
            return result
        except Exception as e:
            self._on_failure()
            logger.warning(f"Redis operation failed, using fallback: {e}")
            return fallback_func(*args, **kwargs)
    
    def _on_success(self):
        """Handle successful operation."""
        self.failure_count = 0
        self.state = "CLOSED"
    
    def _on_failure(self):
        """Handle failed operation."""
        self.failure_count += 1
        self.last_failure_time = time.time()
        if self.failure_count >= self.failure_threshold:
            self.state = "OPEN"
    
    def _should_attempt_reset(self):
        """Check if circuit breaker should attempt reset."""
        import time
        return (time.time() - self.last_failure_time) > self.recovery_timeout


class RedisService(BaseCfgModule):
    """Redis service with automatic configuration and circuit breaker."""
    
    def __init__(self):
        super().__init__()
        self._client = None
        self._circuit_breaker = RedisCircuitBreaker()
    
    @property
    def client(self) -> Optional[redis.Redis]:
        """Get Redis client with lazy initialization."""
        if self._client is None:
            self._client = self._create_client()
        return self._client
    
    def _create_client(self) -> Optional[redis.Redis]:
        """Create Redis client from configuration."""
        try:
            config = self.get_config()
            if not config:
                logger.warning("No config available, Redis disabled")
                return None
            
            # Get Redis config from main config
            redis_config = getattr(config, 'cache', None)
            if not redis_config:
                logger.warning("No Redis config found, using default")
                redis_url = "redis://localhost:6379/0"
            else:
                redis_url = getattr(redis_config, 'redis_url', "redis://localhost:6379/0")
            
            return redis.Redis.from_url(redis_url, decode_responses=True)
            
        except Exception as e:
            logger.error(f"Failed to create Redis client: {e}")
            return None
    
    def get_cache(self, key: str) -> Any:
        """Get value from cache with circuit breaker."""
        def redis_get():
            if not self.client:
                raise redis.ConnectionError("Redis client not available")
            data = self.client.get(key)
            return json.loads(data) if data else None
        
        def fallback_get():
            # Fallback to Django cache (database)
            return cache.get(key)
        
        return self._circuit_breaker.call(redis_get, fallback_get)
    
    def set_cache(self, key: str, value: Any, ttl: int = 300) -> bool:
        """Set value in cache with circuit breaker."""
        def redis_set():
            if not self.client:
                raise redis.ConnectionError("Redis client not available")
            data = json.dumps(value) if value is not None else ""
            return self.client.setex(key, ttl, data)
        
        def fallback_set():
            # Fallback to Django cache (database)
            cache.set(key, value, ttl)
            return True
        
        return self._circuit_breaker.call(redis_set, fallback_set)
    
    def delete_cache(self, key: str) -> bool:
        """Delete key from cache."""
        def redis_delete():
            if not self.client:
                raise redis.ConnectionError("Redis client not available")
            return self.client.delete(key)
        
        def fallback_delete():
            cache.delete(key)
            return True
        
        return self._circuit_breaker.call(redis_delete, fallback_delete)
    
    def increment(self, key: str, amount: int = 1, ttl: Optional[int] = None) -> int:
        """Increment counter with circuit breaker."""
        def redis_incr():
            if not self.client:
                raise redis.ConnectionError("Redis client not available")
            result = self.client.incr(key, amount)
            if ttl:
                self.client.expire(key, ttl)
            return result
        
        def fallback_incr():
            # Simple fallback - just return amount (no persistence)
            logger.warning(f"Redis unavailable, counter increment for {key} not persisted")
            return amount
        
        return self._circuit_breaker.call(redis_incr, fallback_incr)
    
    def get_user_access_cache(self, user_id: int, endpoint_group: str) -> Optional[Dict]:
        """Get cached user access info."""
        key = f"access:{user_id}:{endpoint_group}"
        return self.get_cache(key)
    
    def set_user_access_cache(self, user_id: int, endpoint_group: str, access_info: Dict, ttl: int = 60) -> bool:
        """Set cached user access info."""
        key = f"access:{user_id}:{endpoint_group}"
        return self.set_cache(key, access_info, ttl)
    
    def track_usage(self, user_id: int, endpoint_group: str, response_time_ms: Optional[int] = None) -> None:
        """Track API usage with rate limiting."""
        # Increment request counter
        usage_key = f"usage:{user_id}:{endpoint_group}"
        self.increment(usage_key, ttl=3600)  # 1 hour window
        
        # Track response time if provided
        if response_time_ms:
            rt_key = f"response_time:{user_id}:{endpoint_group}"
            def redis_track_rt():
                if not self.client:
                    raise redis.ConnectionError("Redis client not available")
                self.client.lpush(rt_key, response_time_ms)
                self.client.ltrim(rt_key, 0, 99)  # Keep last 100
                self.client.expire(rt_key, 3600)
            
            def fallback_track_rt():
                pass  # Skip response time tracking in fallback
            
            self._circuit_breaker.call(redis_track_rt, fallback_track_rt)
    
    def check_rate_limit(self, user_id: int, endpoint_group: str, limit: int, window: int = 3600) -> Dict:
        """Check rate limit for user."""
        rate_key = f"rate:{user_id}:{endpoint_group}:{window}"
        
        def redis_check():
            if not self.client:
                raise redis.ConnectionError("Redis client not available")
            current = self.client.get(rate_key) or 0
            return {
                'allowed': int(current) < limit,
                'current': int(current),
                'limit': limit,
                'window': window
            }
        
        def fallback_check():
            # Fallback - always allow (no rate limiting)
            logger.warning(f"Redis unavailable, rate limiting disabled for user {user_id}")
            return {
                'allowed': True,
                'current': 0,
                'limit': limit,
                'window': window
            }
        
        return self._circuit_breaker.call(redis_check, fallback_check)
