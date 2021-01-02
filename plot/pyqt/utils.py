import pandas as pd
import numpy as np

data = pd.read_csv('../FMW/L-wanshen_FMW.csv')

columns = data.columns
print(len(columns))
time = data.iloc[:, :1].copy()
time.dropna(axis=0, inplace=True)
print(time)
EMG_cols = [c for c in columns if "EMG" in c]

print(EMG_cols)

emg9 = data.iloc[:, 1:2].copy()
emg9 = emg9.iloc[:len(time), :]
print(emg9)

dd = data[EMG_cols[0]].copy()[:len(time)]
print(time.shape)
print(dd.shape)
