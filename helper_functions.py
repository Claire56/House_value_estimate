import pandas as pd
import numpy as np
import seaborn as sb
import matplotlib.pyplot as plt
from matplotlib import rcParams

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split


rcParams['figure.figsize'] = 6, 4
sb.set_style('whitegrid')

from flask import request, session

################################################################################

df = pd.read_csv("pop_cities.csv")
df = df.drop(['Unnamed: 0', 'Unnamed: 0.1','zip_code'],axis =1 )

def column_names():
	# takes in nothing and returns a list of column names
    
    cols = df.columns.tolist() #make list 
    return cols

def x_features():
	 #drop the price column and return a list of remaining columns

    columns = df.drop('sale_price', axis =1 ).columns
    columns = [c.replace(' ', '_') for c in columns]
    return columns

# statistics for the visuals
def stat_data():
	d = df[['sale_price','num_bedrooms', 'has_fireplace','year_built']]
	bins = np.linspace(1900,2018, num =8)  #create bins => np.linspace(min,max,numberOfBins)
	d["Year_levels"] = pd.cut(d['year_built'],bins,labels= ['1901-1917','1918-1934','1935-1950','1951-1967','1968-1984','1985-2001','2002-2018'])#divide dataset
	return d.groupby("Year_levels").size()

	
def get_chosen_city():
    # function used a get request to get the values of the user inputs, 
    # use it to estimate house value and return the estimate to the user. 
    features = x_features()
    city = ''
    print (features)
    for feature in features[15:]:
    	print(request.args.get(feature))
    	if request.args.get(feature)== "None":
        	print(feature)
        	city = feature
    return city


def hash_password(password):
	import hashlib, binascii
	dk = hashlib.pbkdf2_hmac('sha256', password, b'claire', 100000)
	return binascii.hexlify(dk)

def registration():
	username = request.form.get('username')
	password = request.form['password']
	hashed_password = hash_password(password)
	store_to_db(username, hashed_password) #finnd a way to store this

def login():
	username = request['username']
	password = request['password']
	hashed_password = hash_password(password)
	stored_hashed_password = get_from_db(username) # get from db is fiction too
	if hashed_password == stored_hashed_password:
		print('login successful')
		session['username'] = username #better to store userid than name in the session
	else:
		print('login failed')

def other_page():
	username = session.get('username')
	if not username:
		# redirect to login
		return request.redirect('login')

	some_info = get_user_info(username)

stats1 = pd.read_csv('stats1.csv')
# stats1 = stats1.drop(Unnamed: 0')
# print(claire.columns)

