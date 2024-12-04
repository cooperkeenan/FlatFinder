from flask import Flask, render_template, request, jsonify, session
from models import db
from models import Property
import json
from property_filters import filter_price, clean_price, filter_bedrooms, filter_location




app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///flatfinder.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
app.secret_key = 'very_secure_key'


# Home page 
@app.route('/')
def home():
    return render_template('index.html')  

# For You  
@app.route('/for-you')
def for_you():
    return render_template('for_you.html')  

# Search Filter Page
@app.route('/search')
def search():
    return render_template('search.html')


# Search Results 
@app.route('/search/results')
def search_results():
    # Get filter parameters 
    min_price = request.args.get('min_price')
    max_price = request.args.get('max_price')
    bedrooms = request.args.get('bedrooms')  
    location = request.args.get('location')  

    # remove symobols 
    min_price = clean_price(min_price) if min_price else None
    max_price = clean_price(max_price) if max_price else None
    bedrooms = int(bedrooms) if bedrooms else None

    properties = Property.query.all()

    # Apply filters
    properties = filter_price(properties, min_price, max_price)
    properties = filter_bedrooms(properties, bedrooms)
    properties = filter_location(properties, location)

    return render_template('search_results.html', properties=properties)




@app.route('/viewings')
def viewings():
    return render_template('viewing_manager.html')


@app.route('/property/<property_id>')
def property_detail(property_id):
    property = Property.query.get(property_id)
    image_urls = json.loads(property.image_urls)
    return render_template('view_property.html', property=property, image_urls=image_urls)


@app.route('/profile')
def profile():
   return render_template('profile.html')


@app.route('/lister')
def lister():
    return "<h1>Lister Portal</h1>"

@app.route('/contact')
def contact():
    return "<h1>Contact Page</h1>"





@app.cli.command("init_db")
def init_db():
    """Create the database and tables."""
    db.create_all()
    print("Database initialized.")

@app.cli.command("drop_db")
def drop_db():
    """Drop all tables in the database."""
    db.drop_all()
    print("Database cleared.")


@app.template_filter('formatdate')
def format_date(value, format='%Y-%m-%d'):
    """Custom Jinja2 filter to format datetime objects."""
    if value is None:
        return ""
    return value.strftime(format)


if __name__ == "__app__":
    app.run(debug=True)
