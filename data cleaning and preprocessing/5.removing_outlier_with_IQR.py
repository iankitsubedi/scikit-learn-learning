import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

dataset = pd.read_csv("loan.csv")
dataset.head(3)

dataset.describe()

plt.figure(figsize=(15,5))
sns.boxplot(x = "CoapplicantIncome" , data = dataset)

dataset.shape
q1 = dataset["CoapplicantIncome"].quantile(0.25)
q3 = dataset["CoapplicantIncome"].quantile(0.75)
IQR = q3 - q1

min_range = q1 - (1.5 * IQR)
max_range = q3 + (1.5 * IQR)
new_dataset = dataset[dataset["CoapplicantIncome"]<=max_range]

new_dataset.shape
plt.figure(figsize=(15,5))
sns.boxplot(x = "CoapplicantIncome" , data = new_dataset)