package Scaler;

public class LenghtLastword {
    public static void main(String[] args) {
        String A = "Hello World";
        System.out.println(lastword(A));
    }

    private static int lastword(String A) {
        String [] str = A.split(" ");
        return str[str.length-1].length();
    }
    
}
