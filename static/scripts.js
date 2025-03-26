// Preview chosen images
const imagesInput = document.getElementById('images');
const imagesArray = [];
const storedImages = new FormData;
imagesInput.addEventListener('change', function(event) {
    const previewContainer = document.getElementById('img-preview-container')
    const images = event.target.files
    for (let i = 0; i < images.length; i++) {
        imagesArray.push(images[i]);
        let img = document.createElement('img');
        img.className = 'img-preview';
        img.src = URL.createObjectURL(images[i]);
        previewContainer.appendChild(img);
    }
    // imagesInput.value = '';

    // imagesArray.forEach(image => {
    //     storedImages.append('images', image)
    // });
    // console.log(storedImages);
})
