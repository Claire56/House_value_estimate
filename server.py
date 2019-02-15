from flask import Flask ,render_template,sessions , request ,redirect
from flask_debugtoolbar import DebugToolbarExtension
from jinja2 import StrictUndefined


app = Flask('__name__')
app.jinja_env.undefined = StrictUndefined
app.jinja_env.auto_reload = True

# Required to use Flask sessions and the debug toolbar
app.secret_key = "nabadda"

House_features = ["No of Bedrooms", "No of Bathrooms","Has swimmingpool", 
 'Year Built', 'Number of Stories', 'size in sqr feet', 'What City should we use',]

boolean_features = ['Garage attached', 'Side Garage', 'Car port','Fire place',
 'Central Heating', 'Central Cooling']

#Add Routes
@app.route('/')
def homepage():

	return render_template('homepage.html')

@app.route('/home-info')
def home_info():
	features = House_features

	return render_template('home_info.html', features = features, 
		boolean_features = boolean_features)
	
app.route('/value')
def home_value():
	

	return render_template('home_value.html')


app.route('/locaton_value')
def loc_value():
	pass










if __name__== "__main__":


	# debug=True gives us error messages in the browser and also "reloads"
	# the web app if we change the code.


	# Use the DebugToolbar
    DebugToolbarExtension(app)



    app.run(debug = True , host = "0.0.0.0")