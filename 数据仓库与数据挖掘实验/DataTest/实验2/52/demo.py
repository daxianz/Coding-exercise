import pandas as pd
import numpy as np
rng = pd.date_range('2/2/2020',periods=12,freq='min')
s1 = pd.Series(np.arange(12),index=rng)
print(s1.resample('5min').ohlc())

