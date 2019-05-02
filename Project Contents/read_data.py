# Project: Trend of Suicide Rate in x Countries compared to United States
##Importing package and data
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

master = pd.read_csv('Project Contents/master.csv')

master.head()

master_mean_country_year = pd.DataFrame(master.groupby(['country'])['suicides/100k pop'].mean()).sort_values(by=['suicides/100k pop'], ascending=False)[0:3]
## The highest average suicide rates are in countries: Lithuania, Sri Lanka, and Russian Federation

select_country = master['country'].isin(master_mean_country_year.index.tolist() + ['United States'])

master_select_country = master[select_country]

test = sns.lineplot(x='year', y='suicides/100k pop', hue='country', data=master_select_country)
plt.xlabel('year')
plt.ylabel('Suicide Rate per 100k People')
plt.title('Suicide Rate per 100k People\n'
          'in Lithuania, Sri Lanka, Russian Federation, and the United States')
plt.legend()
fig = test.get_figure()

fig.savefig("Project Contents/Trend Graphs.png")