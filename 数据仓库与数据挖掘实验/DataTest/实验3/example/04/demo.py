import numpy as np
import matplotlib.pyplot as plt
# 计算x,y坐标对应的高度值
def f(x, y):
    return (1-x/2+x**5+y**3) * np.exp(-x**2-y**2)
# 生成x,y的数据
n = 256
x = np.linspace(-3, 3, n)
y = np.linspace(-3, 3, n)
# 把x,y数据转换为二维数据
X, Y = np.meshgrid(x, y)
# 填充等高线
plt.contourf(X, Y, f(X, Y))
# 显示图表
plt.show()
