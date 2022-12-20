package Scaler;

import java.util.ArrayList;
import java.util.Arrays;

public class Count_ways_sum_odd_even_indexed {
    public static void main(String[] args) {
        ArrayList <Integer> A = new ArrayList<>(Arrays.asList(1,1,1));
        System.out.println(countodd_even(A));
    }

    public static int countodd_even(ArrayList<Integer> a) {
        int pse[] = new int[a.size()];
        int pso[] = new int[a.size()];
        pse[0]=a.get(0);
        pso[0]=0;
        for (int i = 1; i < pso.length; i++) {
            if (i%2==0) {
                pse[i]=a.get(i)+pse[i-1];
                pso[i]=pso[i-1];

            } else {
                pso[i]=pso[i-1]+a.get(i);
                pse[i]=pse[i-1];
            }
        }
        int j = special_index(pse,pso);
        return j;
    }
    
    public static int special_index(int[] pse, int[] pso) {
        int count=0;
        int sumE=0,sumO=0;
        for (int i = 0; i < pso.length; i++) {
            if(i==0){
                sumE=pso[pso.length-1];
                sumO=pse[pso.length-1]-pse[0];
                if(sumE==sumO){
                    count++;
                }
            }else{
                sumE=pse[i-1]+pso[pso.length-1]-pso[i];
                sumO=pso[i-1]+pse[pso.length-1]-pse[i];
                if (sumE==sumO) {
                    count++;
                }
            }
        }
        return count;
    }
}
