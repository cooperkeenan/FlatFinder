function initMap() {
    // Retrieve latitude and longitude from data attributes
    var mapElement = document.getElementById('map');
    var latitude = parseFloat(mapElement.dataset.latitude);
    var longitude = parseFloat(mapElement.dataset.longitude);
    var propertyLocation = { lat: latitude, lng: longitude };

    // Create the map centered at the property's location
    var map = new google.maps.Map(mapElement, {
        center: propertyLocation,
        zoom: 15,
    });

    // Add a marker at the property's location
    var marker = new google.maps.Marker({
        position: propertyLocation,
        map: map,
        title: 'Property Location',
    });
}
