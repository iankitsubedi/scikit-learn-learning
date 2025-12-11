import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

dataset = pd.read_csv("predictionfile.csv")
dataset.columns

dataset = dataset.drop(columns=['Id', 'Bedrooms', 'Bathrooms', 'Floors', 'YearBuilt',
                      'Location', 'Condition', 'Garage',])
dataset.isnull().sum()
x = dataset[["Area"]]
y = dataset["Price"]

x_train , x_test , y_train , y_test = train_test_split(x , y , test_size=0.2 , random_state=1)
lr = LinearRegression()
lr.fit(x_train , y_train)

lr.score(x_test , y_test)