package Scaler;

import java.util.ArrayList;
import java.util.Arrays;

public class GoodSubarraysEasy {
    public static void main(String[] args) {
        ArrayList <Integer> a = new ArrayList<>(Arrays.asList(13, 16, 16, 15, 9, 16, 2, 7, 6, 17, 3, 9));
        int B=65;
        System.out.println(goodsubarray(a,B));
    }

    private static int goodsubarray(ArrayList<Integer> A, int B) {
        int count=0;
        for (int i = 0; i < A.size(); i++) {
            int sum=0;
            for (int j = i; j < A.size(); j++) {
                sum=sum+A.get(j);
                int k=j-i+1;
                if (k%2==0 && sum < B) {
                    count++;
                } else if (k%2!=0 && sum > B){
                    count++;
                }
            }
        }
        return count;
    }
}
