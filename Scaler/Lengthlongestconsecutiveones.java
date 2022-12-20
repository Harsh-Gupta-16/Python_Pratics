package Scaler;

public class Lengthlongestconsecutiveones {
    public static void main(String[] args) {
        String A = "111000";
        System.out.println(lengthlong(A));
    }

    private static int lengthlong(String A) {
        int count=0;
        for (int i = 0; i < A.length(); i++) {
            if (A.charAt(i)=='1') {
                count++;
            }
        }
        return count;
    }
}
