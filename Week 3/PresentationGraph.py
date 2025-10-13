import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt


# Fetch the data.
retirement_df = pd.read_csv("Week 3/sabrins_table(in).csv")
print(retirement_df)

#retirment_df = retirement_df.mask(retirement_df["Entity"] !=  "OECD average")
#clean_retirement_df = retirement_df.mask(retirement_df["Entity"] != "Europe average")
#print(clean_retirement_df)

#yearly_average= clean_retirement_df.groupby("Year")[["Average effective age of retirement, women (OECD)", "Average effective age of retirement, men (OECD)"]].mean().reset_index()
#print(yearly_average)

#for x in retirement_df.index():
    #if df.loc[x, "Entity"] == "OECD average":
        #retirement_df.drop(x, inplace=True)

#used two axes as the scales were so different 
fig, ax = plt.subplots()

ax.scatter(retirement_df['year'], retirement_df['average_age_women'])
ax.set_xlabel("Year")
#ax.set_ylabel('Average women retirement age', color='blue')
#ax1.tick_params(axis='y', labelcolor='blue')

# Create a second y-axis for the second line
#ax2 = ax1.twinx()
ax.scatter(retirement_df['year'], retirement_df['average_age_men'])
ax.set_ylabel("Average Age")
#ax.set_ylabel('Average men retirement age', color='red')
#ax2.tick_params(axis='y', labelcolor='red')

plt.title('Global Retirement Age Trends by Gender (1970–2018)')
plt.legend(["Average women retirement age","Average men retirement age"])

plt.savefig('Correlation.png', bbox_inches= 'tight')

# Show the plot
plt.show()
