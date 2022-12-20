package Scaler;

public class Square_root {
    public static void main(String[] args) {
        System.out.println(SquareRoot(5));
        System.out.println(String.format("%.3f", SquareRoot(5, 3)));
    }

    // Normal Square Root
    static int SquareRoot(int n) {
        int i = 1;
        while (i * i <= n) {
            i = i + 1;
        }
        return i - 1;
    }

    // Square Root to Precision (square root upto decimal without libary function)
    // arugment first is number & second is upto positon
    static double SquareRoot(int n, int p) {
        double i = 0;
        double inc = 1;
        // for loop is for getting the position of the value
        for (int work = 0; work <= p; work++) {
            // finalise the digit at current place
            while (i * i <= n) {
                i = i + inc;
            }
            // one step backward
            i = i - inc;
            inc = inc / 10;
        }
        return i;
    }
}
