package Scaler;

import java.util.Scanner;

public class Vowel_Or_Consonant {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        char c = sc.next().charAt(0);
        if (c=='a'||c=='e'||c=='i'||c=='o'||c=='u') {
            System.out.println("1");
        } else {
            System.out.println("0");
        }
        sc.close();
    }
}
