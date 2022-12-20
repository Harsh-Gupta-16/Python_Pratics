package Scaler;

public class LargestPalindrome {
    public static void main(String[] args) {
        String A = "abcba";
        System.out.println(largeParlindrome(A));
    }

    private static int largeParlindrome(String A) {
        int ans = 1;
        for (int i = 0; i < A.length(); i++) {
            if (i % 2 == 0) {
                ans = Math.max(ans, getpalidromelenght(A, i, i));
            } else
                ans = Math.max(ans, getpalidromelenght(A, i, i + 1));
        }
        return ans;
    }

    static int getpalidromelenght(String S, int i, int j) {
        if (i >= 0 && j < S.length() && S.charAt(i) == S.charAt(j)) {
            i--;
            j++;
        }
        return j - i - 1;

    }
}
