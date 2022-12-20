package Scaler;

import java.util.ArrayList;
import java.util.Arrays;

public class ColumnSum {
    public static void main(String[] args) {
        ArrayList<ArrayList<Integer>> A = new ArrayList<>();
        ArrayList<Integer> a1 = new ArrayList<>(Arrays.asList(1, 2, 3, 4));
        ArrayList<Integer> a2 = new ArrayList<>(Arrays.asList(5, 6, 7, 8));
        ArrayList<Integer> a3 = new ArrayList<>(Arrays.asList(9, 2, 3, 4));
        A.add(a1);
        A.add(a2);
        A.add(a3);
        System.out.println(colsum(A));
    }

    private static ArrayList<Integer> colsum(ArrayList<ArrayList<Integer>> A) {
        ArrayList<Integer> result = new ArrayList<Integer>();
        for (int i = 0; i < A.get(0).size(); i++) {
            int sum = 0;
            for (int j = 0; j < A.size(); j++) {
                sum += A.get(j).get(i);
            }
            result.add(sum);
        }
        return result;
    }
}
