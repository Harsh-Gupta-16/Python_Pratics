package Scaler;

import java.util.ArrayList;
import java.util.Arrays;

public class Product_array_puzzle {
    public static void main(String[] args) {
        ArrayList<Integer> A = new ArrayList<>(Arrays.asList(5, 1, 10, 1));
        System.out.println(product_array(A));
    }

    public static ArrayList<Integer> product_array(ArrayList<Integer> a) {
        int prod = 1;
        int count=0;
        for (Integer integer : a) {
            prod=prod*integer;
        }
        for (Integer integer : a) {
            a.set(count, prod/integer);
            count++;
        }
        return a;
    }
}
