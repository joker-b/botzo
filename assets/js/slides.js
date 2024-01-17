// from https://cheesecat47.github.io/programming/2019/01/04/make-slideshow/
//    which borrowed from https://www.w3schools.com/howto/howto_js_slideshow.asp

var slideIndex = 0;
var slideTimer = 0;
var slidesDelay = 5000;
var slidesFinalDelay = 2; // if zero, don't cycle, just hold on end slide
var slidePause = false;

// besr way to start the slideshow: currentSlide(0, slideDelayValue)
function currentSlide(n, Delay) {
  slidesDelay = Delay || slidesDelay;
  if (slideTimer) clearTimeout(slideTimer);
  var slides = document.getElementsByClassName("mySlides");
  if (slides.length < 1) return;
  slideIndex = Math.max(1, Math.min(slides.length, n));
  slideIndex --;
  showSlides(slidesDelay);
}

function plusSlides(delta) {
  var Delta = delta | 1;
  if (slideTimer) clearTimeout(slideTimer);
  var slides = document.getElementsByClassName("mySlides");
  if (slides.length < 1) return;
  slideIndex += Delta;
  slideIndex = Math.max(1, Math.min(slides.length, slideIndex));
  slideIndex --;
  showSlides(slidesDelay);
}

function negSlides() {
  plusSlides(-1);
}

function stopStartSlides() {
  slidePause = !slidePause;
  var playMark = document.getElementById("slide-play");
  var pauseMark = document.getElementById("slide-paused");
  if (slidePause) {
    if (slideTimer) clearTimeout(slideTimer);
    if (pauseMark) pauseMark.style.display = "block";
    if (playMark) playMark.style.display = "none";
  } else {
    if (pauseMark) pauseMark.style.display = "none";
    if (playMark) playMark.style.display = "block";
    showSlides(slidesDelay);
  }
}

function setSlidesFinal(delayFactor) {
  slidesFinalDelay = delayFactor;
}

function showSlides(Delay, ForcePlay) {
  slidesDelay = Delay || slidesDelay;
  if (ForcePlay) slidePause = false;
  var adjDelay = slidesDelay;
  var slides = document.getElementsByClassName("mySlides");
  if (slides.length < 1) return;
  var dots = document.getElementsByClassName("slide-dot");
  var dotsOkay = (slides.length == dots.length);
  for (var i = 0; i < slides.length; i++) {
    slides[i].style.display = "none";
    if (dotsOkay) dots[i].style.backgroundColor = "#b0b0b0";
  }
  slideIndex++;
  if (slideIndex == slides.length) {
    adjDelay *= slidesFinalDelay;
  }
  if (slideIndex > slides.length) {
    slideIndex = 1;
  }
  slides[slideIndex-1].style.display = "flex";
  if (dotsOkay) dots[slideIndex-1].style.backgroundColor = "black";
  if ((adjDelay > 0) && (!slidePause)) {
    slideTimer = setTimeout(showSlides, adjDelay, Delay);
  } else {
    slideTimer = 0;
  }
}

// eof
