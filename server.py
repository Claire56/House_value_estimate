from flask import Flask ,render_template, session,jsonify, request ,redirect, make_response
from flask_debugtoolbar import DebugToolbarExtension
from jinja2 import StrictUndefined
from sklearn.externals import joblib
from helper_functions import x_features ,best5
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
features =[f.replace('_',' ') for f in features ]
features =[f.replace('city','') for f in features ]
print(f'these are the {features}')


#Add Routes
@app.route('/')
def homepage():

	return render_template('homepage.html')

@app.route('/login')
def login():
    #do some coding here to produce the graphs 
    return render_template('login.html')
@app.route('/loginfo')
def loginfo():
    #do some coding here to produce the graphs 
    return render_template('loginfo.html')

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
    # Show which features have been set

    print("\n:::FORM DATA:::")
    for f in features:
        if f in request.args:
            print(f, ":", request.args.get(f))
        else:
            print(f, ":", "(not submitted)")
    print(":::END FORM DATA:::")

    home_features = [request.args.get(i) or 0.0 for i in features]
    print(home_features)
    city =''
    for feature in features[15:]:
        print(request.args.get(feature))
        if request.args.get(feature)== "None":
            print(feature)
            city = feature

    chosen_city = city
    graph_city = 'city'+chosen_city.replace(' ',"_")
    session['city'] = graph_city
    print(graph_city)

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
@app.route('/pop')
def popularity():

    return render_template('popularity.html') 

@app.route('/avg_price')
def avg_price():

    return render_template('avg_price.html') 

@app.route('/charts') #madi help
def charts():
    #do some coding here to produce the graphs 
    return render_template('charts.html')
@app.route('/relations')
def relations():

    return render_template('relations.html')


@app.route('/grg.json')
def grg_data():
    #do some coding here to produce the graphs
    data = best5()
    data = data[['garage_type', 'sale_price']].groupby('garage_type').mean()

    jdata = data.to_json() #this can jsonify a dataframe but dont need it 

    data = { "labels": ['garage attached','Detached','None'], #"data": [round(i,2) for i in y]}

              "datasets" : [ 
              {
                        "data": [round(i,2) for i in data.sale_price],
                        "backgroundColor": ['pink', 'yellow','grey'],
                        'collectionAlias': "Average Price",
                        'label': "Average price per garage type ",
                            
                         }
                    ]
              }         

    return jsonify(data)



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
    houses = dm.House.query.filter(dm.House.sale_price <3000000).all()
    data =[house.get_chart() for house in houses]

    # a = [ big list comp]

    return jsonify(points=data)

@app.route('/mean_price_bed.json')
def bed_mean_data():

    beds = dm.House.query.with_entities(dm.House.num_bedrooms,
        func.avg(dm.House.sale_price)).group_by(dm.House.num_bedrooms).order_by(dm.House.num_bedrooms).all()

    jdata = json.dumps(beds, cls=dm.DecimalEncoder)# print(beds)
    # data = [bed.avg_by_beds() for bed in beds]
    data = json.loads(jdata)
    x = [i[0] for i in data]
    y = [i[1] for i in data]

    data = { "labels": x, #"data": [round(i,2) for i in y]}

              "datasets" : [ 
              {
                        "data": [round(i,2) for i in y],
                        "backgroundColor": ['purple']*11,
                        'collectionAlias': "Average Price",
                        'label': "Average price per No of bedrooms ",
                            
                         }
                    ]
              }          
    return jsonify(data)
@app.route('/pool.json')
def pool_mean_data():

    pool = dm.House.query.with_entities(dm.House.has_pool,
        func.avg(dm.House.sale_price)).group_by(dm.House.has_pool).all()

    jdata = json.dumps(pool, cls=dm.DecimalEncoder)# uses DecimalEnconder to make json
    
    data = json.loads(jdata) #send data back to json
    print(data) # data is a list of lists
    x = [i[0] for i in data]
    y = [i[1] for i in data]

    data = { "labels": ['None','Swimming Pool'], #"data": [round(i,2) for i in y]}

              "datasets" : [ 
              {
                        "data": [round(i,2) for i in y],
                        "backgroundColor": ['red','green'],
                        'collectionAlias': "Average Price",
                        'label': "Average price ",
                            
                         }
                    ]
              }          
    return jsonify(data)

@app.route('/has_fireplace.json')
def fireplace_data():

    fireplace = dm.House.query.with_entities(dm.House.has_fireplace,
        func.avg(dm.House.sale_price)).group_by(dm.House.has_fireplace).all()

    jdata = json.dumps(fireplace, cls=dm.DecimalEncoder)# uses DecimalEnconder to make json
    
    data = json.loads(jdata) #send data back to json
    print(data) # data is a list of lists
    x = [i[0] for i in data]
    y = [i[1] for i in data]

    data = { "labels": ['None','Fireplace'], #"data": [round(i,2) for i in y]}

              "datasets" : [ 
              {
                        "data": [round(i,2) for i in y],
                        "backgroundColor": ['red','green'],
                        'collectionAlias': "Average Price ",
                        'label': "Average price ",
                            
                         }
                    ]
              }          
    return jsonify(data)


