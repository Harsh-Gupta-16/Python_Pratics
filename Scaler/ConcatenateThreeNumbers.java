package Scaler;

public class ConcatenateThreeNumbers {
    public static void main(String[] args) {
        int A = 55;
        int B = 43;
        int C = 47;
        int min, max;
        if (A > B && A > C) {
            max = A;
        } else if (B > A && B > C) {
            max = B;
        } else {
            max = C;
        }
        if (A < B && A < C) {
            min = A;
        } else if (B < A && B < C) {
            min = B;
        } else {
            min = C;
        }
        System.out.print(min+""+(A+B+C-min-max)+""+max);
    }
}
