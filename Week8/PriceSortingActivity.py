import numpy as np
import pandas as pd
from time import perf_counter
import matplotlib.pyplot as plt 


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#Calculating the daily change in assest price
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#Fetch the data.
pricing_df = pd.read_csv("Week8/NVIDIA CORPORATION (03-20-2024 _ 11-07-2025).csv")
print(pricing_df)

pricing_df['Price Change'] = pricing_df['Close'].diff()
print(pricing_df[['Date', 'Close', 'Price Change']])


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#Looping through start and close price to calculate change
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

'''for i in range(len(pricing_df['Close']) -1):
    start_price = pricing_df['Close'][i]
    next_price = pricing_df['Close'][i + 1]
    change_price = next_price - start_price
    changes.append(change_price)

pricing_df['Price Change'] = change_price
print(pricing_df[['Date', 'Close', 'Price Change']])'''


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#Looping through dataset to calculate time taken to sort
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
sample_size = list(range(7,365))
time = []

for n in sample_size:
    start_time = perf_counter()
    subset_sample = pricing_df['Close'][:n]
    sorted_sample = sorted(subset_sample)
    end_time = perf_counter()
    time.append(end_time - start_time) 


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#Graph 1: Showing time taken to data as sample size increases
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ 
plt.plot(sample_size, time)
plt.title('Daily Price Change NVDIA Calculation Time')
plt.legend(["Calculation Time"])
plt.xlabel('Sample Number')
plt.ylabel('Time Taken to Sort')
plt.savefig('Correlation.png', bbox_inches= 'tight')

# Show the plot
plt.show()




