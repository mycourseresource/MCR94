import pandas as pd
import numpy as np

df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]})

def calc_mean(row):
    print(row)
    return np.mean(row)

df['MEAN'] = df.apply(calc_mean, axis=1)

print(df)