package Scaler;

import java.util.ArrayList;
import java.util.Arrays;

public class EvenSubarrays {
    public static void main(String[] args) {
        ArrayList <Integer> a = new ArrayList<>(Arrays.asList(121, 351, 314, 562, 953, 319, 859, 413, 201, 640, 66, 723, 998, 612, 291, 539, 463, 340, 64, 251, 807, 457, 584, 944, 315, 327, 769, 675, 113, 364, 488, 579, 674, 340, 950, 516, 618, 599, 186, 496, 403, 450, 833, 79, 229, 150, 497, 256, 971, 687, 318, 717, 540, 126, 906, 843, 417, 557, 97, 370, 409, 148, 968, 562, 534, 845, 378));
        System.out.println(evensub(a));
    }

    public static String evensub(ArrayList<Integer> A) {
        if(A.size()%2!=0||A.get(0)%2!=0||A.get(A.size()-1)%2!=0)
            return "NO";
        else
            return "YES";
    }
}
