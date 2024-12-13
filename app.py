from flask import Flask, render_template, request, jsonify, session, redirect, flash, url_for
from models import db
from models import Property, User
import json
from property_filters import filter_price, clean_price, filter_bedrooms, filter_location
from flask_bcrypt import Bcrypt
from flask_migrate import Migrate 
import os



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///flatfinder.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
bcrypt = Bcrypt(app)  # Initialize Bcrypt
migrate = Migrate(app, db)  # Initialize Flask-Migrate if applicable
app.secret_key = os.urandom(24)


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
    # Default to 'SavedProperties' if no tab parameter is passed
    tab = request.args.get('tab', 'SavedProperties')
    
    if 'user_id' not in session:
        return render_template('profile.html', logged_in=False, user=None, active_tab=tab)
    else:
        user = User.query.get(session['user_id'])
        if user:
            return render_template('profile.html', logged_in=True, user=user, active_tab=tab)
        else:
            session.pop('user_id', None)
            flash('Session expired. Please log in again.')
            return redirect(url_for('login'))





@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        
        # Fetch the user by email
        user = User.query.filter_by(email=email).first()
        
        if user and user.verify_password(password):
            session['user_id'] = user.id
            session['logged_in'] = True
            return redirect(url_for('profile'))
        else:
            flash('Invalid email or password.')  # Updated message
            return redirect(url_for('login'))
    else:
        # Render the login form page if it's a GET request
        return render_template('profile.html')



# Logout Route
@app.route('/logout', methods=['POST'])
def logout():
    session.pop('user_id', None)
    session.pop('logged_in', None)
    flash('You have been logged out successfully.')
    return redirect(url_for('home'))



@app.route('/register', methods=['POST'])
def register():
    # Retrieve form data
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    email = request.form['email']
    password = request.form['password']
    phone = request.form['phone']

    # Check if email already exists
    if User.query.filter_by(email=email).first():
        flash('Email already registered.')
        return redirect(url_for('login'))

    # Create a new user instance with hashed password
    new_user = User(
        first_name=first_name,
        last_name=last_name,
        email=email,
        password=password,  # Password setter handles hashing
        phone=phone
    )

    # Add the new user to the database
    db.session.add(new_user)
    db.session.commit()

    flash('Registration successful. Please log in.')
    return redirect(url_for('login'))


@app.route('/update_name', methods=['POST'])
def update_name():
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    tab = request.form.get('tab', 'SavedProperties') 
    user = User.query.get(session['user_id'])
    user.first_name = first_name
    user.last_name = last_name
    db.session.commit()
    flash('Name updated successfully!')
    return redirect(url_for('profile', tab=tab))

@app.route('/update_email', methods=['POST'])
def update_email():
    if 'user_id' not in session:
        flash('You need to log in to update your email.')
        return redirect(url_for('login'))
    
    email = request.form['email']
    tab = request.form.get('tab', 'AccountSettings')
    
    user = User.query.get(session['user_id'])
    if not user:
        flash('User not found.')
        return redirect(url_for('login'))
    
    # Check if the new email is already in use
    if User.query.filter_by(email=email).first():
        flash('Email is already in use.')
        return redirect(url_for('profile', tab=tab))
    
    user.email = email
    db.session.commit()
    
    flash('Email updated successfully!')
    return redirect(url_for('profile', tab=tab))


@app.route('/update_phone', methods=['POST'])
def update_phone():
    phone = request.form['phone']
    tab = request.form.get('tab', 'AccountSettings')  # Ensure the tab is passed
    user = User.query.get(session['user_id'])
    user.phone = phone
    db.session.commit()
    flash('Phone number updated successfully!')
    return redirect(url_for('profile', tab=tab))

@app.route('/update_password', methods=['POST'])
def update_password():
    if 'user_id' not in session:
        flash('You need to log in to update your password.')
        return redirect(url_for('login'))
    
    user = User.query.get(session['user_id'])
    if not user:
        flash('User not found.')
        return redirect(url_for('login'))
    
    new_password = request.form['password']
    tab = request.form.get('tab', 'AccountSettings')
    
    if not new_password:
        flash('Password cannot be empty.')
        return redirect(url_for('profile', tab=tab))
    
    user.password = new_password  # Password setter handles hashing
    db.session.commit()
    
    flash('Password updated successfully!')
    return redirect(url_for('profile', tab=tab))




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
