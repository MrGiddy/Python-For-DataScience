import pandas as pd

df = pd.read_csv("https://www.sololearn.com/uploads/ca-covid.csv")
df.drop('state', axis=1, inplace=True)					# drop 'state' column
df['date'] = pd.to_datetime(df['date'], format='%d.%m.%y') 		# convert 'date' to datatime

df['weekday'] = df['date'].dt.strftime("%A") 				# extract day of the week

print(df.iloc[-7:])
