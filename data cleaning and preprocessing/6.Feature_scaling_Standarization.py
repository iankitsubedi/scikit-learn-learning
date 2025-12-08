import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

dataset = pd.read_csv("loan.csv")
dataset.head(3)
dataset.isnull().sum()

dataset["ApplicantIncome"] = dataset["ApplicantIncome"].fillna(dataset["ApplicantIncome"].mean())
sns.displot(dataset["ApplicantIncome"])

from sklearn.preprocessing import StandardScaler
ss = StandardScaler()
x = ss.fit_transform(dataset[["ApplicantIncome"]])
dataset["ApplicantIncome_ss"] = pd.DataFrame(x , columns=["x"])
dataset.head(3)

plt.figure(figsize=(12,5))
plt.subplot(1,2,2)
sns.distplot(dataset["ApplicantIncome"])

plt.subplot(1,2,1)
sns.distplot(dataset["ApplicantIncome_ss"])
