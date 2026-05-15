package simulation.entities;

import java.io.Serializable;

public class Ground implements Serializable {

    private String name;
    private int capacity;

    public Ground(String name, int capacity) {
        this.name = name;
        this.capacity = capacity;
    }

    public String getName() {
        return name;
    }
    public int getCapacity() {
        return capacity;
    }

    @Override
    public String toString() {
        return name + ", " + capacity + " Plätze";
    }

}

