import pandas as pd

# 读取数据
jc_content_viewlog = pd.read_csv('../data/jc_content_viewlog.csv')

# 提取属性
website_informations = jc_content_viewlog[['content_id', 'page_path', 'username',
                                          'userid', 'date_time']]

# 删除用户ID为空的记录
website_informations = website_informations.dropna(subset=['userid'])

# 查看缺失值情况
print('缺失值情况：', website_informations.isnull().sum())
# 删除缺失值
website_informations = website_informations.dropna()
# # 转换为字符类型
# website_informations = website_informations.applymap(str)

# 构建二元矩阵
content_id = website_informations['content_id'].drop_duplicates().tolist()
userid =website_informations[['userid']].drop_duplicates()
userid = userid.iloc[:,0].tolist()
# 创建新的数据框，index为userid值，columns为content_id值
ruledata = pd.DataFrame(index=userid, columns=content_id)
# 利用for循环获得二元矩阵
for i in range(len(userid)):
    for j in range(len(content_id)):
        test_list = website_informations[(website_informations['userid']==userid[i]) &
                           (website_informations['content_id']==content_id[j])].index.tolist()
        if len(test_list) != 0:
            ruledata.iloc[i,j] = 1
        else:
            ruledata.iloc[i,j] = 0
            
# 实现关联分析
from apriori import * 
support = 0.1
confidence = 0.5
ms = "---"
result = find_rule(ruledata,support,confidence,ms)

