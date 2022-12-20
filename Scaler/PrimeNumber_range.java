package Scaler;

import java.util.Scanner;

public class PrimeNumber_range {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter the range of Prime number: ");
        int N = sc.nextInt();
        int j = 1;
        if (N >= 1 && N <= 300) {
            while (j <= N) {
                int i = 2;
                int count = 0;
                while (i <= j / 2) {
                    if (j % i == 0) {
                        count = count + 1;
                        break;
                    }
                    i++;
                }
                if (count == 0 && j != 1) {
                    System.out.println(j);
                }
                j++;
            }
        }
        sc.close();
    }
}