package Scaler;

import java.util.Scanner;

public class Electricity_bill_1 {
    private static Scanner sc;

    public static void main(String[] args) {
        sc = new Scanner(System.in);
        System.out.print("Enter the Consume unit: ");
        int use = sc.nextInt();
        double sum = 0;
        if (use > 0 && use <= 50) {
            sum = use*0.5;
        } else if (use > 50 && use <= 150) {
            sum = (50*0.50) + (use - 50)*0.75;
        } else if (use > 150 && use <= 250) {
            sum = (50*0.50) + (100*0.75)+(use - 150)*1.20;
        } else {
            sum = use*1.20;
        }
        sum = sum + (0.20*sum);
        System.out.println("Total Bill is " + Math.floor(sum));
    }
}
