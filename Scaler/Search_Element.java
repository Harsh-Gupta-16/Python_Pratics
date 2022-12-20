package Scaler;

import java.util.Scanner;

public class Search_Element {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int T = sc.nextInt();
        for (int k = 0; k < T; k++) {
            int N = sc.nextInt();
            int a[] = new int[N];
            for (int i = 0; i < N; i++) {
                a[i] = sc.nextInt();
            }
            int search = sc.nextInt();
            int count=search_value(a,search);
            if (count==0) {
                System.out.println("0");
            } else {
                System.out.println("1");
            }
        }
        sc.close();
    }

    public static int search_value(int[] a, int search) {
        int count=0;
        for (int i = 0; i < a.length; i++) {
            if (a[i]==search) {
                count++;
            }
        }
        return count;
    }

    
}
