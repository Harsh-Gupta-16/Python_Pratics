package Scaler;

public class Trailing_zero_factor {
    public static void main(String[] args) {
        System.out.println(findTrailingZeros(100));
    }

    static int findTrailingZeros(int n) {
        int ans = 0;
        int p = 5;
        while (n / p > 0) {
            ans = ans + n / p;
            p = p * 5;
        }
        return ans;
    }
}
