import numpy as np 
import matplotlib.pyplot as plt
import pandas as pd 

#Fitting and forecasting activity to test wheather a model is a good fit to a dataset
#Fitting a sub-sample to polynomials 


#Reading the data from the excel
CO2_emissions_df= pd.read_csv("Week8/TemperatureAnomoly.csv")
CO2_emissions_df["Year"] = pd.to_numeric(CO2_emissions_df["Year"], errors="coerce")
print(CO2_emissions_df)


#~~~~~~~~~~~~~~~~~~~~~~~~~~
#Cleaning and sorting data 
#~~~~~~~~~~~~~~~~~~~~~~~~~~

#Cleaning the data 
df_world = CO2_emissions_df[CO2_emissions_df['Entity'] == 'World']
CO2_df = df_world[(df_world['Year'] >= 1925) & (df_world['Year'] <= 2015)]
print(CO2_df)

#Created second df to only include 10 most recent years
second_df = df_world[(df_world['Year'] >= 1925) & (df_world['Year'] <= 2025)]
print(second_df)


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#Variables and Polynomial function
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#defining my x and y axis
x = CO2_df['Year']
y = CO2_df['Global average temperature anomaly relative to 1861-1890']

#creating a new variable to include all 100 years
x2 = second_df['Year']

coefficients = np.polyfit(x, y, 6)
print("Ploynomial Fit Coefficients:", coefficients)

# Create polynomial function
p = np.poly1d(coefficients)


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#Graph 1: Showing polynomial fit with order of 6
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
 
#Ploynomial fit with an order of 6 
plt.scatter(x, y, label='Data Points')
plt.plot(x, p(x), label='Polynomial Fit', color='red')
plt.legend()
plt.show()


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Chi-squared test checking for polynomial degrees
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
degrees = range(1, 11)

chi2_list = []
chi2_reduced_list = []
bic_list = []

sigma = 0.05 * np.ones_like(y)
 
for i in degrees:

    coeff = np.polyfit(x, y, deg=i)

    p = np.poly1d(coeff)

    y_pred = p(x)
 
    chi2 = np.sum(((y - y_pred) / sigma) ** 2)
    dof = len(x) - (i + 1)        # n − number_of_parameters
    chi2_reduced = chi2 / dof
 
    BIC = chi2 + (i + 1) * np.log(len(x))
    
    chi2_list.append(chi2)
    chi2_reduced_list.append(chi2_reduced)
    bic_list.append(BIC)


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~    
#Graph 2: Showing reduced chi-sqaured   
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#Plot graph for reduced chi-squared
plt.figure(figsize=(8,5))
plt.plot(degrees, chi2_reduced_list, marker="o")
plt.xlabel("Polynomial Degree")
plt.ylabel("Reduced Chi-Squared")
plt.title("Model Degree vs Reduced Chi-Squared")
plt.grid(True)
plt.show()


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#Graph 3: Showing bayesian information criterion
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#Plot graph for bayesian information criterion
plt.figure(figsize=(8,5))
plt.plot(degrees, bic_list, marker="o")
plt.xlabel("Polynomial Degree")
plt.ylabel("Bayesian Information Criterion")
plt.title("Model Degree vs BIC")
plt.grid(True)
plt.show()


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#Fit for a polynomial and return covariance matrix
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
coeffs, cov = np.polyfit(x, y, deg=6, cov=True)
print(coeffs, cov)