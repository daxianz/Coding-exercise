import pandas as pd
#解决数据输出时列名不对齐的问题
pd.set_option('display.unicode.east_asian_width', True)
data = [110,105,99,120,115]
index=[1,2,3,4,5]
df = pd.DataFrame(data=data,index=index,columns=['英语'])

df['升降']=df['英语']-df['英语'].shift()
print(df)
