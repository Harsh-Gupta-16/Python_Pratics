package Scaler;

import java.util.ArrayList;
import java.util.Arrays;

public class Leaders_array {
    public static void main(String[] args) {
        ArrayList <Integer> A = new ArrayList<>(Arrays.asList(16, 17, 4, 3, 5, 2));
        System.out.println(leader(A));
    }

    public static ArrayList<Integer> leader(ArrayList<Integer> A) {
        ArrayList<Integer> result = new ArrayList<>();
        int rightmost = A.get(A.size()-1);
        result.add(rightmost);
        for (int i = A.size()-2; i >=0; i--) {
            if (rightmost<A.get(i)) {
                rightmost=A.get(i);
                result.add(rightmost);
            }
        }
        return result;
    }
}
