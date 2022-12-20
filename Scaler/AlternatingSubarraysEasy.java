package Scaler;

import java.util.ArrayList;
import java.util.Arrays;

public class AlternatingSubarraysEasy {
    public static void main(String[] args) {
        ArrayList<Integer> A = new ArrayList<>(Arrays.asList(1, 0, 1, 0, 1));
        int B = 1;
        System.out.println(AlternateSub(A, B));
    }

    public static ArrayList<Integer> AlternateSub(ArrayList<Integer> A, int B) {
        ArrayList<Integer> result = new ArrayList<Integer>();
        int lenght = (2*B)+1;
        for (int s = 0; s <= A.size()-lenght; s++) {
            int flag=0;
            for (int e = s; e < s+lenght-1; e++) {
                if (A.get(e)==A.get(e+1)) {
                    flag=1;
                    break;
                }
            }
            if (flag==0) {
                result.add((s+(s+lenght-1))/2);
            }
        }
        return result;
    }
}
