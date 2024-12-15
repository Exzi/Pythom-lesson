import pandas as pd
import random

lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'who': lst})

one_hot_complete = pd.DataFrame({
    'robot': [1 if x == 'robot' else 0 for x in data['who']],
    'human': [1 if x == 'human' else 0 for x in data['who']]
})

result_complete = pd.concat([data, one_hot_complete], axis=1)

print(result_complete.head())