document.addEventListener("DOMContentLoaded", function () {
    const filtersPanel = document.querySelector(".mobile-filters-panel");
    const filtersBtn = document.querySelector(".filters-btn");
    const closeFiltersBtn = document.querySelector(".close-filters-btn");
    const filtersForm = document.querySelector(".mobile-filters-panel form");

    // Open the filters panel
    filtersBtn.addEventListener("click", () => {
        filtersPanel.classList.add("show-filters");
        document.body.classList.add("no-scroll"); // Disable scrolling
    });

    // Close filters when clicking the background
    filtersPanel.addEventListener("click", (e) => {
        if (!filtersForm.contains(e.target)) {
            filtersPanel.classList.remove("show-filters");
            document.body.classList.remove("no-scroll"); // Enable scrolling
        }
    });

    // Close filters when clicking the close button
    closeFiltersBtn.addEventListener("click", () => {
        filtersPanel.classList.remove("show-filters");
        document.body.classList.remove("no-scroll");
    });
});
