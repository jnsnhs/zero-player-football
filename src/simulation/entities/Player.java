package simulation.entities;

import simulation.attributes.*;

public class Player extends Person {

    private Position mainPosition;
    private Position[] altPositions;
    private int skill;
    
    public Player(
        Nationality nationality,
        int birthYear,
        Gender gender,
        Position mainPosition,
        Position[] altPositions,
        int skill
    ) {
        super(nationality, birthYear, gender);
        setMainPosition(mainPosition);
        setAltPositions(altPositions);
        setSkill(skill);
    }

    private void setMainPosition(Position mainPosition) {
        this.mainPosition = mainPosition;
    }
    public void setAltPositions(Position[] altPositions) {
        this.altPositions = altPositions;
    }
    public void setSkill(int skill) {
        this.skill = skill;
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
