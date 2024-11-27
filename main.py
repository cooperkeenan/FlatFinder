from flask import Flask, render_template, request

app = Flask(__name__)

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
    # Extract query parameters if needed
    location = request.args.get('location')
    min_price = request.args.get('min_price')
    max_price = request.args.get('max_price')
    bedrooms = request.args.get('bedrooms')

    # Pass any search data to the template
    return render_template('search_results.html', location=location, min_price=min_price, max_price=max_price, bedrooms=bedrooms)

@app.route('/viewings')
def viewings():
    return render_template('viewing_manager.html')

@app.route('/profile')
def profile():
    return "<h1>Profile Page</h1>"

@app.route('/lister')
def lister():
    return "<h1>Lister Portal</h1>"

@app.route('/contact')
def contact():
    return "<h1>Contact Page</h1>"

if __name__ == "__main__":
    app.run(debug=True)
