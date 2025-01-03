# 5.3数据探索
# 导入模块
import pandas as pd
import matplotlib.pyplot as plt

# 读取数据
user_info = pd.read_csv('../data/用户信息表.csv', encoding='gbk')
learn_info = pd.read_csv('../data/学习详情表.csv', encoding='gbk')
login_info = pd.read_csv('../data/登录详情表.csv', encoding='gbk')

# 自定义descr函数，对数据（用户信息表+学习详情表+登录详情表）进行描述性统计分析
def descr(data):
    describe_data = pd.DataFrame(data.describe()).round(2).T  # 描述性统计分析
    # 重命名表头
    if data is login_info:
        describe_data.columns = ['数据总量', '唯一值量', '频数最高的值', '频数最高值的总量']
    else:
        describe_data.columns = ['数据总量', '均值', '标准差', '最小值', '1/4分位数',
                                 '中位数', '3/4分位数', '最大值']
    print(describe_data)
# 输出结果
descr(user_info); descr(learn_info); descr(login_info)


# 自定义lack函数，查看整体数据中的缺失值及重复值
def lack(value):
    print('各属性缺失值占比为(%)：\n', 100*(value.isnull().sum()/len(value)))
    print('重复值个数为：\n', value.duplicated().sum())
# 输出结果
lack(user_info); lack(learn_info); lack(login_info)


# 查看用户信息表中的用户账号属性的重复情况
print(user_info['用户账号'].duplicated().sum())


# 将课程单价进行划分
label = ('0元', '(0, 200]元', '(200, 400]元', '(400, 600]元', '(600, 800]元', '(800, 1000]元', '1000元以上')
learn_info_cut = pd.cut(learn_info['课程单价（元）'], [-1, 0, 200, 400, 600, 800, 1000, 3000], labels=label)
learn_info_count = learn_info_cut.value_counts(sort=False)
# 绘制各价格区间的用户人数柱状图
plt.rcParams['font.sans-serif'] = ['SimHei']  # 设置中文显示
plt.rcParams['axes.unicode_minus'] = False
plt.figure(figsize=(6.5, 5))
plt.xticks(rotation=45)
plt.xlabel('价格')
plt.ylabel('用户人数')
plt.title('各价格区间的用户人数')
plt.bar(learn_info_count.index, learn_info_count.values)
plt.show()



# 5.3数据预处理
# 删除缺失值
user_info = user_info.dropna()  # 用户信息表
learn_info = learn_info.dropna()  # 学习详情表

# 删除重复值
user_info = user_info.drop_duplicates(keep='first')  # 删除数据中的重复值
user_info = user_info.drop_duplicates(subset=['用户账号'], keep='last')  # 删除用户账号属性中的重复值

# 替换异常值
# 将最近登录时间为“--”的数值，用对应的注册时间进行替换
user_info.loc[user_info['最近访问时间'] == '--', '最近访问时间'] = user_info['注册时间']
# 写出预处理后的数据
user_info.to_csv('../tmp/处理后的用户信息表.csv', index=False, encoding='gbk')
learn_info.to_csv('../tmp/处理后的学习详情表.csv', index=False, encoding='gbk')
