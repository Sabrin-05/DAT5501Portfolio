import pandas as pd
import matplotlib.pyplot as plt 
from sklearn import tree
from sklearn.model_selection import train_test_split

from ucimlrepo import fetch_ucirepo 
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Copied code instructions to import dataset
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# fetch dataset 
tic_tac_toe_endgame = fetch_ucirepo(id=101) 
  
# data (as pandas dataframes) 
X = tic_tac_toe_endgame.data.features 
y = tic_tac_toe_endgame.data.targets 
  
# metadata 
print(tic_tac_toe_endgame.metadata) 
  
# variable information 
print(tic_tac_toe_endgame.variables) 


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#Test Train Split: 70/30 split
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42)
