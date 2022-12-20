package Scaler;
public class SpiralOrderMatrixII {
    public static void main(String[] args) {
        int A = 2;
        System.out.println(generateMatrix(A));
    }

    public static int[][] generateMatrix(int A) {

        int[][] result = new int[A][A];
        int resi = 0, resj = 0;
        int N = A;
        int a = 1;
        while (N > 1) {
            for (int k = 1; k < N; k++) {
                result[resi][resj] = a;
                resj++;
                a++;
            }
            for (int k = 1; k < N; k++) {
                result[resi][resj] = a;
                resi++;
                a++;
            }
            for (int k = 1; k < N; k++) {
                result[resi][resj] = a;
                resj--;
                a++;
            }
            for (int k = 1; k < N; k++) {
                result[resi][resj] = a;
                resi--;
                a++;
            }

            resi++;
            resj++;
            N = N - 2;
        }
        if (N == 1) {
            result[A / 2][A / 2] = a;
        }
        return result;
    }
}
