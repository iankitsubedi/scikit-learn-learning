import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

dataset = pd.read_csv("loan.csv") 
dataset.head(3)
sns.displot(dataset["CoapplicantIncome"])

from sklearn.preprocessing import MinMaxScaler
ms = MinMaxScaler()
dataset["new"] = ms.fit_transform(dataset[["CoapplicantIncome"]])
dataset