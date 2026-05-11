package generators;

import java.util.Random;

import simulation.attributes.Gender;
import simulation.attributes.Nationality;
import simulation.entities.Referee;

public class RefereeGenerator {

    public static Referee run(int currentYear) {
        return new Referee(
            randomNationality(),
            currentYear - randomAge(),
            Gender.MALE,
            randomExpertise(),
            randomStrictness()
        );
    }

    private static Nationality randomNationality() {
        return Nationality.DE;
    }

    private static int randomAge() {
        double meanRefereeAgeEndOfYear = 38.2;
        double stdevRefereeAgeEndOfYear = 4.5;
        int randomRefereeAge = (int) Math.round(new Random().nextGaussian(
            meanRefereeAgeEndOfYear, stdevRefereeAgeEndOfYear));
        return randomRefereeAge >= 18 ? randomRefereeAge : 18;
    }

    private static int randomExpertise() {
        return new Random().nextInt(1, 13);
    }

    private static int randomStrictness() {
        return new Random().nextInt(1, 13);
    }

}
