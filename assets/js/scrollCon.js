function scrollToNextImage() {
    var container = document.querySelector('.scrolling-container');
    var wrapper = document.querySelector('.images-wrapper');
    var images = wrapper.querySelectorAll('img');
    var button = document.querySelector('.scroll-button');
  
    var containerWidth = container.clientWidth;
    var scrollLeft = container.scrollLeft;
  
    // Find the next image position
    var nextImageIndex = -1;
    for (var i = 0; i < images.length; i++) {
      if (images[i].offsetLeft > scrollLeft + containerWidth) {
        nextImageIndex = i;
        break;
      }
    }
  
    if (nextImageIndex !== -1) {
      // Smoothly scroll to the next image
      wrapper.scrollTo({
        left: images[nextImageIndex].offsetLeft,
        behavior: 'smooth'
      });
    } else {
      // Hide button if at the end
      button.style.display = 'none';
    }
  }
  