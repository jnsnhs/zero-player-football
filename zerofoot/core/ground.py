from uuid import uuid4
from random import triangular


class Ground:

    def __init__(
        self,
        name: str,
        current_year: int,
        league_level: int,
        capacity: int = 0
    ) -> None:
        self.id = uuid4()
        self.name = name
        self.capacity = capacity if capacity else \
            self.set_capacity(league_level)

    def set_capacity(self, league_level: int) -> int:
        match league_level:
            case 1:
                MIN_CAPACITY = 35_000
                MEAN_CAPACITY = 52_000
                MAX_CAPACITY = 94_000
            case 2:
                MIN_CAPACITY = 1_000
                MEAN_CAPACITY = 5_000
                MAX_CAPACITY = 17_000
            case _:
                pass
        capacity = triangular(MIN_CAPACITY, MAX_CAPACITY, MEAN_CAPACITY)
        return int(capacity * 100 // 100)

    def __str__(self) -> str:
        return f"{self.name}, {self.capacity} Plätze"
