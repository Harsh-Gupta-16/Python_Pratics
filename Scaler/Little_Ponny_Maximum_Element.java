package Scaler;

import java.util.Scanner;

public class Little_Ponny_Maximum_Element {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int[] a= new int[N];
        for (int i = 0; i < N; i++) {
            a[i]=sc.nextInt();
        }
        int B = sc.nextInt();
        int flag=0;
        for (int i = 0; i < a.length; i++) {
            if(a[i]==B){
                flag=1;
            }
        }
        if(flag==1){
            int count=0;
            for (int i = 0; i < a.length; i++) {
                if (a[i]<B) {
                    count++;
                }
            }
            System.out.println(count);
        }else{
            System.out.println("-1");
        }
        sc.close();
    }
}
