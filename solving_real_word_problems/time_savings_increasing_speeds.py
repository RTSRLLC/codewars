# v = d*t^1/2 : t = d/v : d = vt
# dv/dt =  (1/2)*d * t^(-1/2)

import pandas as pd
import numpy as np


def lag_roll(df: pd.DataFrame, hr: str, time_frame: str):
    for i in range(1, len(df_)):
        col = f'{time_frame}_w/{i}_roll'
        df_.loc[:, col] = hr.rolling(i).sum().round(4)
    return df


speeds = [35, 40, 45, 50, 55, 60, 65, 70, 75, 80]

short_distances = [1, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 70, 80, 90, 100, 110, 120, 150, 200, 250, 300, 350, 400, 500, 600, 700, 800]

# todo: what are the time savings when traveling if you your speed is increased incrementally

t = lambda d, v: d / v

cols = ['distance', 'avg speed', 'hrs']
dist = []
speed = []
hrs = []

for d in short_distances:
    for s in speeds:
        dist.append(int(d))
        speed.append(int(s))
        hrs.append(float(round(t(d, s), 4)))

arr = np.array([dist, speed, hrs]).T
df = pd.DataFrame(arr, columns=cols)

df_final = None
set_it = df.distance.unique()
for d in set_it:
    df_ = df[df.distance == d].copy()

    hrs = df_['hrs']

    df_ = lag_roll(df_, hrs, 'hrs')

    df_.loc[:, 'mins'] = (hrs * 60).round(4)

    df_ = lag_roll(df_, hrs, 'mins')

    df_.loc[:, 'secs'] = (hrs * 3600).round(4)

    df_ = lag_roll(df_, hrs, 'secs')

    df_ = df_.fillna(0)

    if df_final is None:
        df_final = df_
    else:
        df_final = pd.concat([df_final, df_], axis=0)