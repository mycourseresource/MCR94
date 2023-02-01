import pandas as pd

python_list = [
    ['Dog', 'Bailey', None],
    ['Dog', 'Noodles', 45],
    ['Bulldog', 'Luigi', 40],
    ['Dog', 'Pickles', 100],
    ['Dog', 'Badger', 15],
    ['Dog', 'Rex', 30],
    ['Bird', 'Anastasia', 11],
    ['Cat', 'Sugar', None]]

# Use the hash key for comments in Python
pandas_pets = pd.DataFrame(python_list, columns = ['Pet', 'Name', 'Height'])

print(pandas_pets)
print(pandas_pets.describe())

