package Scaler;

public class ReversetheString {
    public static void main(String[] args) {
        String A = "the sky is blue ";
        System.out.println(ReverseStr(A));
    }

    private static char[] ReverseStr(String A) {
        char[] ch = A.toCharArray();
        int start=0;
        for (int end = 0; end < ch.length; end++) {
            // from the space
            if(ch[end]==' '){
                reverse(ch, start, end);
                start=end+1;
            }
        }
        // last word
        reverse(ch, start, ch.length-1);
        reverse(ch, 0, ch.length-1);
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
