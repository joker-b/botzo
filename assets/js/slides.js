// from https://cheesecat47.github.io/programming/2019/01/04/make-slideshow/
//    which borrowed from https://www.w3schools.com/howto/howto_js_slideshow.asp

var slideIndex = 0;
var slideTimer;
var slidesDelay = 5000;
showSlides();

function currentSlide(n) {
  clearTimeout(slideTimer);
  var slides = document.getElementsByClassName("mySlides");
  if (slides.length < 1) return;
  slideIndex = Math.max(1, Math.min(slides.length, n));
  slideIndex --;
  showSlides();
}

function plusSlides(delta) {
  clearTimeout(slideTimer);
  var slides = document.getElementsByClassName("mySlides");
  if (slides.length < 1) return;
  slideIndex += delta;
  slideIndex = Math.max(1, Math.min(slides.length, slideIndex));
  slideIndex --;
  showSlides();
}

function showSlides(Delay) {
  if (Delay) slidesDelay = Delay;
  var slides = document.getElementsByClassName("mySlides");
  if (slides.length < 1) return;
  for (var i = 0; i < slides.length; i++) {
    slides[i].style.display = "none";
  }
  slideIndex++;
  if (slideIndex > slides.length) {slideIndex = 1}
  slides[slideIndex-1].style.display = "block";
  slideTimer = setTimeout(showSlides, slidesDelay);
}

// eof
