import pandas as pd
import matplotlib.pyplot as plt

def plot_data(df, title='Stock prices'):
    """ Plot stock prices with a custom title and meaningul axis labels """
    ax = df.plot(title=title, fontsize=12)
    ax.set_xlabel("Date")
    ax.set_ylabel("Price")
    plt.show()

def get_data(symbols, dates):
    # Create empty dataframe
    df = pd.DataFrame(index=dates)

    # Read SPY data into temporary dataframe
    dfSPY = pd.read_csv("data/VOO.csv", index_col="Date",
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

        # Drop dates SPY did not trade
        if symbol == 'SPY':
            df = df.dropna(subset=['SPY'])

    return df

def test_run():
    # Read data
    dates = pd.date_range('2012-01-01', '2012-12-31')
    symbols = ['SPY']
    df = get_data(symbols, dates)

    # Plot SPY data, retain matplotlib axis object
    ax = df['SPY'].plot(title='SPY rolling stats', label='SPY')

    # Compute rolling mean using a 20-day window
    rm_SPY = df['SPY'].rolling(window=10).mean()

    # Add rolling mean to same plot
    rm_SPY.plot(label='Rolling mean', ax=ax)

    # Add axis labels and legend
    ax.set_xlabel('Date')
    ax.set_ylabel('Price')
    ax.legend(loc='upper left')
    plt.show()

if __name__ == "__main__":
    test_run()
    