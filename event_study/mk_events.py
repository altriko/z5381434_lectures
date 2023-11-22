""" mk_events.py

Utilities to create events from recommendations
"""
import pandas as pd
import event_study.config as cfg


#   Functions to process recommendations into events
def mk_event_df(tic):
    """ Subsets and processes recommendations given a ticker and return a data
    frame with all events in the sample.

    Parameters
    ----------
    tic : str
        Ticker

    Returns
    -------
    pandas dataframe

        The columns are:
        * event_date : string
            Date string with format 'YYYY-MM-DD'
        * firm : string
            Name of the firm (upper case)
        * event_type : string
            Either "downgrade" or "upgrade"

        index: integer
            Index named 'event_id' starting at 1

    Notes
    -----
    This function will perform the following actions:

    1. Read the appropriate CSV file with recommendations into a data frame
    2. Create variables identifying the firm and the event date
    3. Deal with multiple recommendations
    4. Create a table with all relevant events

    """
    # Step 1. Read the appropriate CSV file with recommendations into a dataframe
    # a. Read source file, set column "Date" as a DatetimeIndex
    pth = cfg.csv_locs(tic)["rec_csv"]
    df = pd.read_csv(pth, index_col='Date', parse_dates=['Date'])

    #b. Standardize the column and only keep the important col
    cols = ['firm', 'action']
    df = cfg.standardise_colnames(df)[cols]


    #Step 2. Create variables identifying the firm and the event date
    #c. CAPS all the firm name
    df.loc[:,'firm'] = df.loc[:,'firm'].str.upper()

    # d. create event_date column
    df.loc[:, 'event_date'] = df.index.strftime('%Y-%m-%d')

    #Step 3. Deal with multiple recommendations
    df.sort_index(inplace = True)
    groups = df.groupby(["event_date", "firm"])
    # we will use the last observation from the datetimeindex, then we will
    # reset the index to make index -> columns
    df = groups.last().reset_index()


    #Step 4. Create a table with all relevant events
    cond = df.loc[:,'action'].str.contains('up|down')  #will only pick up or down
    df = df.loc[cond]

    #convert to upgrade / downgrade
    def _mk_et(value):
        ''' Converts the string 'value' into:
            - "down" -> "downgrade"
            - "up" -> "upgrade"
        and raise exception if not either of two
        '''
        if value == 'down':
            return 'downgrade'
        elif value == 'up':
            return 'upgrade'
        else:
            raise Exception(f"Unknown value for column 'action: {value}")

    df.loc[:,'event_type'] = df['action'].apply(_mk_et)

    #Change the integer to start with 1 instead of 0
    df.reset_index(inplace=True)
    df.index += 1
    df.index.name = "event_id"

    #Final step: reogranize the columns
    cols = ['firm', 'event_date', 'event_type']
    df = df.loc[:,cols]

    return df





if __name__ == "__main__":
    tic = 'TSLA'
    df = mk_event_df(tic)
    print(df)
    df.info()
    # cond = df.firm.str.contains('DEUTSCHE')
    # print(df.loc[cond])