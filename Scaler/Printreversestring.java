package Scaler;

public class Printreversestring {
    public static void main(String[] args) {
        String A = "ymedacarelacs";
        reverse(A.substring(0, A.length()));

    }
    private static void reverse(String A) {
        if (A==null||A.length()<=1) {
            System.out.print(A);
        } else {
            System.out.print(A.charAt(A.length()-1));
            reverse(A.substring(0, A.length()-1));
        }
    }
   
}
