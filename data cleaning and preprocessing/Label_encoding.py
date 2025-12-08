# LabelEncoder is used for nominal data which have no relation with each other , counter of ordinal data which have some relation existing
import pandas as pd 
df = pd.DataFrame({"Name":["Ankit","Harry","Cat","Momo"]})
df

from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
df["en_name"] = le.fit_transform(df["Name"])
dataset = pd.read_csv("loan.csv")
dataset

la = LabelEncoder()
dataset["Property_Area"] = la.fit_transform(dataset["Property_Area"])
dataset