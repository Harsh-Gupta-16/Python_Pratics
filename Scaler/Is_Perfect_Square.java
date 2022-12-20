package Scaler;

import java.util.Scanner;

public class Is_Perfect_Square {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int A = sc.nextInt();
        double x = Math.sqrt(A);
        if(A%x==0){
            System.out.println("1");;
        }else{
            System.out.println("0");
        }
        sc.close();
    }
}
