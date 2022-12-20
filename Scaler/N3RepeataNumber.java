package Scaler;

import java.util.ArrayList;
import java.util.Arrays;

public class N3RepeataNumber {
    public static void main(String[] args) {
        ArrayList <Integer> A = new ArrayList<>(Arrays.asList(1,2,3,1,1));
        System.out.println(repeatedNumber(A));
    }

    private static int repeatedNumber(ArrayList<Integer> A) {
        int count1=1,count2=1;
        int ME1=0,ME2=0;
        for (int i = 1; i < A.size(); i++) {
            if (ME1==A.get(i)) {
                count1++;
            } else if (ME2==A.get(i)) {
                count2++;
            } else if (count1==0) {
                count1=1;
                ME1=i;
            } else if (count2==0) {
                count2=1;
                ME2=i;
            } else {
                count1--;
                count2--;
            }
        }
        count1=0;count2=0;
        for (int i = 0; i < A.size(); i++) {
            if (A.get(ME1)==A.get(i)) {
                count1++;
            } else if (A.get(ME2)==A.get(i)) {
                count2++;
            }
        }
        if (count1>(A.size())/3) {
           return A.get(ME1);
        }
        if (count2>A.size()/3) {
            return A.get(ME2);
        }
        return -1;
        
    }
}
