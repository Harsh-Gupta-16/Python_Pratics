package Scaler;

import java.util.Scanner;

public class Pascal_Triangle {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int zero = n;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j <= i; j++) {
                System.out.print(BinomalConfficent.binomialCoeff(i, j) + " ");
            }
            int s = 0;
            while (s < zero - 1) {
                System.out.print("0 ");
                s++;
            }
            zero = zero - 1;
            System.out.println();
        }
        sc.close();
    }
}
