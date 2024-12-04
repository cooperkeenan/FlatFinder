from flask import Flask, render_template, request, jsonify, session, redirect, flash, url_for
from models import db
from models import Property, User
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
    if 'logged_in' not in session or not session['logged_in']:
        return render_template('profile.html', logged_in=False)
    else:
        # Assuming session['user_id'] holds the ID of the logged-in user
        user = User.query.get(session['user_id'])
        if user:
            return render_template('profile.html', logged_in=True, user=user)
        else:
            # Handle case where user is not found
            flash('User not found')
            return redirect(url_for('logout'))



@app.route('/login', methods=['POST'])
def login():
    email = request.form['email']
    password = request.form['password']
    # This is a simplistic check; replace with actual authentication in production
    user = User.query.filter_by(email=email, password=password).first()
    if user:
        session['logged_in'] = True
        session['user_id'] = user.id
        return redirect(url_for('profile'))
    else:
        flash('Invalid credentials')
        return redirect(url_for('profile'))


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
