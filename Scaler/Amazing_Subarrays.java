package Scaler;

public class Amazing_Subarrays {
    public static void main(String[] args) {
        String A = "ABEC";
        System.out.println(Amazing(A));
    }

    public static int Amazing(String a) {
        int count_substr=0;
        for (int i = 0; i < a.length(); i++) {
            if(a.charAt(i)=='A'||a.charAt(i)=='E'||a.charAt(i)=='I'||a.charAt(i)=='O'||a.charAt(i)=='U'||
            a.charAt(i)=='a'||a.charAt(i)=='e'||a.charAt(i)=='i'||a.charAt(i)=='o'||a.charAt(i)=='u'){
                for(int j =i;j<a.length();j++)
                    count_substr++;
            }
        }
        return count_substr%10003;
    }
}
