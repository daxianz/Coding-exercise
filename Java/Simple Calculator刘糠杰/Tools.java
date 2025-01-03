public class Tools {
    // 循环打印重复字符
    public static final void Print(String str,int num) {
        for(int i = 0;i < num; i++) {
            System.out.print(str);
        }
    }
    // 清空控制台输出
    public static final void Clear() {
        System.out.print("\033[H\033[2J");
	    System.out.flush();
    }
}

