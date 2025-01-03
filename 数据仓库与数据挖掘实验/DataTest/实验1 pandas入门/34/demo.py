import pandas as pd
#解决数据输出时列名不对齐的问题
pd.set_option('display.unicode.east_asian_width', True)
data = [[110,105,99],[105,88,115],[109,120,130],[112,115,140]]
name = ['明日','七月流火','高袁圆','二月二']
columns = ['语文','数学','英语']
df = pd.DataFrame(data=data, index=name, columns=columns)
print('原数据：')
print(df)

#修改整行数据
df.loc['明日']=[120,115,109]
print('修改后的数据：')
print(df)

#各科成绩均加10分
df.loc['明日']=df.loc['明日']+10


#修改整列数据
df.loc[:,'语文']=[115,108,112,118]


#修改某一数据
df.loc['明日','语文']=115


#使用iloc方法修改数据
df.iloc[0,0]=115                   #修改某一数据
df.iloc[:,0]=[115,108,112,118]    #修改整列数据
df.iloc[0,:]=[120,115,109]        #修改整行数据

