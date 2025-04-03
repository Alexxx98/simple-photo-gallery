const imagesInput = document.getElementById('images');
const imagesStored = [];
const previewContainer = document.getElementById('img-preview-container')

// Preview chosen images
imagesInput.addEventListener('change', function(event) {
    const images = event.target.files
    for (let i = 0; i < images.length; i++) {
        imagesStored.push(images[i]);
        let img = document.createElement('img');
        img.className = 'img-preview';
        img.src = URL.createObjectURL(images[i]);
        img.alt = images[i].name;
        previewContainer.appendChild(img);
    }
})

// Remove image from preview
previewContainer.addEventListener('click', function(event) {
    let img = event.target;
    imagesStored.forEach((imgFile, index) => {
        if (imgFile.name === img.alt) {
            imagesStored.splice(index, 1);
            previewContainer.removeChild(img);
        } 
    });
})

const submitButton = document.getElementById('send-images')

// Send images
submitButton.addEventListener('click', function() {
    fetch('http://cloud.home/gallery/upload')
})
