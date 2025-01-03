import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Test {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        List<Double> results = new ArrayList<Double>();
        Function fun = new Function();

        Tools.Print("-", 50);
        System.out.println();
        Tools.Print(" ", 18);
        System.out.println("产品功能介绍");
        Tools.Print(" ", 14);
        System.out.println("1. 支持简易的四则运算");
        Tools.Print(" ", 13);
        System.out.println("2. 可查询每次的计算结果");
        Tools.Print("-", 50);
        System.out.println();


        while (true) {
            try {
                System.out.println("计算请按Y/y");
                System.out.println("计算结果查询请按F/f");
                System.out.println("退出程序请按N/n");
                
                char choice = scanner.nextLine().charAt(0);
                
                if(choice == 'Y' || choice == 'y') {
                    results.add(fun.Calculate());
                } else if(choice == 'F' || choice == 'f') {
                    fun.Find(results);
                } else if(choice == 'N' || choice == 'n') {
                    Tools.Clear();
                    System.out.println("感谢您的使用，如果您对我们的项目感兴趣，欢迎您加入我们的团队。");
                    System.out.println("网址");
                    break;
                }  else {
                    System.out.println("无效的指令！请重新输入！");
                    continue;
                }
            } catch (Exception e) {
                System.out.println("输入无效，错误信息：" + e.getMessage());
            }
            
        }
      scanner.close();
    }
}
