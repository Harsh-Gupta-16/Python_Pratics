package Scaler;

public class SingleNumber {
    public static void main(String[] args) {
        int [] A = new int[]{1, 2, 2, 3, 1};
        System.out.println(singleNumber(A));
    }

    private static int singleNumber(int[] a) {
        int ans=0;
        for (int i = 0; i < a.length; i++) {
                ans=ans^a[i];
        }
        return ans;
    }
}
