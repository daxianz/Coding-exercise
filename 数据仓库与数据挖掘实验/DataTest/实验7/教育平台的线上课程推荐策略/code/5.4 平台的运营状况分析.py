import re
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from chinese_calendar import is_workday

plt.rcParams['font.family'] = ['SimHei']  # 或其他中文字体
plt.rcParams['axes.unicode_minus'] = False

user_info = pd.read_csv('../tmp/处理后的用户信息表.csv', encoding='gbk')
learn_info = pd.read_csv('../tmp/处理后的学习详情表.csv', encoding='gbk')
login_info = pd.read_csv('../data/登录详情表.csv', encoding='gbk')

# 合并用户信息表和登录详情表
user_learn_info = pd.merge(user_info, login_info, on='用户账号')
# 自定义times函数获取年月日，以便于后续的时间划分
def times(value):
    time_data = pd.to_datetime([re.split(' ', i)[0] for i in value])
    return time_data
   
user_learn_info['注册时间年月日'] = times(user_learn_info['注册时间'])
user_learn_info['登录时间年月日'] = times(user_learn_info['登录时间'])
# 提取注册时间年月日的唯一值，以便于后续统计不同日期的用户人数
only_enroll_time = list(user_learn_info['注册时间年月日'].unique())
# 计算日新增用户数、次日留存用户数、第7日留存用户数和第30日留存用户数量
column = ['日新增用户数', '次日留存用户数', '第7日留存用户数', '第30日留存用户数']
retention_data = pd.DataFrame(data=None, columns=column, index=only_enroll_time)
for i in only_enroll_time:
    time1 = user_learn_info.loc[user_learn_info['注册时间年月日'] == i]
    retention_data.loc[i, '日新增用户数'] = time1['用户账号'].nunique()  # 统计每日新增用户
    k = 1
    for j in [1, 6, 29]:  # 统计次日、，第7日、，第30日的留存用户
        p = i + pd.Timedelta(days = j)
        time2 = time1.loc[time1['登录时间年月日'] == p]
        retention_data.loc[i,column[k]] = time2['用户账号'].nunique() 
        k += 1

# 自定义retention_amount函数，绘制新增用户及留存用户数量折线图
def retention_amount(a, b):
    plt.subplot(2, 2, a)
    plt.xlabel('时间', fontsize=15)
    plt.ylabel('用户数量', fontsize=15)
    plt.title(b, fontsize=15)
    plt.plot(only_enroll_time, retention_data[b], linewidth=1)
    plt.xticks(rotation=0)
    plt.tick_params(labelsize=15)  # 设置坐标轴字体大小
    plt.locator_params(axis='y', nbins=20)  # 设置Y轴显示刻度数
# 实例化绘图参数进行绘图
plt.figure(figsize=(15, 10))
for i in range(1, 5):
    retention_amount(i, retention_data.columns[i - 1])
plt.tight_layout()  # 设置默认的间距
plt.show()


# 自定义rate_value函数，计算次日、第7日和第30日留存率
retention_rate = pd.DataFrame([])
def rate_value(values):
    rate = values / retention_data['日新增用户数'] * 100
    return rate
# 调用自定义函数，计算对应的留存率
retention_rate['次日留存率(%)'] = rate_value(retention_data['次日留存用户数'])
retention_rate['第7日留存率(%)'] = rate_value(retention_data['第7日留存用户数'])
retention_rate['第30日留存率(%)'] = rate_value(retention_data['第30日留存用户数'])

# 自定义retention_rate函数，绘制次日、第7日和第30日留存率折线图
def plot_retention_rate(a, b):
    plt.subplot(3, 1, a)
    plt.xlabel('时间', fontsize=10)
    plt.ylabel('留存率（%）', fontsize=10)
    plt.title(b, fontsize=10)
    plt.plot(only_enroll_time, retention_rate[b], linewidth=0.6)
    plt.xticks(rotation=0)
    plt.locator_params(axis='y', nbins=10)  # 设置Y轴显示刻度数

# 设置画布
plt.figure(figsize=(6, 6.5))
for i in range(1, 4):
    plot_retention_rate(i, retention_rate.columns[i - 1])
plt.tight_layout()  # 设置默认的间距
plt.show()


# 划分工作日
login_info['登录时间'] = pd.to_datetime(login_info['登录时间'])
login_info['工作日'] = login_info['登录时间'].apply(lambda x : '是' if is_workday(x) else '否')
# 划分时间段
time_divide = ['0:00-2:00', '2:00-4:00', '4:00-6:00', '6:00-8:00', '8:00-10:00', '10:00-12:00',
      '12:00-14:00', '14:00-16:00', '16:00-18:00', '18:00-20:00', '20:00-22:00', '22:00-24:00']
login_info['时间段'] = login_info['登录时间'].dt.hour.apply(lambda x: time_divide[int(np.floor(x / 2))])
# 添加时间类别属性，将各时间段分成12个数值型的类别，方便后续的绘图操作
login_info['时间类别'] = login_info['登录时间'].dt.hour.apply(lambda x: range(1, 13)[int(np.floor(x / 2))])

time_count = login_info.groupby(['工作日', '时间段', '时间类别'])['用户账号'].count().reset_index()
time_count.columns = ['工作日', '时间段', '时间类别', '用户登录次数']
canvas = plt.figure(figsize=(7, 7))
# 自定义time_amount函数，绘制工作日与非工作日各时间段用户登录次数柱状图
def time_amount(a, b, c):
    ax = canvas.add_subplot(2, 1, a)
    week_day = time_count[time_count['工作日'] == b].sort_values(by='时间类别')
    plt.bar(week_day['时间段'], week_day['用户登录次数'])
    plt.title(c)
    plt.xlabel('时间段')
    plt.ylabel('登录次数')
    plt.xticks(rotation=45)

time_amount(1, '是', '工作日各时间段用户登录次数柱状图')
time_amount(2, '否', '非工作日各时间段用户登录次数柱状图')
plt.tight_layout()  # 设置默认的间距
plt.show()


# 统计每门个课程的用户人数
course_amount = pd.value_counts(learn_info['课程编号']).reset_index()
course_amount.columns = ['课程编号', '用户数量']
# 计算课程的受欢迎程度
course_max = np.max(course_amount['用户数量'])
course_min = np.min(course_amount['用户数量'])
course_amount['受欢迎程度'] = course_amount['用户数量'].apply(lambda x : round(
    (x-course_min) / (course_max-course_min), 2))
# 提取对应的课程单价
course_money = learn_info[['课程编号', '课程单价（元）']].drop_duplicates(subset='课程编号')
course_popularity = pd.merge(course_money, course_amount, on='课程编号', how='left')

# 绘制排名前10名的课程受欢迎程度柱状图
courses = course_popularity.sort_values(by='受欢迎程度', ascending=False)[:10]
plt.figure(figsize=(6.5, 5))
plt.bar(courses['课程编号'], courses['受欢迎程度'])
plt.title('排名前10的课程受欢迎程度')
plt.xlabel('课程编号')
plt.ylabel('受欢迎程度')
plt.show()


# 写出数据
user_learn_info.to_csv('../tmp/user_learn_info.csv', index=False, encoding='gbk')
login_info.to_csv('../tmp/新登录详情表.csv', index=False, encoding='gbk')
