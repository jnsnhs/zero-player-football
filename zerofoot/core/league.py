
from random import shuffle
from uuid import uuid4

from ..core.club import Club, Region
from ..core.matchday import Matchday


class League():

    def __init__(
        self,
        name: str,
        level: int,
        regions: list[Region],
        clubs: list[Club]
    ) -> None:
        self.id = uuid4()
        self.name = name
        self.level: int = level
        self.regions: list[Region] = regions
        self.clubs: list[Club] = clubs
        self.matchdays: list[Matchday] = self.create_matchdays(clubs)
        self.days_played: int = 0

    def create_matchdays(self, clubs: list[Club]) -> list[Matchday]:
        """
        According to "Harmonischer Schlüsselplan":\n
        https://de.wikipedia.org/wiki/Spielplan_(Sport)\n
        Works only with a even number of clubs!
        """
        if len(clubs) % 2 != 0:
            raise Exception("Unable to create fixtures with an uneven"
                            "number of clubs!")
        pool = clubs.copy()
        shuffle(pool)
        a = list(range(1, len(pool) // 2))
        b = list(range(len(pool) - 1, len(pool) // 2, -1))
        c = len(pool) // 2
        x = len(pool)
        first_half_of_season: list[Matchday] = []
        second_half_of_season: list[Matchday] = []
        for i in range(1, len(pool)):
            matchday_first_half = Matchday("Liga", i)
            matchday_second_half = Matchday("Liga", i + len(pool) - 1)
            for j in range(0, len(pool) // 2 - 1):
                if (a[j] + b[j]) % 2 == 0:
                    if a[j] > b[j]:
                        matchday_first_half.add_fixture(
                            pool[a[j]-1], pool[b[j]-1])
                        matchday_second_half.add_fixture(
                            pool[b[j]-1], pool[a[j]-1])
                    else:
                        matchday_first_half.add_fixture(
                            pool[b[j]-1], pool[a[j]-1])
                        matchday_second_half.add_fixture(
                            pool[a[j]-1], pool[b[j]-1])
                else:
                    if b[j] < a[j]:
                        matchday_first_half.add_fixture(
                            pool[b[j]-1], pool[a[j]-1])
                        matchday_second_half.add_fixture(
                            pool[a[j]-1], pool[b[j]-1])
                    else:
                        matchday_first_half.add_fixture(
                            pool[a[j]-1], pool[b[j]-1])
                        matchday_second_half.add_fixture(
                            pool[b[j]-1], pool[a[j]-1])
            if c <= len(pool) / 2 - 1 and c <= len(pool) - 2:
                matchday_first_half.add_fixture(pool[c-1], pool[x-1])
                matchday_second_half.add_fixture(pool[x-1], pool[c-1])
            else:
                matchday_second_half.add_fixture(pool[x-1], pool[c-1])
                matchday_first_half.add_fixture(pool[c-1], pool[x-1])
            first_half_of_season.append(matchday_first_half)
            second_half_of_season.append(matchday_second_half)
            if i % 2 != 0:
                a.append(c)
                c = a.pop(0)
            else:
                b.insert(0, c)
                c = b.pop()
        return first_half_of_season + second_half_of_season

    def __str__(self) -> str:
        lines = f"{self.name}\n\n"
        for club in self.clubs:
            lines += f"{club.name}\n"
        lines += f"{self.matchdays[self.days_played]}"
        return lines
