package Scaler;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;

public class SubarraySumEqualsK {
    public static void main(String[] args) {
        ArrayList<Integer> A = new ArrayList<>(Arrays.asList(1, 0, 1));
        int B = 1;
        System.out.println(subarraysum(A, B));
    }

    private static int subarraysum(ArrayList<Integer> A, int B) {
        HashMap<Integer, Integer> map = new HashMap<>();
        int count = 0;
        int sum = 0;
        for (int i = 0; i < A.size(); i++) {
            sum += A.get(i);
            if (sum == B) {
                count++;
            }
            if (map.containsKey(sum - B)) {
                count += map.get(sum - B);
            }
            Integer diff = map.get(sum);
            if (diff == null) {
                map.put(sum, 1);
            } else
                map.put(sum, diff + 1);
        }
        return count;
    }
}
