# importing libraries
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

###############################################################################\

cal_df = pd.read_csv('./dataset/calendar.csv')

cal_cols = list(cal_df.columns)

print(cal_df['date'].min())
print(cal_df['date'].max())
print(cal_df.isnull().sum())

# changing the datatype of date attribute
cal_df['date'] = pd.to_datetime(cal_df['date'])

season = cal_df[cal_df['available']=='f']
season = season.groupby('date')['listing_id'].count().reset_index()
season['month'] = season['date'].dt.strftime('%b')
season['day'] = season['date'].dt.day

plt.plot(season['date'], season['listing_id'])
plt.title('Booking Demand')
plt.xlabel('date')
plt.xticks(rotation='vertical')
plt.ylabel('listing');

season['weekday'] = season['date'].dt.weekday_name

sub_season_1 = season[(season['date']>='2019-03-11')& \
                      (season['date']<='2019-06-08')]
sub_season_2 = season[(season['date']>='2019-06-09')& \
                      (season['date']<='2019-09-06')]
sub_season_3 = season[(season['date']>='2019-09-07')& \
                      (season['date']<='2020-03-09')]

sns.violinplot(x='weekday', y='listing_id', data=sub_season_1, inner = 'quartile')
plt.xticks(rotation='vertical')
plt.show()

sns.violinplot(x='weekday', y='listing_id', data=sub_season_2, inner = 'quartile')
plt.xticks(rotation='vertical')
plt.show()

sns.violinplot(x='weekday', y='listing_id', data=sub_season_3, inner = 'quartile')
plt.xticks(rotation='vertical')
plt.show()

