from uuid import uuid4

from ..core.club import Club


class Fixture:

    def __init__(
        self,
        home_club: Club,
        away_club: Club,
    ) -> None:
        self.id = uuid4()
        self.home_club: Club = home_club
        self.away_club: Club = away_club
        self.result = None

    def __str__(self) -> str:
        return f"{self.home_club.name} : {self.away_club.name}"
