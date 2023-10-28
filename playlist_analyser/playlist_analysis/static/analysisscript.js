window.addEventListener('load', function() {
    const spinnerContainer = document.querySelector('.spinner_container');
    spinnerContainer.style.display = 'none';
});

document.addEventListener('DOMContentLoaded', function() {
    const spinnerContainer = document.querySelector('.spinner_container');
    spinnerContainer.style.display = 'flex';
});

const toggleButton = document.getElementById('down_button');
const attributeContainer = document.getElementById('all_attributes_container');
const title = document.getElementById('title');
const author = document.getElementById('author');
const image = document.getElementById('album_art');

toggleButton.addEventListener('click', function() {
    toggleButton.style.display = 'none';
    title.classList.add('shrink');
    author.style.display = 'none';
    // change size of image
    image.classList.add('shrink');
    //display attribute container
    attributeContainer.style.display = 'flex';
});

//create a set of attribute names getting it from the html
const parentElement = document.getElementById('all_attributes_container');
const attributeContainers = parentElement.querySelectorAll('[class$="attribute_container"]');
console.log(attributeContainers);

//create array from nodelist using a map function to the text content of each element (the names of the attributes)
// const attributeNames = Array.from(attributeContainers).map(function(attributeContainer) {
//     return attributeContainer.textContent.trim();
// });

// var radius = circle.r.baseVal.value;
// var circumference = radius * 2 * Math.PI;

//get circle and data classes from each item in the node list and store them as a pair in an array
const mapped_values = Array.from(attributeContainers).map(function(attributeContainer) {

    const circle = attributeContainer.querySelector('circle');
    const data = Math.abs(attributeContainer.querySelector('data').value);
    console.log(data);  
    const attributeName = attributeContainer.dataset.textContent;
    console.log(attributeName);
    return {
        circle: circle,
        data: data,
        attributeName: attributeName
    };
});

//function that takes in an array of circles, values and attribute names and sets the progress of each circle
function setProgresses(mapped_values) {
    mapped_values.forEach(function(mapped_value) {
        const circle = mapped_value.circle;
        // if attribute name is loudness, set the data to be the absolute value of the data
        if (mapped_value.attributeName === 'Loudness') {
            mapped_value.data = Math.log(Math.abs(mapped_value.data)) * 10;

        }
        const data = mapped_value.data <= 100 ? mapped_value.data : Math.log(mapped_value.data) * 10;
        const percent = data;
        setProgress(percent, circle);
    });
}

function setProgress(percent, specified_circle) {
    const radius = specified_circle.r.baseVal.value;
    const circumference = radius * 2 * Math.PI;

    const hue = 290;
    const saturation = '50%'; 

    const lightness = `${100 - percent}%`;
    specified_circle.style.stroke = `hsl(${hue}, ${saturation}, ${lightness})`;
    specified_circle.style.strokeDasharray = `${circumference} ${circumference}`;
    specified_circle.style.strokeDashoffset = `${circumference}`;

    // use Intersection Observer API to detect when the circle is in the viewport
    const observer = new IntersectionObserver(function(entries) {
        entries.forEach(function(entry) {
            if (entry.isIntersecting) {
                const offset = circumference - percent / 100 * circumference;
                specified_circle.style.strokeDashoffset = offset;
            }
        });
    });

    observer.observe(specified_circle);
    
}

setProgresses(mapped_values);