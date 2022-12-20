package Scaler;

public class ToggleCase {
    public static void main(String[] args) {
        String A = "HelLo";
        toggle(A);
    }

    private static void toggle(String A) {
        char [] ch = A.toCharArray();
        for (int i = 0; i < ch.length; i++) {
            ch[i]^=32;
        }
        System.out.println(ch);
    }
}
