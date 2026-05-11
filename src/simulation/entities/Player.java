package simulation.entities;

import simulation.attributes.*;

public class Player extends Person {

    private Position mainPosition;
    private Position[] altPositions;
    private int skill;
    private int motivation;
    private int fitness;
    
    public Player(
        Nationality nationality,
        int birthYear,
        Gender gender,
        Position mainPosition,
        Position[] altPositions,
        int skill,       // 1-12
        int motivation,  // 0-120
        int fitness      // 0-20
    ) {
        super(nationality, birthYear, gender);
        this.mainPosition = mainPosition;
        this.altPositions = altPositions;
        this.skill = skill;
        this.motivation = motivation;
        this.fitness = fitness;
    }

    public Position getMainPosition() {
        return mainPosition;
    }
    public Position[] getAltPositions() {
        return altPositions;
    }
    public int getSkill() {
        return skill;
    }
    public int getMotivation() {
        return motivation;
    }
    public int getFitness() {
        return fitness;
    }

    public double calcActualSkill() {
        double motivationalFactor;
        if (motivation > 110) {
            motivationalFactor = (double) (220 - motivation) / 100;
        } else {
            motivationalFactor = (double) motivation / 100;
        }
        double result = ((double) skill - 1 + (double) fitness / 10) * motivationalFactor;
        result = (double) Math.floor(result * 10) / 10;
        result = result < 14.0 ? result : 13.9;
        result = result > 0.0 ? result : 0.1;
        return result;
    }

    public String altPositionsToString() {
        String result = "";
        for (Position position : altPositions) {
            result += position != null ? position.toString() : " ";
        }
        return result;
    }

    @Override
    public String toString() {
        String result = "  ";
        result += getFullName() + ", " + getNationality() + ", ";
        result += "*" + getBirthDate().getYear() + ", ";
        result += mainPosition;
        result += altPositions.length > 0 ? " (" + altPositions[0] +")" : "";
        result += ", St: " + skill;
        return result;
    }

}
