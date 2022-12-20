package Scaler;

import java.util.Scanner;

public class Inverse_pattern {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int row = sc.nextInt();
        for (int i = row; i > 0; i--) {
            for (int s = 4; s >= i; s--) {
                System.out.print(" ");
            }
            for (int j = i; j > 0; j--) {
                System.out.print(" * ");
            }
            System.out.println();
        }
        for (int i = 0; i < row; i++) {
            for (int s = 1; s < row - i; s++) {
                System.out.print(" ");
            }
            for (int j = 0; j <= i; j++) {
                System.out.print(" * ");
            }
            System.out.println();
        }
        sc.close();
    }
}
