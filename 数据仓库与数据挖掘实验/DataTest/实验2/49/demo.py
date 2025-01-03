import pandas as pd
index = pd.date_range('02/02/2020', periods=9, freq='T')
series = pd.Series(range(9), index=index)
print(series)
print(series.resample('3T').sum())
