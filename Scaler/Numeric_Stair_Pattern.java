package Scaler;

import java.util.Scanner;

public class Numeric_Stair_Pattern {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int i = 0;
        while (i < N) { // row
            int num = 1, j = 0;
            while (j <= i) { // col
                System.out.print(num + " ");
                j++;
                num += 1;
            }
            i++;
            System.out.println();

            sc.close();
        }
    }
}
