import pandas as pd

df = pd.read_csv('music_log.csv')
df = df.rename(columns = {'  user_id': 'user_id', 'total play':'total_play', 'Artist':'artist' })
columns_to_replace = ['track', 'artist', 'genre']
for column in columns_to_replace:
    df[column] = df[column].fillna('unknown')
df = df.drop_duplicates().reset_index(drop = True)
print(df.head(20))