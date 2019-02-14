"""Models and database functions for Ratings project."""

from flask_sqlalchemy import SQLAlchemy

# This is the connection to the PostgreSQL database; we're getting this through
# the Flask-SQLAlchemy helper library. On this, we can find the `session`
# object, where we do most of our interactions (like committing, etc.)

db = SQLAlchemy()


##############################################################################
# Model definitions

class House(db.Model):
    """User of ratings website."""

    __tablename__ = "houses"


    house_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    year_built = db.Column(db.String(14), nullable=True)
    stories = db.Column(db.Integer, nullable=True)
    baths = db.Column(db.Integer, nullable=True)
    zipcode = db.Column(db.String(10), nullable=True)
    half_bathrooms = db.Column(db.Integer, nullable = True )
    livable_sqft = db.Column(db.Integer, nullable=True)
    total_sqft = db.Column(db.Integer, nullable=True)
    garage_sqft = db.Column(db.Integer, nullable=True)
    carport_sqft = db.Column(db.Integer, nullable=True)
    has_fireplace = db.Column(db.String(14), nullable=True)    #boleean
    has_pool = db.Column(db.Integer, nullable=True)   #bool
    has_central_cooling = db.Column(db.Integer, nullable=True) #bool
    has_central_heating = db.Column(db.Integer, nullable=True)    #bool
    sale_price = db.Column(db.Integer, nullable = True )
    garage_type_detached = db.Column(db.Integer, nullable=True) 
    garage_type_attached = db.Column(db.Integer, nullable=True) 
    city_Wendybury =db.Column(db.Integer, nullable=True)
    East_Lucas =db.Column(db.Integer, nullable=True)
    North_Erinville = db.Column(db.Integer, nullable=True)
    Port_Andrealand =db.Column(db.Integer, nullable=True)
    Port_Jonathanborough =db.Column(db.Integer, nullable=True)




    def __repr__(self):
        """Provide helpful representation when printed."""

        return "Year Built={} ,baths ={} ,beds ={} , total_sqft = {},sale_price = {} ".format(self.year_built,self.baths,self.beds,self.total_sqft,self.sale_price)



 
##############################################################################
# Helper functions


def connect_to_db(app):
    """Connect the database to our Flask app."""

    # Configure to use our PstgreSQL database
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///ratings'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.app = app
    db.init_app(app)


if __name__ == "__main__":
    # As a convenience, if we run this module interactively, it will leave
    # you in a state of being able to work with the database directly.

    from server import app
    connect_to_db(app)
    print("Connected to DB.")
