import pandas as pd
df = pd.read_csv('music_log_upd.csv')
pop_music = df[df['genre_name'] =='pop']
pop_music = pop_music[pop_music['total_play_seconds'] > 0]
pop_music_max_total_play = pop_music['total_play_seconds'].max()
#print(pop_music_max_total_play)
pop_music_min_total_play = pop_music['total_play_seconds'].min()
#print(pop_music_min_total_play)

pop_music_min_info = pop_music[pop_music['total_play_seconds'] == pop_music['total_play_seconds'].min()]
#print(pop_music_min_info)

pop_music_median = pop_music['total_play_seconds'].median()
#print(pop_music_median)
pop_music_mean = pop_music['total_play_seconds'].mean()
print(pop_music_mean)