package simulation.entities;

import java.io.Serializable;

public class Club implements Serializable {
    
    private String name;
    private Ground ground;
    private Manager manager;
    private Squad squad;

    public Club(
        String name,
        Ground ground,
        Manager manager,
        Squad squad
    ) {
        this.name = name;
        this.ground = ground;
        this.manager = manager;
        this.squad = squad;
    }

    public String getName() {
        return name;
    }

    public Ground getGround() {
        return ground;
    }

    public Manager getManager() {
        return manager;
    }

    public Squad getSquad() {
        return squad;
    }

    @Override
    public String toString() {
        String result = "";
        result += name.toUpperCase() + "\n\n";
        result += "Spielstätte: \n  " + ground + "\n";
        result += "Trainer: \n  " + manager + "\n";
        result += "Kader (" + squad.getSize() + " Spieler): \n" + squad;
        return result;
    }

}
