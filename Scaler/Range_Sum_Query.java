package Scaler;

public class Range_Sum_Query {
    public static void main(String[] args) {
        int a[] = new int[] { 1, 2, 3, 4, 5 };
        int b[][] = new int[][] { { 1, 4 }, { 2, 3 } };
        int ps[] = new int[a.length];
        int arr[] = new int[b.length];
        ps[0] = a[0];
        for (int i = 1; i < a.length; i++) {
            ps[i] = ps[i - 1] + a[i];
        }
        for (int i = 0; i < b.length; i++) {
            int left = b[i][0]-1;
            int right = b[i][1]-1;
            if (left<=0) {
                arr[i]=ps[right];
            } else {
                arr[i]=ps[right]-ps[left-1];
            }
        }
        for (int i : arr) {
            System.out.print(i+" ");
        }
    }
}
