package Scaler;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashSet;
import java.util.List;

public class DiffkII {
    public static void main(String[] args) {
        ArrayList<Integer> A = new ArrayList<>(Arrays.asList(1, 5, 3));
        int B = 2;
        System.out.println(diffPossible(A, B));
    }

    public static int diffPossible(final List<Integer> A, int B) {
        HashSet<Integer> hs = new HashSet<>();
        int count = 0;
        for (int i = 0; i < A.size() - 1; i++) {
            for (int j = i + 1; j < A.size(); j++) {
                if (hs.contains(B + A.get(i))) {
                    count++;
                } else
                    hs.add(B + A.get(i));
            }
        }
        if (count>0) {
            return 1;
        } else {
            return 0;
        }
    }
}
