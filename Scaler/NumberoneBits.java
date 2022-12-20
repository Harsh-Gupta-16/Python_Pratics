package Scaler;

public class NumberoneBits {
    public static void main(String[] args) {
        int A = 1;
        System.out.println(numSetBits(A));
    }

    private static int numSetBits(int A) {
        int count = 0;
        while (A > 0) {
            int carry = A % 2;
            if (carry == 1)
                count++;
            A = A / 2;
        }
        return count;
    }
}
