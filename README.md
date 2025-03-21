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










