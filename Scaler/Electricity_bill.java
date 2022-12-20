package Scaler;

import java.util.Scanner;

public class Electricity_bill {
    private static Scanner sc;

    public static void main(String[] args) {
        sc = new Scanner(System.in);
        System.out.print("Enter the Consume unit: ");
        int use = sc.nextInt();
        if (use < 0 && use <= 100) {
            System.out.println("No bill needs to pay");
        } else if (use > 100 && use <= 200) {
            int sum = (use - 100) * 5;
            System.out.println("Total Bill is " + sum);
        } else if (use > 200 && use <= 300) {
            int sum = (100 * 5) + ((use - 200) * 10);
            System.out.println("Total Bill is " + sum);
        } else {
            int sum = (100 * 5) + (100 * 10) + ((use - 300) * 12);
            System.out.println("Total Bill is " + sum);
        }
    }
}
