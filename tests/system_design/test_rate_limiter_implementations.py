import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from system_design.implementations.rate_limiter import (
    FixedWindowRateLimiter,
    SlidingWindowLogRateLimiter,
    TokenBucketRateLimiter,
)


class FakeClock:
    def __init__(self, start: float = 0.0) -> None:
        self.now = start

    def __call__(self) -> float:
        return self.now

    def advance(self, seconds: float) -> None:
        self.now += seconds


def test_fixed_window_resets_between_windows() -> None:
    clock = FakeClock()
    limiter = FixedWindowRateLimiter(limit=2, window_seconds=10, time_func=clock)

    assert limiter.allow("user-1") is True
    assert limiter.allow("user-1") is True
    assert limiter.allow("user-1") is False

    clock.advance(10)

    assert limiter.allow("user-1") is True


def test_sliding_window_log_expires_old_requests() -> None:
    clock = FakeClock()
    limiter = SlidingWindowLogRateLimiter(limit=2, window_seconds=10, time_func=clock)

    assert limiter.allow("user-1") is True
    clock.advance(4)
    assert limiter.allow("user-1") is True
    assert limiter.allow("user-1") is False

    clock.advance(7)

    assert limiter.allow("user-1") is True


def test_token_bucket_refills_over_time() -> None:
    clock = FakeClock()
    limiter = TokenBucketRateLimiter(
        refill_rate_per_second=2.0, capacity=3.0, time_func=clock
    )

    assert limiter.allow("tenant-a") is True
    assert limiter.allow("tenant-a") is True
    assert limiter.allow("tenant-a") is True
    assert limiter.allow("tenant-a") is False

    clock.advance(0.5)
    assert limiter.allow("tenant-a") is True
    assert limiter.allow("tenant-a") is False

    clock.advance(1.0)
    assert limiter.allow("tenant-a", cost=2.0) is True
