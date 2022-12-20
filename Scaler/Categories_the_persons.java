package Scaler;

import java.util.Scanner;

public class Categories_the_persons {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        float A = sc.nextFloat();
        if (A>=195) {
            System.out.println("abnormal");
        } else if (A<195 && A>=165) {
            System.out.println("taller");
        } else if (A<165 && A>=150) {
            System.out.println("average");
        } else {
            System.out.println("dwarf");
        }
        sc.close();
    }
}
