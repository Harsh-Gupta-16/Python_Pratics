package Scaler;

import java.util.ArrayList;
import java.util.Scanner;

public class Separate_Odd_Even {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int T = sc.nextInt();
        for(int k =0;k<T;k++){
            int N = sc.nextInt();
            int a[] = new int[N];
            ArrayList <Integer> even = new ArrayList<>();
            ArrayList <Integer> odd = new ArrayList<>();
            for (int i = 0; i < a.length; i++) {
                a[i]=sc.nextInt();
            }
            for (int i = 0; i < a.length; i++) {
                if (a[i]%2==0) {
                    even.add(a[i]);
                } else {
                    odd.add(a[i]);
                }
            }
            for (Integer integer : odd) {
                System.out.print(integer+" ");
            }
            System.out.println();
            for (Integer integer : even) {
                System.out.print(integer+" ");
            }
        }
        sc.close();
    }
}