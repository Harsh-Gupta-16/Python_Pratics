package Scaler;

import java.util.Scanner;

public class Multiplication_preivous_next {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        //int a[]= {1,2,3,4,5};
        int a[]= {5,17,100,11};
        int b[]=solve(a);
        for (int i : b) {
            System.out.print(i+" ");
        }
        sc.close();
    }

    public static int[] solve(int[] a) {
        int result[]= new int[a.length];
        for (int i = 0; i < result.length; i++) {
                if(i==0){
                    result[i]=a[i]*a[i+1];
                }else if (i==a.length-1) {
                    result[i]=a[i]*a[i-1];
                } else {
                    result[i]=a[i-1]*a[i+1];
                }
        }
        return result;
    }

}
