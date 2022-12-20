package Scaler;

import java.util.Scanner;

public class Is_it_prime_optize {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int num = sc.nextInt();
        int cnt = checkprime(num);
        if (cnt == 2) {
            System.out.println("yes");
        } else {
            System.out.println("No");
        }
        sc.close();
    }

    public static int checkprime(int num) {
        int cnt = 0;
        for (int i = 1; i < Math.sqrt(num); i++) {
            if (num % i == 0) {
                if (Math.pow(i, 2) == num) {
                    cnt += 1;
                }
                cnt += 2;

            }
        }
        return cnt;
    }
}
