package Scaler;

public class Special_Subsequences {
    public static void main(String[] args) {
        String A = "ABCGAG";
        System.out.println(special(A));
    }

    public static int special(String a) {
        int ans=0,count_a=0;
        for (int i = 0; i < a.length(); i++) {
            if (a.charAt(i)=='A') {
                count_a++;
            }
            if(a.charAt(i)=='G'){
                ans+=count_a;
            }
        }
        return ans;
    }
}
