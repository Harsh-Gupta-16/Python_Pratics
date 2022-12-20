package Scaler;

import java.util.Scanner;

public class Insert_that {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int a[]= new int [N];
        for(int i=0;i<N;i++){
            a[i]=sc.nextInt();
        }
        int x = sc.nextInt();
        int y = sc.nextInt();

        int insert[]= insertion(a,x,y);
        for (int i : insert) {
            System.out.print(i+" ");
        }

        sc.close();
    }
    static int [] insertion(int[] arr, int k,int l){
        int [] b = new int[arr.length+1];
        for (int i = 0; i < b.length; i++) {
            if (i<k-1) {
                b[i]=arr[i];
            } else if (i==k-1) {
                b[i]=l;
            } else {
                b[i]=arr[i-1];
            }   
        }
        return b;

    }
}
