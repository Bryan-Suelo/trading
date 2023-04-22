import pandas as pd

def get_data(symbols, dates):
    # Create empty dataframe
    df1 = pd.DataFrame(index=dates)

    # Read SPY data into temporary dataframe
    dfSPY = pd.read_csv("SPY.csv", index_col="Date",
                        parse_dates=True, usecols=['Date', 'Adj Close'],
                        na_values=['nan'])
    
    # Rename 'Adj Close' colum to 'SPY' to prevent clash
    dfSPY = dfSPY.rename(columns={'Adj Close':'SPY'})
    
    # Join the two dataframes using DataFrame.join(), with how = 'inner'
    df1.join(dfSPY, how='inner')

    # Read in more stocks
    for symbol in symbols:
        df_temp = pd.read_csv("data/{}.csv".format(symbol), index_col='Date',
                              parse_dates= True, usecols=['Date', 'Adj Close'], 
                              na_values=['nan'])
        # Rename to prevent clash
        df_temp = df_temp.rename(columns={'Adj Close': symbol})
        df1 = df1.join(df_temp, how='inner')

        if symbol == 'SPY':
            df1 = df1.dropna(subset=['SPY'])
            
    return df1
    
    print(df1)
def test_run():
    # Define a date range
    dates = pd.date_range('2010-01-01', '2010-12-31')

    # Choose stock symbols to read
    symbols = ['GOOG', 'IBM', 'GLD']

    # Get stock data
    df = get_data(symbols, dates)

    # Slice by row range (dates)
    # Using DataFrame.ix[] selector
    print( df.ix['2010-01-01': '2010-01-31'])



