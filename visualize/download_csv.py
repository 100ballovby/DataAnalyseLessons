import pandas as pd
import matplotlib.pyplot as plt

download_url = 'https://raw.githubusercontent.com/fivethirtyeight/data/master/college-majors/recent-grads.csv'

df = pd.read_csv(download_url)
#df.plot(x='Rank', y=['P25th', 'Median', 'P75th'])
#df.plot(x='Major_category', y='P75th')
#plt.show()

top_5 = df.sort_values(by='Median', ascending=False).head()
top_5.plot(x='Major', y='Median', kind='bar', rot=5, fontsize=8)

top_medians = df[df['Median'] > 60000].sort_values('Median')
top_medians.plot(x='Major', y=['P25th', 'Median', 'P75th'], kind='bar', rot=10, fontsize=8)
plt.show()