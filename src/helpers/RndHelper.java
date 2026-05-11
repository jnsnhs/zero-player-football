package helpers;

public class RndHelper {
    
    public static double triangularDistribution(double a, double b, double c) {
        double F = (c - a) / (b - a);
        double rand = Math.random();
        if (rand < F) {
            return a + Math.sqrt(rand * (b - a) * (c - a));
        } else {
            return b - Math.sqrt((1 - rand) * (b - a) * (b - c));
        }
    }

    public static int chooseIndex(int[] weights) {
        int sumOfWeights = 0;
        for (int weight : weights) {
            sumOfWeights += weight;
        }
        double randomNumber = Math.random() * sumOfWeights;
        int runningWeights = 0;
        int choice = 0;
        for (int i = 0; i < weights.length; i++) {
            runningWeights += weights[i];
            if (randomNumber < runningWeights) {
                break;
            } else {
                choice++;
            }
        }
        return choice;
    }

}
