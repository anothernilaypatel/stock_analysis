# -*- coding: utf-8 -*-
"""
Created on Sun Dec  8 18:03:27 2024

@author: Nilay Patel
"""

import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import os  # Import os module to create directories

# Define the tickers for the Magnificent 7 tech stocks
tickers = ['GOOGL', 'AAPL', 'MSFT', 'AMZN', 'NVDA', 'META', 'TSLA']

# Download stock data for the year
data = yf.download(tickers, start="2024-01-01", end="2024-12-31")

# Calculate the daily percentage change for each stock
price_changes = data['Adj Close'].pct_change() * 100

# Standardize the daily percentage change using Z-score normalization
price_changes_standardized = (price_changes - price_changes.mean()) / price_changes.std()

# Define earnings dates (example dates for 2024, adjust based on actual earnings release dates)
earnings_dates = {
    'GOOGL': ['2024-01-31', '2024-04-30', '2024-07-31', '2024-10-30'],
    'AAPL': ['2024-01-28', '2024-04-30', '2024-07-30', '2024-10-28'],
    'MSFT': ['2024-01-25', '2024-04-29', '2024-07-30', '2024-10-25'],
    'AMZN': ['2024-02-01', '2024-04-30', '2024-07-31', '2024-10-31'],
    'NVDA': ['2024-02-15', '2024-04-25', '2024-07-25', '2024-10-25'],
    'META': ['2024-02-01', '2024-05-01', '2024-07-31', '2024-10-31'],
    'TSLA': ['2024-02-01', '2024-04-30', '2024-07-31', '2024-10-31']
}

# Color map for earnings reports (red, orange, green, blue)
colors = {'1': 'red', '2': 'orange', '3': 'green', '4': 'blue'}

# Find the global min and max for all stocks to set the y-axis range
y_min = price_changes_standardized.min().min()  # Minimum value across all stocks
y_max = price_changes_standardized.max().max()  # Maximum value across all stocks

# Create a directory to save the plots
save_dir = 'saved_plots'
os.makedirs(save_dir, exist_ok=True)  # Create directory if it doesn't exist

# Loop through each stock and create its own plot
for ticker in tickers:
    plt.figure(figsize=(10, 6))

    # Plot the standardized stock price change
    plt.plot(price_changes_standardized[ticker], label=ticker, color='black')

    # Mark earnings report dates and surrounding weeks
    for i, earnings_date in enumerate(earnings_dates[ticker]):
        # Convert string to datetime
        earnings_date = pd.to_datetime(earnings_date)
        
        # Determine the color for earnings and surrounding weeks
        quarter = f'{i+1}' if i == 0 else f'{i+1}' if i == 1 else f'{i+1}' if i == 2 else f'{i+1}'
        report_color = colors[quarter]
        darker_color = plt.cm.colors.to_rgba(report_color, alpha=0.85)
        lighter_color = plt.cm.colors.to_rgba(report_color, alpha=0.15)

        # Mark the week before earnings (darker color)
        plt.axvspan(earnings_date - pd.Timedelta(days=7), earnings_date, color=darker_color, alpha=0.7)
        
        # Mark the earnings day itself (default color)
        plt.axvline(earnings_date, color=report_color, linestyle='--')
        
        # Mark the week after earnings (lighter color)
        plt.axvspan(earnings_date, earnings_date + pd.Timedelta(days=7), color=lighter_color, alpha=0.5)

    # Customize the plot for each stock
    plt.title(f'{ticker} Standardized Stock Price Change with Earnings Reports')
    plt.xlabel('Date')
    plt.ylabel('Standardized Price Change (Z-score)')
    plt.legend()
    plt.grid(True)
    plt.xticks(rotation=45)

    # Set the same y-axis limits for all plots
    plt.ylim(y_min, y_max)

    # Save the plot to the specified directory
    plot_filename = os.path.join(save_dir, f'{ticker}_standardized_plot.png')
    plt.tight_layout()
    plt.savefig(plot_filename)  # Save the figure as a PNG file
    
    # Optionally, show the plot (comment out if not needed)
    plt.show()

