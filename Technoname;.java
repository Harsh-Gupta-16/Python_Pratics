import java.util.Scanner;

class Technoname
{
	public static void getDate(int d, String m)
	{
		 int[] days = { 31, 29, 31, 30, 31, 30,
		    31, 31, 30, 31, 30, 31 };
		 String[] month = { "January", "February", "March",
		     "April", "May", "June", "July",
		     "August", "September", "October",
		     "November", "December" };
		 int count = 183;
		 int current_month = 0;
		 for(int i = 0; i < 12; i++)
		  if (m == month[i])
		   current_month = i;
		 int current_date = d;
		
		 while (true)
		 {
			  while (count > 0 && current_date <= days[current_month])
			  {
			   count -= 1;
			   current_date += 1;
			  }
			  if (count == 0)
			  break;
			  current_month = (current_month + 1) % 12;
			  current_date = 1;
		 }
		 System.out.println(current_date + " " +month[current_month]);
	}
	public static void main(String args[])
	{
		 int D;
		 String M;
		 Scanner sc=new Scanner(System.in);
		 D=sc.nextInt();
		 M=sc.next();
		 getDate(D, M);
	}
}