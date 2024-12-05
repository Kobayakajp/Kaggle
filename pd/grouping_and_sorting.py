import pandas as pd

reviews = pd.read_csv("winemag-data-130k-v2.csv")

print(reviews.groupby('points').points.count())

