from sklearn.externals import joblib

# Load the model we trained previously
model = joblib.load('trained_model.pkl')

# For the house we want to value, we need to provide the features in the exact same
# arrangement as our training data set.
house_to_value = [
    # House features
    2017,   # year_built
    1,      # stories
    2,      # num_bedrooms
    2,      # full_bathrooms
    0,      # half_bathrooms 
    1311,   # livable_sqft
    1694,   # total_sqft
    206,      # garage_sqft
    0,      # carport_sqft
    True,   # has_fireplace
    False,  # has_pool
    True,   # has_central_heating
    True,   # has_central_cooling
    
    # Garage type: Choose only one
    0,      # attached
    1,      # detached
    
    
    # City: Choose only one
    0,      # Amystad
    0,      # Brownport
    0,      # North Erinville
    0,      # West Ann
    0,      # Port Andrealand
    1,      # Port Jonathanborough
    
]

#zipcodes 10250,11295 ,11510,10748,11911


# scikit-learn assumes you want to predict the values for lots of houses at once, so it expects an array.
# We just want to look at a single house, so it will be the only item in our array.
homes_to_value = [
    house_to_value
]

# Run the model and make a prediction for each house in the homes_to_value array
predicted_home_values = model.predict(homes_to_value)


# Since we are only predicting the price of one house, just look at the first prediction returned
predicted_value = predicted_home_values[0]

print("This house has an estimated value of ${:,.2f}".format(predicted_value))


