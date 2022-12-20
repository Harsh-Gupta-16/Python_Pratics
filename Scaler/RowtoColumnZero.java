package Scaler;

import java.util.ArrayList;
import java.util.Arrays;

public class RowtoColumnZero {
    public static void main(String[] args) {
        ArrayList<ArrayList<Integer>> A = new ArrayList<>();
        ArrayList<Integer> a1 = new ArrayList<>(Arrays.asList(1, 2, 3, 4));
        ArrayList<Integer> a2 = new ArrayList<>(Arrays.asList(5, 6, 7, 0));
        ArrayList<Integer> a3 = new ArrayList<>(Arrays.asList(2, 9, 0, 4));
        A.add(a1);
        A.add(a2);
        A.add(a3);
        System.out.println(rowcolzero(A));
    }

    public static ArrayList<ArrayList<Integer>> rowcolzero(ArrayList<ArrayList<Integer>> A) {
        ArrayList<ArrayList<Integer>> result = new ArrayList<>();
        ArrayList<Integer> row = new ArrayList<>();
        ArrayList<Integer> col = new ArrayList<>();
        for (int i = 0; i < A.size(); i++) {
            for (int j = 0; j < A.get(0).size(); j++) {
                if (A.get(i).get(j) == 0) {
                    row.add(i);
                    col.add(j);
                }
            }
        }
        for (int i = 0; i < A.size(); i++) {
            ArrayList<Integer> val = new ArrayList<>();
            for (int j = 0; j < A.get(0).size(); j++) {
                if (row.contains(i) || col.contains(j)) {
                    val.add(0);
                } else {
                    val.add(A.get(i).get(j));
                }
            }
            result.add(val);
        }
        return result;
    }
}
