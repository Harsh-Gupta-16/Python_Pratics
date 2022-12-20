package Scaler;

public class BinomalConfficent {
    static int binomialCoeff(int n,int r){
        return Factorial.factorial(n)/(Factorial.factorial(n-r)* Factorial.factorial(r));
    }
    public static void main(String[] args) {
        System.out.println(binomialCoeff(5,3));
    }
}
