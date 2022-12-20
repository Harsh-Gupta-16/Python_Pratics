package Scaler;

public class CheckPalindromeRes {
    public static void main(String[] args) {
        String A ="naman";
        System.out.println(solve(A));
    }
    public static int solve(String A) {
        if(isPllaindrome(A)){
            return 1;
        }
        else
          return 0;
    }

    static boolean isPllaindrome(String A){
        int n = A.length();
        if(n==0) 
           return true;
        else
          return checkPallindrome(A, 0,n-1);
    }

    static boolean checkPallindrome(String A, int start, int end){
         if(start>=end){
             return true;
         }
        if(A.charAt(start)==A.charAt(end)){
           return checkPallindrome(A,++start,--end);
        }
        return false;
    
    }
}
