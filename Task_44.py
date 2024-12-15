import pandas as pd
import random

lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'who': lst})

print(data.head())

one_hot_robot = pd.DataFrame({'robot': [1 if x == 'robot' else 0 for x in data['who']]})
result_robot = pd.concat([data, one_hot_robot], axis=1)

print(result_robot.head())