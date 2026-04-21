from uuid import uuid4

from ..core.club import Club


class Cup():

    def __init__(
        self,
        name: str,
        clubs: list[Club]
    ) -> None:
        self.id = uuid4()
        self.name = name
        self.clubs = clubs

    def __str__(self) -> str:
        lines = f"{self.name}:\n\n"
        for club in self.clubs:
            lines += f"{club.name}\n"
        return lines
