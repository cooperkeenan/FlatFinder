

document.addEventListener('DOMContentLoaded', function() {
    // Initially activate the first tab and display its content
    document.getElementById("SavedProperties").style.display = "block"; // Show the Saved Properties tab content
    document.getElementsByClassName("tab-button")[0].className += " active"; // Set the first tab button as active

    const loginModal = document.getElementById('loginModal');
    if (loginModal) {
        loginModal.style.display = 'block'; // Optionally display the login modal if it's meant to be shown
    }

    // Listen for clicks to toggle forms within the modal
    document.getElementById('loginModal').addEventListener('click', function(event) {
        if (event.target.classList.contains('modal')) {
            closeModal();
        }
    });

    // Prevent modal close when clicking inside modal content
    document.querySelector('.modal-content').addEventListener('click', function(event) {
        event.stopPropagation();
    });

    // Attach event listener for toggling forms
    const createAccountBtn = document.querySelector('#loginForm button[type="button"]');
    if (createAccountBtn) {
        createAccountBtn.addEventListener('click', showRegisterForm);
    }
});

function openTab(evt, tabName) {
    var tabcontent = document.getElementsByClassName("tab-content");
    var tabbuttons = document.getElementsByClassName("tab-button");

    // Hide all tab content and remove 'active' class from buttons
    Array.from(tabcontent).forEach(content => content.style.display = "none");
    Array.from(tabbuttons).forEach(button => button.className = button.className.replace(" active", ""));

    // Show the selected tab and mark the button as active
    document.getElementById(tabName).style.display = "block";
    evt.currentTarget.className += " active";
}

function closeModal() {
    const modal = document.getElementById('loginModal');
    modal.style.display = 'none';
}

function showRegisterForm() {
    // Hide the login form and show the register form
    document.getElementById('loginForm').style.display = 'none';
    document.getElementById('registerForm').style.display = 'block';
}


function openModal(modalId) {
    document.getElementById(modalId).style.display = 'block';
}

function closeModal(event) {
    const modals = document.querySelectorAll('.modal');
    modals.forEach(modal => {
        if (event.target === modal) {
            modal.style.display = 'none';
        }
    });
}

// Optional: Close modal on pressing Escape key
document.addEventListener('keydown', function(event) {
    if (event.key === 'Escape') {
        const modals = document.querySelectorAll('.modal');
        modals.forEach(modal => modal.style.display = 'none');
    }
});
