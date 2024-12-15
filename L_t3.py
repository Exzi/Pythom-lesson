import pandas as pd
file_path_2 = 'advertising_2.csv'
adv2_df = pd.read_csv(file_path_2, index_col='Number')
rows_533_to_536 = adv2_df.loc[533:536]
print(rows_533_to_536)
