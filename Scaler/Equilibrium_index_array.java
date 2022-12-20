package Scaler;

import java.util.ArrayList;
import java.util.Arrays;

public class Equilibrium_index_array {
    public static void main(String[] args) {
        ArrayList <Integer> A = new ArrayList<>(Arrays.asList(1,2,3));
        System.out.println(prefix(A));
    }

    public static int prefix(ArrayList<Integer> A) {
        int ps[]=new int[A.size()];
        ps[0]=A.get(0);
        for (int i = 1; i < A.size(); i++) {
            ps[i]=A.get(i)+ps[i-1];
        }
        int k = equilibrium(ps);
        return k;
    }
    
    public static int equilibrium(int[] ps) {
        int left=0,right=0;
        for (int j = 0; j < ps.length; j++) {
            if (j==0) {
                left=0;
                right=ps[ps.length-1]-ps[j];
            } else if (j==ps.length-1) {
                right=0;
                left=ps[j-1];
                
            } else{
                left=ps[j-1];
                right=ps[ps.length-1]-ps[j];  
            }
            if (left==right) {;
                return j;
            }
        }
        return -1;
    }
}
