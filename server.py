from flask import Flask ,render_template,sessions , request ,redirect
from flask_debugtoolbar import DebugToolbarExtension
from jinja2 import StrictUndefined
from sklearn.externals import joblib
import ml_model


app = Flask('__name__')
app.jinja_env.undefined = StrictUndefined
app.jinja_env.auto_reload = True

# Required to use Flask sessions and the debug toolbar
app.secret_key = "nabawanda"

# House_features = ['year_built ','stories' ,'beds' ,'full_baths ','half_baths']
# House_features2 = ['livable_sqft', 'total_sqft','garage_sqft','carport_sqft']
# more_features =['fireplace ','pool','central_heating','central_cooling']

# features = ['garage_type_attached', 'garage_type_detached']
# cities = ['East_Lucas','North_Erinville','Port_Andrealand','Port_Jonathanborough', 'Wendybury','West_Ann']
features = ml_model.home_features()


#Add Routes
@app.route('/')
def homepage():

	return render_template('homepage.html')


@app.route('/home-info')
def home_info():
	return render_template('home_info.html', features =features)

# @app.route('/home-info')
# def home_info():
	
	

# 	return render_template('home_info.html', features = features, cities=cities,
# 		more_features=more_features ,House_features=House_features)
	
# @app.route('/value')
# def home_value():
# 	year_built = request.args.get('year_built')
# 	stories = request.args.get('stories')
# 	beds = request.args.get('beds')
# 	full_baths = request.args.get('full_baths')
# 	zipcode = request.args.get('zipcode')
# 	half_baths = request.args.get('half_baths')
# 	livable_sqft = request.args.get('livable_sqft')
# 	total_sqft = request.args.get('total_sqft')
# 	garage_sqft = request.args.get('garage_sqft')
# 	carport_sqft = request.args.get('carport_sqft')
# 	fireplace = request.args.get('fireplace')    
# 	pool = request.args.get('pool')
# 	central_cooling = request.args.get('central_cooling')
# 	central_heating = request.args.get('central_heating')    #
# 	sale_price = request.args.get('sale_price')
# 	garage_type_detached = request.args.get('garage_type_detached')
# 	garage_type_attached = request.args.get('garage_type_attached') 
# 	Wendybury = request.args.get('Wendybury')
# 	East_Lucas = request.args.get('East_Lucas')
# 	North_Erinville = request.args.get('North_Erinville')
# 	Port_Andrealand = request.args.get('Port_Andrealand')
# 	Port_Jonathanborough = request.args.get('Port_Jonathanborough')
# 	West_Ann = request.args.get('West_Ann')


# 	Home_features = [year_built,stories,beds,full_baths,zipcode,half_baths,livable_sqft,
#     total_sqft, garage_sqft ,carport_sqft, fireplace, pool ,central_heating, central_cooling,
#     				garage_type_attached, garage_type_detached, Wendybury , West_Ann ,Port_Jonathanborough,
#     				Port_Andrealand ,North_Erinville , East_Lucas ]

# 	model = joblib.load('trained_model.pkl')

# 	predicted = model.predict([Home_features])

# 	return render_template('home_value.html', predicted = predicted)


@app.route('/locaton_value')
def loc_value():
	pass



@app.route('/sht_value')
def get_value():
	
	home_features = [request.args.get(i) or 0.0 for i in features]

	model = joblib.load('trained_model.pkl')

	predicted = model.predict([home_features])
	predicted = round(predicted[0],2)

	return render_template('home_value.html', predicted = predicted)

	
		








if __name__== "__main__":


	# debug=True gives us error messages in the browser and also "reloads"
	# the web app if we change the code.


	# Use the DebugToolbar
    DebugToolbarExtension(app)



    app.run(debug = True , host = "0.0.0.0")