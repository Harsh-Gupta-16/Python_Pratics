package Scaler;

import java.util.Scanner;

public class ArmstrongNumbers {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        for (int i = 1; i < N; i++) {
            int sum = 0;
            int rem = 0;
            int n = i;
            // int pow = power(n);
            while (n != 0) {
                rem = n % 10;
                sum = (int) (sum + Math.pow(rem, 3));
                n = n / 10;
            }
            if (sum == i) {
                System.out.println(sum);
            }
            sc.close();
        }
    }

    public static int power(int n) {
        int count = 0;
        while (n != 0) {
            n = n / 10;
            count += 1;
        }
        return count;
    }
}
