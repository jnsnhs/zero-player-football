import database.Database;
import gui.DatabaseViewer;

public class App {

    static Database database;
    static DatabaseViewer viewer;

    public static void main() {
        database = new Database();
        viewer = new DatabaseViewer();
        viewer.setDatabase(database);
        viewer.setVisible(true);
    }

}
