from dataclasses import dataclass
from datetime import datetime

@dataclass
class TokenBucket:
    capacity: int
    refill_rate: float  # tokens per second
    tokens: float
    last_refill: datetime

    def refill(self, now: datetime):
        elapsed = (now - self.last_refill).total_seconds()
        added = elapsed * self.refill_rate
        self.tokens = min(self.capacity, self.tokens + added)
        self.last_refill = now

    def allow(self, now: datetime, cost: int = 1) -> bool:
        self.refill(now)
        if self.tokens >= cost:
            self.tokens -= cost
            return True
        return False
