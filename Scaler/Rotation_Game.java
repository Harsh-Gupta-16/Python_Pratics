package Scaler;

import java.util.Scanner;

public class Rotation_Game {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int arr[] = new int[N];
        for (int i = 0; i < N; i++) {
            arr[i] = sc.nextInt();
        }
        int R = sc.nextInt();
        for (int i = 0; i < R; i++) {
            int x = arr[N-1];
            for (int j = N-1; j > 0; j--) {
                arr[j]=arr[j-1];
            }
            arr[0]=x;
        }
        for (int i : arr) {
            System.out.print(i);
        }
        sc.close();
    }
}
