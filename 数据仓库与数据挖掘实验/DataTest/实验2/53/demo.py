import matplotlib.pylab as plt
import numpy as np
import pandas as pd
index=pd.date_range('20200201','20200215')
data=[3,6,7,4,2,1,3,8,9,10,12,15,13,22,14]
s1_data=pd.Series(data,index=index)
print(s1_data)
