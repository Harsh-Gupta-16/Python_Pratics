package Scaler;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;

public class CommonElements {
    public static void main(String[] args) {
        ArrayList<Integer> A = new ArrayList<>(Arrays.asList(2, 1, 4, 10));
        ArrayList<Integer> B = new ArrayList<>(Arrays.asList(3, 6, 2, 10, 10));
        System.out.println(commonelt(A, B));
    }

    private static ArrayList<Integer> commonelt(ArrayList<Integer> A, ArrayList<Integer> B) {
        ArrayList<Integer> result = new ArrayList<>();
        HashMap<Integer, Integer> hmA = new HashMap<>();
        HashMap<Integer, Integer> hmB = new HashMap<>();
        for (int i = 0; i < A.size(); i++) {
            if (hmA.containsKey(A.get(i))) {
                hmA.put(A.get(i), hmA.get(A.get(i))+1);
            } else {
                hmA.put(A.get(i), 1);
            }
        }
        for (int i = 0; i < B.size(); i++) {
            if (hmB.containsKey(B.get(i))) {
                hmB.put(B.get(i), hmB.get(B.get(i))+1);
            } else {
                hmB.put(B.get(i), 1);
            }
        }
        for (int i = 0; i < A.size(); i++) {
            if (hmB.containsKey(A.get(i))) {
                if (hmA.get(A.get(i))!=0 && hmB.get(A.get(i))!=0) {
                    result.add(A.get(i));
                    hmA.put(A.get(i), hmA.get(A.get(i)) - 1);
                    hmB.put(A.get(i), hmB.get(A.get(i)) - 1);
                }
            }
        }
        return result;
    }
}