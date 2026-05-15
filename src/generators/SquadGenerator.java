package generators;

import java.util.ArrayList;
import java.util.Random;

import helpers.RndHelper;
import simulation.attributes.*;
import simulation.entities.*;

public abstract class SquadGenerator {

    public static Squad run(
        int currentYear,
        int leagueLevel,
        double attackingBonus,
        double defendingBonus
    ) {
        Squad squad = new Squad();
        int numberOfPlayers = getRandomNumberOfPlayers();
        for (Position mainPosition : getRandomMainPositions(numberOfPlayers)) {
            Player player = PlayerGenerator.run(
                currentYear,
                leagueLevel,
                attackingBonus,
                defendingBonus,
                mainPosition
            );
            squad.addPlayer(player);
        }
        return squad;
    }

    // Current values based on Bundesliga data from 1995.
    // TODO add current year and leagueLevel as parameters
    private static int getRandomNumberOfPlayers() {
        return (int) Math.round(RndHelper.triangularDistribution(
                20, 31, 24.2));
    }

    private static ArrayList<Position> getRandomMainPositions(
            int numberOfPlayers) {
        ArrayList<Position> positions = new ArrayList<>(30);
        int numberOfGk = Math.random() < 0.75 ? 2 : 3;
        for (int i = 0; i < numberOfGk; i++) {
            positions.add(Position.GK);
        }
        Position[] defaultOutfieldPositions =
         {
            Position.SW, Position.LB, Position.CB, Position.CB, Position.RB,
            Position.DM, Position.AM, Position.LM, Position.RM,
            Position.LW, Position.CF, Position.CF, Position.RW
        };
        for (Position position : defaultOutfieldPositions) {
            positions.add(position);
        }
        if (positions.size() < numberOfPlayers) {
            Random rnd = new Random();
            while (positions.size() < numberOfPlayers) {
                positions.add(defaultOutfieldPositions[rnd.nextInt(
                    0, defaultOutfieldPositions.length)]);
            }
        }
        return positions;
    }

}
