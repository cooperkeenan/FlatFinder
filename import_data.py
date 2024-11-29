import json
from datetime import datetime
from models import db, Property
from app import app 

# Load data from a JSON file
def load_json(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

# Extracts image URLs from the property images data
def extract_image_urls(property_images):
    if not property_images:
        return [], ''
    
    if isinstance(property_images, str):
        try:
            property_images = json.loads(property_images)
        except json.JSONDecodeError:
            return [], ''
    
    images = property_images.get('images', [])
    image_urls = [img['srcUrl'] for img in images if 'srcUrl' in img]
    main_image_url = property_images.get('mainImageSrc', '')
    return image_urls, main_image_url

# Format the date 
def format_date(date_str):
    if date_str:
        try:
            date = datetime.strptime(date_str, "%Y-%m-%dT%H:%M:%SZ")
            return date.strftime('%Y-%m-%d')
        except ValueError:
            return None
    return None

# Insert data into database 
def insert_data():
    listings = load_json('listings.json')
    with app.app_context():
        for listing in listings:
            property_images = listing.get('propertyImages', '{}')
            image_urls, main_image_url = extract_image_urls(property_images)
            
            customer_data = listing.get('customer', {})
            if isinstance(customer_data, str):
                try:
                    customer_data = json.loads(customer_data)
                except json.JSONDecodeError:
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
                listing_company=customer_data.get('branchDisplayName'),
                date_added=format_date(listing.get('firstVisibleDate')),
                lister_logo=customer_data.get('brandPlusLogoUrl')  # Assuming you have this field now in your model
            )
            db.session.add(new_property)
        db.session.commit()

if __name__ == '__main__':
    insert_data()
