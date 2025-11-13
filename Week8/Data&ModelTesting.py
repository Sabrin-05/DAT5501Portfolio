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
CO2_df = df_world[(df_world['Year'] >= 1925) & (df_world['Year'] <= 2025)]
print(CO2_df)
#x = CO2_emissions_df['year']