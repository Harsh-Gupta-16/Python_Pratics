package Scaler;

import java.util.Scanner;

public class Remove_that {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int a[]= new int [N];
        for(int i=0;i<N;i++){
            a[i]=sc.nextInt();
        }
        int x = sc.nextInt();

        int delele[]= deletion(a,x);
        for (int i : delele) {
            System.out.print(i+" ");
        }

        sc.close();
    }
    static int [] deletion(int[] arr, int k){
        int [] b = new int[arr.length-1];
        for (int i = 0; i < b.length; i++) {
            if (i<k-1) {
                b[i]=arr[i];
            } else {
                b[i]=arr[i+1];
            }   
        }
        return b;

    }
}
