# Import packages

import pandas as pd
import numpy as np
import winsound
import matplotlib.pyplot as plt
import seaborn as sns
%matplotlib inline

# Download preprocessed datasets with annual returns and sharpe values

path = "D:\\PhD_KSU\\2nd_YEAR\\COURSES\\Discrete_math\\Analytics_day\\CSV\\return_agg_annul.csv"
path2 = "D:\\PhD_KSU\\2nd_YEAR\\COURSES\\Discrete_math\\Analytics_day\\CSV\\sharpe.csv"
df = pd.read_csv(path, header='infer')
df2 = pd.read_csv(path2, header='infer')
# Convert Date column into date format

df['Date'] = pd.to_datetime(df['Date'])
df.head()
# Convert Date column into date format

df2['Date'] = pd.to_datetime(df2['Date'])
df2.head()
# Divide dataset with returns by maturity

df_1y = df[df['Maturity'] == '1_year']
df_1y = df_1y.drop('Maturity', axis=1)
df_3y = df[df['Maturity'] == '3_year']
df_3y = df_3y.drop('Maturity', axis=1)
df_5y = df[df['Maturity'] == '5_year']
df_5y = df_5y.drop('Maturity', axis=1)
df_10y = df[df['Maturity'] == '10_year']
df_10y = df_10y.drop('Maturity', axis=1)
df_15y = df[df['Maturity'] == '15_year']
df_15y = df_15y.drop('Maturity', axis=1)
df_20y = df[df['Maturity'] == '20_year']
df_20y = df_20y.drop('Maturity', axis=1)
df_30y = df[df['Maturity'] == '30_year']
df_30y = df_30y.drop('Maturity', axis=1)
# Divide dataset with sharpe ratios by maturity

ds_1y = df2[df2['Maturity'] == '1_year']
ds_1y = ds_1y.drop('Maturity', axis=1)
ds_3y = df2[df['Maturity'] == '3_year']
ds_3y = ds_3y.drop('Maturity', axis=1)
ds_5y = df2[df['Maturity'] == '5_year']
ds_5y = ds_5y.drop('Maturity', axis=1)
ds_10y = df2[df['Maturity'] == '10_year']
ds_10y = ds_10y.drop('Maturity', axis=1)
ds_15y = df2[df['Maturity'] == '15_year']
ds_15y = ds_15y.drop('Maturity', axis=1)
ds_20y = df2[df['Maturity'] == '20_year']
ds_20y = ds_20y.drop('Maturity', axis=1)
ds_30y = df2[df['Maturity'] == '30_year']
ds_30y = ds_30y.drop('Maturity', axis=1)
# Creating function for simulations

def simulation(data, num_stock, num_iter):
    iteration_mean = {}
    company_counts = [] 
    random.seed(8)
    for i in range(num_iter):
        # Select stock names randomly
        random_stocks = [np.random.choice(column_names) for _ in range(num_stock)]
        for stock in range(5, num_stock, 10):
            subsample_stocks = np.random.choice(random_stocks, stock, replace=False)
            size_iter = data[subsample_stocks].mean(axis=0)
            iteration_mean[f'portfolio size {stock}'] = np.mean(size_iter)
            
    return iteration_mean

# Creating function for simulating portfolios with different number of stocks

def portfolio_sim(list_of_datasets, num_stocks):
    means = []
    random.seed(8)
    for dataset in list_of_datasets:
        portfolio = simulation(dataset, num_stocks, 1000)
        means.append(portfolio)
    return means

# Creating function for simulating indstries for certain number of stocks

def industry_simulation(data, num_stock, num_iter):
    company_counts = list()
    random.seed(8)
    for i in range(num_iter):
        # Select stock names randomly
        random_stocks = [np.random.choice(column_names) for _ in range(num_stock)]
        for stock in range(5, num_stock, 1000):
            subsample_stocks = np.random.choice(random_stocks, stock, replace=False)
            company_counts.extend(subsample_stocks)
         
    return company_counts
# Running simulations for return rates

list_of_datasets = [df_1y, df_3y, df_5y, df_10y, df_15y, df_20y, df_30y]
returns = portfolio_sim(list_of_datasets, 51)
# Display returns for each stock

gr = df.groupby('Maturity').agg('mean')
gr.sort_values(by='AAPL')
# Display simulated returns for different sizes of portfolio

pd.DataFrame(returns)
# Create table file for returns

table2 = pd.DataFrame(returns)
# Running simulations for Sharpe ratios

list_of_datasets = [ds_1y, ds_3y, ds_5y, ds_10y, ds_15y, ds_20y, ds_30y]
sharpe_ratio = portfolio_sim(list_of_datasets, 51)
pd.DataFrame(sharpe_ratio)
table1 = pd.DataFrame(sharpe_ratio)
# Display average Sharpe ratios for different sizes of portfolio

np.mean(pd.DataFrame(sharpe_ratio))
# Save the DataFrame to a CSV file

table2.to_csv('file1.csv', index=False)
table1.to_csv('file2.csv', index=False)
cd "D:\PhD_KSU\2nd_YEAR\COURSES\Discrete_math\Analytics_day\CSV"
import csv

# Initialize an empty dictionary for industry names
industry = {}

# Open the CSV file with industry names and read its content into a dictionary
with open('Industry.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)  # Skip header if it exists
    for row in reader:
        key, value = row
        industry[key] = value
# Simulating company names for optimal portfolio of 35 stocks and 30-years

company_names = industry_simulation(ds_30y, 36, 10000)

from collections import defaultdict

# Initialize a defaultdict to count occurrences of each company

company_counts = defaultdict(int)

# Count occurrences of each company

for company in company_names:
    company_counts[company] += 1

    
# Creating a new dictionary with keys replaced by industry names

replaced_keys_dict = {industry[key]: value for key, value in company_counts.items() if key in industry}
sorted_dict = dict(sorted(replaced_keys_dict.items(), key=lambda item: item[1], reverse=True))
print(sorted_dict)

