import pandas as pd

#dataframeはディクショナリと同じ形、ラベルはリストと同じ形になる。
pd.DataFrame({'yes': [50, 21], 'no':[131, 2]})

pd.DataFrame({'Bob': ['I liked it.', 'It was awful.'], 
              'Sue': ['Pretty good.', 'Bland.']}, 
              index = ['Product A', 'Product B'] ) 

data = pd.Series([0,1,2], index = ["a","b","c"], name = "test data")
#print(data)

#index_col インデックスが始める値？
reviews = pd.read_csv("winemag-data-130k-v2.csv", index_col = 1)
print(reviews)
#dataframeはseriesの寄せ集めと考えられる。

