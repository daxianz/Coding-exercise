## 捕获异常
- Java程序的执行过程中如果出现异常，会自动生成一个异常类对象，该异常对象将被提交给Java运行时系统，这个过程叫做抛出异常
- 在编写程序时，要在可能经常出错的地方加上异常处理代码捕获异常并处理
- 捕获异常的代码格式如下
```java 
//* 捕获了一个异常 */
package test;
public class Test {
    public static void main(String[] args) {
        int i = 0;
        try{ // 用try{...}来括住可能出现的异常
            System.out.println(3/0);
        } catch(Exception e) { // 当不知道捕获的是什么类型的异常时，可以用所有异常类的父类Exception
            // 对捕获的异常进行处理
            e.getStackTrace(); // 输出发生异常时的堆栈信息
            System.out.println("捕获到了异常：" + e.getMessage()); // 输出捕获的异常信息
        } finally { // 无论是否出现异常，都会执行finally中的代码
            
        }
        System.out.println("Hello World");
    }
}
```

## 人工抛出异常
- java异常对象除了在代码执行过程中出现异常时由系统自动生成外，也可以人工创建异常
    - 语法格式1：throw new 异常类名(异常信息);
    - 语法格式2：IOException e = new IOException(); throw e;
- 示例代码
```java
package test;
public class Test {
    public static void main(String[] args) {
        A a = new A();
        try { 
            a.getAge(160);
        } catch (Exception e) {
            System.out.println(e.getMessage());
        }
    }
}
class A {
    int age=10;

    public void getAge(int age) throws Exception {
        // 人工抛出异常
        if( age < 0 || age > 150) {
            throw new Exception("年龄不在0~150之间");
        } else {
            System.out.println("年龄：" + age);
        }
    }
}
```


## 使用ANSI转义码清空控制台模拟计算器每次新计算不保留上次计算结果的功能
- ANSI转义码在字符串中以“33”开头，随后是一些控制字符。[H将光标移到左上角，[2J清除屏幕。配合System.out.flush()，可以确保所有输出都被立即显示。
```java
System.out.print("33[H33[2J");
System.out.flush();
```
## `char charAt(int index)`
- 函数说明：返回字符串中指定位置的字符  
- 参数：index，要返回的字符的索引位置
- 返回字符

## List集合
- List集合的各方面描述如同python中List列表
- ArrayList用于动态数组的实现，提供了可以调整大小的数组功能，它是对List接口的实现
- 本项目中的关于List集合使用介绍  
`List<String> lst = new ArrayList<String>();`  创建List集合  
`lst.add(int index,Object element)`  添加元素  
`lst.get(int index)`  根据索引返回元素