import java.util.Scanner;
public class Homework6 {
	public static void main(String[] args) {
		Scanner in = new Scanner(System.in);
        System.out.print("Enter the radius and length of a cylinder：");
        double radius = in.nextDouble();
        double length = in.nextDouble();
        //从用户处获取radius和length
        double area = radius * radius *3.1415926;
        //计算面积
        double volume = area * length;
        //计算体积
        System.out.println("The area is："+area);
        System.out.println("The volume is："+volume);
        //输出结果
        
	}
}
