package Scaler;

import java.util.Scanner;

public class Summation_Game {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        System.out.println((N*(N+1)/2));
        sc.close();
    }
}
