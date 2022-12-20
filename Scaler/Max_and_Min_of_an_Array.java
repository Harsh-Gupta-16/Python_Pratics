package Scaler;

import java.util.Scanner;

public class Max_and_Min_of_an_Array {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int [] A = new int[N];
        for (int i = 0; i < A.length; i++) {
            A[i]=sc.nextInt();
        }
        System.out.print(Max(A)+" "+Min(A));
        sc.close();
    }
    public static int Max(int []A){
        int Maxi=A[0];
        for (int i = 0; i < A.length-1; i++) {
            if(A[i+1]>Maxi){
                Maxi=A[i+1];
            }
        }
        return Maxi;
    }
    public static int Min(int []A){
        int Mini=A[0];
        for (int i = 0; i < A.length-1; i++) {
            if(A[i+1]<Mini){
                Mini=A[i+1];
            }
        }
        return Mini;
    }
}
