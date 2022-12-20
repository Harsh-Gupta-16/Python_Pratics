package Scaler;

import java.util.ArrayList;
import java.util.Arrays;

public class Multiple_left_rotationsaray {
    public static void main(String[] args) {
        ArrayList <Integer> A = new ArrayList<>(Arrays.asList(1,2,3,4,5));
        ArrayList <Integer> B = new ArrayList<>(Arrays.asList(2,3));
        System.out.println(solve(A,B));
    }
    public static ArrayList<ArrayList<Integer>> solve(ArrayList<Integer> A, ArrayList<Integer> B) {
        ArrayList <ArrayList <Integer>> result = new ArrayList<>();
        for (int i = 0; i < B.size(); i++) {
            int pivot = B.get(i)%A.size();
            ArrayList <Integer> row = new ArrayList<>();
            row.addAll(A.subList(pivot, A.size()));
            row.addAll(A.subList(0,pivot));
            result.add(row);
        }
        return result;
    }
}
