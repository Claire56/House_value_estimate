"""Utility file to seed ratings database from MovieLens data in seed_data/"""

from sqlalchemy import func
from model import User
from model import Ratings
from model import Movie

from model import connect_to_db, db
from server import app
from datetime import datetime as dt 


def load_houses():
    """Load houses into database."""

    print("Houses")

    # Delete all rows in table, so if we need to run this a second time,
    # we won't be trying to add duplicate users
    User.query.delete()

    # Read u.user file and insert data
    for row in open("pop_cities.csv"):
        row = row.rstrip()
        row = row.split()
        

        year_built ,stories ,baths ,zipcode ,half_bathrooms ,livable_sqft ,
        total_sqft ,garage_sqft ,carport_sqft ,has_fireplace ,has_pool,
        has_central_cooling ,has_central_heating ,sale_price,garage_type_detached ,
        garage_type_attached ,city_Wendybury ,East_Lucas,North_Erinville,
        Port_Andrealand ,Port_Jonathanborough = row[2:]


        house = House(year_built=year_built ,stories=stories ,baths=baths ,zipcode=zipcode ,
            half_bathrooms=half_bathrooms ,livable_sqft =livable_sqft,total_sqft=total_sqft ,
            garage_sqft=garage_sqft ,carport_sqft=carport_sqft ,has_fireplace=has_fireplace ,
            has_pool=has_pool,has_central_cooling=has_central_cooling ,
            has_central_heating=has_central_heating ,sale_price=sale_price,
            garage_type_detached=garage_type_detached ,garage_type_attached=garage_type_attached ,
            city_Wendybury=city_Wendybury ,East_Lucas=East_Lucas,North_Erinville=North_Erinville,
            Port_Andrealand=Port_Andrealand ,Port_Jonathanborough = Port_Jonathanborough)

        # We need to add to the session or it won't ever be stored
        db.session.add(house)

    # Once we're done, we should commit our work
    db.session.commit()





def set_val_user_id():
    """Set value for the next house_id after seeding database"""

    # Get the Max house_id in the database
    result = db.session.query(func.max(User.user_id)).one()
    max_id = int(result[0])

    # Set the value for the next house_id to be max_id + 1
    query = "SELECT setval('users_user_id_seq', :new_id)"
    db.session.execute(query, {'new_id': max_id + 1})
    db.session.commit()


if __name__ == "__main__":
    connect_to_db(app)

    # In case tables haven't been created, create them
    db.create_all()

    # Import different types of data
    load_houses()
    load_ratings()
    set_val_user_id()

