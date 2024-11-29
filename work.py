import pandas as pd

df = pd.read_csv('music_log.csv')

shape_table = df.shape

info = df.info
observation_info_table = 67963
observation_table = shape_table[0]

if observation_info_table == observation_table:
    print("Решение верно, количество наблюдений равно", observation_table)
else: 
    print('Решение неверно, проверьте еще раз')