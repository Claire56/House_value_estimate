import pandas as pd
import numpy as np
from pandas import Series, DataFrame


from sklearn import ensemble
from sklearn.metrics import mean_absolute_error
from sklearn.externals import joblib
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split,GridSearchCV
# from data_model import House
from helper_functions import df

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.inspection import inspect


db = SQLAlchemy()

def Gsmodel():
    data = df()
    X = data.drop('sale_price', axis =1 ).values
    y = data['sale_price'].values
    X_train, X_test, y_train, y_test = train_test_split(X, y,
     test_size=0.2, random_state=0)

    gsmodel = ensemble.GradientBoostingRegressor()

    param_grid = {'n_estimators':[1000,500,300,200],
        'learning_rate': [0.1,0.08,0.5,0.02],
        'max_depth':[6,4,2],
        'min_samples_leaf': [9,3,5,16],
        'max_features':[0.1,1, 0.3],
        'loss':['huber','ls','lad'],
        'random_state':[0,2,5]
    }

    gs_cv = GridSearchCV(gsmodel,param_grid,n_jobs =4)

    gs_cv.fit(X_train, y_train)
    # print(gs_cv.best_params)

    # Find the error rate on the training set
    mse = mean_absolute_error(y_train, gs_cv.predict(X_train))
    print("GS -Training Set Mean Absolute Error: %.4f" % mse)

    # Find the error rate on the test set
    mse = mean_absolute_error(y_test, gs_cv.predict(X_test))
    print("GS -Test Set Mean Absolute Error: %.4f" % mse)
    


def modeling(house_table):
    # Load the cleaned data
    data = df()
    # data = House.query().all()
    # data = db.session.query(House).all()
    # df = pd.DataFrame([(d.candid, d.rank, d.user_id) for d in data], 
    #               columns=['candid', 'rank', 'user_id'])

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


if __name__ == "__main__":
    # As a convenience, if we run this module interactively, it will leave
     # from server import app
     Gsmodel()



