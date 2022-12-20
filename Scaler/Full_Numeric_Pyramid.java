package Scaler;

import java.util.Scanner;

public class Full_Numeric_Pyramid {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int row = sc.nextInt();
        // Row
        int i, zero, j;
        for (i = 1; i <= row; i++) {
            // number of zero
            for (zero = 1; zero <= row - i; zero++) {
                System.out.print("0" + " ");
            }
            // increase number
            for (j = i; j <= (2 * i) - 1; j++) {
                System.out.print(j + " ");
            }
            // decrease number
            for (j = (2 * i) - 2; j >= i; j--) {
                System.out.print(j + " ");
            }
            // number of zero
            for (zero = 1; zero <= row - i; zero++) {
                System.out.print("0"+" ");
            }
            System.out.println();
        }
        sc.close();

    }
}
