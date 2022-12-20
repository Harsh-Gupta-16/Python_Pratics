

public class MajorityElement {
    public static void main(String[] args) {
        int [] A = new int []{1,2,2};
        System.out.println(majorityElement(A));
    }
    public static int majorityElement(final int[] A) {
        int count=1;
        int ME=0;
        for (int i = 0; i < A.length; i++) {
            if (A[ME]==A[i])
                count++;
            else count--;
            if(count==0){
                ME=i;
                count=1;
            }
        }
        return A[ME];
    }
}
