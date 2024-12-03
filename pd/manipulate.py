import pandas as pd

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

