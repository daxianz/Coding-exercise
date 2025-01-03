import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

fig = plt.figure()
axes3d = fig.add_subplot(111, projection='3d')  # 使用 add_subplot 创建3D子图
zs = [1, 5, 10, 15, 20]

for z in zs:
    x = np.arange(0, 10)
    y = np.random.randint(0, 30, size=10)
    axes3d.bar(x, y, zs=z, zdir='y', color=['r', 'green', 'yellow', 'c', 'b'], alpha=0.8)  # zdir可改为'y'或'z'以呈现不同的方向

plt.show()
