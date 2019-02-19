import pandas as pd
import numpy as np
from pandas import Series, DataFrame


from sklearn import ensemble
from sklearn.metrics import mean_absolute_error
from sklearn.externals import joblib
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from data_model import House

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.inspection import inspect


db = SQLAlchemy()


def modeling(house_table):
    # Load the cleaned data
    # data = pd.read_csv("pop_cities.csv")
    data = House.query().all()
    data = db.session.query(House).all()
    df = pd.DataFrame([(d.candid, d.rank, d.user_id) for d in data], 
                  columns=['candid', 'rank', 'user_id'])

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

    # Find the error rate on the training set
    mse = mean_absolute_error(y_train, model.predict(X_train))
    print("Training Set Mean Absolute Error: %.4f" % mse)

    # Find the error rate on the test set
    mse = mean_absolute_error(y_test, model.predict(X_test))
    print("Test Set Mean Absolute Error: %.4f" % mse)
    return model 


#helper functions
def home_features():
	return data.drop('sale_price', axis =1 ).columns

if __name__ == "__main__":
    # As a convenience, if we run this module interactively, it will leave
     from server import app




     rough 
     class LPRRank(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    candid = db.Column(db.String(40), index=True, unique=False)
    rank = db.Column(db.Integer, index=True, unique=False) 
    user_id = db.Column(db.Integer, db.ForeignKey('lprvote.id'))

    def __init__(self, candid=None, rank=None, user_id=None):
        self.data = (candid, rank, user_id)

    def __repr__(self):
        return (self.candid, self.rank, self.user_id) 

data = db.session.query(LPRRank).all()
df = pd.DataFrame([(d.candid, d.rank, d.user_id) for d in data], 
                  columns=['candid', 'rank', 'user_id'])