# Project: Trend of Suicide Rate in x Countries compared to United States
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