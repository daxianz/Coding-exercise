import pandas as pd
import glob
filearray=[]
filelocation=glob.glob(r'./aa/*.xlsx')  #指定目录下的所有Excel文件
#遍历指定目录
for filename in filelocation:
    filearray.append(filename)
    print(filename)
res=pd.read_excel(filearray[0])   #读取第一个Excel文件
#顺序读取Excel文件并进行合并
for i in range(1,len(filearray)):
    A=pd.read_excel(filearray[i])
    res=pd.concat([res,A],ignore_index=True,sort=False)
print(res.index)
#写入Excel文件，并保存
writer = pd.ExcelWriter('all.xlsx')
res.to_excel(writer,'sheet1')
writer._save()

