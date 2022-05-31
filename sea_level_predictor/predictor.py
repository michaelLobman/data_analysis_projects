import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np

df = pd.read_csv('./epa-sea-level.csv')

s = plt.scatter(x="Year", y="CSIRO Adjusted Sea Level", data=df)

x1 = df['Year'].values
y1 = df["CSIRO Adjusted Sea Level"].values
x1_future = np.arange(1880, 2051)
res1 = linregress(x=x1, y=y1)
plt.plot(x1_future, res1.intercept + res1.slope * x1_future, 'r', label="fitted line")

recent_df = df[df['Year'] > 1999]
x2 = recent_df['Year'].values
y2 = recent_df["CSIRO Adjusted Sea Level"].values
x2_future = np.arange(2000, 2051)
res2 = linregress(x=x2, y=y2)
plt.plot(x2_future, res2.intercept + res2.slope * x2_future, 'r', label="fitted line 2")

plt.title(label="Rise in Sea Level")
plt.xlabel(xlabel="Year")
plt.ylabel(ylabel="Sea Level (inches)")


plt.show()