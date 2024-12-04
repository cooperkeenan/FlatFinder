document.addEventListener('DOMContentLoaded', function() {
    // Activate the first tab and display its content
    document.getElementById("SavedProperties").style.display = "block"; // Show the Saved Properties tab content
    document.getElementsByClassName("tab-button")[0].className += " active";// Set the first tab button as active

});



function openTab(evt, tabName) {
    // Hide all tab content
    var tabcontent = document.getElementsByClassName("tab-content");
    for (var i = 0; i < tabcontent.length; i++) {
        tabcontent[i].style.display = "none";
    }
    // Remove 'active' class from all buttons
    var tabbuttons = document.getElementsByClassName("tab-button");
    for (var i = 0; i < tabbuttons.length; i++) {
        tabbuttons[i].className = tabbuttons[i].className.replace(" active", "");
    }
    // Show the selected tab
    document.getElementById(tabName).style.display = "block";
    evt.currentTarget.className += " active";
}


function showModal() {
    console.log('Showing modal...'); // Check if the modal is triggered
    const modal = document.getElementById('loginModal');
    if (modal) {
        modal.style.display = 'block';
    }
}

// Assuming you have some close logic for the modal
function closeModal() {
    const modal = document.getElementById('loginModal');
    modal.style.display = 'none';
}
