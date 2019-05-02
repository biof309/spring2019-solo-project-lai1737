# Project: Trend of Suicide Rate in x Countries compared to United States

##Project Question
The study question of this project is to identify the trends of suicide rates over years for x countries, and compare the trends to that of the US.

##Method
* First identify countries with the highest average suicide rates and then select the top 3 to compare trends with the US.

* With Seaborn package, draw trends of suicide rates / 100k in these countries.

##Importing package and data
```
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cross_validation import train_test_split
import seaborn as sns
import numpy as np

master = pd.read_csv('master.csv')

master.head()

##Preliminary frequency table to see what generations there are
pd.crosstab(index=master['generation'], columns='count')

### Filter for "Millenials"
master_mil = master[master['generation']=='Millenials']
master_mil_1114 = master_mil[(master_mil['year'] >= 2011) & (master_mil['year'] <= 2014)]

master_mil.columns

pd.crosstab(index=master_mil['year'], columns='count')

plt.plot('year', 'gdp_per_capita ($)', data=master_mil_1114[master_mil['country']=='United States'], color='skyblue', label='United States')
plt.plot('year', 'gdp_per_capita ($)', data=master_mil_1114[master_mil['country']=='Canada'], color='red', label='Canada')
plt.plot('year', 'gdp_per_capita ($)', data=master_mil_1114[master_mil['country']=='United Kingdom'], color='black', label='United Kingdom')
plt.legend()
```

##Seaborn Graph
plt.show()