package Scaler;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashSet;
import java.util.List;

public class LongestConsecutiveSequence {
    public static void main(String[] args) {
        List<Integer> A = new ArrayList<>(Arrays.asList(2, 1));
        System.out.println(longestConsecutive(A));
    }
    public static int longestConsecutive(final List<Integer> A) {
        HashSet <Integer> hs = new HashSet<>();
        int ans=0;
        for (int i = 0; i < A.size(); i++) {
            hs.add(A.get(i));
        }
        for (Integer i : hs) {
            int length =1,k=1;
            if(!hs.contains(i-1)){
                while (hs.contains(i+k)) {
                    length++;
                    k++;
                }
                ans=Math.max(length, ans);
            }
        }

        return ans;
    }
}
