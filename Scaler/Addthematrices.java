package Scaler;

import java.util.ArrayList;

public class Addthematrices {
    public static void main(String[] args) {
        ArrayList<ArrayList<Integer>> aList = new ArrayList<ArrayList<Integer>>();
        // master list (ArrayList of ArrayList)
        ArrayList<Integer> a1 = new ArrayList<Integer>();
        a1.add(1);
        a1.add(2);
        a1.add(3);
        aList.add(a1);

        ArrayList<Integer> a2 = new ArrayList<Integer>();
        a2.add(4);
        a2.add(5);
        a2.add(6);
        aList.add(a2);

        ArrayList<Integer> a3 = new ArrayList<Integer>();
        a3.add(7);
        a3.add(8);
        a3.add(9);
        aList.add(a3);
        ArrayList<ArrayList<Integer>> bList = new ArrayList<ArrayList<Integer>>();
        // master list (ArrayList of ArrayList)
        ArrayList<Integer> b1 = new ArrayList<Integer>();
        b1.add(9);
        b1.add(8);
        b1.add(7);
        bList.add(b1);

        ArrayList<Integer> b2 = new ArrayList<Integer>();
        b2.add(6);
        b2.add(5);
        b2.add(4);
        bList.add(b2);

        ArrayList<Integer> b3 = new ArrayList<Integer>();
        b3.add(3);
        b3.add(2);
        b3.add(1);
        bList.add(b3);

        // System.out.println("2D ArrayList… :");
        // System.out.println(aList);
        // System.out.println(bList);
        // System.err.println("row "+bList.size());
        // System.err.println("col "+bList.get(0).size());
        System.out.println(Addthematrc(aList, bList));
    }

    public static ArrayList<ArrayList<Integer>> Addthematrc(ArrayList<ArrayList<Integer>> A,
            ArrayList<ArrayList<Integer>> B) {
        ArrayList<ArrayList<Integer>> result = new ArrayList<>();
        for (int i = 0; i < A.size(); i++) {
            ArrayList <Integer> row = new ArrayList<>();
            for (int j = 0; j < B.size(); j++) {
                int sum = 0;
                sum = A.get(i).get(j)+B.get(i).get(j) ;
                row.add(sum);
            }
           result.add(row);
        }
        return result;
    }
}
