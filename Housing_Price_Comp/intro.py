import pandas as pd

#save file path to variable
melbourne_file_path = 'melb_data.csv'

#read the data and store data in DataFrame
melbourne_data = pd.read_csv(melbourne_file_path)

#print summary of the data in Melbourne data
#print(melbourne_data.describe())

print(melbourne_data.columns)

#dropna drops missing values (thinks of na as "not available")
melbourne_data = melbourne_data.dropna(axis = 0)

#selecting the prediction target
y = melbourne_data.Price
#print(y)


#choosing features
melbourne_features = ['Rooms', 'Bathroom', 'Landsize', 'Lattitude', 'Longtitude']
X = melbourne_data[melbourne_features]

print(X.describe())
print(X.head)

