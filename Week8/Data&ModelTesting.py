import numpy as np 
import matplotlib.pyplot as plt
import pandas as pd 

#Fitting and forecasting activity to test wheather a model is a good fit to a dataset
#Fitting a sub-sample to polynomials 

#Reading the data from the excel
CO2_emissions_df= pd.read_csv("Week8/temperature-anomaly.csv")
print(CO2_emissions_df)

#Cleaning the data 