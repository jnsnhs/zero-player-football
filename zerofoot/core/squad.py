from random import choices, random, triangular

from ..core.player import Player, Position


class Squad:

    def __init__(
        self,
        current_year: int,
        avg_gf: float,
        avg_ga: float,
        league_level: int
    ) -> None:
        self.players: list[Player] = self.autofill_squad(
            year=current_year,
            league_lvl=league_level,
            avg_gf=avg_gf,
            avg_ga=avg_ga
        )

    def add_player(self, player: Player):
        self.players.append(player)

    def get_squad_size(self) -> int:
        return round(triangular(18, 24, 20))

    def get_rnd_positions(self, desired_team_size: int = 20) -> list:
        """Returns a list of semi-randomly picked positions
        based on the desired size of a team."""
        number_of_gk = 2 if random() <= 0.75 else 3
        DEFAULT_OUTFIELD_POSITIONS = [
            Position.SW, Position.LB, Position.CB, Position.CB, Position.RB,
            Position.DM, Position.AM, Position.LM, Position.RM,
            Position.LW, Position.CF, Position.CF, Position.RW]
        result = [Position.GK] * number_of_gk + DEFAULT_OUTFIELD_POSITIONS
        if len(result) < desired_team_size - number_of_gk:
            additional_players = desired_team_size + number_of_gk - len(result)
            result += choices(DEFAULT_OUTFIELD_POSITIONS, k=additional_players)
        result.sort(key=lambda position: position.value)
        return result

    def autofill_squad(self, year, league_lvl, avg_gf, avg_ga) -> list[Player]:
        squad = []
        size = self.get_squad_size()
        positions = self.get_rnd_positions(size)
        for position in positions:
            squad.append(Player(
                current_year=year,
                league_level=league_lvl,
                avg_gf=avg_gf,
                avg_ga=avg_ga,
                position=position
            ))
        return squad

    def __str__(self) -> str:
        lines = ""
        for player in self.players:
            lines += f"{player}\n"
        return lines
