window.addEventListener('load', function() {
    const spinnerContainer = document.querySelector('.spinner_container');
    spinnerContainer.style.display = 'none';
});

document.addEventListener('DOMContentLoaded', function() {
    const spinnerContainer = document.querySelector('.spinner_container');
    spinnerContainer.style.display = 'flex';
});

const toggleButton = document.getElementById('down_button');
const attributeContainer = document.getElementById('attribute_container');
const title = document.getElementById('title');
const author = document.getElementById('author');
const image = document.getElementById('album_art');

toggleButton.addEventListener('click', function() {
    attributeContainer.style.display = 'block';
    toggleButton.style.display = 'none';
    title.style.display = 'none';
    author.style.display = 'none';
    // change size of image
    image.classList.add('shrink');
});