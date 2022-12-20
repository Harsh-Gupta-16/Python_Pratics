package Scaler;

import java.util.Scanner;

public class Is_It_Prime {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
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
            System.out.println("YES");
        } else {
            System.out.println("NO");
        }
        sc.close();
    }
}