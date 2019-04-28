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

###############################################################################

list_df = pd.read_csv('./dataset/listings.csv')

list_df = list_df.dropna(subset=['host_is_superhost','zipcode', 'reviews_per_month'], axis=0)

grouped_list_df = list_df.groupby('zipcode')['reviews_per_month'].count().sort_values(ascending=False).reset_index()
grouped_list_df = grouped_list_df.head(10)
grouped_list_df = grouped_list_df.sort_values(by=['zipcode'])

sns.barplot(data=grouped_list_df, x='zipcode', y='reviews_per_month')
plt.xticks(rotation='vertical')
plt.show()

sub_list_df = list_df.loc[list_df['zipcode'].isin(grouped_list_df['zipcode'])]
sub_list_df = sub_list_df.sort_values(by=['zipcode'])
sns.boxplot(data=sub_list_df, x='zipcode', y='reviews_per_month')
plt.xticks(rotation='vertical')
plt.show()


grouped_list_df = list_df.groupby('zipcode')['reviews_per_month'].sum().sort_values(ascending=False).reset_index()
grouped_list_df = grouped_list_df.head(10)
grouped_list_df = grouped_list_df.sort_values(by=['zipcode'])

sns.barplot(data=grouped_list_df, x='zipcode', y='reviews_per_month')
plt.xticks(rotation='vertical')
plt.show()


sub_list_df = list_df.loc[list_df['zipcode'].isin(grouped_list_df['zipcode'])]
sub_list_df = sub_list_df.sort_values(by=['zipcode'])
sns.boxplot(data=sub_list_df, x='zipcode', y='reviews_per_month')
plt.xticks(rotation='vertical')
plt.show()


new_list_df = list_df.loc[list_df['host_is_superhost'] == 't']
grouped_list_df = new_list_df.groupby('zipcode')['host_is_superhost'].count().sort_values(ascending=False).reset_index()
grouped_list_df = grouped_list_df.head(10)
grouped_list_df = grouped_list_df.sort_values(by=['zipcode'])

sns.barplot(data=grouped_list_df, x='zipcode', y='host_is_superhost')
plt.xticks(rotation='vertical')
plt.show()

###############################################################################

list_df = pd.read_csv('./dataset/listings.csv')


new_df = list_df[['id', 'name', 'description']]

list_df['name'] = list_df['name'].astype('str')
list_df['description'] = list_df['description'].astype('str')

new_df.isnull().sum()


new_df['content'] = new_df[['name', 'description']].astype(str).apply(lambda x: ' // '.join(x), axis = 1)

new_df = new_df.drop(['name', 'description'], axis=1)


from sklearn.feature_extraction.text import TfidfVectorizer
tf = TfidfVectorizer()
tf_matrix = tf.fit_transform(new_df['content'])


from sklearn.metrics.pairwise import linear_kernel
cosine_similarities = linear_kernel(tf_matrix, tf_matrix)


results = {}
for idx, row in new_df.iterrows():
    similar_indices = cosine_similarities[idx].argsort()[:-100:-1]
    similar_items = [(cosine_similarities[idx][i], new_df['id'][i]) for i in similar_indices]
    results[row['id']] = similar_items[1:]
   
 
def item(id):
    name   = new_df.loc[new_df['id'] == id]['content'].tolist()[0].split(' // ')[0]
    desc   = ' \nDescription: ' + new_df.loc[new_df['id'] == id]['content'].tolist()[0].split(' // ')[1][0:165] + '...'
    prediction = name  + desc
    return prediction

def recommend(item_id, num):
    print('Recommending ' + str(num) + ' products similar to ' + item(item_id))
    print('---')
    recs = results[item_id][:num]
    for rec in recs:
        print('\nRecommended: ' + item(rec[1]) + '\n(score:' + str(rec[0]) + ')')


recommend(item_id = 29061, num = 5)

