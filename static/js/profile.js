// profile.js

document.addEventListener('DOMContentLoaded', function() {
    // Initially activate the first tab and display its content if activeTab is not set
    if (!activeTab) {
        activeTab = "SavedProperties";
    }

    // Hide all tab content
    const tabContents = document.querySelectorAll(".tab-content");
    tabContents.forEach(content => content.style.display = "none");

    // Remove the active class from all buttons
    const tabButtons = document.querySelectorAll(".tab-button");
    tabButtons.forEach(button => button.classList.remove("active"));

    // Show the active tab and set the button as active
    const activeTabContent = document.getElementById(activeTab);
    const activeTabButton = document.querySelector(`.tab-button[onclick="openTab(event, '${activeTab}')"]`);

    if (activeTabContent) activeTabContent.style.display = "block";
    if (activeTabButton) activeTabButton.classList.add("active");

    // Handle Login Modal Display
    const loginModal = document.getElementById('loginModal');
    if (loginModal) {
        loginModal.style.display = 'block'; // Display the login modal if user is not logged in
    }

    // Attach event listeners to "Change" buttons
    const changeButtons = document.querySelectorAll('.change-btn');
    changeButtons.forEach(button => {
        button.addEventListener('click', function() {
            const modalId = this.getAttribute('onclick').match(/openModal\('(.+)'\)/)[1];
            openModal(modalId);
        });
    });

    // Attach event listener to "Create Account" button
    const createAccountBtn = document.querySelector('#loginForm button[type="button"]');
    if (createAccountBtn) {
        createAccountBtn.addEventListener('click', showRegisterForm);
    }

    // Optionally, attach event listener to "Back to Login" button if you have one
    const backToLoginBtn = document.querySelector('#registerForm button[type="button"]');
    if (backToLoginBtn) {
        backToLoginBtn.addEventListener('click', showLoginForm);
    }
});

// Function to show the registration form and hide the login form
function showRegisterForm() {
    document.getElementById('loginForm').style.display = 'none';
    document.getElementById('registerForm').style.display = 'block';
}

// Function to show the login form and hide the registration form
function showLoginForm() {
    document.getElementById('registerForm').style.display = 'none';
    document.getElementById('loginForm').style.display = 'block';
}

// Function to open a specific modal
function openModal(modalId) {
    const modal = document.getElementById(modalId);
    if (modal) {
        modal.style.display = 'block';
    }
}

// Function to close modals when clicking outside or on the close button
function closeModal(event) {
    if (event) {
        const target = event.target;
        if (target.classList.contains('modal')) {
            target.style.display = 'none';
        }
    }
}

// Optional: Close modal on pressing Escape key
document.addEventListener('keydown', function(event) {
    if (event.key === 'Escape') {
        const modals = document.querySelectorAll('.modal');
        modals.forEach(modal => modal.style.display = 'none');
    }
});

// Function to handle tab switching
function openTab(evt, tabName) {
    // Hide all tab content
    const tabContents = document.querySelectorAll(".tab-content");
    tabContents.forEach(content => content.style.display = "none");

    // Remove the active class from all buttons
    const tabButtons = document.querySelectorAll(".tab-button");
    tabButtons.forEach(button => button.classList.remove("active"));

    // Show the selected tab and mark the button as active
    const selectedTabContent = document.getElementById(tabName);
    const selectedTabButton = evt.currentTarget;

    if (selectedTabContent) selectedTabContent.style.display = "block";
    selectedTabButton.classList.add("active");
}
