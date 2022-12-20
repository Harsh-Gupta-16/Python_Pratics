package Scaler;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashSet;

public class Pairsarraysum {
    public static void main(String[] args) {
        ArrayList<Integer> A = new ArrayList<>(Arrays.asList(3, 4, 2, 6, 7));
        System.out.println(pairsum(A));
    }

    private static int pairsum(ArrayList<Integer> A) {
        HashSet<Integer> hs = new HashSet<>();
        int count = 0;
        for (int i = 0; i < A.size(); i++) {
            hs.add(A.get(i));
        }
        for (int i = 0; i < A.size(); i++) {
            for (int j = i + 1; j < A.size(); j++) {
                int sum = 0;
                sum = A.get(i) + A.get(j);
                if (hs.contains(sum)) {
                    count++;
                }
            }
        }
        return count;
    }
}
