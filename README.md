# Portfolio-Diversification-Analysis-using-S-P-500-Stocks

# Introduction
For a novice investor, it's a natural question to ask: "How many stocks should I buy, for what duration, and which industries should I invest in to maximize my returns?" Our project revolves around determining the optimal parameters of the  investments in stocks to create a well-diversified portfolio that outperforms the market index. 

We will perform our analysis by exploring how the diversification concept operates across various industries, timeframes, and portfolio sizes in historical stock dataset. 

## Methodology

Data Collection: 
The S&P 500 index is one of the most widely followed stock market indices. It includes 500 large US companies that capture approximately 80% coverage of available US market capitalization. Our dataset consists of 270 stocks of different companies, which include the price of each stock between 1980 – 2023.
 


Sharp Ratio:
The Sharpe ratio is a measure used to evaluate the performance of an investment by adjusting for its risk. It measures the excess return (or risk premium) per unit of risk in an investment asset or trading strategy. 
Formula:  Sharpe Ratio = (𝑹_𝒂− 𝑹_𝒇)/𝝈_𝒂  , where:
𝑹_𝒂 = Asset return,  𝑹_𝒇 = Risk-free rate
𝝈_𝒂 = Standard deviation of asset returns (risk measurement metric)


Combinations:
The combinations refer to selecting randomly a subset of stocks from a population set of companies form S&P500 listing - C(n, k), where:

n = Population set,  k = subset

We took combinations for different portfolio sizes of stocks like 5, 15,.., 45. C(𝟐𝟕𝟎¦𝟏𝟎) = 4.793227598 E+17 out of which we have considered 10000 combinations.	 


## Results

The outcome provides insights into portfolio optimization. We find that the optimal number of stocks an investor should hold is approximately 35. This specific quantity corresponds to the highest Sharpe Ratios, signifying an ideal equilibrium between return and risk within this stock combination. We have also found that the time is a key factor. We can clearly see the compounding effect can significantly boost the overall return on the investment. The longer the investment is held, the more pronounced diversification effect becomes. The pie Chart shows the most represented industries. Our ideal portfolio is concentrated in industries like Technology, Banks and Financial Services, Drug manufacturing and Healthcare, etc.



![image](https://github.com/user-attachments/assets/c92330d6-01ab-4ec8-94bb-1c1c49b26d0b)

Compounding effect:
accumulates interest from previous periods, causing exponential-like growth

Averaging effect:
reduces the impact of market volatility and shocks by spreading your investments over uncorrelated stocks


# References:

1. https://www.investopedia.com/terms/s/sharperatio.asp
2. https://www.investopedia.com/terms/d/diversification.asp#:~:text=Diversification%20is%20a%20risk%20management,any%20single%20asset%20or%20risk
3. https://www.macrotrends.net/




