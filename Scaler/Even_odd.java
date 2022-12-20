package Scaler;

import java.util.Scanner;

public class Even_odd {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        if (n % 2 == 0) {
            System.out.print("0");
        } else {
            System.out.println("1");
        }
        sc.close();
    }
}