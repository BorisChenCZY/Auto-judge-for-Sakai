import java.util.Scanner;
public class Homework6 {
	public static void main(String[] args) {
		Scanner in = new Scanner(System.in);
        System.out.print("Enter the radius and length of a cylinder��");
        double radius = in.nextDouble();
        double length = in.nextDouble();
        //���û�����ȡradius��length
        double area = radius * radius *3.1415926;
        //�������
        double volume = area * length;
        //�������
        System.out.println("The area is��"+area);
        System.out.println("The volume is��"+volume);
        //������
        
	}
}
