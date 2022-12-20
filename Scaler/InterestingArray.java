package Scaler;

import java.util.ArrayList;
import java.util.Arrays;

public class InterestingArray {
    public static void main(String[] args) {
        ArrayList <Integer> A = new ArrayList<>(Arrays.asList(1));
        System.out.println(solve(A));
    }
    public static String solve(ArrayList<Integer> A) {
        int merge,splt=0;
        for (int i = 0; i < A.size()-1; i++) {
            merge = A.get(i)^A.get(i+1);
            if (merge>0) {
                splt=merge/2;
            }
            if (splt>0) {
                merge = splt^splt;
            }
            if (merge==0) {
                return "Yes";
            }
        }
        return "No";
    }
}
