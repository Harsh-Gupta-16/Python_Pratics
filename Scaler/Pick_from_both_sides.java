package Scaler;

import java.util.ArrayList;
import java.util.Arrays;

public class Pick_from_both_sides {
    public static void main(String[] args) {
        ArrayList <Integer> A = new ArrayList<>(Arrays.asList(5, -2, 3 , 1, 2));
        int B = 3;
        System.out.println(pickboth(A,B));
    }

    public static int pickboth(ArrayList<Integer> a, int b) {
        int max=0, current=0;
        for(int i =0;i<b;i++){
            current +=a.get(i);
        }
        max=current;
        int lst = a.size()-1;
        for (int i = b-1; i >= 0 ; i--) {
            current=current+a.get(lst)-a.get(i);
            max=Math.max(current, max);
            lst--;
        }
        return max;
    }
}
