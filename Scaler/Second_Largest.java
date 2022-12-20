package Scaler;

import java.util.Arrays;
import java.util.Scanner;

public class Second_Largest {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int T = sc.nextInt();
        for (int k = 0; k < T; k++) {
            int N = sc.nextInt();
            int a[] = new int[N];
            if (N>=2) {
                for (int i = 0; i < a.length; i++) {
                    a[i]=sc.nextInt();
                }
                Arrays.sort(a);
                System.out.println(a[N-2]);
                
            } else {
                System.out.println("-1");
            }
        }
        sc.close();
    }
}
