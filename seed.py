"""Utility file to seed ratings database from MovieLens data in seed_data/"""

from sqlalchemy import func
from data_model import House


from data_model import connect_to_db, db
from server import app
from datetime import datetime as dt 


def load_houses():
    """Load houses into database."""

    print("houses")

    # Delete all rows in table, so if we need to run this a second time,
    # we won't be trying to add duplicate users
    House.query.delete()

    # Read u.user file and insert data
    for row in open("pop_cities.csv"):
        row = row.rstrip()
        row = row.split(',')
        row = row[2:]


        year_built ,stories ,beds ,full_baths ,half_baths,livable_sqft, total_sqft = row[:7] 

        garage_sqft,carport_sqft,fireplace ,pool,central_heating,central_cooling = row[7:13]

        zipcode, sale_price, garage_type_attached, garage_type_detached, East_Lucas =row[13:18]
        North_Erinville, Port_Andrealand, Port_Jonathanborough, Wendybury, West_Ann =row[18:]



        house = House(year_built=year_built ,stories=stories ,beds=beds,full_baths=full_baths ,zipcode=zipcode ,
            half_baths=half_baths,livable_sqft =livable_sqft,total_sqft=total_sqft ,
            garage_sqft=garage_sqft ,carport_sqft=carport_sqft ,fireplace=fireplace ,
            pool=pool, central_cooling =central_cooling ,central_heating=central_heating ,sale_price=sale_price,
            garage_type_detached=garage_type_detached ,garage_type_attached=garage_type_attached ,
            Wendybury=Wendybury ,East_Lucas=East_Lucas,North_Erinville=North_Erinville,West_Ann=West_Ann,
            Port_Andrealand =Port_Andrealand ,Port_Jonathanborough = Port_Jonathanborough)

        # We need to add to the session or it won't ever be stored
        db.session.add(house)

    # Once we're done, we should commit our work
    db.session.commit()




def set_val_user_id():
    """Set value for the next house_id after seeding database"""

    # Get the Max house_id in the database
    result = db.session.query(func.max(House.house_id)).one()
    max_id = int(result[0])

    # Set the value for the next house_id to be max_id + 1
    query = "SELECT setval('House_house_id_seq', :new_id)"
    db.session.execute(query, {'new_id': max_id + 1})
    db.session.commit()


if __name__ == "__main__":
    connect_to_db(app)

    # In case tables haven't been created, create them
    db.create_all()

    # Import different types of data
    load_houses()
    set_val_user_id()

