"""Models and database functions for Ratings project."""

from flask_sqlalchemy import SQLAlchemy
from helper_functions import column_names

# This is the connection to the PostgreSQL database; we're getting this through
# the Flask-SQLAlchemy helper library. On this, we can find the `session`
# object, where we do most of our interactions (like committing, etc.)

db = SQLAlchemy()


##############################################################################
# Model definitions
col_names = column_names()
print(len(col_names))

class House(db.Model):
    """User of ratings website."""

    __tablename__ = "houses"


    house_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    year_built = db.Column(db.String(14), nullable=True)
    stories = db.Column(db.Integer, nullable=True)
    num_bedrooms = db.Column(db.Integer, nullable=True)
    full_bathrooms = db.Column(db.Integer, nullable=True)
    # zipcode = db.Column(db.String(10), nullable=True)
    half_bathrooms = db.Column(db.Integer, nullable = True )
    livable_sqft = db.Column(db.Integer, nullable=True)
    total_sqft = db.Column(db.Integer, nullable=True)
    garage_sqft = db.Column(db.Integer, nullable=True)
    carport_sqft = db.Column(db.Integer, nullable=True)
    has_fireplace = db.Column(db.Boolean, nullable=True)    
    has_pool = db.Column(db.Boolean, nullable=True)   #bool
    has_central_cooling = db.Column(db.Boolean, nullable=True) 
    has_central_heating = db.Column(db.Boolean, nullable=True)    #
    sale_price = db.Column(db.Integer, nullable = True )
    garage_type_attached = db.Column(db.Integer, nullable=True) 
    garage_type_detached = db.Column(db.Integer, nullable=True) 
    city_East_Lucas =db.Column(db.Integer, nullable=True)
    city_North_Erinville = db.Column(db.Integer, nullable=True)
    city_Port_Andrealand =db.Column(db.Integer, nullable=True)
    city_Port_Jonathanborough =db.Column(db.Integer, nullable=False)
    city_Wendybury =db.Column(db.Integer, nullable=True)
    city_West_Ann =db.Column(db.Integer,nullable=False)

# class House(db.Model):

#     __tablename__ = 'houses'

#     house_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    
#     # thought the code below was cool but it didnt work
    # for name in col_names:
    #     name = db.Column(db.Numeric, nullable=True)



    def __repr__(self):
        """Provide helpful representation when printed."""

        return f'Year: {self.year_built} T_sqft: {self.total_sqft} Price: {self.sale_price}'

    
    def get_chart(self):

        return {'x': self.sale_price, 'y': self.total_sqft}

    def get_line(self):

        return {'x':self.sale_price,'y': self.num_bedrooms}

##############################################################################
# Helper functions


def connect_to_db(app):
    """Connect the database to our Flask app."""

    # Configure to use our PstgreSQL database
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///homes'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.app = app
    db.init_app(app)


if __name__ == "__main__":
    # As a convenience, if we run this module interactively, it will leave
    # you in a state of being able to work with the database directly.

    from server import app
    connect_to_db(app)
    print("Connected to DB.")
