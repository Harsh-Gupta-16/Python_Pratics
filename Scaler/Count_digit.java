package Scaler;

import java.util.Scanner;

public class Count_digit {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int T = sc.nextInt();
        int i = 0;
        while (i < T) {
            int j = 0;
            int n = sc.nextInt();
            if (n == 0) {
                System.out.println(j);
            } else {
                while (n != 0) {
                    n = n / 10;
                    j++;
                }
                i++;
                System.out.println(j);
            }
        }
        sc.close();
    }
}
