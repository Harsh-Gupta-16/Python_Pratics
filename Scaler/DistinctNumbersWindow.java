package Scaler;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashSet;

public class DistinctNumbersWindow {
    public static void main(String[] args) {
        ArrayList<Integer> A = new ArrayList<>(Arrays.asList(1, 1, 2, 2));
        int B = 1;
        System.out.println(dNums(A, B));
    }

    public static ArrayList<Integer> dNums(ArrayList<Integer> A, int B) {
        ArrayList<Integer> result = new ArrayList<>();
        if (B > A.size()) {
            return result;
        } else {
            for (int i = 0; i < A.size()-B+1; i++) {
                HashSet<Integer> hs = new HashSet<>();
                for (int j = i; j < i+B; j++) {
                    hs.add(A.get(j));
                }
                result.add(hs.size());
                hs.clear();
            }
            return result;
        }
    }
}
