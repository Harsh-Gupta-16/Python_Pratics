package Scaler;

import java.util.ArrayList;
import java.util.Arrays;

public class Subarray_with_least_average {
    public static void main(String[] args) {
        ArrayList<Integer> A = new ArrayList<>(Arrays.asList(3, 7, 90, 20, 10, 50, 40));
        int B = 3;
        System.out.println(subarryavg(A, B));
    }

    private static int subarryavg(ArrayList<Integer> A, int B) {
        int currentsum = 0;
        for (int i = 0; i < B; i++) {
            currentsum = currentsum + A.get(i);
        }
        int minsum = currentsum;
        int i = 0, j = B, x = 0;
        while (j < A.size()) {
            currentsum = currentsum + A.get(j) - A.get(i);
            if (currentsum < minsum) {
                minsum = currentsum;
                x = i + 1;
            }
            j++;
            i++;

        }
        return x;
    }
}
