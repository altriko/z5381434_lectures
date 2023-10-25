# |            | AUD/USD | EUR/AUD |
# |------------+---------+---------|
# | 2020-09-08 | 0.7280  | 1.6232  |
# | 2020-09-09 | 0.7209  | 1.6321  |
# | 2020-09-10 | NaN     | 1.6221  |
# | 2020-09-11 | 0.7263  | 1.6282  |
# | 2020-09-14 | 0.7281  | NaN     |
# | 2020-09-15 | 0.7285  | 1.6288  |
#
# <class 'pandas.core.frame.DataFrame'>
# Index: 6 entries, 2020-09-08 to 2020-09-15
# Data columns (total 2 columns):
#  #   Column   Non-Null Count  Dtype
# ---  ------   --------------  -----
#  0   AUD/USD  5 non-null      float64
#  1   EUR/AUD  5 non-null      float64
# dtypes: float64(2)

import pandas as pd
import numpy as np

data = {
    'AUD/USD': [ 0.7280, 0.7209, np.nan, 0.7263, 0.7281, 0.7285,],
    'EUR/AUD': [ 1.6232, 1.6321, 1.6221, 1.6282, np.nan, 1.6288,],
    }
index = [ '2020-09-08', '2020-09-09', '2020-09-10', '2020-09-11', '2020-09-14', '2020-09-15',]
df = pd.DataFrame(data, index)

new_df = df.copy()
new_df.loc['1', :] = 1

print(df.loc['AUD/USD'])

#Test changes
