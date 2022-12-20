package Scaler;

import java.util.ArrayList;
import java.util.Arrays;

public class SortbyColor {
    public static void main(String[] args) {
        ArrayList<Integer> A = new ArrayList<>(Arrays.asList(0,1,2,0,1,2));
        System.out.println(sortColors(A)); 
    }
    public static ArrayList<Integer> sortColors(ArrayList<Integer> A) {
        int low=0,mid=0;
        int high=A.size()-1;
        while (mid<=high) {
            if (A.get(mid)==0) {
              swap(A,low,mid);
              mid++;
              low++;
            } else if(A.get(mid)==1){
                mid++;
            }else if (A.get(mid)==2) {
                swap(A, mid, high);
                high--;
            }
        }
        return A;
    }
    private static void swap(ArrayList<Integer> a, int first, int second) {
        int temp=a.get(first);
        a.set(first, a.get(second));
        a.set(second, temp);
    }
}
