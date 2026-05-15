package generators;

import java.util.Random;

import helpers.RndHelper;
import simulation.attributes.Gender;
import simulation.attributes.Nationality;
import simulation.entities.Manager;

public abstract class ManagerGenerator {

    public static Manager run(
        int currentYear,
        int leagueLevel,
        double attClubBonus,
        double defClubBonus
    ) {
        return new Manager(
            randomNationality(currentYear, leagueLevel),
            currentYear - randomAge(),
            Gender.MALE,
            randomExpertise(leagueLevel, attClubBonus, defClubBonus)
        );
    }

    private static Nationality randomNationality(
        int currentYear,
        int leagueLevel
    ) {
        Nationality nationality;
        double domesticRatio = switch(currentYear) {
            case 2025 -> 0.6;
            case 1995 -> 0.8;
            default   -> 1.0;  // 1965
        };
        if (Math.random() < 1 - (1 - domesticRatio) / leagueLevel) {
            nationality = Nationality.DE;
        } else {
            Nationality[] nationalities = new Nationality[]{
                Nationality.AT, Nationality.HR, Nationality.DK, Nationality.CH,
                Nationality.PL, Nationality.BE, Nationality.ES
            };
            nationality = nationalities[RndHelper.chooseIndex(
                nationalities.length)];
        }
        return nationality;
    }

    private static int randomAge() {
        double meanManagerAgeEndOfYear = 44.7;
        double stdevManagerAgeEndOfYear = 6.4;
        int randomManagerAge = (int) Math.round(new Random().nextGaussian(
            meanManagerAgeEndOfYear, stdevManagerAgeEndOfYear));
        return randomManagerAge >= 18 ? randomManagerAge : 18;
    }

    /**
     * Expertise is supposed to be the general skill level of a manager. 
     * Values range from 1 to 12. For the sake of simplicity and in order 
     * to get a few more extreme values expertise is modeled as being 
     * equally distributed instead of normally.
     * @param leagueLevel 
     */
    private static int randomExpertise(
        int leagueLevel,
        double attackingBonus,
        double defendingBonus
    ) {
        double totalBonus = 1 + (attackingBonus + defendingBonus) / 2;
        int maxExpertise, avgExpertise, minExpertise;
        switch (leagueLevel) {
            case 1:
                maxExpertise = 12;
                avgExpertise = 8;
                minExpertise = 7;
                break;
            case 2:
                maxExpertise = 7;
                avgExpertise = 6;
                minExpertise = 5;
                break;
            case 3:
                maxExpertise = 5;
                avgExpertise = 4;
                minExpertise = 3;
                break;
            case 4:
                maxExpertise = 3;
                avgExpertise = 2;
                minExpertise = 1;
                break;
            default:
                maxExpertise = 12;
                avgExpertise = 6;
                minExpertise = 1;
        }
        int expertise = (int) Math.round(avgExpertise * totalBonus);
        expertise = expertise <= maxExpertise ? expertise : maxExpertise;
        expertise = expertise >= minExpertise ? expertise : minExpertise;
        return expertise;
    }
    
}
