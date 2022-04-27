---
layout: post
title: "Petroglyphs, New Mexico"
image:
  path: https://www.botzilla.com/pix2022/petro/bjorke_NM_DSCF7816.jpg
  thumbnail: https://www.botzilla.com/pix2022/petro/bjorke_NM_DSCF7816.jpg
categories: [fStop]
tags: [Sketchbook, Fujifilm]
slides: [pix2022/petro/bjorke_NM_DSCF7400.jpg,
  pix2022/petro/bjorke_NM_DSCF7491.jpg,
  pix2022/petro/bjorke_NM_DSCF7461.jpg,
  pix2022/petro/bjorke_NM_DSCF7490.jpg,
  pix2022/petro/bjorke_NM_DSCF7647.jpg,
  pix2022/petro/bjorke_NM_KBXF5515.jpg,
  pix2022/petro/bjorke_NM_DSCF7553.jpg,
  pix2022/petro/bjorke_NM_DSCF7816.jpg,
  pix2022/petro/bjorke_NM_DSCF8155.jpg,
  pix2022/petro/bjorke_NM_DSCF8075.jpg,
  pix2022/petro/bjorke_NM_DSCF8139.jpg,
  pix2022/petro/bjorke_NM_KBXF5513.jpg]
captions: [shelter,
  message,
  museum,
  shadow,
  church,
  frontier parking only,
  ship,
  explorer,
  watcher,
  marker,
  continuity,
  ghost]
slideDelay: 6000
picless: true
---

<!--more-->


<!-- http://css3.bradshawenterprises.com/cfimg/ BETTER?-->

<!-- from https://cheesecat47.github.io/programming/2019/01/04/make-slideshow/ */

<!-- todo: move to a layout -->


<!-- Slideshow container -->
<div class="slideshow-container">

  {% for slide in page.slides %}
    <div class="mySlides slide-fade">
      <div class="slideshow-counter">{{ forloop.index }} / {{ forloop.length }}</div>
      {% if page.captions %}
        <img src="https://www.botzilla.com/{{ slide }}" style="max-height: 670px"
          alt="{{ page.captions[forloop.index0] }}">
        <!-- <div class="slideshow-caption">{{ page.captions[forloop.index0] }}</div> -->
      {% else %}
        <img src="https://www.botzilla.com/{{ slide }}" style="max-height: 670px">
      {% endif %}
    </div>
  {% endfor %}


  <!-- Next and previous buttons -->
  <!-- <a class="slide-prev" onclick="plusSlides(-1)">&#10094;</a>
  <a class="slide-next" onclick="plusSlides(1)">&#10095;</a> -->

  <!-- This code makes left and right arrow button to change next and previous picture,
  but it makes a timing error when user clicked. So I make this code to comment. -->
</div>
<br>
<script>
  showSlides({{ page.slideDelay }});
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

