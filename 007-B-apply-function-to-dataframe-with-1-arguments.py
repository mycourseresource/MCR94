import pandas as pd
#import numpy as np

df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]})

def calc_vat(row, vat_rate):
    print(row)
    print(row['A'])
    print(vat_rate)
    return row['A'] / 100 * vat_rate

df['VAT'] = df.apply(calc_vat, vat_rate=23, axis=1)

print(df)