package Scaler;

public class NthMagicalNumber {
    public static void main(String[] args) {
        int A = 10;
        System.out.println(Magical(A));
    }

    private static int Magical(int A) {
        int sum=0;
        int count=1;
        while(A>0){
            int rem = A%2;
            sum = sum+rem*(int)Math.pow(5, count);
            A=A/2;
            count++;
        }
        return sum;
    }
}
