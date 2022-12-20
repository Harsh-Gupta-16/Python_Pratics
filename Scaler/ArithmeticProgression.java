package Scaler;

import java.util.ArrayList;
import java.util.Arrays;

public class ArithmeticProgression {
    public static void main(String[] args) {
        ArrayList<Integer> A = new ArrayList<>(Arrays.asList(2, 4, 1));
        System.out.println(AP(A));
    }

    private static int AP(ArrayList<Integer> A) {
        int diff = A.get(1) - A.get(0);
        int count = 0;
        for (int i = 1; i < A.size() - 1; i++) {
            if ((A.get(i + 1) - A.get(i)) == diff) {
                count++;
            }
        }
        if (count != 0) {
            return 1;
        } else {
            return 0;

        }
    }
}
