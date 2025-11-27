import pandas as pd
import matplotlib.pyplot as plt 
from sklearn import tree
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree
import matplotlib.pyplot as plt

from ucimlrepo import fetch_ucirepo 
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Copied code instructions to import dataset
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# fetch dataset 
breast_cancer_wisconsin_original = fetch_ucirepo(id=15) 
  
# data (as pandas dataframes) 
X = breast_cancer_wisconsin_original.data.features 
y = breast_cancer_wisconsin_original.data.targets 
  
# metadata 
print(breast_cancer_wisconsin_original.metadata) 
  
# variable information 
print(breast_cancer_wisconsin_original.variables) 


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#Test Train Split: 70/30 split
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42)

