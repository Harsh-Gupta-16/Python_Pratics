package Scaler;

import java.util.Scanner;

public class Binary_to_Decimal_2 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int a = sc.nextInt();
        int n=0,sum=0;
        while(true){
            if(a==0){
                break;
            }else{
                int temp = a%10;
                sum += temp*Math.pow(2, n);
                a=a/10;
            }
            n++;
        }
        System.out.println(sum);
        sc.close();
    }
}
