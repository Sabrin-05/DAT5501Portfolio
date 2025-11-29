#Importing required libraries
import pandas as pd 
import matplotlib.pyplot as plt 


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#Reading the US Election Data
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
df = pd.read_csv('Week6/US2016Primary.csv', delimiter=';')
print(df)


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#Calculating average votes for [John Kasich] 
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#Filtering the dataframe for candidate John Kasich and his votes
candidate_name = "John Kasich"
candidate_votes = df[df["candidate"] == candidate_name]
print(candidate_votes)

#Calculating the average votes per state for John Kasich
average_per_state = candidate_votes.groupby(["state","candidate"])["fraction_votes"].sum().reset_index()
print(average_per_state)
    


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#Graph 1: Histogram showing average votes per state for John Kasich
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
plt.hist(average_per_state["fraction_votes"], bins=10, edgecolor='black')
plt.title("Distribution of votes per state for John Kasich")
plt.ylabel("Number of States")
plt.xlabel("Average Votes")
plt.show()