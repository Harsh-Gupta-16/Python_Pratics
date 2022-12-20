package Scaler;

import java.util.Scanner;

public class Binary_to_Decimal {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String a = sc.next();
        System.out.println(Integer.parseInt(a,2));
        sc.close();
    }
}
