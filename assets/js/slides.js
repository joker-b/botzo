// from https://cheesecat47.github.io/programming/2019/01/04/make-slideshow/
//    which borrowed from https://www.w3schools.com/howto/howto_js_slideshow.asp

var slideIndex = 0;
var slideTimer = 0;
var slidesDelay = 5000;
var slidesFinalDelay = 2; // if zero, don't cycle, just hold on end slide
showSlides();

function currentSlide(n) {
  if (slideTimer) clearTimeout(slideTimer);
  var slides = document.getElementsByClassName("mySlides");
  if (slides.length < 1) return;
  slideIndex = Math.max(1, Math.min(slides.length, n));
  slideIndex --;
  showSlides();
}

function plusSlides(delta) {
  if (slideTimer) clearTimeout(slideTimer);
  var slides = document.getElementsByClassName("mySlides");
  if (slides.length < 1) return;
  slideIndex += delta;
  slideIndex = Math.max(1, Math.min(slides.length, slideIndex));
  slideIndex --;
  showSlides();
}

function showSlides(Delay) {
  if (Delay) slidesDelay = Delay;
  var adjDelay = slidesDelay;
  var slides = document.getElementsByClassName("mySlides");
  if (slides.length < 1) return;
  for (var i = 0; i < slides.length; i++) {
    slides[i].style.display = "none";
  }
  slideIndex++;
  if (slideIndex == slides.length) {
    adjDelay *= slidesFinalDelay;
  }
  if (slideIndex > slides.length) {
    slideIndex = 1;
  }
  slides[slideIndex-1].style.display = "block";
  if (adjDelay > 0) {
    slideTimer = setTimeout(showSlides, adjDelay);
  } else {
    slideTimer = 0;
  }
}

// eof
