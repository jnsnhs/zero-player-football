package generators;

import java.util.ArrayList;
import java.util.Random;

import helpers.RndHelper;
import simulation.attributes.*;
import simulation.entities.*;

public class SquadGenerator {

    public static Squad run(
        int currentYear,
        int leagueLevel,
        double attackingBonus,
        double defendingBonus
    ) {
        Squad squad = new Squad();
        int numberOfPlayers = getRandomNumberOfPlayers(currentYear);
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
    // TODO add current year as parameter
    private static int getRandomNumberOfPlayers(int currentYear) {
        return (int) Math.round(
            RndHelper.triangularDistribution(18, 24, 20));
    }

    private static ArrayList<Position> getRandomMainPositions(int numberOfPlayers) {
        ArrayList<Position> result = new ArrayList<>(30);
        int numberOfGk = Math.random() < 0.75 ? 2 : 3; // TODO
        for (int i = 0; i < numberOfGk; i++) {
            result.add(Position.GK);
        }
        Position[] defaultOutfieldPositions =
         {
            Position.SW, Position.LB, Position.CB, Position.CB, Position.RB,
            Position.DM, Position.AM, Position.LM, Position.RM,
            Position.LW, Position.CF, Position.CF, Position.RW
        };
        for (Position position : defaultOutfieldPositions) {
            result.add(position);
        }
        if (result.size() < numberOfPlayers) {
            Random rnd = new Random();
            while (result.size() < numberOfPlayers) {
                result.add(defaultOutfieldPositions[rnd.nextInt(
                    0, defaultOutfieldPositions.length)]);
            }
        }
        return result;
    }

}