@app.route('/baths.json')
def baths_data():

    baths = dm.House.query.with_entities(dm.House.full_bathrooms ,
        func.avg(dm.House.sale_price)).group_by(dm.House.full_bathrooms).order_by(dm.House.full_bathrooms).all()

    jdata = json.dumps(baths, cls=dm.DecimalEncoder)# uses DecimalEnconder to make json
    
    data = json.loads(jdata) #send data back to json
    print(data) # data is a list of lists
    x = [i[0] for i in data]
    y = [i[1] for i in data]

    data = { "labels": x, #"data": [round(i,2) for i in y]}

              "datasets" : [ 
              {
                        "data": [round(i,2) for i in y],
                        "backgroundColor": ['blue']*11,
                        'collectionAlias': "Average Price ",
                        'label': "Average price per No of bathrooms ",
                            
                         }
                    ]
              }          
    return jsonify(data)
# popularity routes
@app.route('/popbed.json')
def popbed_data():

    beds = dm.House.query.with_entities(dm.House.num_bedrooms,
        func.count(dm.House.sale_price)).group_by(dm.House.num_bedrooms).order_by(dm.House.num_bedrooms).all()

    jdata = json.dumps(beds, cls=dm.DecimalEncoder)# print(beds)
    # data = [bed.avg_by_beds() for bed in beds]
    data = json.loads(jdata)
    x = [i[0] for i in data]
    y = [i[1] for i in data]

    data = { "labels": x, #"data": [round(i,2) for i in y]}

              "datasets" : [ 
              {
                        "data": y,
                        "backgroundColor": ['purple']*11,
                        'collectionAlias': "Beds Count",
                        'label': "popularity of bedrooms ",
                            
                         }
                    ]
              }          
    return jsonify(data)
  

@app.route('/poppool.json')
def poppool_data():

    pool = dm.House.query.with_entities(dm.House.has_pool,
        func.count(dm.House.sale_price)).group_by(dm.House.has_pool).all()

    jdata = json.dumps(pool, cls=dm.DecimalEncoder)# uses DecimalEnconder to make json
    
    data = json.loads(jdata) #send data back to json
    print(data) # data is a list of lists
    x = [i[0] for i in data]
    y = [i[1] for i in data]

    data = { "labels": ['None','Swimming Pool'], #"data": [round(i,2) for i in y]}

              "datasets" : [ 
              {
                        "data": [i for i in y],
                        "backgroundColor": ['red','green'],
                        'collectionAlias': "pool",
                        'label': "Popularity of pool ",
                            
                         }
                    ]
              }          
    return jsonify(data)

@app.route('/popgrg.json')
def popgrg_data():

    data = best5()
    data = data.groupby('garage_type').count()

    jdata = data.to_json() #this can jsonify a dataframe but dont need it 

    data = { "labels": ['garage attached','Detached','None'], #"data": [round(i,2) for i in y]}

              "datasets" : [ 
              {
                        "data": [i for i in data.sale_price],
                        "backgroundColor": ['green', 'yellow','red'],
                        'collectionAlias': "Average Price",
                        'label': "Average price per garage type ",
                            
                         }
                    ]
              }         

    return jsonify(data)

@app.route('/popfireplace.json')
def popfireplace_data():

    fireplace = dm.House.query.with_entities(dm.House.has_fireplace,
        func.count(dm.House.sale_price)).group_by(dm.House.has_fireplace).all()

    jdata = json.dumps(fireplace, cls=dm.DecimalEncoder)# uses DecimalEnconder to make json
    
    data = json.loads(jdata) #send data back to json
    print(data) # data is a list of lists
    x = [i[0] for i in data]
    y = [i[1] for i in data]

    data = { "labels": ['None','Fireplace'], #"data": [round(i,2) for i in y]}

              "datasets" : [ 
              {
                        "data": y,
                        "backgroundColor": ['red','green'],
                        'collectionAlias': "Fireplace ",
                        'label': "Fireplace count ",
                            
                         }
                    ]
              }          
    return jsonify(data)

@app.route('/popbaths.json')
def popbaths_data():

    baths = dm.House.query.with_entities(dm.House.full_bathrooms ,
        func.count(dm.House.sale_price)).group_by(dm.House.full_bathrooms).order_by(dm.House.full_bathrooms).all()

    jdata = json.dumps(baths, cls=dm.DecimalEncoder)# uses DecimalEnconder to make json
    
    data = json.loads(jdata) #send data back to json
    print(data) # data is a list of lists
    x = [i[0] for i in data]
    y = [i[1] for i in data]

    data = { "labels": x, #"data": [round(i,2) for i in y]}

              "datasets" : [ 
              {
                        "data": [i for i in y],
                        "backgroundColor": ['red','green'],
                        'collectionAlias': "Average Price ",
                        'label': "popularity of full bathrooms ",
                            
                         }
                    ]
              }          
    return jsonify(data)   


