import pandas as pd
adv1_df = pd.read_csv('advertising_1.csv', index_col='Number')
print(adv1_df.head(10))