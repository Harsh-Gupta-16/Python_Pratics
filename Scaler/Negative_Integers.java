package Scaler;

import java.util.Scanner;

public class Negative_Integers {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int a[]= new int [N];
        for(int i=0;i<N;i++){
            a[i]=sc.nextInt();
            if (a[i]<0) {
                System.out.print(a[i]+" ");
            }
        }
        sc.close();
    }
}
