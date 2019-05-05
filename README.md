# CRISP-DM process for data analysis

### Introduction
Cross Industry Standard Process for Data Mining helps in understanding the data. In this project, I have used Montreal, Airbnb dataset for answer the following questions:
* Which season is best for promotion and advertisement of Airbnb?
* Which Montreal area has best rooms available?
* Is there any similar type of listing available?

### Dataset
I have used Montreal Airbnb dataset. I have used their two csv files
* [listing.csv](http://data.insideairbnb.com/canada/qc/montreal/2019-03-11/data/listings.csv.gz)
* [calendar.csv](http://data.insideairbnb.com/canada/qc/montreal/2019-03-11/data/calendar.csv.gz)

### Libraries
* Numpy  
<code>pip install numpy</code>
* Pandas  
<code>pip install pandas</code>
* Seaborn  
<code>pip install seaborn</code>
* Matplotlib  
<code>pip install matplotlib</code>
* Scikit-Learn  
<code>pip install scikit-learn</code>

### Motivation
The motivation behind this project is to increase the profit of Airbnb Montreal by finding out
dips in the season which will help the Airbnb to promote and advertise itself. Then, finding
the best area to book a room, which will help the Airbnb customers to have the best in class rooms.
At the end, recommending similar types of room, a user wants to book.

### Summary
* Which season is best for promotion and advertisement of Airbnb?
> Overall, we need to focus on advertisements and promotions during the period of "2019-04" 
to "2019-09". During this period, we will target the audience only on ['Monday', 'Tuesday', 
'Wednesday', 'Sunday'].

* Which Montreal area has best rooms available?
> Overall, we cay that H2X, H2Y 0A8, H3B are some of the zipcode areas where anyone can find
best rooms based on customer reviews and superhost availability.

* Is there any similar type of listing available?
> Using cosine similarity on TF-matrix defined by using TfidfVectorizer() method on name and
description column of dataset, we can find some similar recommendation of rooms.

### References
* Udacity's DataScience Process chapter
* [Kaggle Recommendation system](https://www.kaggle.com/barkincavdaroglu/airbnb-content-based-recommendation-system)



