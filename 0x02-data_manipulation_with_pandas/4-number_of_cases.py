import pandas as pd

df = pd.read_csv("https://www.sololearn.com/uploads/ca-covid.csv")

df.drop('state', axis=1, inplace=True)
df['date'] = pd.to_datetime(df['date'], format='%d.%m.%y')
df['month'] = df['date'].dt.month_name()
df.set_index('date', inplace=True)

custom_month_df = df[df['month']==input()]

maxim = custom_month_df['cases'].max()

print(df[df['cases']==maxim])
