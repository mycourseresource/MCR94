import pandas as pd
#import numpy as np

df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]})

def calc_vat(row, column, vat_rate):
    print(row)
    print(row[column])
    print(vat_rate)
    return row[column] / 100 * vat_rate

df['VAT_A'] = df.apply(calc_vat, vat_rate=23, column='A', axis=1)
df['VAT_B'] = df.apply(calc_vat, vat_rate=23, column='B', axis=1)
df['VAT_C'] = df.apply(calc_vat, vat_rate=23, column='C', axis=1)

print(df)