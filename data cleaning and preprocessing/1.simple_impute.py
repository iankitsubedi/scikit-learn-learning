import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

dataset = pd.read_csv("Bankloan.csv")
dataset.head(4)

dataset.isnull().sum()

dataset.select_dtypes("float64").columns
from sklearn.impute import SimpleImputer
si = SimpleImputer(strategy="mean")
ar = si.fit_transform(dataset[['age', 'ed', 'income', 'debtinc', 'creddebt', 'othdebt']])

new_dataset = pd.DataFrame(ar,columns=dataset.select_dtypes("float64").columns)
new_dataset.isnull().sum()