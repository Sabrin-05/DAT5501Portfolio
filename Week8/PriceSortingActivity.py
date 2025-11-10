import numpy as np
import pandas as pd
from time import perf_counter

 # Calculating the daily change in assest price

 # Fetch the data.
pricing_df = pd.read_csv("Week8/NVIDIA CORPORATION (03-20-2024 _ 11-07-2025).csv")
print(pricing_df)

#pricing_df['Price Change'] = pricing_df['Close'].diff()
#print(pricing_df[['Date', 'Close', 'Price Change']])

changes = []


for i in range(len(pricing_df['Close']) -1):
    start_price = pricing_df['Close'][i]
    next_price = pricing_df['Close'][i + 1]
    change_price = next_price - start_price
    changes.append(change_price)

pricing_df['Price Change'] = change_price
print(pricing_df[['Date', 'Close', 'Price Change']])

#start = perf_counter()






