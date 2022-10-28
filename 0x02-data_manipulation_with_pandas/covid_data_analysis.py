import pandas as pd

df = pd.read_csv("https://www.sololearn.com/uploads/ca-covid.csv")

df.drop('state', axis=1, inplace=True)
df.set_index('date', inplace=True)

df['ratio'] = df['deaths'] / df['cases']	# create ratio column

max_ratio = df['ratio'].max()	# obtain largest ratio

print(df[df['ratio']==max_ratio])	# output row with largest ratio
