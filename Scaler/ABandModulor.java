package Scaler;

public class ABandModulor {
    public static void main(String[] args) {
        int A=10,B=20;
        System.out.println(Modul(A,B));
    }

    private static int Modul(int A, int B) {
        return Math.abs(B-A);
    }
}
