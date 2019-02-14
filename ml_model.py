import pandas as pd
import numpy as np
from pandas import Series, DataFrame


from sklearn import ensemble
from sklearn.metrics import mean_absolute_error
from sklearn.externals import joblib
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

import seaborn as sb
import matplotlib.pyplot as plt
%matplotlib inline
from matplotlib import rcParams
rcParams['figure.figsize'] = 6, 4
sb.set_style('whitegrid')




# Load the cleaned data
data = pd.read_csv("pop_cities.csv")


#drop columns that are not needed
data = data.drop(columns=['house_number','street_name','unit_number','Year_levels'])

## considering to remove 'zip_code'

# Replace categorical data with one-hot encoded data
features = pd.get_dummies(data, columns=['garage_type', 'city'])

# Remove the sale price from the features data
del features['sale_price']

# Create the X and y arrays
X = features.values()
y = data['sale_price'].values()

# Split the data set in a training set (70%) and a test set (30%)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)

# Fit regression model
model = ensemble.GradientBoostingRegressor(
    n_estimators=1000,
    learning_rate=0.1,
    max_depth=6,
    min_samples_leaf=9,
    max_features=0.1,
    loss='huber',
    random_state=0
)
model.fit(X_train, y_train)

# Save the trained model to a file so we can use it in other programs
joblib.dump(model, 'trained_house_classifier_model.pkl')
#get the score for the model
model.score
