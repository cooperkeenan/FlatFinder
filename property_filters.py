
# Remove other characters and convert to int
def clean_price(price_str):
    if price_str:
        return int(price_str.replace('£', '').replace('pcm', '').replace(',', '').strip())
    return 0


# Filter Price
def filter_price(properties, min_price=None, max_price=None):
    filtered = []
    for prop in properties:
        prop_price = clean_price(prop.price_pcm)
        if ((min_price is None or prop_price >= min_price) and 
            (max_price is None or prop_price <= max_price)):
            filtered.append(prop)
    return filtered


#Filter Bedrooms
def filter_bedrooms(properties, bedrooms=None):
    filtered = []
    for prop in properties:
        if bedrooms is None or prop.bedrooms == bedrooms:
            filtered.append(prop)
    return filtered 


#Filter Location 
def filter_location(properties, location=None):
    filtered = []
    for prop in properties:
        location = location.lower().strip()
        if location in prop.address.lower():
            filtered.append(prop)
    return filtered


