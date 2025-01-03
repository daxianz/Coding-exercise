from pandas import Series
#从pandas引入Series对象，就可以直接使用Series对象了，如Series([88,60,75],index=[1,2,3])
s1=Series([88,60,75],index=[1,2,3])
print(s1)
print(s1.reindex([1,2,3,4,5]))

#重新设置索引,NaN以0填充
print(s1.reindex([1,2,3,4,5],fill_value=0))





