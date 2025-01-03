import pandas as pd
df = pd.read_excel('fl4.xls')
df1=df[['label1','label2']].head()
tuples = [tuple(x) for x in df1.values]
for t in tuples:
    print(t)

