package Scaler;

//Perfect number is a positive integer which is equal to the sum of its proper positive divisors
import java.util.Scanner;

public class Is_it_perfect_number {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int T = sc.nextInt();
        for (int i = 0; i < T; i++) {
            int n = sc.nextInt();
            int sum = 0;
            for (int j = 1; j < n; j++) {
                if (n % j == 0) {
                    sum += j;
                }
            }
            if (sum==n) {
                System.out.println("YES");
            } else {
                System.out.println("NO");
            }

        }
        sc.close();
    }
}
