package simulation.entities;

import simulation.attributes.*;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.IOException;
import java.io.Serializable;
import java.time.LocalDate;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.Random;

public abstract class Person implements Serializable {
    
    protected Nationality nationality;
    protected LocalDate birthDate;
    private Gender gender;
    protected String lastName;
    protected String firstName;
    private int intelligence;
    private HashMap<Trait, Integer> personality;

    Person(
        Nationality nationality,
        int birthYear,
        Gender gender
    ) {
        setNationality(nationality);
        setBirthDate(randomBirthDate(birthYear));
        setGender(gender);
        setLastName(randomlastName(nationality));
        setFirstName(randomfirstName(nationality, birthYear, gender));

        setIntelligence(randomIntelligence());
        setPersonality(randomPersonality());
    }

    protected void setNationality(Nationality nationality) {
        this.nationality = nationality;
    }

    protected void setBirthDate(LocalDate birthDate) {
        this.birthDate = birthDate;
    }

    private void setGender(Gender gender) {
        this.gender = gender;
    }

    protected void setFirstName(String firstName) {
        this.firstName = firstName;
    }

    protected void setLastName(String lastName) {
        this.lastName = lastName;
    }

    private void setIntelligence(int intelligence) {
        this.intelligence = intelligence;
    }

    public void setPersonality(HashMap<Trait, Integer> personality) {
        this.personality = personality;
    }

    public String getFirstName() {
        return firstName;
    }
    public String getLastName() {
        return lastName;
    }
    public String getFullName() {
        return firstName + " " + lastName;
    }
    public String getAbbName() {
        return firstName.charAt(0) + ". " + lastName;
    }
    public String getAbbNameRev() {
        return lastName + ", " + firstName.charAt(0) + ".";
    }
    public LocalDate getBirthDate() {
        return birthDate;
    }
    public int getAge(LocalDate today) {
        int age = today.getYear() - birthDate.getYear();
        return today.getDayOfYear() < birthDate.getDayOfYear() ? age-- : age;
    }
    public Nationality getNationality() {
        return nationality;
    }
    public Gender getGender() {
        return gender;
    }
    public int getIntelligence() {
        return intelligence;
    }
    public HashMap<Trait, Integer> getPersonality() {
        return personality;
    }

    private LocalDate randomBirthDate(int birthYear) {
        boolean isLeapYear = LocalDate.ofYearDay(
            birthYear, 1).isLeapYear();
        int numberOfDays = isLeapYear ? 366 : 365;
        int dayOfYear = (int) Math.random() * numberOfDays + 1;
        return LocalDate.ofYearDay(birthYear, dayOfYear);
    }

    private int randomIntelligence() {
        return  (int) new Random().nextGaussian(100, 15);
    }

    /**
     * Based on the Big Five Personality Traits Model:
     * https://en.wikipedia.org/wiki/Big_Five_personality_traits
     */
    private HashMap<Trait, Integer> randomPersonality() {
        HashMap<Trait, Integer> personality = new HashMap<>();
        Random r = new Random();
        for (Trait trait : Trait.values()) {
            personality.put(trait, r.nextInt(1, 11));
        }
        return personality;
    }

    static String randomlastName(Nationality nationality) {
        String fileName = "last_names_" + 
            nationality.toString().toLowerCase() + ".txt";
        String path = "res/last_names/" + fileName;
        try {
            ArrayList<String> names = readLinesFromFile(path);
            return names.get(new Random().nextInt(0, names.size()));
        } catch (Exception e) {
            IO.println("Nachname konnte nicht zugewiesen werden (" + fileName + ").");
            return "N/A";
        }
    }

    static String randomfirstName(Nationality nationality, int birthYear, Gender gender) {
        int decade = Math.floorDiv(birthYear, 10) * 10;
        String fileName = "first_names_" + nationality.toString().toLowerCase() 
            + "_" + (gender == Gender.MALE ? "m" : "f") + "_" + decade + ".txt";
        String path = "res/first_names/" + fileName;
        if (!new File(path).exists()) {
            fileName = "first_names_" + nationality.toString().toLowerCase() 
            + "_" + (gender == Gender.MALE ? "m" : "f") + ".txt";
            path = "res/first_names/" + fileName;
        }
        String randomFirstName;
        try {
            ArrayList<String> names = readLinesFromFile(path);
            randomFirstName = names.get(
                new Random().nextInt(0, names.size()));
        } catch (Exception e) {
            IO.println("Vorname konnte nicht zugewiesen werden (" + fileName + ").");
            return "N/A";
        }
        return randomFirstName;
    }

    public static ArrayList<String> readLinesFromFile(String pathToFile) {
        File file = new File(pathToFile);
        ArrayList<String> lines = new ArrayList<String>();
        try (BufferedReader reader = new BufferedReader(new FileReader(file))) {
            String line = reader.readLine();
            while (line != null) {
                lines.add(line);
                line = reader.readLine();
            }
        } catch (IOException e) {
            IO.println(e);
        }
        return lines;
    }

}
