import pandas as pd

# 创建一个示例时间序列数据
date_rng = pd.date_range(start='2023-01-01', end='2023-01-02', freq='T')
s1 = pd.DataFrame(date_rng, columns=['date'])
s1['data'] = pd.Series(range(1, len(s1) + 1))

# 将日期列设置为索引
s1.set_index('date', inplace=True)

# 改为小写的 'h' 表示每6小时
s1_6h_asfreq = s1.resample('6h').asfreq()

# 使用 ffill() 而不是 pad()
s1_6h_pad = s1.resample('6h').ffill()

# 输出结果
print(s1_6h_asfreq)
print(s1_6h_pad)
