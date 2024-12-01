import pandas as pd

reviews = pd.read_sql("winemag-data-130k-v2.csv")

print(reviews)