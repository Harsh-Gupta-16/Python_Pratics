package Scaler;

import java.util.Scanner;

public class PrimeFactor {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int num = sc.nextInt();
        int divisor = 2;
        while(num!=1){
            if(num%divisor==0){
                System.out.print(divisor);
                num=num/divisor;
                if (num!=1) {
                    System.out.print(" X ");
                }
            }else{
                divisor++;
            }
        }
        sc.close();
    }
}
