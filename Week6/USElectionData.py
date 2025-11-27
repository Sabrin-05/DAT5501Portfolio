#Importing required libraries
import pandas as pd 
import matplotlib.pyplot as plt 


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#Reading the US Election Data
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
df = pd.read_csv('Week6/US2016Primary.csv', delimiter=';')
print(df)


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#Calculating average votes for [John Kasich] and [Ted Cruz]
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def average_votes():
    '''
    Function calculates the average votes for a particular candidate in each state
    '''
    candidate_name = "John Kasich"
    candidate_votes = df[df["candidate"] == candidate_name]
    average_per_state = candidate_votes.groupby("state")["votes"].mean().reset_index()
    print(f"John Kasich votes per state, {average_per_state}")
    
average_votes()


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#Graph 1: Histogram showing average votes per state for John Kasich
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
plt.hist(average_votes, bins=10)
plt.title("Distribution of votes per state for John Kasich")
plt.ylabel("Number of States")
plt.xlabel("Average Votes") 