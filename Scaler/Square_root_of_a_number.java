package Scaler;

import java.util.Scanner;

public class Square_root_of_a_number {
    public static void main(String[] args) {
        Scanner sc  = new Scanner(System.in);
        int n = sc.nextInt();
        System.out.println(squreroot(n));
        sc.close();
    }

    public static int squreroot(int n) {
        int count=0,ans=0;
        for (int i = 1; i <= Math.sqrt(n); i++) {
            if (i*i==n){
                ans=i;
                count+=1;
            }
        }
        if (count==1) {
            return ans;
        } else {
            return -1;
        }
    }
}
