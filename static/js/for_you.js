document.addEventListener('DOMContentLoaded', function () {
    // Get the content of the script tag by its ID and parse it
    const propertyDataElement = document.getElementById('property-data');
    const properties = JSON.parse(propertyDataElement.textContent);
    
    let currentIndex = 0;
    
    function renderProperty(index) {
      if (index >= properties.length) {
        document.getElementById('property-container').innerHTML = "<p>No more properties!</p>";
        return;
      }
    
      const property = properties[index];
      let imageList = [];
      try {
        imageList = JSON.parse(property.image_urls);
      } catch (e) {
        console.error("Error parsing image_urls:", e);
      }
    
      let smallImagesHtml = "";
      if (imageList.length > 1) {
        for (let i = 1; i < imageList.length; i++) {
          smallImagesHtml += `
            <div class="small-image">
              <img src="${imageList[i]}" alt="Small Image" style="width:100%; height:100%; border-radius:5px;">
            </div>`;
        }
      } else {
        smallImagesHtml = `<div class="small-image">No Additional Images</div>`;
      }
    
      const propertyHtml = `
        <div class="property-card">
          <div class="left-column">
            <h2>${property.price_pcm}  (${property.price_pw})</h2>
            <h3>${property.flat_type || 'Property'}</h3>
            <p>${property.address}</p>
            <div class="image-gallery">
              <div class="large-image">
                <img src="${property.main_image_url}" alt="Main Image" style="width:100%; height:100%; border-radius:5px;">
              </div>
              <div class="small-images">
                ${smallImagesHtml}
              </div>
            </div>
            <div class="property-details">
              <div class="details-column">
                <span class="detail-item">• ${property.flat_type || 'Unfurnished'}</span>
                <span class="detail-item">• Long Term</span>
                <span class="detail-item">• Available Now</span>
              </div>
              <div class="details-column">
                <span class="detail-item">• No Pets</span>
                <span class="detail-item">• Deposit £1000</span>
                <span class="detail-item">• EPC Rating D</span>
              </div>
            </div>
            <div class="details-row lower">
              <span class="detail-item"><i class="fas fa-ruler-combined"></i> Square Foot</span>
              <span class="detail-item"><i class="fas fa-building"></i> Apartment</span>
              <span class="detail-item"><i class="fas fa-bed"></i> ${property.bedrooms} Beds</span>
              <span class="detail-item"><i class="fas fa-shower"></i> ${property.bathrooms || 'N/A'} Baths</span>
              <span class="detail-item"><i class="fas fa-map-marked-alt"></i> Floor Plan</span>
            </div>
          </div>
          <div class="right-column">
            <div class="map-placeholder">
              Map for ${property.address}
            </div>
            <div class="description-tile">
              <h3>Description</h3>
              <p>${property.description}</p>
              <a href="#">Tap to see full description</a>
            </div>
          </div>
        </div>
      `;
    
      document.getElementById('property-container').innerHTML = propertyHtml;
    }
    
    renderProperty(currentIndex);
    
    document.querySelector('.like-btn').addEventListener('click', function () {
      currentIndex++;
      renderProperty(currentIndex);
    });
    
    document.querySelector('.dislike-btn').addEventListener('click', function () {
      currentIndex++;
      renderProperty(currentIndex);
    });
  });
  