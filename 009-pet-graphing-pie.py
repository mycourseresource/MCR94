import pandas as pd
import matplotlib.pyplot as plt

python_list = [
    ['Dog', 'Bailey', None, None, 'White Brown Black', True, None],
    ['Dog', 'Noodles', 45, 'cm', 'White', True, '2021-01-01'],
    ['Bulldog', 'Luigi', 16, 'inches', 'Black', True, '2019-04-10'],
    ['Dog', 'Pickles', 1, 'm', 'Ginger', True, '2021-07-23'],
    ['Dog', 'Badger', 15, 'cm', 'Black White', True, '2022-10-01'],
    ['Dog', 'Rex', 1, 'foot', 'Brown White', True, '2020-06-01'],
    ['Bird', 'Anastasia', 0.11, 'm', 'White', True, '1996-11-01'],
    ['Cat', 'Sugar', None, None, 'White Yellow', True, None],
    ['Dog', 'Darky', 2, 'foot', 'Black', True, '1970-07-19'],
    ['Cat', 'Ann', 30, 'cm', 'Black', True, '2020-04-01'],
    ['Cat', 'Domino', 30, 'cm', 'Grey', True, '2013-09-03'],
    ['Dog', 'Yorkie', 20, 'cm', 'Brown', True, '2015-07-07'],
    ['Dog', 'Penny', 70, 'cm', 'Golden Yellow', True, '2014-06-01'],
    ['Dog', 'Jeddy', 20, 'cm', 'Brown White', True, '2018-06-01'],
    ['Cat', 'Fluffy', 32, 'cm', 'Black', True, '2010-09-17'],
    ['Cat', 'Cookie', 26, 'cm', 'Silver', True, '2022-03-29'],
    ['Cat', 'Trixie', 30, 'cm', 'White Black Ginger', True, '2015-10-28']
    ]

# Use the hash key for comments in Python
pandas_pets = pd.DataFrame(python_list, columns = ['Pet', 'Name', 'Height', 'Height Unit', 'Colour', 'Own', 'DOB'])

def normalize_height(row):
    height = row['Height']
    unit = row['Height Unit']
    #if height.isnumeric() == False:
    #    return 'NaN'
    if unit == 'foot':
        return height * 25.4 * 12
    elif unit == 'inches':
        return height * 25.4
    elif unit == 'mm':
        return height
    elif unit == 'cm':
        return height * 10
    elif unit == 'm':
        return height * 1000
    else:
        return 'ERROR - UNKNOWN UNIT'


pandas_pets.dropna(subset=['Height', 'Height Unit'], axis=0, inplace=True)

pandas_pets['Height (mm)'] = pandas_pets.apply(normalize_height, axis=1)

# pandas_pets_sorted = pandas_pets.sort_values('Height (mm)', ascending=False)

counts = pandas_pets['Pet'].value_counts()
print(counts)

counts.plot(kind='pie')
plt.title('Pet Counts')
plt.xlabel('Pet')
plt.ylabel('Count')
plt.savefig('009-pet-graphing-pie.png', bbox_inches='tight')

