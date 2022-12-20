package Scaler;

import java.util.Scanner;

public class LCM {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n1 = sc.nextInt();
        int n2 = sc.nextInt();
        int i = 1, gcd = 1;
        while (i < n1 && i < n2) {
            if (n1 % i == 0 && n2 % i == 0) {
                gcd = i;
            }
            i++;
        }
        System.out.println(((n1 * n2) / gcd));
        sc.close();
    }
}