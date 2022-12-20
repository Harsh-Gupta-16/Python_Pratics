package Scaler;

public class AntiDiagonals {
    public static void main(String[] args) {
        int a[][]={{1,2,3},{4,5,6},{7,8,9}};
        System.out.println(diagonal(a));
    }

    public static int[][] diagonal(int[][] A) {
        int N = A.length;
        int[][] result = new int[2 * N - 1][N];
        int resi = 0, resj = 0;
        // when row is zero , fidning columns
        for (int col = 0; col < N; col++) {
            int startrow = 0;
            int startcolumn = col;
            while (startrow < N && startcolumn >= 0) {
                result[resi][resj] = A[startrow][startcolumn];
                startrow++;
                startcolumn--;
                resj++;
            }
            resi++;
            resj = 0;
        }

        for (int row = 1; row < N; row++) {
            int startrow = row;
            int startcolumn = N - 1;
            while (startrow < N && startcolumn >= 0) {
                result[resi][resj] = A[startrow][startcolumn];
                startrow++;
                startcolumn--;
                resj++;
            }
            resi++;
            resj = 0;
        }
        return result;

    }
}
