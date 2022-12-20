package Scaler;

public class Copy_the_Array {
    public static void main(String[] args) {
        int a[]= new int[5];
        int b=5;
        
        int [] cpy = solve(a,b);
        for (int i : cpy) {
            System.out.println(i);
        }

    }
    public static int[] solve(int[] a, int B) 
    {
        int[] outArr = new int[a.length];
        for(int i=0;i<outArr.length;i++)
        {
            outArr[i]= a[i]+B;
        }
        return outArr ;
        
    }
}
