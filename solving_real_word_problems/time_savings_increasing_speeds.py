# v = d*t^1/2 : t = d/v : d = vt
# dv/dt =  (1/2)*d * t^(-1/2)

import pandas as pd
import numpy as np

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
    df_ = df[df.distance == d]
    df_['hr_diff'] = round(df_['hrs'].diff(), 4)

    df_['mins'] = round(df_['hrs'] * 60, 4)
    df_['min_diff'] = round(df_['mins'].diff(), 4)

    df_['secs'] = round(df_['hrs'] * 3600, 4)
    df_['secs_diff'] = round(df_['secs'].diff(), 4)

    df_ = df_.fillna(0)

    if df_final is None:
        df_final = df_
    else:
        df_final = pd.concat([df_final, df_], axis=0)