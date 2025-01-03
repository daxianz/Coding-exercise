import pandas as pd
#解决数据输出时列名不对齐的问题
pd.set_option('display.unicode.east_asian_width', True)
df = pd.DataFrame({
    '语文':[110,105,99],
     '数学':[105,88,115],
     '英语':[109,120,130],
      '班级':'高一7班'
},index=[0,1,2])
print(df)
