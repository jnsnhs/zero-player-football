package generators;

import helpers.RndHelper;
import simulation.entities.Ground;

public class GroundGenerator {

    public static Ground run(
        int year,
        int leagueLevel,
        double attackingBonus,
        double defendingBonus
    ) {
        return new Ground(
            randomName(), 
            randomCapacity(leagueLevel, attackingBonus, defendingBonus)
        );
    }

    private static String randomName() {
        return "Stadion ohne Namen"; // TODO implement random name generator
    }

    private static int randomCapacity(
        int leagueLevel, double attackingBonus, double defendingBonus
    ) {
        int maxCapacity, avgCapacity, minCapacity;
        if (leagueLevel == 1) {
            maxCapacity = 80_000;
            avgCapacity = 40_000;
            minCapacity = 20_000;
        } else if (leagueLevel == 2) {
            maxCapacity = 60_000;
            avgCapacity = 30_000;
            minCapacity = 15_000;
        } else if (leagueLevel == 3 ) {
            maxCapacity = 40_000;
            avgCapacity = 20_000;
            minCapacity = 10_000;
        } else {
            maxCapacity = 25_000;
            avgCapacity = 10_000;
            minCapacity = 2_500;
        }

        double performanceFactor = 1 + (attackingBonus + defendingBonus) / 2;
        avgCapacity *= performanceFactor;
        int rndCapacity =  (int) RndHelper.triangularDistribution(
            minCapacity, maxCapacity, avgCapacity);
        rndCapacity = rndCapacity >= minCapacity ? rndCapacity : minCapacity;
        rndCapacity = rndCapacity <= maxCapacity ? rndCapacity : maxCapacity;
        return rndCapacity;
    }

}
