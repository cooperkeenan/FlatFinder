import json
import ast
from models import db, Property
from app import app 

def load_json(file_path):
    """Load data from a JSON file."""
    with open(file_path, 'r') as file:
        data = json.load(file)  # Changed from json.load('listings.json') to json.load(file)
    return data

import json
import ast  # Use ast.literal_eval to safely evaluate strings containing dictionary-like data
from models import db, Property
from app import app

def insert_data():
    listings = load_json('listings.json')
    with app.app_context():
        for listing in listings:
            # Parse propertyImages if it's a string into a dictionary
            property_images = listing.get('propertyImages', '{}')
            if isinstance(property_images, str):
                try:
                    property_images = json.loads(property_images)
                except json.JSONDecodeError:
                    property_images = {}

            # Now extract image URLs safely
            images = property_images.get('images', [])
            image_urls = [img['srcUrl'] for img in images if 'srcUrl' in img]
            main_image_url = property_images.get('mainImageSrc', '')

            # Handle customer data correctly
            customer_data = listing.get('customer', '{}')
            if isinstance(customer_data, str):
                try:
                    customer_data = ast.literal_eval(customer_data)
                except ValueError:
                    customer_data = {}

            new_property = Property(
                id=listing['id'],
                address=listing['displayAddress'],
                bedrooms=listing.get('bedrooms', 0),
                bathrooms=listing.get('bathrooms', 0),
                price_pcm=listing['price']['displayPrices'][0]['displayPrice'] if 'displayPrices' in listing['price'] else None,
                price_pw=listing['price']['displayPrices'][1]['displayPrice'] if len(listing['price']['displayPrices']) > 1 else None,
                description=listing.get('summary'),
                main_image_url=main_image_url,
                image_urls=json.dumps(image_urls),
                location=f"{listing['location']['latitude']}, {listing['location']['longitude']}",
                listing_company=customer_data.get('branchDisplayName') if 'branchDisplayName' in customer_data else None
            )
            db.session.add(new_property)
        db.session.commit()

if __name__ == '__main__':
    insert_data()

