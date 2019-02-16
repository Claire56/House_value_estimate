import pandas as pd
import numpy as np
from pandas import Series, DataFrame


from sklearn import ensemble
from sklearn.metrics import mean_absolute_error
from sklearn.externals import joblib
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

import matplotlib.pyplot as plt


# Load the cleaned data
data = pd.read_csv("pop_cities.csv")


#drop columns that are not needed
data = data.drop(columns=['Unnamed: 0', 'Unnamed: 0.1','zip_code'])


## considering to remove 'zip_code'

# Replace categorical data with one-hot encoded data in the DataCleaningipnb.
#data = pd.get_dummies(data, columns=['garage_type', 'city'])

# create x and y
X = data.drop('sale_price', axis =1 )
y = data['sale_price']


print(X.columns)

# Create the X and y arrays
X = X.values
y = y.values

# Split the data set in a training set (70%) and a test set (30%)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)

# Fit regression model
model = ensemble.GradientBoostingRegressor(
    n_estimators=900,
    learning_rate=0.08,
    max_depth=6,
    min_samples_leaf=9,
    max_features=0.1,
    loss='huber',
    random_state=0
)
model.fit(X_train, y_train)

# Save the trained model to a file so we can use it in other programs
joblib.dump(model, 'trained_model.pkl')
#get the score for the model
print(model.score(X_test ,y_test))


#helper functions
def home_features():
	return data.drop('sale_price', axis =1 ).columns


