package Scaler;

import java.util.Scanner;

public class First_vs_Last {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int T = sc.nextInt();
        for (int i = 0; i < T; i++) {
            int N = sc.nextInt();
            int last = N%10;
            while(N>=10){
                N = N/10;
            }
            System.out.println(N +" "+last);
        }
        sc.close();
    }
}
