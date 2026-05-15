package simulation.entities;

import simulation.attributes.*;
import helpers.FileHelper;

import java.io.File;
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
        this.nationality = nationality;
        birthDate = randomBirthDate(birthYear);
        this.gender = gender;
        lastName = randomlastName(nationality);
        firstName = randomfirstName(nationality, birthYear, gender);
        intelligence = randomIntelligence();
        personality = randomPersonality();
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
    
    public String getAbbNameReversed() {
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

    private HashMap<Trait, Integer> randomPersonality() {
        HashMap<Trait, Integer> personality = new HashMap<>();
        Random r = new Random();
        for (Trait trait : Trait.values()) {
            personality.put(trait, r.nextInt(1, 11));
        }
        return personality;
    }

    private String randomlastName(Nationality nationality) {
        String fileName = "last_names_" + nationality.toString().toLowerCase() +
             ".txt";
        String path = "res/last_names/" + fileName;
        String randomLastName;
        try {
            ArrayList<String> names = FileHelper.readLinesFromFile(path);
            randomLastName = names.get(new Random().nextInt(
                0, names.size()));
        } catch (Exception e) {
            IO.println("Nachname konnte nicht zugewiesen werden (" + fileName + 
                ").");
            randomLastName = "N/A";
        }
        return randomLastName;
    }

    private String randomfirstName(
        Nationality nationality, int birthYear, Gender gender
    ) {
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
            ArrayList<String> names = FileHelper.readLinesFromFile(path);
            randomFirstName = names.get(
                new Random().nextInt(0, names.size()));
        } catch (Exception e) {
            IO.println("Vorname konnte nicht zugewiesen werden (" + fileName + 
                ").");
            randomFirstName = "N/A";
        }
        return randomFirstName;
    }

}
