import java.util.List;
import java.util.Scanner;

/*
 * 计算器功能类
 */

public class Function {
    Scanner scanner = new Scanner(System.in);
    
    // 运算方法
    public double Calculate() {
        Algorithm algorithm = new Algorithm();
        double num1 = 0;
        double num2 = 0;
        double result = 0;
        char operator;

        Tools.Clear();
        // 提示用户输入操作数和操作符
        System.out.println("请输入第一个操作数：");
        num1 = scanner.nextDouble();

        System.out.println("请输入操作符 (+, -, *, /)：");
        operator = scanner.next().charAt(0);
        // charAt(index),返回字符串中指定位置的字符
        // 参数：index，要返回的字符的索引位置

        System.out.println("请输入第二个操作数：");
        num2 = scanner.nextDouble();

        // 根据操作符选择不同的运算
        switch (operator) {
            case '+':
                result = algorithm.add(num1, num2);
                break;
            case '-':
                result = algorithm.subtract(num1, num2);
                break;
            case '*':
                result = algorithm.multiply(num1, num2);
                break;
            case '/':
                result = algorithm.divide(num1, num2);
                break;
            default:
                System.out.println("无效的操作符！请重新输入。");
        }
        // 输出运算结果
        System.out.println("运算结果：" + result);
        return result;
    }
    
    // 计算结果查询方法
    public void Find(List<Double> results) {
        Tools.Clear();
        System.out.println("请输入您要查询哪次计算结果:");
        int index = scanner.nextInt();
        if(index > results.size()) {
            throw new RuntimeException("还没有算到这么多次喔。");
        }
        System.out.println("第"+index+"次的计算结果为"+results.get(index-1));
        System.out.println("继续计算请按Y/y");
        System.out.println("计算结果查询请按F/f");
        System.out.println("退出程序请按N/n");       
    }
}
