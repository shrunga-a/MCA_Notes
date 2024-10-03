import pandas as pd
import numpy as np
df = pd.read_csv('C:/Users/user/Downloads/Telegram Desktop/student.csv')
print(df.head(11))
df.drop_duplicates(keep=False, inplace=True)
# print(df)
# df.drop_duplicates(subset=["Name"], keep="last", inplace=True)
print(df.head(10))
df.isnull().sum()
print(df.shape)
df_dropped = df.dropna()
print(df.head())
df['Address']=df['Address'].fillna('Coorg')
print(df.head())
#Fill with provided value
mean_val=df['Mobile'].mean()
df['Mobile']=df['Mobile'].fillna(mean_val)
print(df)