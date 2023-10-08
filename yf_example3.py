'''yf_example3.py

This module is for the purpose of Quiz W4 Module
'''

import os
from toolkit_config import DATADIR as cfg
import yf_example2


def qan_prc_to_csv(year):
    '''
    Download qantas stock price from yfinance and export as a csv file

    Parameters
    ----------
    year : int
        Year of the data in 4 digits
    '''
    tic = 'QAN.AX'
    output_path = os.path.join(cfg, f'qan_prc_{year}.csv')
    start_dt = f'{year}-01-01'
    end_dt = f'{year}-12-31'
    df = yf_example2.yf_prc_to_csv(tic, output_path, start_dt, end_dt)


# Example
if __name__ == "__main__":
    year = 2020
    qan_prc_to_csv(year)
