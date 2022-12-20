package Scaler;

public class IsPalindrome {
    public static void main(String[] args) {
        String A = "abcba";
        System.out.println(parlindrome(A));
    }

    private static int parlindrome(String A) {
        int N = A.length();
        int flag=0;
        for (int i = 0; i < N/2; i++) {
            if (A.charAt(i)!=A.charAt(N-i-1)) {
                flag=1;
                break; 
            }
        }
        if (flag==1) {
            return 0;
        } else {
            return 1;
        }
    }
}
