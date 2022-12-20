package Scaler;

import java.util.HashSet;

public class CheckPalindrome {
    public static void main(String[] args) {
        String A = "abcde";
        System.out.println(checkp(A));
    }

    private static int checkp(String A) {
        HashSet <Character> hc = new HashSet<>();
        for (int i = 0; i < A.length(); i++) {
            char ch = A.charAt(i);
            if (hc.contains(ch)) {
                hc.remove(ch);
            } else {
                hc.add(ch);
            }
        }
        if (A.length()%2==0&&hc.isEmpty())
            return 1;
        else if (A.length()%2!=0 && hc.size()==1)
            return 1;
        else 
            return 0;
    }
}
