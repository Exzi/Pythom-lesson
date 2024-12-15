import pandas as pd
import random

lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'who': lst})

print(data.head())

one_hot_human = pd.DataFrame({'human': [1 if x == 'human' else 0 for x in data['who']]})
result_human = pd.concat([data, one_hot_human], axis=1)

print(result_human.head())