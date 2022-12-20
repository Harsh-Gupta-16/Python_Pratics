package Scaler;

public class Tworectanglesoverlap {
    public static void main(String[] args) {
        System.out.println(rectange(0, 0, 4, 4, 2, 2, 6, 6));
    }

    public static int rectange(int A, int B, int C, int D, int E, int F, int G, int H) {

        if (A == C || B == D || E == G || F == H) {
            // the line cannot have positive overlap
            return 1;
        }

        // If one rectangle is on left side of other
        if (A >= G || E >= C) {
            return 1;
        }

        // If one rectangle is above other
        if (D >= F || H >= B) {
            return 1;
        }

        return 0;
    }

}
