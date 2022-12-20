package Scaler;

import java.util.ArrayList;
import java.util.Arrays;

public class SumofAllSubarrays {
    public static void main(String[] args) {
        ArrayList <Integer> A = new ArrayList<>(Arrays.asList(2, 1, 3));
        System.out.println(subarraySum(A));
    }

    private static long subarraySum(ArrayList<Integer> A) {
        long sum=0;
        for (int i = 0; i < A.size(); i++) {
            int start=i+1;
            int end= A.size()-i;
            int freq=start*end;
            sum+=freq*A.get(i);
        }
        return sum;
    }
}
