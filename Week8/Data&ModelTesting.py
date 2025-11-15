import numpy as np 
import matplotlib.pyplot as plt
import pandas as pd 

#Fitting and forecasting activity to test wheather a model is a good fit to a dataset
#Fitting a sub-sample to polynomials 

#Reading the data from the excel
CO2_emissions_df= pd.read_csv("Week8/temperature-anomaly.csv")
print(CO2_emissions_df)

#Cleaning the data 
df_world = CO2_emissions_df[CO2_emissions_df['Entity'] == 'World']
CO2_df = df_world[(df_world['Year'] >= 1925) & (df_world['Year'] <= 2015)]
print(CO2_df)

#Created second df to only include 10 most recent years
second_df = df_world[(df_world['Year'] >= 2015) & (df_world['Year'] <= 2025)]
print(second_df)

#use np.ployfit to create a....
x = CO2_df['Year']
y = CO2_df['Global average temperature anomaly relative to 1861-1890']

coefficients = np.polyfit(x, y, 5)
print("Linear Fit Coefficients:", coefficients)

# Create polynomial function
p = np.poly1d(coefficients)

plt.scatter(x, y, label='Data Points')
plt.plot(x, p(x), label='Linear Fit', color='red')
plt.legend()
plt.show()
