from flask import Flask ,render_template, session,jsonify, request ,redirect, make_response
from flask_debugtoolbar import DebugToolbarExtension
from jinja2 import StrictUndefined
from sklearn.externals import joblib
from helper_functions import x_features 
from sqlalchemy import func
import pandas as pd
import data_model as dm
from decimal import Decimal
import json


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
	# this function renders the information page
	values = {} #create an empty dictionary to store cookies
	for feature in features:
		values[feature] = request.cookies.get(feature)

	print("Session data: %s" % session.get('Year'))#work on sessions look at helper functions

	return render_template('home_info.html', features=features, values=values)




@app.route('/sht_value')
def get_value():
	# function used a get request to get the values of the user inputs, 
	# use it to estimate house value and return the estimate to the user. 
    home_features = [request.args.get(i) or 0.0 for i in features]
    print(home_features)
    city =''
    for feature in features[15:]:
        print(request.args.get(feature))
        if request.args.get(feature)== "on":
            print(feature)
            city = feature

    chosen_city = city
    print(chosen_city)

    # change the strings recieved back to number
    home_features = [1 if feature == 'on' else feature for feature in home_features]
    home_features = [1 if feature == 'None' else feature for feature in home_features]

    # use the trained data to estimate the value 
    model = joblib.load('trained_model.pkl')
    # model = joblib.load('reg_model.pkl')#data type error
    # model = joblib.load('knn_model.pkl')
    predicted = model.predict([home_features])


    # format the results of the prediction
    predicted = round(predicted[0],2)
    predicted = "{:,}".format(predicted)

    resp = make_response(render_template('home_value.html', predicted=predicted, chosen_city=chosen_city))

    # set cookies (giving the user previous info entered)
    for feature in features:
    	feature_value = request.args.get(feature) #get value given by user
    	if feature_value:
    		resp.set_cookie(feature, feature_value) #set the cookie to feature value

    session['Year'] = request.args.get('year_built')

    return resp



@app.route('/statistics')
def show_stats():
	#do some coding here to produce the graphs 
	return render_template('statistics.html')

@app.route('/charts') #madi help
def charts():
    #do some coding here to produce the graphs 
    

    return render_template('charts.html')

@app.route('/stats.json')
def stats_data():
    """Return data about packages popularity."""
    d = pd.read_csv('year.csv')
    print(d.columns)

    data_dict = {
    

                "labels": ['1901-1917','1918-1934','1935-1950',
                '1951-1967','1968-1984','1985-2001','2002-2018' ]                 
                             ,    
             
                "datasets": [
                    {
                        "data": [1,7,30,61,354,2531,4744],
                        "backgroundColor": [
                            "orange",
                            "pink",
                            "#FFCE56"
                            "white",
                            "red",
                            "yellow",
                            "green"
                                
    

                        ],
                        "hoverBackgroundColor": [
                            "#FF6384",
                            "#36A2EB",
                            "#FFCE56",
                            "green",
                            "red",
                            "#FFCE56"
                            "yellow"
                        ]
                    }]
            }
    return jsonify(data_dict)

@app.route('/scatter.json')
def scatter_data():
    houses = dm.House.query.all()
    data =[house.get_chart() for house in houses]

    # a = [ big list comp]

    return jsonify(points=data)

@app.route('/mean_price_bed.json')
def bed_mean_data():

    beds = dm.House.query.with_entities(dm.House.num_bedrooms,
        func.avg(dm.House.sale_price)).group_by(dm.House.num_bedrooms).all()

    data = json.dumps(beds, cls=dm.DecimalEncoder)# print(beds)
    # data = [bed.avg_by_beds() for bed in beds]

    # a = [ big list comp]

    return jsonify(data)





if __name__== "__main__":


	# debug=True gives us error messages in the browser and also "reloads"
	# the web app if we change the code.


	# Use the DebugToolbar
    DebugToolbarExtension(app)
    dm.connect_to_db(app)



    app.run(debug = True , host = "0.0.0.0")