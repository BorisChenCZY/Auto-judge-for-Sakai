import java.util.Scanner;
public class Homework4 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner in = new Scanner(System.in);
		System.out.print("Enter the number of minutes��");
		long a= in.nextLong();
		//���û�����ȡ������
		long b=a/(60*24*365);
		//��������
		long c=(a%(60*24*365))/(60*24);
		//��������
		System.out.print(a+" minutes is approximately "+b+" years and "+c+" days");
		//���
	}

}
