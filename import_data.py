import requests
from datetime import datetime
from sqlalchemy.exc import IntegrityError
from models import db, Property, User
from app import app 
import json
import re



# Load data from a JSON file
def load_json(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data


#Improve image quality 
def upgrade_image(url):

    # Remove 'dir/crop/10:9-16:9/' from the path
    url = url.replace('://media.rightmove.co.uk:443/dir/crop/10:9-16:9/', '://media.rightmove.co.uk/')
    url = url.replace('://media.rightmove.co.uk/dir/crop/10:9-16:9/', '://media.rightmove.co.uk/')
    # Remove '_max_XXXxYYY' from the filename
    url = re.sub(r'_max_\d+x\d+(?=\.(jpg|jpeg|JPG|JPEG|png|PNG|gif|GIF))', '', url)
    return url


# Extract image URLs and main image URL
def extract_image_urls(property_images):
    if not property_images:
        return [], ''
    
    if isinstance(property_images, str):
        try:
            property_images = json.loads(property_images)
        except json.JSONDecodeError:
            return [], ''
    
    images = property_images.get('images', [])
    image_urls = []
    for img in images:
        if 'srcUrl' in img:
            upgraded_url = upgrade_image(img['srcUrl'])
            image_urls.append(upgraded_url)
    main_image_url = property_images.get('mainImageSrc', '')
    main_image_url = upgrade_image(main_image_url)
    return image_urls, main_image_url



# Format the date to YYYY-MM-DD format
def format_date(date_str):
    if date_str:
        try:
            date = datetime.strptime(date_str, "%Y-%m-%dT%H:%M:%SZ")
            return date.strftime('%Y-%m-%d')
        except ValueError:
            return None
    return None

# Insert data into the database
def insert_data():
    listings = load_json('listings.json')
    with app.app_context():
        for listing in listings:
            property_images = listing.get('propertyImages', '{}')
            image_urls, main_image_url = extract_image_urls(property_images)
            customer_data = listing.get('customer', {})
    
            property_id = listing['id']
            existing_property = Property.query.filter_by(id=property_id).first()
    
            location_data = listing.get('location', {})
            latitude = location_data.get('latitude')
            longitude = location_data.get('longitude')
    
            if existing_property:
                # Update existing property
                existing_property.address = listing['displayAddress']
                existing_property.latitude = latitude
                existing_property.longitude = longitude
                existing_property.bedrooms = listing.get('bedrooms', 0)
                existing_property.bathrooms = listing.get('bathrooms', 0)
                existing_property.price_pcm = listing['price']['displayPrices'][0]['displayPrice'] if 'displayPrices' in listing['price'] else None
                existing_property.description = listing.get('summary')
                existing_property.main_image_url = main_image_url  # Use upgraded URL
                existing_property.image_urls = json.dumps(image_urls)  # Use upgraded URLs
                existing_property.location = f"{latitude}, {longitude}"
                existing_property.listing_company = listing.get('customer', {}).get('branchDisplayName', '')
                existing_property.date_added = format_date(listing.get('firstVisibleDate'))
                print(f"Updated existing property: {property_id}")
            else:
                # Insert new property
                new_property = Property(
                    id=property_id,
                    address=listing['displayAddress'],
                    latitude=latitude,
                    longitude=longitude,
                    bedrooms=listing.get('bedrooms', 0),
                    bathrooms=listing.get('bathrooms', 0),
                    price_pcm=listing['price']['displayPrices'][0]['displayPrice'] if 'displayPrices' in listing['price'] else None,
                    description=listing.get('summary'),
                    full_description=listing.get('description'),
                    main_image_url=main_image_url,  # Use upgraded URL
                    image_urls=json.dumps(image_urls),  # Use upgraded URLs
                    lister_logo=customer_data.get('brandPlusLogoUrl'),
                    location=f"{latitude}, {longitude}",
                    listing_company=listing.get('customer', {}).get('branchDisplayName', ''),
                    date_added=format_date(listing.get('firstVisibleDate')),
                    flat_type=listing['propertySubType'],
                    number_floorplans=listing.get("numberOfFloorplans", 0)
                )
                db.session.add(new_property)
                print(f"Inserted new property: {property_id}")
    
        try:
  
            new_user = User(
            id=101,
            first_name='Admin',
            last_name='User',
            phone='101',
            email='admin@example.com',
            password='password'
            
        )
            db.session.add(new_user)


            db.session.commit()
        except IntegrityError as e:
            db.session.rollback()
            print(f"Failed to insert or update property: {e}")


if __name__ == '__main__':
    insert_data()
