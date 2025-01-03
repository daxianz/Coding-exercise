/*
* 运算法则类
*/

public class Algorithm {
    
    // 加法
    public double add(double a, double b) {
        return a + b;
    }

    // 减法
    public double subtract(double a, double b) {
        return a - b;
    }

    // 乘法
    public double multiply(double a, double b) {
        return a * b;
    }

    // 除法
    public double divide(double a, double b) {
        if (b == 0) {
            throw new RuntimeException("除数不能为零");
            //  抛出运行时异常，除数为0
        }
        return a / b;
    }
}
