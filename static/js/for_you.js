document.addEventListener('DOMContentLoaded', function () {
    let currentIndex = 0;
  
    /**
     * Render the property card for the property at the given index.
     * If there are no more properties, show a "No more properties" message.
     */
    function renderProperty(index) {
      if (index >= properties.length) {
        document.getElementById('property-container').innerHTML =
          "<p>No more properties!</p>";
        return;
      }
  
      const property = properties[index];
      let imageList = [];
  
      // Parse the image_urls JSON string; ensure it is stored as a valid JSON array.
      try {
        imageList = JSON.parse(property.image_urls);
      } catch (e) {
        console.error("Error parsing image_urls:", e);
      }
  
      // Build HTML for the small images (skipping the first image, which is used as main)
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
  
      // Build the property card HTML
      const propertyHtml = `
        <div class="property-card">
          <div class="left-column">
            <h2>£${property.price_pcm} pcm (${property.price_pw})</h2>
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
  
      // Update the property container with the new HTML
      document.getElementById('property-container').innerHTML = propertyHtml;
    }
  
    // Initially render the first property
    renderProperty(currentIndex);
  
    // Set up event listeners for the like and dislike buttons
    document.querySelector('.like-btn').addEventListener('click', function () {
      currentIndex++;
      renderProperty(currentIndex);
    });
  
    document.querySelector('.dislike-btn').addEventListener('click', function () {
      currentIndex++;
      renderProperty(currentIndex);
    });
  });
  