# import pandas as pd
#
# # Part (a)
# # Create a pandas series called series_abc with
# # index ['a', 'b', 'c'] and values [1, 2, 3]
# series_abc = pd.Series(data = [1, 2, 3], index = ['a', 'b', 'c'])
#
# # Part (b)
# # Given the stock price-date dictionary prc_date
# # listed below, create a pandas series series_stk
# # with the dates as indices and the prices as values.
# prc_date = {
#     7.1600: '2020-01-02',
#     7.1900: '2020-01-03',
#     7.0000: '2020-01-06',
#     7.1000: '2020-01-07',
#     6.8600: '2020-01-08',
#     6.9500: '2020-01-09',
#     7.0000: '2020-01-10',
#     7.0200: '2020-01-13',
#     7.1100: '2020-01-14',
#     7.0400: '2020-01-15',
#     }
# series_stk = pd.Series(index = prc_date.values(), data = prc_date.keys())
#
# # Part c
# # Given the dictionary
# dic = {i:i+1 for i in range(10000)}
# # create a Pandas series called series_ones
# # with indices from 0 through 9999 and with
# # all values equal to 1.
# # Do not use a secondary dictionary to create the series in Pandas.
# # Instead, specify the data and index arguments directly.
# # print(dic)
# series_ones = pd.Series(data=1, index=dic.keys())
# print(series_ones)
#

# #SLIDE 4
# import pandas as pd
# import numpy as np
# # from unanswered import *
#
# aud_usd_lst = [
#     ('2020-09-08', 0.7280),
#     ('2020-09-09', 0.7209),
#     ('2020-09-11', 0.7263),
#     ('2020-09-14', 0.7281),
#     ('2020-09-15', 0.7285),
#     ]
#
# eur_aud_lst = [
#     ('2020-09-08',  1.6232),
#     ('2020-09-09',  1.6321),
#     ('2020-09-10',  1.6221),
#     ('2020-09-11',  1.6282),
#     ('2020-09-15',  1.6288),
#     ]
#
# # Replace unanswered with your solution.
# aud_usd_series = pd.Series(data = {date: price for date, price in aud_usd_lst})
# eur_aud_series = pd.Series(data = {date: price for date, price in eur_aud_lst})
# df = pd.concat([aud_usd_series, eur_aud_series], axis = 1)
# df.columns = ["AUD/USD", "EUR/AUD"]
#
# print(aud_usd_series)
# print(eur_aud_series)
# # print(date_new)
# print(df)

# SLIDE 6
import pandas as pd
import numpy as np

# Write this function
def mk_df(date_info, aud_usd_info, eur_aud_info):
    """ Combines the information from different sources to produce a dataframe
    with dates row labels. Row labels must be sorted

    Parameters
    ----------
    date_info : list
        date_info = [(row_id, date)]

    aud_usd_info : list
        aud_usd_info = [(row_id, aud/usd)]


    eur_aud_info : list
        eur_aud_info = [(row_id, eur/aud)]

    Returns
    -------
    df
    """
    date_info_series = pd.Series(data = {row: date for row, date in date_info}).sort_values()
    aud_usd_info_series = pd.Series(data = {row: price for row, price in aud_usd_info})
    eur_aud_info_series = pd.Series(data = {row: price for row, price in eur_aud_info})
    print("DIVIDER")
    print(date_info_series)
    print(aud_usd_info_series)
    print(eur_aud_info_series)
    print("DIVIDER")

    df = pd.concat([date_info_series, aud_usd_info_series, eur_aud_info_series], axis =1)
    df.columns = ["Date", "AUD/USD", "EUR/AUD"]
    # df.reset_index(inplace=True)
    df.set_index("Date", inplace=True, drop=True)
    return df


# Sample data for you to develop your function
# date_info = [(row_id, date)]
date_info = [
    (11 , '2020-09-08'),
    (70 , '2020-09-09'),
    (99 , '2020-09-10'),
    (4  , '2020-09-11'),
    (7  , '2020-09-14'),
    (100, '2020-09-15'),
    ]

# aud_usd_info = [(row_id, aud/usd)]
aud_usd_info = [
    (70 ,  0.7209),
    (4  ,  0.7263),
    (11 ,  0.7280),
    (7  ,  0.7281),
    (100,  0.7285),
]


# eur_aud_info = [(row_id, eur/aud)]
eur_aud_info = [
    (70 ,  1.6321),
    (4  ,  1.6282),
    (99 ,  1.6221),
    (100,  1.6288),
    (11 ,  1.6232),
    ]

df = mk_df(date_info, aud_usd_info, eur_aud_info)
print(df)
