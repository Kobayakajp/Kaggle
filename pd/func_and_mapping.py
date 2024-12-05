import pandas as pd
pd.set_option('display.max_rows', 5)
import numpy as np
reviews = pd.read_csv("winemag-data-130k-v2.csv", index_col=0)

description_series = reviews.description

description_counts = description_series.describe()
#print(description_series)
#print(description_counts)

n_trop = reviews.description.map(lambda desc: "tropical" in desc).sum()
n_fruity = reviews.description.map(lambda desc: "fruity" in desc).sum()
descriptor_count = pd.Series([n_trop, n_fruity], index = ['tropical', 'fruity'])

#print(descriptor_count)

def stars(row):
    if row.country == 'Canada':
        return 3
    elif row.points >=95:
        return 3
    elif row.points >= 85:
        return 2
    else:
        return 1 
    
star_ratings = reviews.apply(stars, axis = 'columns')
print(star_ratings)