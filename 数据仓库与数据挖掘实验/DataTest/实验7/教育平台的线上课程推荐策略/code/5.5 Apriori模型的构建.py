import re
import pandas as pd
import numpy as np
from pandas.core.frame import DataFrame 

user_learn_info = pd.read_csv('../tmp/user_learn_info.csv', encoding='gbk')
learn_info = pd.read_csv('../tmp/处理后的学习详情表.csv', encoding='gbk')
login_info = pd.read_csv('../tmp/新登录详情表.csv', encoding='gbk')

# 统计用户的课程清单
user_id = learn_info[['用户账号']].drop_duplicates()
user_course = []
# 利用for循环获取用户的课程信息
for i in range(len(user_id)):
    course_id = learn_info.loc[learn_info['用户账号'] == user_id.iloc[i, 0], '课程编号'].tolist()
    user_course.append(course_id )
# 将user_course转为DataFrame，并进行转置
user_course = DataFrame(user_course).T

# 构建Apriori模型的二元矩阵
course_number = learn_info['课程编号'].drop_duplicates().tolist() 
user_id = list(user_id.iloc[:,0])
# 利用 for 循环获得二元矩阵
rule_data=[]
k = 0
for i in user_id:
    print(k)
    k+=1
    a = learn_info[learn_info['用户账号'] == i]['课程编号'].tolist()
    aa = [int(col in a) for col in course_number]
    rule_data.append(aa)
rule_data = pd.DataFrame(rule_data, index = user_id, columns = course_number)

# 调用已构建好的Apriori模型，实现关联分析
from apriori import * 
support = 0.01
confidence = 0.1
ms = "---" 
rules = find_rule(rule_data,support,confidence,ms,max_len=3)
# 将所得的关联分析结果rules，根据support进行排序
rules_results = rules.sort_values(by=['support'], axis=0, ascending=False)
# 为更好的查看关联分析结果，根据原先的分隔符号---，将关联分析结果拆分成2部分：Ihs, rhs
Ihs, rhs = [], []
for i in range(len(rules_results['rule'])):
    re_data = re.split('---', rules_results['rule'][i])
    Ihs.append(tuple(re_data[:-1]))
    rhs.append(re_data[-1])
# 设置新的分隔符号，以更明确Ihs, rhs之间的关系    
rules_results1 = pd.DataFrame([])
rules_results1['Ihs'] = Ihs
rules_results1[' '] = ['=>'] * len(Ihs)
rules_results1['rhs'] = rhs
rules_results1['support'] = rules_results['support']
rules_results1['confidence'] = rules_results['confidence']

# 以课程130为例，提取课程130的所有课程关联规则
example_rules = rules_results1[rules_results1['Ihs'] == ('课程130',)]
print(example_rules)

# 以课程130为例，整理课程130的课程关联规则、价格和受欢迎程度
course_amount = pd.value_counts(learn_info['课程编号']).reset_index()
course_amount.columns  =['课程编号', '用户数量']
# 计算课程的受欢迎程度
course_max=np.max(course_amount['用户数量'])
course_min=np.min(course_amount['用户数量'])
course_amount['受欢迎程度'] = course_amount['用户数量'].apply(lambda x : round(
    (x-course_min) / (course_max-course_min), 2))
# 提取对应的课程单价
course_money = learn_info[['课程编号', '课程单价（元）']].drop_duplicates(subset = '课程编号')
course_popularity = pd.merge(course_money, course_amount, on = '课程编号', how = 'left')
collation_relevance_rules = pd.merge(example_rules, course_popularity, how='inner',
                                     left_on='rhs', right_on='课程编号') 
collation_relevance_rules.loc[:,['Ihs', 'rhs', 'support', 'confidence', '课程单价（元）',
                                 '受欢迎程度']]
