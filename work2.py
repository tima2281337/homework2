import pandas as pd

df = pd.read_csv('music_log_upd.csv')


genre_counting = df.groupby('user_id')['genre_name']


def user_genres(group):
    for column in group:
        if len(column[1]) > 50:
            user = column[0]
            return user

            
    
search_id = user_genres(genre_counting)
music_use = df[df['user_id'] == search_id]
music_use = music_use[music_use['total_play_seconds'] > 0]
sum_music_use = music_use.groupby('genre_name')['total_play_seconds'].sum()
final_sum = sum_music_use.sort_values(ascending=False)

count_music_user = music_use.groupby('genre_name')['genre_name'].count()
final_count = count_music_user.sort_values(ascending=False)
print(final_count)
