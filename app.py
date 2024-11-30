from flask import Flask, render_template, request
from models import db
from models import Property

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///flatfinder.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)


# Home page route (linked to the logo)
@app.route('/')
def home():
    return render_template('index.html')  # This is the main homepage template

# For You page route
@app.route('/for-you')
def for_you():
    return render_template('for_you.html')  # This is the "For You" page template

# Add other placeholder routes for now
@app.route('/search')
def search():
    return render_template('search.html')


@app.route('/search/results')
def search_results():
    properties = Property.query.all()
    return render_template('search_results.html', properties=properties)
 


@app.route('/viewings')
def viewings():
    return render_template('viewing_manager.html')



@app.route('/property/<property_id>')
def property_detail(property_id):
    property = Property.query.get(property_id)
    if property:
        return render_template('view_property.html', property=property)
    else:
        return "Property not found", 404


@app.route('/profile')
def profile():
    return "<h1>Profile Page</h1>"

@app.route('/lister')
def lister():
    return "<h1>Lister Portal</h1>"

@app.route('/contact')
def contact():
    return "<h1>Contact Page</h1>"





@app.route('/test-db')
def test_db():
    properties = Property.query.all()  # Fetch all properties from the database
    print("Number of properties found:", len(properties))  # Debugging line to check how many properties are fetched
    for prop in properties:  # Print some details to ensure data is loaded correctly
        print(prop.address, prop.price_pcm)
    return render_template('test_db.html', properties=properties)


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
