package generators;

import java.util.Arrays;
import java.util.Random;

import helpers.RndHelper;
import simulation.attributes.*;
import simulation.entities.*;

public abstract class PlayerGenerator {
    
    public static Player run(
        int currentYear,
        int leagueLevel,
        double attackingBonus,
        double defendingBonus,
        Position mainPosition
    ) {
        return new Player(
            randomNationality(currentYear, leagueLevel),
            currentYear - randomAge(),
            Gender.MALE,
            mainPosition,
            randomAltPositions(mainPosition),
            randomSkill(leagueLevel, mainPosition, attackingBonus, defendingBonus),
            randomMotivation(),
            randomFitness()
        );
    }

    /**
     * Based on Bundesliga data from 1965, 1995, and 20205. Lower ratio of
     * foreign players in lower leagues purely based on guessing.
     * @param currentYear
     * @param leagueLevel
     * @return random Nationality
     */
    private static Nationality randomNationality(int currentYear, int leagueLevel) {
        Nationality rndNationality;
        if (currentYear == 1965) {
            rndNationality = Nationality.DE;
        } else if (currentYear == 1995) {
            if (Math.random() < 1 - (1 - 0.74) / leagueLevel) {
                rndNationality = Nationality.DE;
            } else {
                Nationality[] nationalities = new Nationality[]{
                    Nationality.HR, Nationality.PL, Nationality.BR, Nationality.CZ,
                    Nationality.BG, Nationality.NL, Nationality.US, Nationality.SE,
                    Nationality.CH, Nationality.MK, Nationality.DK, Nationality.RU,
                    Nationality.NG, Nationality.TR, Nationality.AT
                };
                int[] weights = new int[] {2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 
                    1};
                rndNationality = nationalities[RndHelper.chooseIndex(weights)];
            }
        } else { // ccurrentYear == 2025
            if (Math.random() < 1 - (1 - 0.41) / leagueLevel) {
                rndNationality = Nationality.DE;
            } else {
                Nationality[] nationalities = new Nationality[]{
                    Nationality.AT, Nationality.FR, Nationality.DK, Nationality.JP,
                    Nationality.CH, Nationality.US, Nationality.NL, Nationality.PT,
                    Nationality.BE, Nationality.HR, Nationality.BR, Nationality.NG,
                    Nationality.TR, Nationality.NO, Nationality.PL, Nationality.CZ,
                    Nationality.SE, Nationality.GB_ENG, Nationality.DZ,
                    Nationality.ES, Nationality.AR, Nationality.XK, Nationality.RS,
                    Nationality.KR, Nationality.GH, Nationality.BA, Nationality.HU 
                };
                int[] weights = new int[] {6, 5, 3, 3, 3, 2, 2, 2, 2, 2, 2, 2, 1, 1, 
                    1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1};
                rndNationality = nationalities[RndHelper.chooseIndex(weights)];
            }
        }
        return rndNationality;
    }

    /**
     * Based on Bundesliga data from 1965, 1975, 1995 and 2025
     * @return random Age between 18 and 39
     */
    private static int randomAge() {
        int minPlayerAge = 18;
        double avgPlayerAge = 25.5;
        int maxPlayerAge = 39;
        return (int) RndHelper.triangularDistribution(
            minPlayerAge, maxPlayerAge, avgPlayerAge);
    }

    private static int randomMotivation() {
        int result = (int) new Random().nextGaussian(110, 5);
        return result <= 120 ? result : 120;
    }

    private static int randomFitness() {
        int result = (int) new Random().nextGaussian(10, 2);
        return result <= 20 ? result : 20;
    }

