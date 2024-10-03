import pandas as pd 
df = pd.read_csv("AirPassengers.csv")
print(df.head())
print(df.tail())
df['Month'] = pd.to_datetime(df['Month'], format='%Y-%m')
print(df.head())
df.index = df['Month']
del df['Month']
print(df.head())


import matplotlib.pyplot as plt
import seaborn as sns
sns.lineplot(df)
#sns.lineplot(data=df)
plt.ylabel("Number of Passengers")

#
rolling_mean = df.rolling(7).mean()
rolling_std = df.rolling(7).std()

plt.plot(df, color="blue",label="Original Passenger Data")

plt.plot(rolling_mean, color="red", label="Rolling Mean Passenger Number")

plt.plot(rolling_std, color="black", label = "Rolling Standard Deviation in Passenger Number")

plt.title("Passenger Time Series, Rolling Mean, Standard Deviation")

plt.legend(loc="best")

from statsmodels.tsa.seasonal import seasonal_decompose
decompose = seasonal_decompose(df['#Passengers'],model='additive', period=7)
decompose.plot()
plt.show()
