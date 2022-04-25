---
layout: page
title: "Slide test"
image:
  path: none
  thumbnail: https://www.botzilla.com/pix2022/bjorke_XEKB2199.jpg
categories: [fStop, GrayScale]
tags: [Ilford, Analog, Darkroom]
---

A test with three slides

<!-- from https://cheesecat47.github.io/programming/2019/01/04/make-slideshow/ */

<!-- Slideshow container -->
<div class="slideshow-container">

  <!-- Full-width images with number and caption text -->
  <div class="mySlides slide-fade">
    <div class="slideshow-counter">1 / 3</div>
    <img src="https://www.botzilla.com/pix2022/bjorke_XEKB2199.jpg" style="width:100%">
    <div class="slideshow-caption">Caption Text</div>
  </div>

  <div class="mySlides slide-fade">
    <div class="slideshow-counter">2 / 3</div>
    <img src="https://www.botzilla.com/pix2022/b-DSCF4949-988.jpg" style="width:100%">
    <div class="slideshow-caption">Caption Two</div>
  </div>

  <div class="mySlides slide-fade">
    <div class="slideshow-counter">3 / 3</div>
    <img src="https://www.botzilla.com/pix2022/L50K6724-988.jpg" style="width:100%">
    <div class="slideshow-caption">Caption Three</div>
  </div>

  <!-- Next and previous buttons -->
  <!-- <a class="slide-prev" onclick="plusSlides(-1)">&#10094;</a>
  <a class="slide-next" onclick="plusSlides(1)">&#10095;</a> -->

  <!-- This code makes left and right arrow button to change next and previous picture,
  but it makes a timing error when user clicked. So I make this code to comment. -->
</div>
<br>
<script>
  showSlides();
  /*I find out the slideshow didn't display automatically at first,
  so add this code to make slideshow display at first or page is refreshed.*/
</script>

<!-- The dots/circles -->
<!-- <div style="text-align:center">
  <span class="slide-dot" onclick="currentSlide(1)"></span>
  <span class="slide-dot" onclick="currentSlide(2)"></span>
  <span class="slide-dot" onclick="currentSlide(3)"></span>
</div> -->

<!-- This code makes a timing error too. -->

