package Scaler;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;

public class Subarraywithsum {
    public static void main(String[] args) {
        ArrayList<Integer> A = new ArrayList<>(Arrays.asList(-1, 1));
        System.out.println(subzero(A));
    }

    private static int subzero(ArrayList<Integer> A) {
        int ps[] = new int[A.size()];
        ps[0] = A.get(0);
        HashMap<Integer, Integer> hs = new HashMap<>();
        for (int i = 1; i < A.size(); i++) {
            ps[i] = ps[i - 1] + A.get(i);
        }
        for (int i = 0; i < ps.length; i++) {
            if (hs.containsKey(ps[i])) {
                hs.put(ps[i], hs.get(ps[i] + 1));
            } else {
                hs.put(ps[i], 1);
            }
        }
        for (int k = 0; k < ps.length; k++) {
            if (hs.containsKey(0)) {
                return 1;
            }
        }
        return 0;
    }
}
