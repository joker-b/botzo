// from https://cheesecat47.github.io/programming/2019/01/04/make-slideshow/
//    which borrowed from https://www.w3schools.com/howto/howto_js_slideshow.asp

var slideIndex = 0;
showSlides();

function showSlides(Delay) {
  var delay = Delay | 5000;
  var i;
  var slides = document.getElementsByClassName("mySlides");
  for (i = 0; i < slides.length; i++) {
    slides[i].style.display = "none";
  }
  slideIndex++;
  if (slideIndex > slides.length) {slideIndex = 1}
  slides[slideIndex-1].style.display = "block";
  setTimeout(showSlides, delay);
}
