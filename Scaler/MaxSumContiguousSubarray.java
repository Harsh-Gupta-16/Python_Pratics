package Scaler;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class MaxSumContiguousSubarray {
    public static void main(String[] args) {
        ArrayList <Integer> A = new ArrayList<>(Arrays.asList(1, 2, 3, 4, -10));
        System.out.println(maxSubArray(A));
    }

    public static int maxSubArray(final List<Integer> A) {
        int max=Integer.MIN_VALUE;
        int current_sum=0;
        for (int i = 0; i < A.size(); i++) {
            current_sum=current_sum+A.get(i);
            max=Math.max(max, current_sum);
            if (current_sum<0) {
                current_sum=0;
            }
        }
        return max;
    }
}
