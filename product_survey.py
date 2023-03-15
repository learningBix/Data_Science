import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import MinMaxScaler

df = pd.read_csv("Mall_Customers.csv")
print(df.head(10))

print(df.isna().sum())
print(df.describe())

X = df.iloc[:,[3,4]]
print(X)

plt.title("Custmer Survey")
plt.xlabel("Annual Income")
plt.ylabel("Spending Score")
plt.scatter(df["Annual Income (k$)"], df["Spending Score (1-100)"])
plt.show()


wcss = []
for i in range(1,11):
    Kmean = KMeans(n_clusters=i, init ="k-means++", random_state= 42)
    Kmean.fit(X)
    wcss.append(Kmean.inertia_)
plt.title("Elbow Methed")
plt.xlabel("Number of cluster")
plt.ylabel("wcss")
plt.plot(range(1,11), wcss)
plt.show()

km = KMeans(n_clusters=5)
y_predict = km.fit_predict(X)
print(y_predict)

df["Cluster"] = y_predict

df1 = df[df["Cluster"]==0]
df2 = df[df["Cluster"]==1]
df3 = df[df["Cluster"]==2]
df4 = df[df["Cluster"]==3]
df5 = df[df["Cluster"]==4]

plt.title("Clustes")
plt.xlabel("Anuual Income")
plt.ylabel("Spending Score")
plt.scatter(df1["Annual Income (k$)"],df1["Spending Score (1-100)"], color = "red", label = "CLUSTER1")
plt.scatter(df2["Annual Income (k$)"],df2["Spending Score (1-100)"], color = "blue", label = "CLUSTER2")
plt.scatter(df3["Annual Income (k$)"],df3["Spending Score (1-100)"], color = "yellow", label = "CLUSTER3")
plt.scatter(df4["Annual Income (k$)"],df4["Spending Score (1-100)"], color = "black", label = "CLUSTER4")
plt.scatter(df5["Annual Income (k$)"],df5["Spending Score (1-100)"], color = "green", label = "CLUSTER5")
plt.legend()
plt.show()