package Scaler;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;

public class Time_to_equality {
    public static void main(String[] args) {
        ArrayList <Integer> A = new ArrayList<>(Arrays.asList(2, 4, 1, 3, 2));
        System.out.println(timeeuality(A));
    }

    public static int timeeuality(ArrayList<Integer> a) {
        int sum=0;
        int max=Collections.max(a);
        for (int i = 0; i < a.size(); i++) {
            sum=sum+(max-a.get(i));
        }
        return sum;
    }
}
