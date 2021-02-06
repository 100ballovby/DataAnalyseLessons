import pandas as pd

nba = pd.read_csv('nba_all_elo.csv')

print(type(nba))
print(len(nba))
print(nba.shape)


# вывод типов данных таблицы
print(nba.info())
print(nba.describe())

print(nba['year_id'].value_counts())
cities = ['Berlin', 'Minsk', 'Tokyo']
revenue = pd.Series([5555, 7000, 1980],
                    index=cities)
print(revenue)


