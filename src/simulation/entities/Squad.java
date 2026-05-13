package simulation.entities;

import java.io.Serializable;
import java.util.ArrayList;

public class Squad implements Serializable{
    
    private ArrayList<Player> players;

    public Squad() {
        players = new ArrayList<Player>();
    }

    public void addPlayer(Player player) {
        players.add(player);
    }
    
    public void removePlayer(Player player) {
        players.remove(player);
    }

    public ArrayList<Player> getPlayers() {
        return players;
    }
    
    public int getSize() {
        return players.size();
    }

    @Override
    public String toString() {
        String result = "";
        for (Player player : players) {
            result += player + "\n";
        }
        return result;
    }
}
