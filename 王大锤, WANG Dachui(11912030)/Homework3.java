import java.util.Scanner;
public class Homework3 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner in = new Scanner(System.in);
        System.out.print("Enter x1 and y1：");
        double x1 = in.nextDouble();
        double y1 = in.nextDouble();
        //从用户处获取第一个点坐标
        System.out.print("Enter x2 and y2：");
        double x2 = in.nextDouble();
        double y2 = in.nextDouble();
        //从用户处获取第二个点坐标
        double distance = (double) Math.sqrt(Math.abs((x1 - x2)*(x1 - x2))+Math.abs((y1 - y2)*(y1 - y2)));
        System.out.print("The distance of the two points is："+distance);
        //计算距离并输出结果
	}
}
