package Scaler;

public class SimpleReverse {
    public static void main(String[] args) {
        String A = "harsh";
        System.out.println(simplerever(A));
    }

    private static char[] simplerever(String A) {
        char [] ch = A.toCharArray();
        reverse(ch, 0, A.length()-1);
        return ch;
    }
    static void reverse(char str[],int start, int end) {
        char temp;
        while (start <= end) {
            temp = str[start];
            str[start] = str[end];
            str[end] = temp;
            start++;
            end--;
        }
    }
}
