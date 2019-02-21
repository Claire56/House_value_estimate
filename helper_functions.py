import pandas as pd
from flask import request, session

df = pd.read_csv("pop_cities.csv")
df = df.drop(['Unnamed: 0', 'Unnamed: 0.1','zip_code'],axis =1 )

def column_names():
	# takes in nothing and returns a list of column names
    
    cols = df.columns.tolist() #make list 
    return cols

def x_features():
	 #drop the price column and return a list of remaining columns

    return df.drop('sale_price', axis =1 ).columns



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


