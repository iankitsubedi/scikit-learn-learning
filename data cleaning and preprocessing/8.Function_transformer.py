import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

dataset = pd.read_csv("loan.csv")
dataset.head(3)

sns.displot(dataset["CoapplicantIncome"])
q1 = dataset["CoapplicantIncome"].quantile(0.25)
q3 = dataset["CoapplicantIncome"].quantile(0.75)
IQR = q3 - q1

min_range = q1 - (1.5 * IQR)
max_range = q3 + (1.5 * IQR)

dataset = dataset[dataset["CoapplicantIncome"]<=max_range]
from sklearn.preprocessing import FunctionTransformer
ft = FunctionTransformer(func=np.log1p)
dataset["CoapplicantIncome_new"] = ft.fit_transform(dataset[["CoapplicantIncome"]])

sns.distplot(dataset["CoapplicantIncome_new"])