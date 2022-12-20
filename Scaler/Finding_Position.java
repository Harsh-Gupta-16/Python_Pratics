package Scaler;

import java.util.Scanner;

public class Finding_Position {
    public static void main(String[] args) {
        Scanner sc  = new Scanner(System.in);
        int n = sc.nextInt();
        System.out.print(solve(n));
        sc.close();
    }

    public static int solve(int x) {
        int i = 1;
        while (i <= x/2) {
            i=i*2;
        }
        return i;    
        
    }
}
