---
layout: post
title: "Petroglyphs, New Mexico"
image:
  path: https://www.botzilla.com/pix2022/petro/bjorke_NM_DSCF7816.jpg
  thumbnail: https://www.botzilla.com/pix2022/petro/bjorke_NM_DSCF7816.jpg
categories: [fStop]
tags: [Sketchbook, Fujifilm]
slides: [ [ pix2022/petro/bjorke_NM_DSCF7400.jpg, the hotel ],
   [ pix2022/petro/bjorke_NM_DSCF7491.jpg, the message ],
   [ pix2022/petro/bjorke_NM_DSCF7461.jpg, the museum ],
   [ pix2022/petro/bjorke_NM_DSCF7490.jpg, the shadow ],
   [ pix2022/petro/bjorke_NM_DSCF7647.jpg, the church ],
   [ pix2022/petro/bjorke_NM_KBXF5515.jpg, FRONTIER parking only ],
   [ pix2022/petro/bjorke_NM_DSCF7553.jpg, the ship ],
   [ pix2022/petro/bjorke_NM_DSCF7816.jpg, the explorer ],
   [ pix2022/petro/bjorke_NM_DSCF8155.jpg, the watcher ],
   [ pix2022/petro/bjorke_NM_DSCF8075.jpg, the marker ],
   [ pix2022/petro/bjorke_NM_DSCF8139.jpg, the seasons ],
   [ pix2022/petro/bjorke_NM_KBXF5513.jpg, the ghost ] ]

slideDelay: 6000
picless: true
---

<!--more-->


<!-- http://css3.bradshawenterprises.com/cfimg/ BETTER?-->

<!-- from https://cheesecat47.github.io/programming/2019/01/04/make-slideshow/ */

<!-- todo: move to a layout -->


<!-- Slideshow container -->
{% if page.slides %}
  <div class="slideshow-container">
    {% for slide in page.slides %}
      <div class="mySlides slide-fade">
        <div class="slideshow-counter">{{ forloop.index }} / {{ forloop.length }}</div>
        {% if slide[1] %}
          <img src="https://www.botzilla.com/{{ slide[0] }}" style="max-height: 670px"
            alt="{{ slide[1] }}">
          <div class="slideshow-caption">{{ slide[1] }}</div>
        {% else %}
          <img src="https://www.botzilla.com/{{ slide[0] }}" style="max-height: 670px">
        {% endif %}
      </div>
    {% endfor %}
    <!-- Next and previous buttons -->
    <a class="slide-prev" onclick="plusSlides(-1)">&#10094;</a>
    <a class="slide-next" onclick="plusSlides(1)">&#10095;</a>
  </div> <!-- slideshow-container -->
  <br> <!-- hokey, but makes some space for captions when they are present -->
  <script>
    showSlides({{ page.slideDelay }});
    /*I find out the slideshow didn't display automatically at first,
    so add this code to make slideshow display at first or page is refreshed.*/
  </script>
  <!-- The dots/circles  -->
  <div style="text-align:center">
    {% for slide in page.slides %}
      <span class="slide-dot" onclick="currentSlide({{ forloop.index }})"></span>
    {% endfor %}
  </div>
{% endif %}
