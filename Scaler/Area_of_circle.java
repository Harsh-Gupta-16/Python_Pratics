package Scaler;

import java.util.Scanner;

public class Area_of_circle {
    public static int solve(int A){
        double ans = Math.ceil(Math.PI*A*A);
        return (int)ans;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int A = sc.nextInt();
        System.out.println(solve(A));
        sc.close();
    }
}
