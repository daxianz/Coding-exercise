import pandas as pd
#解决数据输出时列名不对齐的问题
pd.set_option('display.unicode.ambiguous_as_wide', True)
pd.set_option('display.unicode.east_asian_width', True)
df = pd.read_excel('mingribooks.xls')
df1=df[['订单付款时间','买家会员名','联系手机','买家实际支付金额']]
df1=df1.sort_values(by=['订单付款时间'])
df1 = df1.set_index('订单付款时间') # 将日期设置为索引
#获取某个区间数据
print(df1['2018-05-11':'2018-06-10'])

