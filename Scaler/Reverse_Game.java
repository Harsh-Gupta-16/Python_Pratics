package Scaler;

import java.util.Scanner;

public class Reverse_Game {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int i = 0;
        int T = sc.nextInt();
        while (i < T) {
            int n = sc.nextInt();
            int sum = 0, j = 0;
            while (n != 0) {
                j = n % 10;
                n = n / 10;
                sum = sum * 10 + j;
            }
            System.out.println(sum);
            i++;
        }
        sc.close();
    }
}
