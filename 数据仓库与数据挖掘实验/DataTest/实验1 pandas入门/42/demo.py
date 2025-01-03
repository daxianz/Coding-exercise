from pandas import Series
#从pandas引入Series对象，就可以直接使用Series对象了，如Series([88,60,75],index=[1,2,3])
s1=Series([88,60,75],index=[1,2,3])
print(s1)

print(s1.reindex([1,2,3,4,5],method='ffill'))   #向前填充
print(s1.reindex([1,2,3,4,5],method='bfill'))   #向后填充


