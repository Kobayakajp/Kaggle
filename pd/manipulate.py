import pandas as pd

<<<<<<< HEAD
reviews = pd.read_csv("winemag-data-130k-v2.csv", index_col = 0)
pd.set_option('display.max_row', 5)

print(reviews)
#表の中のcoutryだけを表示
print(reviews.country)
print(reviews['country'])

#表の０行目を表示
print(reviews.iloc[0])
#print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
#表における1~3行、0列目を表示
print(reviews.iloc[:3,0])

#表における後ろから5行の全部を表示
print(reviews.iloc[-5:,:])

#表にtitleを挿入
reviews.set_index("title")
#print(reviews)

#表のcountryがItalyであるものを表示
print(reviews.loc[reviews.country == 'Italy'])
=======
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
>>>>>>> 46a4454d59f7f3f3668ff636c94599255d738ee5

