import java.util.Scanner;
public class Homework4 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner in = new Scanner(System.in);
		System.out.print("Enter the number of minutes：");
		long a= in.nextLong();
		//从用户处获取分钟数
		long b=a/(60*24*365);
		//计算年数
		long c=(a%(60*24*365))/(60*24);
		//计算天数
		System.out.print(a+" minutes is approximately "+b+" years and "+c+" days");
		//输出
	}

}
