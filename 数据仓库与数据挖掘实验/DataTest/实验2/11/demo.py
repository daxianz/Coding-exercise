import pandas as pd
df = pd.DataFrame({'A': [1, 2],
                   'B': [pd.Timestamp('2019'),
                         pd.Timestamp('2020')],
                   'C': [pd.Timedelta('1 days'),
                         pd.Timedelta('2 days')]})
print(df.quantile(0.5, numeric_only=False))
