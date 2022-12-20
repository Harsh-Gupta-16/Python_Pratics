package Scaler;

import java.util.Scanner;

public class Sum_the_Array {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int sum=0;
        int a[]= new int [N];
        for(int i=0;i<N;i++){
            a[i]=sc.nextInt();
            sum += a[i];
        }
        System.out.println(sum);
        sc.close();
    }
}