#scatter plots
@app.route('/relb.json')
def relb_data():

    baths = dm.House.query.with_entities(dm.House.full_bathrooms ,
        func.count(dm.House.sale_price)).group_by(dm.House.full_bathrooms).order_by(dm.House.full_bathrooms).all()

    jdata = json.dumps(baths, cls=dm.DecimalEncoder)# uses DecimalEnconder to make json
    
    data = json.loads(jdata) #send data back to json
    print(data) # data is a list of lists
    x = [i[0] for i in data]
    y = [i[1] for i in data]

    data = { "labels": x, #"data": [round(i,2) for i in y]}

              "datasets" : [ 
              {
                        "data": [i for i in y],
                        "backgroundColor": ['red','green'],
                        'collectionAlias': "Average Price ",
                        'label': "popularity of full bathrooms ",
                            
                         }
                    ]
              }          
    return jsonify(data) 

@app.route('/relbaths.json')
def relbaths_data():
    rbaths = dm.House.query.with_entities(dm.House.full_bathrooms ,
        func.avg(dm.House.sale_price)).group_by(dm.House.full_bathrooms).order_by(dm.House.full_bathrooms).all()

    jdata = json.dumps(rbaths, cls=dm.DecimalEncoder)# uses DecimalEnconder to make json
    
    data = json.loads(jdata) #send data back to json
    x = [i[0] for i in data]
    y = [round(i[1],2) for i in data]

    data = list(zip(x, y)) 
    # data= [dict(i) for i in data]
    print(data)
    print('################################')
    

    return jsonify(plot= data)  


#Individual graphs

@app.route('/idbed.json')
def myidbed_data():

    graph_city = session.get('city')

    beds = dm.House.query.with_entities(dm.House.num_bedrooms,
        func.count(dm.House.sale_price)).filter_by(dm.House.city_East_Lucas == 1).group_by(dm.House.num_bedrooms).order_by(dm.House.num_bedrooms).all()
    print(beds)
    jdata = json.dumps(beds, cls=dm.DecimalEncoder)# print(beds)
    # data = [bed.avg_by_beds() for bed in beds]
    data = json.loads(jdata)
    x = [i[0] for i in data]
    y = [i[1] for i in data]

    data = { "labels": x, #"data": [round(i,2) for i in y]}

              "datasets" : [ 
              {
                        "data": y,
                        "backgroundColor": ['purple']*11,
                        'collectionAlias': "Beds Count",
                        'label': "popularity of bedrooms ",
                            
                         }
                    ]
              }          
    return jsonify(data)   

@app.route('/idrelbaths.json')#relation btwn beds and average price
def idrelbaths_data():
    rbaths = dm.House.query.with_entities(dm.House.full_bathrooms ,
        func.avg(dm.House.sale_price)).group_by(dm.House.full_bathrooms).order_by(dm.House.full_bathrooms).all()

    jdata = json.dumps(rbaths, cls=dm.DecimalEncoder)# uses DecimalEnconder to make json
    
    data = json.loads(jdata) #send data back to json
    x = [i[0] for i in data]
    y = [round(i[1],2) for i in data]

    data = list(zip(x, y)) 
    # data= [dict(i) for i in data]
    print(data)
    print('################################')
    

    return jsonify(plot= data)  


@app.route('/idbaths.json')
def idbaths_data():

    baths = dm.House.query.with_entities(dm.House.num_bedrooms ,
        func.avg(dm.House.sale_price)).group_by(dm.House.num_bedrooms).all()

    jdata = json.dumps(baths, cls=dm.DecimalEncoder)# uses DecimalEnconder to make json
    
    data = json.loads(jdata) #send data back to json
    print(data) # data is a list of lists
    x = [i[0] for i in data]
    y = [i[1] for i in data]

    data = { "labels": x, #"data": [round(i,2) for i in y]}

              "datasets" : [ 
              {
                        "data": [round(i,2) for i in y],
                        "backgroundColor": ['red','green'],
                        'collectionAlias': "Average Price ",
                        'label': "Average price per No of bathrooms ",
                            
                         }
                    ]
              }          
    return jsonify(data)



@app.route('/idsqft.json')
def idscatter_data():
    houses = dm.House.query.all()
    data =[house.get_chart() for house in houses]




if __name__== "__main__":


	# debug=True gives us error messages in the browser and also "reloads"
	# the web app if we change the code.


	# Use the DebugToolbar
    DebugToolbarExtension(app)
    dm.connect_to_db(app)



    app.run(debug = True , host = "0.0.0.0")