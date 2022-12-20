package Scaler;

import java.util.Scanner;

public class Find_The_Floor {
    public static int solve(int A){
        double ans = Math.floor(A/200.0);
        return (int)ans;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int A = sc.nextInt();
        System.out.println(solve(A));
        sc.close();
    }
}
