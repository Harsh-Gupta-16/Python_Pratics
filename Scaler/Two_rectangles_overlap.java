package Scaler;

public class Two_rectangles_overlap {
    public static void main(String[] args) {
        System.out.println(rectangle(0,0,4,4,2,2,6,6));
    }

    public static int rectangle(int a, int b, int c, int d, int e, int f, int g, int h) {
        if (c <= e || d <= f || a >= g || b >= h) {
            return 0;
        } else {
            return 1;

        }

    }
}
