package Scaler;

import java.util.ArrayList;
import java.util.Arrays;

public class MaximumSubarrayEasy {
    public static void main(String[] args) {
        ArrayList<Integer> C = new ArrayList<>(Arrays.asList(2, 2, 2));
        int A = 3, B = 1;
        System.out.println(maxSubarray(A, B, C));
    }

    public static int maxSubarray(int A, int B, ArrayList<Integer> C) {
        int max=0;
        for (int i = 0; i < A; i++) {
            int sum=0;
            for (int j = i; j < A; j++) {
                sum+=C.get(j);
            }
            if (sum<=B) {
                max=Math.max(max, sum);
            }
        }
        return max ;
    }
}
