# EPS.py
### The Code
To start with, there are very standard imports shown below. yfinance helps us get the stock data. matplotlib helps us plot the data into clean graphs. pandas is good for dataframes. numpy is good for numerical work. Lastly, os is needed to save the images onto my computer into a clean folder so I can upload it to GitHub.

>import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import os  # Import os module to create directories

After this, we must download the stock data for each stock, or ticker. We are only looking at the span of this year, as looking over multiple years makes it harder to view this graph. We also have 7 stocks, each with 4 earnings, so looking over multiple years becomes excessive.

>tickers = ['GOOGL', 'AAPL', 'MSFT', 'AMZN', 'NVDA', 'META', 'TSLA']
data = yf.download(tickers, start="2024-01-01", end="2024-12-31")

Now, we can calculate the daily percentage change for each stock. We use Z-Score Normalization to plot our information to adjust for wild jumps in stock prices. With normalization, it makes the data across multiple stocks easier to compare, even though there are many variables when it comes to stock.
>price_changes = data['Adj Close'].pct_change() * 100
>price_changes_standardized = (price_changes - price_changes.mean()) / price_changes.std()

Now, we can collect the earnings dates for each stock. I did this manually since it seemed excessive to write code to do so. I couldn't find a standardized place to find this information, but since this is a ballpark estimation, I still think that these dates are relevant enough to use. 
>earnings_dates = {
    'GOOGL': ['2024-01-31', '2024-04-30', '2024-07-31', '2024-10-30'],
    'AAPL': ['2024-01-28', '2024-04-30', '2024-07-30', '2024-10-28'],
    'MSFT': ['2024-01-25', '2024-04-29', '2024-07-30', '2024-10-25'],
    'AMZN': ['2024-02-01', '2024-04-30', '2024-07-31', '2024-10-31'],
    'NVDA': ['2024-02-15', '2024-04-25', '2024-07-25', '2024-10-25'],
    'META': ['2024-02-01', '2024-05-01', '2024-07-31', '2024-10-31'],
    'TSLA': ['2024-02-01', '2024-04-30', '2024-07-31', '2024-10-31']

 I also wanted to color-coordinate the earnings, so I set up a dictionary that can be easily called from a for loop.
>colors = {'1': 'red', '2': 'orange', '3': 'green', '4': 'blue'}

For continuity, I then found the minimum and maximum changes amongst all stocks so that I can have a standardized y-axis, which would allow for ease of comparison between multiple graphs.
>y_min = price_changes_standardized.min().min()
y_max = price_changes_standardized.max().max()

After that, the final part of the setup is the create the folder in which I will be storing all of my plots in. My GitHub has been having some issues, so I have to do this process manually, and since there will be many plots, it seems best to do this.
>save_dir = 'saved_plots'
os.makedirs(save_dir, exist_ok=True)

We then loop through each stock and plot the baseline information. Usually, a gray line is ideal, but after looking at the graphs, I needed more contrast between the line and the colors, so I opted for black.
>for ticker in tickers:
   -->plt.figure(figsize=(10, 6))
    -->plt.plot(price_changes_standardized[ticker], label=ticker, color='black')

Going back on the original point, I wanted each earnings to have a range of viewed information, specifically one week prior and one week after the earnings are announced. The below code sets up vertical bars to delineate this information.
> -->for i, earnings_date in enumerate(earnings_dates[ticker]):
        -->-->earnings_date = pd.to_datetime(earnings_date)
        -->-->quarter = f'{i+1}' if i == 0 else f'{i+1}' if i == 1 else f'{i+1}' if i == 2 else f'{i+1}'
        -->-->report_color = colors[quarter]
        -->-->darker_color = plt.cm.colors.to_rgba(report_color, alpha=0.85)
        -->-->lighter_color = plt.cm.colors.to_rgba(report_color, alpha=0.15)
        -->-->plt.axvspan(earnings_date - pd.Timedelta(days=7), earnings_date, color=darker_color, alpha=0.7)
        -->-->plt.axvline(earnings_date, color=report_color, linestyle='--')
        -->-->plt.axvspan(earnings_date, earnings_date + pd.Timedelta(days=7), color=lighter_color, alpha=0.5)

Now that all of the information is plotted, we have to make the graph look presentable. Below is the information to set up the graphs as is. We use the limits from earlier to set up that standardized y-axis amongst all graphs.
>plt.title(f'{ticker} Standardized Stock Price Change with Earnings Reports')
    plt.xlabel('Date')
    plt.ylabel('Standardized Price Change (Z-score)')
    plt.legend()
    plt.grid(True)
    plt.xticks(rotation=45)
	plt.ylim(y_min, y_max)

### The Analysis
For some stocks, there seems to be a stronger correlation. For Tesla, TSLA, there tends to be a lot of action a week prior to earnings being released. This makes sense, since electric vehicles are still seen as an innovative venture, so their earnings are strongly correlated to demand. On the contrary, Microsoft does not have a lot of sway with their earnings, and that makes sense with the public's views on Microsoft as a company. Earnings are less indicative of their success since they have been a pioneer in tech for a while, and they do not need to innovate constantly for them to receive positive returns.

If we analyze Amazon, we can see that the week prior does not have any substantive information, but as soon as earnings are announced, major swings happen in the stock. They seem to stabilize shortly after that, which could indicate that the concept of day-trading with Amazon may be beneficial.

Holistically, I think it is safe to assume that there is a correlation between the innovative tendencies of a company and the impacts their quarterly earnings report have on their stock. Tesla, Google, and Amazon tend to have sharper changes in their stocks while Microsoft and Apple don't show that correlation. Meta and Nvidia have inconclusive data, and it is hard to conclude anything.
