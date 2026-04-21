from uuid import uuid4

from ..core.fixture import Fixture
from ..core.club import Club


class Matchday:

    def __init__(
        self,
        competition,
        number,
    ) -> None:
        self.id = uuid4()
        self.competition = competition
        self.number: int = number
        self.fixtures: list = []

    def add_fixture(self, home_club: Club, away_club: Club) -> None:
        fixture = Fixture(
            home_club=home_club,
            away_club=away_club
        )
        self.fixtures.append(fixture)

    def __str__(self) -> str:
        output = f"\nMatchday {self.number}\n\n"
        for fixture in self.fixtures:
            output += f"{fixture}\n"
        return output
