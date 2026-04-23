import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme(style="whitegrid")
df = pd.read_csv("AI/SuperMarket_Analysis.csv")
print(df.head())
print(df.info())
print(df.shape)
print(df.columns)
print(df.describe())
print(df["City"].value_counts())
print(df["Gender"].value_counts())
print(df["Payment"].value_counts())
print(df.groupby("City")["gross income"].sum().idxmax())
print(df.groupby("Product line")["Quantity"].sum().idxmax())
print(df.groupby("Gender")["Quantity"].sum().idxmax())
df["Total"] = df["Quantity"] * df["Unit price"]
print(df["Total"].mean())

plt.figure()
df.groupby("City")["gross income"].sum().plot(kind="bar")
plt.title("Sehereler gore satis")
plt.xlabel("Seher")
plt.ylabel("Gelir")


plt.figure()
df.groupby("Product line")["Quantity"].sum().plot(kind="bar")
plt.title("Mehsul xettine gore satis")
plt.xlabel("Mehsul xetti")
plt.ylabel("Satis")

plt.figure()
sns.countplot(x="Gender", data=df)
plt.title("Gender uzre alis sayi")

plt.figure()
sns.countplot(x="Payment", data=df)
plt.title("Odenis usullari")

plt.figure()
sns.histplot(df["gross income"], bins=30)
plt.title("Gelir paylanmasi")

plt.figure()
sns.boxplot(x="City", y="gross income", data=df)
plt.title("Şəhərlərə görə gəlir paylanmasi")



print(" Lider seher:", df.groupby("City")["gross income"].sum().idxmax())
print("En cox satilan mehsul:", df.groupby("Product line")["Quantity"].sum().idxmax())
print("en cox istifade olunan odenis usulu:", df["Payment"].value_counts().idxmax())

plt.show()
