package Scaler;

import java.util.ArrayList;
import java.util.Arrays;

public class ClosestMinMax {
    public static void main(String[] args) {
        ArrayList <Integer> A = new ArrayList<>(Arrays.asList(1,2,3,1,3,4,6,4,6,3));
        System.out.println(closest(A));
    }

    public static int closest(ArrayList<Integer> a) {
        int min=a.get(0),max=a.get(0);
        for (int i = 0; i < a.size(); i++) {
            if (a.get(i)<min) {
                min=a.get(i);
            }
        }
        for (int i = 0; i < a.size(); i++) {
            if (a.get(i)>max) {
                max=a.get(i);
            }
        }
        int pos_min=-1,pos_max=-1,ans=Integer.MAX_VALUE;
        for (int i = 0; i < a.size(); i++) {
            if(a.get(i)==min)
                pos_min=i;
            if (a.get(i)==max) {
                pos_max=i;
            }
            if (pos_min!=-1 && pos_max!=-1) {
                ans=Math.min(ans, Math.abs(pos_min-pos_max)+1);
            }
        }
        return ans;
    }
}
