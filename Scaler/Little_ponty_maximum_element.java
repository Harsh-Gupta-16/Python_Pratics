package Scaler;

public class Little_ponty_maximum_element {
    public static void main(String[] args) {
        int a []={2,4,1,5};
        int b=3;
        System.out.println(solve(a,b));
    }

    private static int solve(int[] a, int b) {
        int count = 0,check=0;
        for (int i = 0; i < a.length; i++){
            if (a[i]==b) {
                check=1;
            }
        }
        if (check==1) {
            for (int i = 0; i < a.length; i++) {
                if (a[i]>b) {
                    count+=1;
                }
            }
        } else {
            return -1;
        }
        return count;
    }
}
