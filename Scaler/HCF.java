package Scaler;

import java.util.Scanner;

public class HCF {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();
        int j = 0;
        while (j < t) {
            int n1 = sc.nextInt();
            int n2 = sc.nextInt();
            int i = 1, HCF = 1;
            while (i < n1 || i < n2) {
                if (n1 % i == 0 && n2 % i == 0) {
                    HCF = i;
                }
                i++;
            }
            System.out.println(HCF);
            j++;
        }
        sc.close();
    }
}
