package Scaler;

import java.util.Scanner;

public class Simple_interest {
    private static Scanner sc = new Scanner(System.in);

    public static void main(String[] args) {
        int p = sc.nextInt();
        int t = sc.nextInt();
        float r = sc.nextFloat();
        double si = (p * r * t) / 100;
        System.out.println("The Simple Interset is : " + si);

    }
}
