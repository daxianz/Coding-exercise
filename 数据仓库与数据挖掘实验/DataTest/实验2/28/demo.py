import pandas as pd
#解决数据输出时列名不对齐的问题
pd.set_option('display.unicode.east_asian_width', True)
df = pd.DataFrame({'a':[1,2,3,4,5], 'b':[(1,2), (3,4),(5,6),(7,8),(9,10)]})
print(df)
df[['b1', 'b2']] = df['b'].apply(pd.Series)
# #或者
# df= df.join(df['b'].apply(pd.Series))
print(df)
