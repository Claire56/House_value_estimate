from flask import Flask ,render_template,sessions , request ,redirect
from flask_debugtoolbar import DebugToolbarExtension
from jinja2 import StrictUndefined
from sklearn.externals import joblib
from delete import x_features

app = Flask('__name__')
app.jinja_env.undefined = StrictUndefined
app.jinja_env.auto_reload = True

# Required to use Flask sessions and the debug toolbar
app.secret_key = "nabawanda"


features = x_features()


#Add Routes
@app.route('/')
def homepage():

	return render_template('homepage.html')


@app.route('/home-info')
def home_info():
	return render_template('home_info.html', features =features)




@app.route('/locaton_value')
def loc_value():
	pass



@app.route('/sht_value')
def get_value():
	# function used a get request to get the values of the user inputs, 
	# use it to estimate house value and return the estimate to the user. 
	
	home_features = [request.args.get(i) or 0.0 for i in features]
	print(home_features)

	# change the strings recieved back to number
	home_features = [1 if feature == 'on' else feature for feature in home_features]
	print(home_features)

	# use the trained data to estimate the value 
	model = joblib.load('trained_model.pkl')
	# model = joblib.load('reg_model.pkl')#data type error
	# model = joblib.load('knn_model.pkl')
	predicted = model.predict([home_features])


	# format the results of the prediction
	predicted = round(predicted[0],2)
	predicted = "{:,}".format(predicted)

	return render_template('home_value.html', predicted = predicted)




if __name__== "__main__":


	# debug=True gives us error messages in the browser and also "reloads"
	# the web app if we change the code.


	# Use the DebugToolbar
    DebugToolbarExtension(app)



    app.run(debug = True , host = "0.0.0.0")