# Project: Trends of Suicide Rate 3 High-Rate Countries compared to United States



## Project Question
The study question of this project is to identify the trends of suicide rates over years for 3 countries (Lithuania, Sri Lanka, Russian Federation), and compare the trends to that of the US.

--------------------------------------------------------------------------------------------------------------------

## Dataset
The dataset is obtained from www.Kaggle.com/datasets under "Suicide Rates Overview 1985 to 2016".

### Description from Kaggle Website:
**Content**  

This compiled dataset pulled from four other datasets linked by time and place, and was built to find signals correlated to increased suicide rates among different cohorts globally, across the socio-economic spectrum.  

**References**
* United Nations Development Program. (2018). Human development index (HDI).
* World Bank. (2018). World development indicators: GDP (current US$) by country:1985 to 2016.
* [Szamil]. (2017). Suicide in the Twenty-First Century [dataset].
* World Health Organization. (2018). Suicide prevention.  

**Inspiration**  

Suicide Prevention.
---------------------------------------------------------------------------------------------------------------

## Method
* First identify countries with the highest average suicide rates and then select the top 3 to compare trends with the US.

* With Seaborn package, draw trends of suicide rates / 100k in these countries.
--------------------------------------------------------------------------------------------------------------

## Importing package and data
```
##Importing package and data
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

master = pd.read_csv('Project Contents/master.csv')

master.head()
master.columns

master_mean_country_year = 
pd.DataFrame(master.groupby(['country'])['suicides/100k pop'].mean()).
sort_values(by=['suicides/100k pop'], ascending=False)[0:3]
## The highest average suicide rates are in countries: Lithuania, Sri Lanka, 
and Russian Federation

select_country = master['country'].isin(master_mean_country_year.index.tolist() 
+ ['United States'])

master_select_country = master[select_country]

test = sns.lineplot(x='year', y='suicides/100k pop', hue='country', 
data=master_select_country)
plt.xlabel('year')
plt.ylabel('Suicide Rate per 100k People')
plt.title('Suicide Rate per 100k People\n'
          'in Lithuania, Sri Lanka, 
          Russian Federation, 
          and the United States')
          
plt.legend()
fig = test.get_figure()

fig.savefig("Project Contents/Trend Graphs.png")
```

## Seaborn Graph
![](https://raw.githubusercontent.com/biof309/spring2019-solo-project-lai1737/master/Project%20Contents/Trend%20Graphs.png)
-------------------------------------------------------------------------------------------------------------------------
## If I had more time... or sometime in the future...
1. See if the trends are decreasing significantly
2. See if the trend for the US is significant at all
3. Look at more countries
4. Predict future trends for country of interest
