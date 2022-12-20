package Scaler;

import java.util.ArrayList;
import java.util.Arrays;

public class print2Dmatric_Arraylist {
    public static void main(String[] args) {
        ArrayList<ArrayList<Integer>> A = new ArrayList<>();
        ArrayList<Integer> a1 = new ArrayList<>(Arrays.asList(1, 2, 3));
        ArrayList<Integer> a2 = new ArrayList<>(Arrays.asList(4, 5, 6));
        ArrayList<Integer> a3 = new ArrayList<>(Arrays.asList(7, 8, 9));
        A.add(a1);
        A.add(a2);
        A.add(a3);
        for (int i = 0; i < A.size(); i++) {
                System.out.print(A.get(i));
                System.out.println();
        }
    }

}
