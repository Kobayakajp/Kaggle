import pandas as pd

reviews = pd.read_csv("winemag-data-130k-v2.csv",index_col = 0)

#print(reviews)

#loc, iloc,indexの振る舞いが違う

#全ての行の0列目を出力する。
reviews_country = reviews.iloc[:,0]
#print(reviews_country)

#ilocではできない操作
reviews_country = reviews.loc[:,'country']

#listを引数として渡すこともできる
reviews.loc[:, ['taster_name', 'taster_twitter_handle', 'points']]

#表から国がItalyのものだけを抽出する
reviews_Italy = reviews.loc[reviews.country == 'Italy']
print(reviews_Italy)

#条件分は複数かける
reviews_Italy = reviews.loc[(reviews.country == 'Italy') & (reviews.points >= 90)]

