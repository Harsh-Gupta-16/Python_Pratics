package Scaler;

public class AddBinaryStrings {
    public static void main(String[] args) {
        String A = "100";
        String B = "11";

        System.out.println(addBinary(A, B));
    }

    public static String addBinary(String A, String B) {
        int i = A.length()-1;
        int j = B.length()-1;
        String str = "";
        int sum=0,rem;
        int carry=0;
        while (i >= 0 && j >= 0) {
            sum=carry+A.charAt(i)-'0'+B.charAt(j)-'0';
            rem=sum%2+'0';
            str=str+(char)rem;
            carry=sum/2;
            i--;j--;
        }
        while(i>=0){
            sum=carry+A.charAt(i)-'0';
            carry=sum/2;
            rem=sum%2+'0';
            str=str+(char)rem;
            i--;
        }
        while(j>=0){
            sum=carry+A.charAt(j)-'0';
            carry=sum/2;
            rem=sum%2+'0';
            str=str+(char)rem;
            j--;
        }
        return str;
    }
}
