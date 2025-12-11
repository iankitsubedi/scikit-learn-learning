import pandas as pd

dataset = pd.read_csv("BostonHousing.csv")
dataset.head(3)

input_dataset = dataset.iloc[:,:-1]
output_dataset = dataset["medv"]

from sklearn.model_selection import train_test_split
x_train , x_test , y_train , y_test = train_test_split(input_dataset , output_dataset,test_size=0.25) 
x_test