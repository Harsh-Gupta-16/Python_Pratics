package Scaler;

public class ExcelColumnNumber {
    public static void main(String[] args) {
        String A = "ABCD";
        System.out.println(excelcol(A));
    }

    private static int excelcol(String A) {
        int result = 0;
        for (int i = 0; i < A.length(); i++) {
            int d = A.charAt(i) - 'A' + 1;
            result = 26 * result + d;
        }
        return result;
    }
}
