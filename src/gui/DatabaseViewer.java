package gui;

import javax.swing.*;
import java.awt.*;
import java.io.File;
import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.ObjectInputStream;
import java.io.ObjectOutputStream;
import java.util.ArrayList;

import database.Database;
import simulation.entities.*;

public class DatabaseViewer extends JFrame {

    private Database database;
    
    public DatabaseViewer() {
        setTitle("Zero Player Football - Database Viewer");
        setSize(640, 480);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setLayout(new FlowLayout());
        setJMenuBar(createMenuBar());
    }

    public void setDatabase(Database database) {
        this.database = database;
    }

    private JMenuBar createMenuBar() {
        JMenuBar menuBar = new JMenuBar();
        JMenu menu = new JMenu("Datei");
        JMenuItem newFileItem = new JMenuItem("Neu...");
        newFileItem.addActionListener(_ -> {
            createNewDatabase();
        });
        menu.add(newFileItem);
        JMenuItem saveFileItem = new JMenuItem("Speichern...");
        saveFileItem.addActionListener(_ -> {
            saveCurrentDatabase();
        });
        menu.add(saveFileItem);
        JMenuItem loadFileItem = new JMenuItem("Laden...");
        loadFileItem.addActionListener(_ -> {
            loadExistingDatabase();
        });
        menu.add(loadFileItem);
        menuBar.add(menu);
        return menuBar;
    }

    private void createClubSelectionBox() {
        getContentPane().removeAll();
        JComboBox<String> comboBox = new JComboBox<>();
        for (Club club : database.getClubs()) {
            comboBox.addItem(club.getName());
        }
        getContentPane().add(comboBox);
        JPanel panel = new JPanel();
        panel.setBounds(20, 20, 300, 200);
        JButton button = new JButton("Verein Anzeigen");
        button.addActionListener(_ -> {
            int i = comboBox.getSelectedIndex();
            displayClubDetails(panel, database.getClubs()[i]);
        });
        getContentPane().add(button);
        getContentPane().add(panel);        
        setVisible(true);
    }

    private void displayClubDetails(JPanel panel, Club club) {
        panel.removeAll();
        int rowCount = club.getSquad().getSize();
        ArrayList<Player> players = club.getSquad().getPlayers();
        String data[][] = new String[rowCount][];
        String column[] = new String[]{
            "Name",
            "Alter",
            "Nat.",
            "IQ",
            "Pos.",
            "St."
        };
        for (int i = 0; i < rowCount; i++) {
            Player player = players.get(i);
            data[i] = new String[]{
                player.getFullName(),
                String.valueOf(player.getAge(database.getCalendar().getToday())),
                player.getNationality().toString(),
                String.valueOf(player.getIntelligence()),
                player.getMainPosition().toString(),
                String.valueOf(player.getSkill())
            };
        }
        JTable table = new JTable(data, column);
        table.setBounds(30, 40, 250, 100);
        JScrollPane scrollpane = new JScrollPane(table);
        scrollpane.setBounds(20, 20, 250, 100);
        panel.add(scrollpane);
        panel.setVisible(true);
        setVisible(true);
    }

    private void createNewDatabase() {
        String[] options = {"1965", "1995", "2025"};
        int x = JOptionPane.showOptionDialog(
            this,
            "Für welches Jahr soll der Datensatz angelegt werden?",
            "Wählen Sie ein Jahr:",
            JOptionPane.DEFAULT_OPTION,
            JOptionPane.INFORMATION_MESSAGE, 
            null,
            options,
            options[0]
        );
        if (x >= 0) {
            database.createContent(Integer.parseInt(options[x]));
            createClubSelectionBox();
        }
    }

    private void saveCurrentDatabase() {
        JFileChooser fileChooser = new JFileChooser();
        if (fileChooser.showSaveDialog(this) == JFileChooser.APPROVE_OPTION) {
            File selectedFile = fileChooser.getSelectedFile();
            try {
                selectedFile.createNewFile();
            } catch (Exception exception) {
                IO.println("Datei existiert und wird überschrieben.");
            }
            try (ObjectOutputStream oos = new ObjectOutputStream(
                new FileOutputStream(selectedFile))) {
                    oos.writeObject(database);
                    oos.flush();
                    JOptionPane.showMessageDialog(this, "Datenbank gespeicher" +
                        "t.\n\n" + selectedFile);
            } catch (Exception exception) {
                JOptionPane.showMessageDialog(this, "Datenbank konnte nicht g" +
                    "espeichert werden.\n\n" + exception);
            }
        }
    }

    private void loadExistingDatabase() {
        JFileChooser fileChooser = new JFileChooser();
        if (fileChooser.showOpenDialog(this) == JFileChooser.APPROVE_OPTION) {
            File selectedFile = fileChooser.getSelectedFile();
            try (ObjectInputStream ois = new ObjectInputStream(
                new FileInputStream(selectedFile))) {
                    database = (Database) ois.readObject();
                    createClubSelectionBox();
            } catch (Exception exception) {
                JOptionPane.showMessageDialog(this, "Datenbank konnte nicht g" +
                    "eladen werden.\n\n" + exception);
            }
        }
    }

}
