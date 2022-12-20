package Scaler;

import java.util.ArrayList;
import java.util.Arrays;

public class CountingSubarraysEasy {
    public static void main(String[] args) {
        ArrayList <Integer> A = new ArrayList<>(Arrays.asList(2, 5, 6));
        int B = 10;
        System.out.println(countingsub(A,B));
    }

    private static int countingsub(ArrayList<Integer> A, int B) {
        int count=0;
        for (int i = 0; i < A.size(); i++) {
            int sum=0;
            for (int j = i; j < A.size(); j++) {
                sum+=A.get(j);
                if (sum<10) {
                    count++;
                }
            }
        }
        return count;
    }
}
