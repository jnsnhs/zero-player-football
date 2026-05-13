package simulation.entities;

import simulation.attributes.*;

public class Manager extends Person {
    
    private int expertise;

    public Manager(
        Nationality nationality,
        int birthyear,
        Gender gender,
        int expertise
    ) {
        super(nationality, birthyear, gender);
        this.expertise = expertise;
    }

    public int getExpertise() {
        return expertise;
    }

    @Override
    public String toString() {
        String result = getFullName() + " (*" + getBirthDate().getYear() + "), ";
        result += "Expertise " + getExpertise();
        return result;
    }

}
