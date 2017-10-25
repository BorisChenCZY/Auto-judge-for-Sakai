import java.util.Scanner;
public class Homework7 {
	public static void main(String[] args) {
	Scanner in = new Scanner(System.in);
	System.out.print("Enter a number between 0 and 1000：");
	int A= in.nextInt();
	//从用户处获取数字
	int b=A/100;
	//计算百位数
	int c=(A-b*100)/10;
	//计算十位数
	int d=A%10;
	//计算个位数
	int sum=b+c+d;
	//求和
	System.out.println("The sum of the digits is :"+sum);
	//输出结果
	
	

	}
}
