#Importing required libraries
import pandas as pd 
import matplotlib.pyplot as plt 


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#Reading the US Election Data
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
df = pd.read_csv('US-2016-primary.csv', delimiter=';')
print(df)


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#Calculating average votes for [name] and [name]
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def average_votes():
    '''
    Function calculates the average votes for a particular candidate in each state
    '''
    
