from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Property(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    address = db.Column(db.String(500))
    postcode = db.Column(db.String(50))
    latitude = db.Column(db.Float)  
    longitude = db.Column(db.Float)
    lister_id = db.Column(db.Integer, db.ForeignKey('lister.id'))
    checklist_id = db.Column(db.Integer, db.ForeignKey('checklist.id'))
    bedrooms = db.Column(db.Integer)
    bathrooms = db.Column(db.Integer)
    price_pcm = db.Column(db.String(100))  
    price_pw = db.Column(db.String(100))
    description = db.Column(db.Text)
    full_description = db.Column(db.Text)
    main_image_url = db.Column(db.String(500))
    image_urls = db.Column(db.Text) 
    location = db.Column(db.String(255))
    listing_company = db.Column(db.String(255))
    date_added = db.Column(db.String(255))
    lister_logo = db.Column(db.String(500))
    flat_type = db.Column(db.String(500))
    number_floorplans = db.Column(db.Integer)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    phone = db.Column(db.String(50))
    email = db.Column(db.String(100))
    password = db.Column(db.String(100))  



class Lister(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    companyName = db.Column(db.String(50))
    phone = db.Column(db.String(50))
    email = db.Column(db.String(100))
    password = db.Column(db.String(100))  


class Checklist(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    price = db.Column(db.Integer)
    description = db.Column(db.Text)
    bathrooms = db.Column(db.Integer)
    balcony = db.Column(db.Boolean)
    carpet = db.Column(db.Boolean)
    double_glazing = db.Column(db.Boolean)
    deposit = db.Column(db.Integer)
    availability_date = db.Column(db.Date)
    parking = db.Column(db.Boolean)

