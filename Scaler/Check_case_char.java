package Scaler;

import java.util.Scanner;

public class Check_case_char {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        char s = sc.next().charAt(0);
        if (Character.isLowerCase(s)) {
            System.out.println("lowercase");
        } else {
            System.out.println("UPPERCASE");
        }
        sc.close();
    }
}