    private static Position[] randomAltPositions(Position mainPosition) {
        Position[] altPositions;
        boolean hasAltPosition = Math.random() < 0.5 ? true : false;
        if (!hasAltPosition || mainPosition == Position.GK) {
            altPositions = new Position[0];
        } else {
            Position[] defPositions = new Position[]{
                Position.SW, Position.LB, Position.CB, Position.RB
            };
            Position[] midPositions = new Position[]{
                Position.DM, Position.LM, Position.RM, Position.AM
            };
            Position[] attPositions = new Position[]{
                Position.LW, Position.CF, Position.RW
            };
            Position result = mainPosition;
            while (result == mainPosition) {
                if (Arrays.asList(defPositions).contains(mainPosition)) {
                    result = defPositions[RndHelper.chooseIndex(
                        new int[]{1, 1, 1, 1})];
                } else if (Arrays.asList(attPositions).contains(mainPosition)) {
                    result = attPositions[RndHelper.chooseIndex(
                        new int[]{1, 1, 1})];
                } else {
                    result = midPositions[RndHelper.chooseIndex(
                        new int[]{1, 1, 1, 1})];
                }
            }
            altPositions = new Position[]{result};
        }
        return altPositions;
    }

    public static int randomSkill(
        int leagueLevel,
        Position mainPosition,
        double attClubBonus,
        double defClubBonus
    ) {
        int maxClubSkill, avgClubSkill, minClubSkill;
        switch (leagueLevel) {
            case 1:
                maxClubSkill = 10;
                avgClubSkill = 9;
                minClubSkill = 8;
                break;
            case 2:
                maxClubSkill = 8;
                avgClubSkill = 7;
                minClubSkill = 6;
                break;
            case 3:
                maxClubSkill = 6;
                avgClubSkill = 5;
                minClubSkill = 4;
                break;
            case 4:
                maxClubSkill = 4;
                avgClubSkill = 3;
                minClubSkill = 2;
                break;
            default:
                maxClubSkill = 12;
                avgClubSkill = 6;
                minClubSkill = 1;
        }
        double expectedAttSkill = expectedAttackingSkill(
            attClubBonus, minClubSkill, avgClubSkill, maxClubSkill);
        double expectedDefSkill = expectedDefensiveSkill(
            defClubBonus, minClubSkill, avgClubSkill, maxClubSkill);
        double expectedSkill;
        if (hasDefensivePosition(mainPosition) || mainPosition == Position.GK) {
            expectedSkill = expectedDefSkill;
        } else if (hasAttackingPosition(mainPosition)) {
            expectedSkill = expectedAttSkill;
        } else {
            expectedSkill = (expectedDefSkill + expectedAttSkill) / 2;
        }
        int randomSkill = (int) Math.round(
            new Random().nextGaussian(expectedSkill, 1.0));
        randomSkill = randomSkill <= 12 ? randomSkill : 12;
        randomSkill = randomSkill >= 1 ? randomSkill : 1;
        return randomSkill;
    }

    private static double expectedAttackingSkill(
        double attClubBonus,
        int minClubSkill,
        int avgClubSkill,
        int maxClubSkill
    ) {
        double result = avgClubSkill;
        if (attClubBonus > 0) {
            result += (maxClubSkill - avgClubSkill) * attClubBonus / 0.5;
            result = result <= maxClubSkill ? result : maxClubSkill;
        }
        if (attClubBonus < 0) {
            result += (avgClubSkill - minClubSkill) * attClubBonus / 0.5;
            result = result >= minClubSkill ? result : minClubSkill;
        }
        return result;
    }

    private static double expectedDefensiveSkill(
        double defClubBonus,
        int minClubSkill,
        int avgClubSkill,
        int maxClubSkill
    ) {
        double result = avgClubSkill;
        if (defClubBonus > 0) {
            result += (maxClubSkill - avgClubSkill) * defClubBonus / 0.5;
            result = result <= maxClubSkill ? result : maxClubSkill;
        }
        if (defClubBonus < 0) {
            result += (avgClubSkill - minClubSkill) * defClubBonus / 0.5;
            result = result >= minClubSkill ? result : minClubSkill;
        }
        return result;
    }

    private static boolean hasDefensivePosition(Position mainPosition) {
        if (mainPosition == Position.SW || mainPosition == Position.CB ||
            mainPosition == Position.LB || mainPosition == Position.RB
        ) {
            return true;
        } else {
            return false;
        }
    }

    private static boolean hasAttackingPosition(Position mainPosition) {
        if (mainPosition == Position.LW || mainPosition == Position.RW ||
            mainPosition == Position.CF) {
            return true;
        } else {
            return false;
        }
    }

}
