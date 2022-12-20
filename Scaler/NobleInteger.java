package Scaler;

import java.util.ArrayList;
import java.util.Arrays;

public class NobleInteger {
    public static void main(String[] args) {
        ArrayList <Integer> A = new ArrayList<>(Arrays.asList(1, 1, 3, 3));
        System.out.println(noble(A));
    }

    private static int noble(ArrayList<Integer> A) {
        int flag=0;
        for (int i = 0; i < A.size(); i++) {
            if (i==A.get(i)) {
                flag=1;
            }
        }
        if (flag==1) {
            return 1;
        }else
        return -1;
    }
}
