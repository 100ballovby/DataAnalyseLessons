import pandas as pd

download_url = 'https://raw.githubusercontent.com/fivethirtyeight/data/master/college-majors/recent-grads.csv'

df = pd.read_csv(download_url)
df.plot(x='Rank', y=['P25th', 'Median', 'P75th'])