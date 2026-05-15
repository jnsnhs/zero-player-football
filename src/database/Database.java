package database;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.IOException;
import java.io.Serializable;
import java.util.ArrayList;

import generators.*;
import simulation.entities.*;

public class Database implements Serializable{

    private Calendar calendar;
    private Club[] clubs;
    private Referee[] referees;

    public Database() {}

    public void createContent(int startingYear) {
        setCalendar(startingYear, 7, 1);
        setClubs(startingYear);
        setReferees(startingYear);
    }

    private void setCalendar(int year, int month, int day) {
        this.calendar = new Calendar(year, month, day);
    }

    private void setClubs(int year) {
        String pathToFile = "res/clubs/clubs_de_" + year + ".csv";
        ArrayList<String> clubData = readRecordsFromCsv(pathToFile);
        clubData.removeFirst();
        Club[] clubs = new Club[clubData.size()];
        for (int i = 0; i < clubData.size(); i++) {
            String[] values = clubData.get(i).split(",");
            clubs[i] = ClubGenerator.run(
                year,
                values[0],                      // name of club
                (int) Integer.parseInt(values[5]),    // league level
                (double) Double.parseDouble(values[2]),  // avg goals for club
                (double) Double.parseDouble(values[3]),  // avg goals against club
                (double) Double.parseDouble(values[4])   // avg  goals per league game
            );
        }
        this.clubs = clubs;  
    }

    private void setReferees(int startingYear) {
        int numberOfReferees = (int) Math.round(clubs.length * 0.6);
        Referee[] referees = new Referee[numberOfReferees];
        for (int i = 0; i < numberOfReferees; i++) {
            referees[i] = RefereeGenerator.run(startingYear);
        }
        this.referees = referees;
    }

    public Calendar getCalendar() {
        return calendar;
    }

    public Club[] getClubs() {
        return clubs;
    }

    public Referee[] getReferees() {
        return referees;
    }

    private ArrayList<String> readRecordsFromCsv(String pathToFile) {
        File file = new File(pathToFile);
        ArrayList<String> records = new ArrayList<>();
        try (BufferedReader reader = new BufferedReader(new FileReader(file))) {
            String record = reader.readLine();
            while (record != null) {
                records.add(record);
                record = reader.readLine();
            }
        } catch (IOException exception) {
            IO.println(exception);
        }
        return records;
    }

}
