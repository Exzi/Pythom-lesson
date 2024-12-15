import pandas as pd
file_path = 'advertising_1.csv'
adv1_df = pd.read_csv(file_path, index_col='Number')
print("Размер датафрейма (строк, столбцов):", adv1_df.shape)
average_internet_time = adv1_df.loc[8, 'Daily Internet Usage']
print(f"Среднее ежедневное время нахождения в интернете пользователя под номером 8: {average_internet_time} минут")