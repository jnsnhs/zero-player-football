from uuid import uuid4

from ..core.manager import Manager
from ..core.squad import Squad
from ..core.ground import Ground


# class Region(Enum):
#     N = "Nord"
#     W = "West"
#     SW = "Südwest"
#     S = "Süd"
#     NE = "Nordost"


class Club:

    def __init__(
        self,
        current_year: int,
        name: str,
        avg_gf: float,
        avg_ga: float,
        league_level: int,
        qualified_for_cup: bool,
        region: str
    ) -> None:
        self.id = uuid4()
        self.name: str = name
        self.league_level: int = league_level
        self.qualified_for_cup: bool = qualified_for_cup
        self.region: str = self.set_region(region)
        self.manager: Manager = Manager(
            current_year=current_year,
            league_level=league_level,
            avg_gf=avg_gf,
            avg_ga=avg_ga
        )
        self.squad: Squad = Squad(
            current_year=current_year,
            league_level=league_level,
            avg_gf=avg_gf,
            avg_ga=avg_ga
        )
        self.ground: Ground = Ground(
            current_year=current_year,
            name="Stadion an der Hauptstraße",
            league_level=league_level
        )

    def set_region(self, region: str) -> str:
        match region:
            case "north":
                return "n"
            case "northeast":
                return "ne"
            case "south":
                return "s"
            case "southwest":
                return "sw"
            case _:
                return "w"

    def __str__(self) -> str:
        lines = ""
        # lines += f"{self.name}\n"
        # lines += f"League Level: {self.league_level}\n"
        lines += f"Trainer:\n\n{self.manager}\n"
        lines += f"\nSpielstätte:\n\n{self.ground}\n"
        lines += f"\nMannschaft:\n\n{self.squad}"
        return lines
