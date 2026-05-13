package simulation.entities;

import simulation.attributes.*;

public class Referee extends Person {

    private int expertise; 
    private int strictness;

    public Referee(
        Nationality nationality,
        int birthYear,
        Gender gender,
        int expertise,
        int strictness
    ) {
        super(nationality, birthYear, gender);
        this.expertise = expertise;
        this.strictness = strictness;
    }
    
    public int getExpertise() {
        return expertise;
    }
    
    public int getStrictness() {
        return strictness;
    }

    @Override
    public String toString() {
        String result = super.toString();
        result += ", Expertise " + getExpertise() + 
            ", Strictness " + getStrictness();
        return result;
    }
    
}
