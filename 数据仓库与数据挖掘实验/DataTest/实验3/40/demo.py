import seaborn as sns
import matplotlib.pyplot as plt
plt.figure(figsize=(4,3))
x=[1,2,3,4,5]
y=[10,20,30,40,50]
plt.bar(x,y)
plt.show()
sns.set_style('darkgrid')
sns.barplot(x,y)
plt.show()