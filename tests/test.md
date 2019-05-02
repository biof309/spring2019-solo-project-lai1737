# Project: Trends of Suicide Rate 3 High-Rate Countries compared to United States

##Project Question
The study question of this project is to identify the trends of suicide rates over years for x countries, and compare the trends to that of the US.

##Method
* First identify countries with the highest average suicide rates and then select the top 3 to compare trends with the US.

* With Seaborn package, draw trends of suicide rates / 100k in these countries.

##Importing package and data
```
##Importing package and data
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

master = pd.read_csv('master.csv')

master.head()

master_mean_country_year = pd.DataFrame(master.groupby(['country'])['suicides/100k pop'].mean()).sort_index(by=['suicides/100k pop'], ascending=False)[0:3]
## The highest average suicide rates are in countries: Lithuania, Sri Lanka, and Russian Federation

select_country = master['country'].isin(master_mean_country_year.index.tolist() + ['United States'])

master_select_country = master[select_country]

sns.boxplot('country', 'suicides/100k pop', data=master_select_country)
plt.show()

test = sns.lineplot(x='year', y='suicides/100k pop', hue='country', data=master_select_country)
plt.xlabel('year')
plt.ylabel('Suicide Rate per 100k People')
plt.title('Suicide Rate per 100k People\n'
          'in Lithuania, Sri Lanka, Russian Federation, and the United States')
plt.legend()
plt.show()
```

##Seaborn Graph
