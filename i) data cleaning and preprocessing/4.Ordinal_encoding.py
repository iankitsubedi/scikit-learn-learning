import pandas as pd

df = pd.DataFrame({"size":["s","m","l","xl","s","m","l","s","s","l","xl","m"]})
df.head(3)
data = [["s","m","l","xl"]]
from sklearn.preprocessing import OrdinalEncoder
oe = OrdinalEncoder(categories=data) # normally it is done on alphabetical order
df["size_en"] = oe.fit_transform(df[["size"]])

dataset = pd.read_csv("loan.csv")
dataset.head(3)

dataset["Property_Area"].unique()
dataset["Property_Area"].fillna(dataset["Property_Area"].mode()[0] , inplace = True)
order_en = [["Urban","Rural","Semiurban"]]
from sklearn.preprocessing import OrdinalEncoder
x = OrdinalEncoder(categories=order_en)
dataset["Property_Area"] = x.fit_transform(dataset[["Property_Area"]])

dataset