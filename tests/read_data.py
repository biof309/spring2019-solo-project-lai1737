# Project: Millenial GDP Over the Years in Various Countries
##Importing package and data
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import numpy as np

master = pd.read_csv('master.csv')

master.head()

master_mean_country_year = master.groupby(['country', 'year'])['suicides/100k pop'].mean()

#ind = master_mean_country_year.index

select_country = master['country'].isin(['United States', 'Japan', 'United Kingdom'])

master_select_country = master[select_country]

sns.boxplot('country', 'suicides/100k pop', data=master_select_country)
plt.show()

test = sns.lineplot(x='year', y='suicides/100k pop', hue='country', data=master_select_country)
plt.xlabel('year')
plt.ylabel('Suicide Rate per 100k People')
plt.title('Suicide Rate per 100k People in US, UK, and Japan')
plt.legend()
plt.show()










##Preliminary frequency table to see what generations there are
pd.crosstab(index=master['generation'], columns='count')

### Filter for "Millenials"
master_mil = master[master['generation']=='Millenials']
master_mil_1114 = master_mil[(master_mil['year'] >= 2011) & (master_mil['year'] <= 2014)]


country_count = pd.crosstab(index=master_mil['country'], columns='count')
complete_country = country_count[country_count['count']==72]

#try seaborn instead
test = sns.lineplot(x='year', y='gdp_per_capita ($)', hue='country', data=master_mil_1114[master_mil_1114['country'].isin(['United States', 'United Kingdom', 'Japan'])])
plt.xlabel('year')
plt.ylabel('GDP per Capita ($)')
plt.title('GDP per Capita among Millenials in US, UK, and Japan')
plt.legend()
plt.show()