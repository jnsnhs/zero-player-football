package simulation.entities;
import java.io.Serializable;
import java.time.LocalDate;

public class Calendar implements Serializable {
    
    private LocalDate today;

    public Calendar(int year, int month, int day) {
        setToday(year, month, day);
    }

    private void setToday(int year, int month, int day) {
        today = LocalDate.of(year, month, day);
    }

    public LocalDate getToday() {
        return today;
    }

    public void goToNextDay() {
        today = today.plusDays(1);
    }

}
