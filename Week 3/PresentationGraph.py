#Import necessary libraries
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#Read and clean data from csv
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Fetch the data.
retirement_df = pd.read_csv("Week 3/RetirementAgeData.csv")
print(retirement_df)

#Masking continents and other averages
retirment_df = retirement_df.mask(retirement_df["Entity"] !=  "OECD average")
clean_retirement_df = retirement_df.mask(retirement_df["Entity"] != "Europe average")
print(clean_retirement_df)

#Creating yealy average retirement age for men and women, grouping by year then calculating the mean
yearly_average= clean_retirement_df.groupby("Year")[["Average effective age of retirement, women (OECD)", "Average effective age of retirement, men (OECD)"]].mean().reset_index()
print(yearly_average)


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#Graph 1: Show the average retirement age in men and women over 48yrs
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#Average retirement age for women
fig, ax = plt.subplots()
ax.scatter(yearly_average['Year'], yearly_average['Average effective age of retirement, women (OECD)'])
ax.set_xlabel("Year")

#Average retirement age for men
ax.scatter(yearly_average['Year'], yearly_average['Average effective age of retirement, men (OECD)'])
ax.set_ylabel("Average Age")

#Create graph
plt.title('Global Retirement Age Trends by Gender (1970–2018)')
plt.legend(["Average women retirement age","Average men retirement age"])
plt.savefig('Correlation.png', bbox_inches= 'tight')
#Show the plot
plt.show()
