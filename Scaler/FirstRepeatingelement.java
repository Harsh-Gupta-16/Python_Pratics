package Scaler;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashSet;

public class FirstRepeatingelement {
    public static void main(String[] args) {
        ArrayList<Integer> A = new ArrayList<>(Arrays.asList(10, 5, 3, 4, 3, 5, 6));
        System.out.println(repert(A));
    }

    private static int repert(ArrayList<Integer> A) {
        HashSet <Integer> hs = new HashSet<>();
        int min=-1;
        for (int i = A.size()-1; i >=0; i--) {
            if (hs.contains(A.get(i))) {
                min=i;
            } else {
                hs.add(A.get(i));
            }
        }
        if (min!=-1) {
            return A.get(min);
        } else {
            return -1;
        }
    }
}
