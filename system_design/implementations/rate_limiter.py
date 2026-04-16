"""Reference rate limiting implementations for interview study and practice."""

from __future__ import annotations

from collections import defaultdict, deque
from typing import Callable


class FixedWindowRateLimiter:
    """Allows a fixed number of requests per key in each discrete time window.

    Interview model:
    - easiest implementation
    - cheapest bookkeeping
    - has boundary burstiness because two adjacent windows can both be used
    """

    def __init__(
        self,
        limit: int,
        window_seconds: float,
        time_func: Callable[[], float],
    ) -> None:
        self.limit = limit
        self.window_seconds = window_seconds
        self.time_func = time_func
        self._counters: dict[str, tuple[int, int]] = {}

    def allow(self, key: str) -> bool:
        current_time = self.time_func()
        window_start = int(current_time // self.window_seconds)
        count, stored_window = self._counters.get(key, (0, window_start))

        # If time moved into a new window, the old count no longer matters.
        if stored_window != window_start:
            count = 0
            stored_window = window_start

        if count >= self.limit:
            self._counters[key] = (count, stored_window)
            return False

        self._counters[key] = (count + 1, stored_window)
        return True


class SlidingWindowLogRateLimiter:
    """Keeps exact timestamps for recent requests to avoid fixed-window bursts.

    Interview model:
    - more precise than fixed window
    - more memory because each recent request timestamp is stored
    """

    def __init__(
        self,
        limit: int,
        window_seconds: float,
        time_func: Callable[[], float],
    ) -> None:
        self.limit = limit
        self.window_seconds = window_seconds
        self.time_func = time_func
        self._requests: dict[str, deque[float]] = defaultdict(deque)

    def allow(self, key: str) -> bool:
        current_time = self.time_func()
        cutoff = current_time - self.window_seconds
        requests = self._requests[key]

        # Drop timestamps that are outside the active sliding window.
        while requests and requests[0] <= cutoff:
            requests.popleft()

        if len(requests) >= self.limit:
            return False

        requests.append(current_time)
        return True


class TokenBucketRateLimiter:
    """Smooths traffic by refilling tokens over time up to a fixed capacity.

    Interview model:
    - supports short bursts up to bucket capacity
    - average rate is controlled by refill rate
    - common production choice for APIs
    """

    def __init__(
        self,
        refill_rate_per_second: float,
        capacity: float,
        time_func: Callable[[], float],
    ) -> None:
        self.refill_rate_per_second = refill_rate_per_second
        self.capacity = capacity
        self.time_func = time_func
        self._buckets: dict[str, tuple[float, float]] = {}

    def allow(self, key: str, cost: float = 1.0) -> bool:
        current_time = self.time_func()
        tokens, last_refill_time = self._buckets.get(
            key, (self.capacity, current_time)
        )

        elapsed_seconds = current_time - last_refill_time
        refilled_tokens = elapsed_seconds * self.refill_rate_per_second
        tokens = min(self.capacity, tokens + refilled_tokens)

        if tokens < cost:
            self._buckets[key] = (tokens, current_time)
            return False

        self._buckets[key] = (tokens - cost, current_time)
        return True
