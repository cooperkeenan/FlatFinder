document.addEventListener("DOMContentLoaded", function() {
    const filtersBtn = document.querySelector(".filters-btn");
    const mobileFilters = document.getElementById("mobileFilters");
    const closeFiltersBtn = document.querySelector(".close-filters-btn");

    filtersBtn.addEventListener("click", function() {
      // Show the overlay
      mobileFilters.classList.add("show-filters");
    });

    closeFiltersBtn.addEventListener("click", function() {
      // Hide the overlay
      mobileFilters.classList.remove("show-filters");
    });
  });