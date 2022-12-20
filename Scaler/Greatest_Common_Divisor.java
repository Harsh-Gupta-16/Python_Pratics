package Scaler;

import java.util.Scanner;

//using Ecludic Alogrithum
public class Greatest_Common_Divisor {
    public static int gcd(int A, int B) {
        if(B==0)
        {
            return A;
        }
        return gcd(B,A%B);
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int A = sc.nextInt();
        int B = sc.nextInt();
        System.out.println(gcd(A, B));
        sc.close();
    }
}
