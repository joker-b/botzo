// from https://cheesecat47.github.io/programming/2019/01/04/make-slideshow/
//    which borrowed from https://www.w3schools.com/howto/howto_js_slideshow.asp

var slideIndex = 0;
var slideTimer = 0;
var slidesDelay = 5000;
var slidesFinalDelay = 2; // if zero, don't cycle, just hold on end slide
var slidePause = false;
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
  var Delta = delta | 1;
  if (slideTimer) clearTimeout(slideTimer);
  var slides = document.getElementsByClassName("mySlides");
  if (slides.length < 1) return;
  slideIndex += delta;
  slideIndex = Math.max(1, Math.min(slides.length, slideIndex));
  slideIndex --;
  showSlides();
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
    showSlides();
  }
}

function showSlides(Delay, ForcePlay) {
  if (Delay) slidesDelay = Delay;
  if (ForcePlay) slidePause = false;
  var adjDelay = slidesDelay;
  var slides = document.getElementsByClassName("mySlides");
  if (slides.length < 1) return;
  var dots = document.getElementsByClassName("slide-dot");
  var dotsOkay = (slides.length == dots.length);
  if (!dotsOkay) {
    console.log("slides.length = " + slides.length + ", dots.length = " + dots.length);
  }
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
  slides[slideIndex-1].style.display = "block";
  if (dotsOkay) dots[slideIndex-1].style.backgroundColor = "black";
  if ((adjDelay > 0) && (!slidePause)) {
    slideTimer = setTimeout(showSlides, adjDelay);
  } else {
    slideTimer = 0;
  }
}

// eof
