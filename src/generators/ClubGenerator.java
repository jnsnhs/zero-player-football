package generators;

import simulation.entities.Club;
import simulation.entities.Ground;
import simulation.entities.Manager;
import simulation.entities.Squad;

public class ClubGenerator {

    public static Club run(
        int year,
        String nameOfClub,
        int leagueLevel,
        double avgGoalsForClub,
        double avgGoalsAgainstClub,
        double avgGoalsInLeagueGame
    ) {
        double attackingBonus = getAttBonus(avgGoalsForClub, avgGoalsInLeagueGame);
        double defendingBonus = getDefBonus(avgGoalsAgainstClub, avgGoalsInLeagueGame);
        Ground ground = GroundGenerator.run(
            year,
            leagueLevel,
            attackingBonus,
            defendingBonus
        );
        Manager manager = ManagerGenerator.run(
            year,
            leagueLevel,
            attackingBonus,
            defendingBonus
        );
        Squad squad = SquadGenerator.run(
            year,
            leagueLevel,
            attackingBonus,
            defendingBonus
        );
        Club club = new Club(
            nameOfClub,
            ground,
            manager,
            squad
        );
        return club;
    }

    private static double getAttBonus(double avgGoalsForClub, double avgGoalsInLeagueGame) {
        return avgGoalsForClub / (avgGoalsInLeagueGame / 2) - 1;
    }

    private static double getDefBonus(double avgGoalsAgainstClub, double avgGoalsInLeagueGame) {
        return 1 - avgGoalsAgainstClub / (avgGoalsInLeagueGame / 2);
    }

}
