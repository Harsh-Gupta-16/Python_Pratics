package Scaler;

import java.util.Arrays;

public class Minimum_Pick {
    public static void main(String[] args) {
        int a[] = {5,15,100,3};
        System.out.println(solve(a));
    }

    private static int solve(int[] a) {
        Arrays.sort(a);
        int max=0,min=0;
        for (int i = a.length-1; i > 0; i++) {
            if (a[i]%2==0) {
                max=a[i];
                break;
            }
        }
        for (int i = 0; i < a.length; i++) {
            if (a[i]%2!=0) {
                min=a[i];
                break;
            }
        }
        
        return max-min;
    }
}
