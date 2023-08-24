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
    title.style.display = 'none';
    author.style.display = 'none';
    // change size of image
    image.classList.add('translate');
    //display attribute container
    attributeContainer.style.display = 'grid';
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
    const attributeName = attributeContainer.textContent.trim();
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
        const data = mapped_value.data;
        const percent = data;
        setProgress(percent, circle);
    });
}

function setProgress(percent, specified_circle) {
    const radius = specified_circle.r.baseVal.value;
    const circumference = radius * 2 * Math.PI;

    //if below 33% set color to green
    if (percent < 35) {
        specified_circle.style.stroke = '#00ff00';
    }
    //if below 66% set color to yellow
    else if (percent < 65) {
        specified_circle.style.stroke = '#ffff00';
    }
    //if below 100% set color to red
    else {
        specified_circle.style.stroke = '#ff0000';
    }

    specified_circle.style.strokeDasharray = `${circumference} ${circumference}`;
    specified_circle.style.strokeDashoffset = `${circumference}`;    
    // const offset = circumference - percent / 100 * circumference;
    // specified_circle.style.strokeDashoffset = offset;
    // add a transitionend event listener to the parent div

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




