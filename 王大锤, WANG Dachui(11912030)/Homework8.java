
public class Homework8 {
	public static void main(String[] args) {
		int i=0;
		//初始值
		System.out.print("number   square   cube");
		//输出第一行
		while (i<=10){//当i不大于10时，执行下列语句
			int b=i*i;//计算平方
			int c=i*i*i;//计算立方
		System.out.printf("\n%6d%9d%7d",i,b,c);//输出结果
		i++;//给i加上1，继续循环，直到i等于10的时候停止
		}
		
	}

}
