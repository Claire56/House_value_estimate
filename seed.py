"""Utility file to seed ratings database from MovieLens data in seed_data/"""

from sqlalchemy import func
from data_model import House
import pandas as pd
# from delete import column_names



from data_model import connect_to_db, db
from server import app



def load_houses():
    """Load houses into database."""

    print("houses")

    # Delete all rows in table, so if we need to run this a second time,
    # we won't be trying to add duplicate users
    House.query.delete()

    # Read u.user file and insert data
    with open("pop_cities.csv")as file:
        next(file)
        i=0
        for row in file:
            row = row.rstrip()
            row = row.split(',')
            row = row[2:]

            # col_names = column_names()

            # col_names[:13]= row[:13]
            # col_names[13:]= row[14:]



            year_built ,stories,num_bedrooms,full_bathrooms ,half_bathrooms,livable_sqft, total_sqft = row[:7]

            

            garage_sqft,carport_sqft,has_fireplace,has_pool,has_central_heating,has_central_cooling = row[7:13]
            if i % 100 == 0:
                print('adding ', year_built)

            sale_price, garage_type_attached, garage_type_detached, city_East_Lucas =row[14:18]

            city_North_Erinville, city_Port_Andrealand, city_Port_Jonathanborough, city_Wendybury, city_West_Ann =row[18:]

            # import pdb; pdb.set_trace()


            house = House(year_built=float(float(year_built)),stories=int(float(stories)),num_bedrooms= int(float(num_bedrooms)),
                full_bathrooms= int(float(full_bathrooms)) ,half_bathrooms= int(float(half_bathrooms)),
                livable_sqft =int(float(livable_sqft)),total_sqft= int(float(total_sqft)),
                garage_sqft=int(float(garage_sqft)) ,carport_sqft=int(float(carport_sqft)) ,
                has_fireplace=int(float(has_fireplace)),
                has_pool=int(float(has_pool)), has_central_cooling = int(float(has_central_cooling)),
                has_central_heating=int(float(has_central_heating)),
                sale_price=float(float(sale_price),garage_type_detached = int(float(garage_type_detached),
                garage_type_attached = int(float(garage_type_attached)), city_Wendybury= int(float(city_Wendybury)),
                city_East_Lucas=int(float(city_East_Lucas)),city_North_Erinville=int(float(city_North_Erinville)),
                city_West_Ann=int(float(city_West_Ann)),
                city_Port_Andrealand = int(float(city_Port_Andrealand)) ,city_Port_Jonathanborough = int(float(city_Port_Jonathanborough)))

            # We need to add to the session or it won't ever be stored
            db.session.add(house)


            # import pdb; pdb.set_trace()
            if i % 100 == 0:
                db.session.commit()

        # Once we're done, we should commit our work
        db.session.commit()


'''

def set_val_user_id():
    """Set value for the next house_id after seeding database"""

    # Get the Max house_id in the database
    result = db.session.query(func.max(House.house_id)).one()
    max_id = int(result[0])

    # Set the value for the next house_id to be max_id + 1
    query = "SELECT setval('House_house_id_seq', :new_id)"
    db.session.execute(query, {'new_id': max_id + 1})
    db.session.commit()
'''

if __name__ == "__main__":
    connect_to_db(app)

    # In case tables haven't been created, create them
    db.create_all()

    # Import different types of data
    load_houses()
    # set_val_user_id()

