package Scaler;

import java.util.ArrayList;
import java.util.Arrays;

public class ElementsRemoval {
    public static void main(String[] args) {
        ArrayList <Integer> A = new ArrayList<>(Arrays.asList(2, 1));
        System.out.println(Elemntremove(A));
    }
    private static int Elemntremove(ArrayList<Integer> A) {
        int sum=0;
        for (int i = 0; i < A.size(); i++) {
            sum=sum+A.get(i)*(i+1);
        }
        return sum;
    }
}
