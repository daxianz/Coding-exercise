import matplotlib.pyplot as plt
#第1个子图表-折线图
plt.subplot(2,2,1)
plt.plot([1, 2, 3, 4,5])
#第2个子图表-散点图
plt.subplot(2,2,2)
plt.plot([1, 2, 3, 4,5], [2, 5, 8, 12,18], 'ro')
#第3个子图表-柱形图
plt.subplot(2,1,2)
x=[1,2,3,4,5,6]
height=[10,20,30,40,50,60]
plt.bar(x,height)
plt.show()

