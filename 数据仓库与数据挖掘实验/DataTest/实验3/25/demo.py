import matplotlib.pyplot as plt
x = [1,2,3,4,5]
y1 =[6,9,5,8,4]
y2 = [3,2,5,4,3]
y3 =[8,7,8,4,3]
y4 = [7,4,6,7,12]
plt.stackplot(x, y1,y2,y3,y4, colors=['g','c','r','b'])
plt.show()