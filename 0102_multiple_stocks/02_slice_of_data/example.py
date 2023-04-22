import os
import pandas as pd
import matplotlib.pyplot as plt

def symbol_to_path(symbol, base_dir='data'):
    # Return CSV file path given ticker symbol
    return os.path.join(base_dir, "{}.csv".format(str(symbol)))

def get_data(symbols, dates):
    # Create empty dataframe
    df = pd.DataFrame(index=dates)

    # Read SPY data into temporary dataframe
    dfSPY = pd.read_csv("SPY.csv", index_col="Date",
                        parse_dates=True, usecols=['Date', 'Adj Close'],
                        na_values=['nan'])
    
    # Rename 'Adj Close' colum to 'SPY' to prevent clash
    dfSPY = dfSPY.rename(columns={'Adj Close':'SPY'})
    
    # Join the two dataframes using DataFrame.join(), with how = 'inner'
    df.join(dfSPY, how='inner')

    # Read in more stocks
    for symbol in symbols:
        df_temp = pd.read_csv("data/{}.csv".format(symbol), index_col='Date',
                              parse_dates= True, usecols=['Date', 'Adj Close'], na_values=['nan'])
        # Rename to prevent clash
        df_temp = df_temp.rename(columns={'Adj Close': symbol})
        df = df.join(df_temp, how='inner')

        if symbol == 'SPY':
            df = df.dropna(subset=['SPY'])

    return df

def plot_data(df, title="Stock Prices"):
    ax = df.plot(title= title, fontsize=2)
    ax.set_xlabel("Date")
    ax.set_ylabel("Price")
    plt.show()

def test_run():
    # Define a date range
    dates = pd.date_range('2010-01-01', '2010-12-31')

    # Choose stock symbols to read
    symbols = ['GOOG', 'IBM', 'GLD']

    # Get stock data
    df = get_data(symbols, dates)

    # Slice by row range (dates)
    print( df.ix['2010-01-01': '2010-01-31'])
    # Slice by column (symbols)
    print(df['GOOG'])
    print(df[['IBM', 'GLD']])
    # Slice by row and column
    print(df.ix['2010-03-10':'2010-03-15', ['SPY','IBM']])

if __name__ == "__main__":
    test_run()



