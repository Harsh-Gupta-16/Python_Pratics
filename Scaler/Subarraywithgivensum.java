package Scaler;

import java.util.ArrayList;
import java.util.Arrays;

public class Subarraywithgivensum {
    public static void main(String[] args) {
        ArrayList<Integer> A = new ArrayList<>(Arrays.asList(1, 2, 3, 4, 5));
        int B = 5;
        System.out.println(solve(A, B));
        ;
    }

    private static ArrayList<Integer> solve(ArrayList<Integer> A, int B) {
        ArrayList<Integer> result = new ArrayList<>();
        int sum = A.get(0);
        int start = 0,end=0;
        for (int i = 1; i <= A.size(); i++) {
            // If currentsum exceeds the required sum,
            // then remove the starting elements
            while (sum > B && start < i - 1) {
                sum = sum - A.get(start);
                start++;
            }
             // If currentsum becomes equal to required sum,  
            // then break  
            if (sum == B) {
                end = i-1;
                break;
            }
            // If currentsum becomes less to required sum,
            // then add one element to sum
            if (i < A.size()) {
                sum += A.get(i);
            }
        }
        for (int i = start; i <= end; i++) {
            result.add(A.get(i));
        }
        return result;
    }
}
