import threading
import time
from datetime import timedelta
from typing import Optional

from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone

User = get_user_model()


class CacheEntry(models.Model):
    """Model to track cache entries for analytics and management"""

    class CacheType(models.TextChoices):
        TIME = "time", "Time-based Cache"
        CRON = "cron", "Cron-based Cache"
        UNKNOWN = "unknown", "Unknown Cache"

    # Thread-local storage for per-thread time caching
    _thread_local = threading.local()

    cache_key = models.CharField(max_length=255, db_index=True)
    original_params = models.TextField(blank=True, null=True)
    function_name = models.CharField(max_length=255, db_index=True)
    cache_backend = models.CharField(max_length=100, default="default")
    cache_type = models.CharField(
        max_length=50,
        choices=CacheType.choices,
        default=CacheType.UNKNOWN,
        db_index=True,
        help_text="Type of cache entry based on the decorator used",
    )

    created_at = models.DateTimeField(auto_now_add=True)
    last_accessed = models.DateTimeField(auto_now=True)
    access_count = models.PositiveIntegerField(default=0)
    hit_count = models.PositiveIntegerField(default=0)
    miss_count = models.PositiveIntegerField(default=0)

    timeout = models.PositiveIntegerField(help_text="Cache timeout in seconds")
    expires_at = models.DateTimeField(
        null=True, blank=True, db_index=True, help_text="When this cache entry expires and should be considered invalid"
    )

    @classmethod
    def _get_cached_current_time(cls):
        """Get cached current time to avoid multiple timezone.now() calls"""
        now = time.time()
        if (
            not hasattr(cls._thread_local, "current_time_cache")
            or now - cls._thread_local.current_time_cache_timestamp > 1
        ):
            cls._thread_local.current_time_cache = timezone.now()
            cls._thread_local.current_time_cache_timestamp = now
        return cls._thread_local.current_time_cache

    class Meta:
        verbose_name = "Cache Entry"
        verbose_name_plural = "Cache Entries"
        indexes = [
            models.Index(fields=["function_name", "created_at"]),
            models.Index(fields=["cache_key", "last_accessed"]),
            models.Index(fields=["expires_at"]),
            models.Index(fields=["hit_count", "miss_count"]),
            models.Index(fields=["cache_backend", "created_at"]),
            models.Index(fields=["last_accessed"]),
            models.Index(fields=["cache_type", "created_at"]),
        ]

    def __str__(self):
        return f"{self.get_cache_type_display()}: {self.function_name} ({self.cache_key[:30]}...)"

    @property
    def type(self):
        """Property to access cache type for cleaner API"""
        return self.cache_type

    @type.setter
    def type(self, value):
        """Allow setting cache type through the type property"""
        valid_types = list(self.CacheType.values)
        if value not in valid_types:
            raise ValueError(f"Invalid cache type: {value}. Valid types are: {valid_types}")
        self.cache_type = value

    @property
    def hit_rate(self):
        """Calculate hit rate percentage"""
        total = self.hit_count + self.miss_count
        return (self.hit_count / total * 100) if total > 0 else 0

    @property
    def is_expired(self) -> bool:
        if not self.expires_at:
            return False
        return self.expires_at < self._get_cached_current_time()

    @property
    def time_left(self) -> timedelta:
        """Time remaining until cache expires"""
        if not self.expires_at:
            return timedelta(0)

        current_time = self._get_cached_current_time()
        if self.expires_at > current_time:
            return self.expires_at - current_time
        return timedelta(0)

    @property
    def time_left_seconds(self) -> float:
        """Cached property for time left in seconds"""
        return self.time_left.total_seconds()

    @classmethod
    def get_by_type(cls, cache_type):
        """Get all cache entries of a specific type"""
        return cls.objects.filter(cache_type=cache_type)

    @classmethod
    def get_statistics_by_type(cls):
        """Get statistics grouped by cache type"""
        from django.db.models import Count, Avg, Sum

        return (
            cls.objects.values("cache_type")
            .annotate(
                count=Count("id"),
                avg_hits=Avg("hit_count"),
                avg_misses=Avg("miss_count"),
                total_hits=Sum("hit_count"),
                total_misses=Sum("miss_count"),
            )
            .order_by("cache_type")
        )


class CacheEventHistory(models.Model):
    """Store cache-related events for analytics"""

    class EventType(models.TextChoices):
        HIT = "hit", "Hit"
        MISS = "miss", "Miss"
        ERROR = "error", "Error"

    event_name = models.CharField(max_length=200, db_index=True)
    event_type = models.CharField(max_length=50, choices=EventType.choices)

    cache_backend = models.CharField(max_length=100, default="default")
    function_name = models.CharField(max_length=200, db_index=True)
    cache_key = models.CharField(max_length=220)

    occurred_at = models.DateTimeField(auto_now_add=True, db_index=True)
    duration_ms = models.PositiveIntegerField(null=True, blank=True)
    original_params = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = "Cache Event"
        verbose_name_plural = "Cache Events"
        ordering = ["-occurred_at"]
        indexes = [
            models.Index(fields=["event_name", "occurred_at"]),
            models.Index(fields=["function_name", "event_type", "occurred_at"]),
        ]
