import java.util.Scanner;

class Interview {
    public static void main(String args[]) {
        Scanner Sc = new Scanner(System.in);
        int size = Sc.nextInt();
        int[] starttime = new int[size];
        int[] endtime = new int[size];
        for (int i = 0; i < size; i++) {
            starttime[i] = Sc.nextInt();
        }
        for (int j = 0; j < size; j++) {
            endtime[j] = Sc.nextInt();
        }
        int count = 1;
        int result = endtime[0];
        for (int k = 0; k < size - 1; k++) {

            if (result <= starttime[k + 1]) {
                result = endtime[k + 1];
                count++;
            }
        }
        System.out.println(count);
    }
}