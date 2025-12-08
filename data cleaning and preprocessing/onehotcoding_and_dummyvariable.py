# encoding means like converting the string into numerical form for the use of it in ML
import pandas as pd
dataset = pd.read_csv("loan.csv")
dataset.head(3)

dataset.isnull().sum()
dataset['Married'] = dataset['Married'].fillna(dataset['Married'].mode()[0])

en_code = dataset[['Gender','Married']] # there is pd dummies to encode but scikit learn's onehotencoder is easier 
from sklearn.preprocessing import OneHotEncoder

ohe = OneHotEncoder(drop="first") 
ar = ohe.fit_transform(en_code).toarray()
ar
# OneHotENcoder(drop = "first") will drop the first column made by encoder , it is used to reduce the columns
# sparse matrix means the matrix contains mostly of 0 and 1 , # toarray will convert the data in to array for
# proper use of it and can be used to replace the new data into the old dataframe

pd.DataFrame(ar , columns=["Gender_Male","Married_Yes"])