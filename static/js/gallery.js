function openModal() {
    document.getElementById('myModal').style.display = "block";
}

function closeModal() {
    document.getElementById('myModal').style.display = "none";
}

var slideIndex = 1;
showSlides(slideIndex);

function plusSlides(n) {
    showSlides(slideIndex += n);
}

function currentSlide(n) {
    showSlides(slideIndex = n);
}

function showSlides(n) {
    var i;
    var slides = document.getElementsByClassName("mySlides");
    if (n > slides.length) {slideIndex = 1}
    if (n < 1) {slideIndex = slides.length}
    for (i = 0; i < slides.length; i++) {
        slides[i].style.display = "none";
    }
    slides[slideIndex-1].style.display = "block";
}


document.addEventListener("DOMContentLoaded", function() {
    // Event listener for the main image
    var mainImage = document.getElementById('main-image');
    mainImage.addEventListener('click', function() {
        openModal();
        currentSlide(1);
    });

    // Event listeners for the other images
    var images = document.querySelectorAll('.other-image');
    images.forEach(function(img) {
        img.addEventListener('click', function() {
            var slideIndex = this.getAttribute('data-slide');
            openModal();
            currentSlide(parseInt(slideIndex));
        });
    });
});
