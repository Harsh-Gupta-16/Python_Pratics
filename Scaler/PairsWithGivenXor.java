package Scaler;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashSet;

public class PairsWithGivenXor {
    public static void main(String[] args) {
        ArrayList<Integer> A = new ArrayList<>(Arrays.asList(3, 6, 8, 10, 15, 50));
        int B = 5;
        System.out.println(pair(A, B));
    }

    private static int pair(ArrayList<Integer> A, int B) {
        int count = 0;
        HashSet<Integer> hs = new HashSet<>();
        for (int i = 0; i < A.size(); i++) {
            if (hs.contains(B^A.get(i))) {
                count++;
            }
            hs.add(A.get(i));
        }
        return count;
    }

}
