import java.util.Scanner;
public class Homework7 {
	public static void main(String[] args) {
	Scanner in = new Scanner(System.in);
	System.out.print("Enter a number between 0 and 1000��");
	int A= in.nextInt();
	//���û�����ȡ����
	int b=A/100;
	//�����λ��
	int c=(A-b*100)/10;
	//����ʮλ��
	int d=A%10;
	//�����λ��
	int sum=b+c+d;
	//���
	System.out.println("The sum of the digits is :"+sum);
	//������
	
	

	}
}
