package Scaler;
import java.util.ArrayList;
import java.util.Arrays;

public class Bulb {
    public static void main(String[] args) {
        ArrayList <Integer> A = new ArrayList<>(Arrays.asList(0, 1, 0, 1));
        System.out.println(Toggle(A));
    }

    public static int Toggle(ArrayList<Integer> a) {
        int switchpress=0;
        int currentstate=0;
        for (int i = 0; i < a.size(); i++) {
            if (switchpress%2==0) {
                currentstate=a.get(i);
            } else {
                currentstate = a.get(i)==0?1:0;
            }
            if(currentstate==0){
                switchpress++;
            }
        }
        return switchpress;
    }
}
