package Scaler;

import java.util.Scanner;

public class PrimeNumber {
    private static Scanner sc = new Scanner(System.in);

    public static void main(String[] args) {
        System.out.print("Enter the number to check Prime or not: ");
        int num = sc.nextInt();
        int count = 0;
        int i = 2;

        while (i <= num / 2) {
            if (num % i == 0) {
                count += 1;
                break;
            }
            i += 1;
        }
        if (count == 0 && num != 1) {
            System.out.println(num + " is the prime number");
        } else {
            System.out.println(num + " is not the prime number");
        }

    }

}
