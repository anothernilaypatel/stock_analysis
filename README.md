# The Correlation Between Quarterly Earnings to the Magnificent 7 Tech Stocks
(COMP3125 Individual Project)
 

Nilay Patel 
B.S. in Computer Science at Wentworth Institute of Technology 
 
 
 
Abstract—This report approaches the age old question of if quarterly earnings truly has an impact on the stock market. This aims to analyze the Magnificent 7 tech stocks, which are Apple, Amazon, Google, Microsoft, Meta, Nvidia, and Tesla. The goal is to see if a correlation does exist.
Keywords—stocks, data science, quarterly earnings

I.	INTRODUCTION
When new investors approach the stock market, a commonly displayed metric are the quarterly earnings of a specific stock and when their earnings will be reported. At first, this is a daunting metric to consider, as it may or may not have a correlation, but it is hard to verify this. It is also widely used, and trading apps like Robinhood have it displayed on the description page while other indicators are in the Advanced section. Seeing how broad the implications quarterly earnings are without any actual guidance provided is the key reason that to researching this.

II.	SELECTION OF DATA
A.	Source of Dataset
 The main data source that is being used is yfinance, a commonly used Python library that contains information about different stocks and their trading information. Yfinance is easy to use, contains a wide range of stock data, and open-source, which makes it a staple when doing financial analysis.

B.	Character of the datasets
The downloaded stock data is only the candlestick information for that stock. This means that, for each day from January 1, 2024 to December 8, 2024, the opening, closing, high, and low points of the stock are recorded. The volume, or the capacity of the market, is also downloaded, but that isn't as pertinent to use for this report. Each row is a new day in this year. Since yfinance is widely used, there isn't any cleaning that needs to be done. A simple script can be done to verify that all of the values are not empty.

III.	METHODS
A.	Z-Score
The method used is not complicated. The key comparison that is needed is to compare how a stock changes during periods of quarterly earnings. Since there is not a defined period of what days are and are not affected by quarterly earnings, the assumption of one week before and after has been made. Also, for consistency amongst all graphs, there will be a Z-Score Normalization applied to each stock. This helps with contextualizing changes over a larger span of time, but are more sensitive to outliers, which will be seen in the META stock. A Z-Score Normalization also may not be fully intuitive for consumers, but the goal is to detect variability in these graphs. Lastly, there is still sample size bias with this. After all, this only look at the span over one year. If there was a streamlined process for analyzing these graphs, it would make sense to maximize the timeframe since more data would help justify this method.

B.	MACD
To justify that this is the right approach, we can also utilize the Moving Average Convergence Divergence approach to buying and selling stocks. This would primarily only be used to analyze the stocks that have a stronger correlation between earnings and stock. This focuses on finding an exponential moving average with different window ranges (typically 12 days and 26 days). The values of these equations aren't fully important since the importance derives from the relation between both the signal line and the MACD line.

IV.	RESULTS
Since there are seven stocks that all have their own images, it is better to group them into categories rather than analyze each individually.

A.	Innovative Stocks
The first category is the innovative stocks. Of these seven, this would TSLA, META, and AMZN. There tends to be a strong correlation with these stocks. Looking at TSLA, there is increased volatility starting the week prior to the earnings being released. In a similar situation, AMZN also has strong correlations with quarterly earnings. The difference is that the volatility comes during the report being announced compared to a week before. Regardless, this is predictable.
 
B.	Powerhouse Stocks
	Although better terminology could be used, these stocks represent companies that are already stabilized in the technology industry. This is primarily AAPL and MSFT, companies that already had their major breakthroughs in the past. When looking at both of these images, there seems to be no correlation between quarterly earnings reports and their stock peformance.  
 
C.	Unknowns
	This leaves a few stocks in which the data is inconclusive. This is mainly NVDA and GOOGL. Seeing that NVDA is fairly new in this category, and since they had and inhuman growth, it is not wild to assume this. As for GOOGL, this may be unexplainable at the time.
 
D.	MACD for Innovative Stocks
	When looking at these graphs holistically it does align with the principle that quarterly earnings affect stocks, these graphs visualize that perfectly. When analyzing MACD vs Signal Line charts, it's important to denote when these graphs overlap with each other. Although this is expected to happen outside of these regions, seeing the frequency of it happening within these regions is supple proof that this correlation does and should exist. Not only that, but even if these lines do not intersect, these lines do approach each other, thus still proving that this correlation is strong rather than definite.   

V.	DISCUSSION
Overall, the results are satisfactory. This report was more research-intensive rather than programming-intensive, so it is hard to justify the programming done. Also, there is very conflicting information regarding quarterly earnings is partially privatized, making researching this a hassle. Overall, keeping this generic helps newer investors with that general principle: more innovative companies will have larger fluctuations with their quarterly earnings compared to existing powerhouses. This makes logical sense.
This report could also have selection bias. After all, these are how the best performing stocks have performed only in the 

past year. To make a claim as general as this one, more stocks would need to be analyzed over a longer time frame. There would also need to be a better isolation of the quarterly earnings (i.e. inflation or policies could have an impact on stocks).
The next part of this project is to create a model to delineate what make a company more innovative than others and what specific results from the quarterly earnings have an impact upon these stocks. After all, this report focused on the timeframe of a quarterly earning rather than the actual content itself. Since there is a lot of variability in that as well as does not have pre-defined guidelines, this is outside of the scope of this project.
