---
layout: post
title: "Differentiable Scratches"
image:
  path: https://www.botzilla.com/pix2021/cumulus_iter_2.jpg
  thumbnail: https://www.botzilla.com/pix2021/cumulus_iter_2.jpg

categories: [PhotoRant]
tags: [Machine Learning, Neurography, Math]
---

A challenge for "neural pictures" is the amount of memory required for rendering even a small photo-like picture. Applying the largest GPUs and TPUs available at Google still may only produce a 2K image. 

An alternative approach is to use _vector graphics,_ that is, images not defined as easily-managed rows of pixels but as abstract lines and curves and fillable regions, as in software like Adobe Illustrator, inkScape, or formats like path-based SVGs. A sharp-edged circle renders as a sharp-edged circle regardless of the final print or JPG size.

Which is what I've been doing, and what this post is about.

<!--more-->

<figure class="align-center">
<img alt="Moto Sketch" src="https://www.botzilla.com/pix2021/motorcycle_09-16-01-03_unclipped.jpg">
<figcaption>Motorcycle Leaning Hard into a Racing Turn</figcaption>
</figure>

The picture above is a rather scruffy and deliberately spare sketch guided by CLIP and based on the prompt phrase: _"motorcycle leaning hard into a racing turn."_ It's made from vector strokes, rather than raster pixels.

Maybe you can see it, maybe not. Intriguing that the system can come up with something using just a few lines. One of my explorations is trying to see just how few strokes can work, with some subjects.

At the heart of such an approach is _differentiable_ vector graphics, which in general hasn't existed. Neighboring pixels in a raster image are differentiable -- that is, you can look at a pixel and its neighbor and decide "what's the difference?" -- which is brighter or darker, and by how much? For random collections of curves, lines, and shapes, without an orderly grid... no. Every color and edge could be anywhere, independant of the others. Which is a challenge for analysis, because those relationships are key for deep learning and other image operations.

Enter a new, mixed approach, published for last December's SIGGRAPH Asia: <a href="https://people.csail.mit.edu/tzumao/diffvg/">"Differential Vector Graphics Rasterization for Editing and Learning."</a>

<center> <iframe width="560" height="315" src="https://www.youtube.com/embed/coV29MzZsGc" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</center>

This new renderer (<a href="https://github.com/BachiLi/diffvg">"diffvg"</a>) was out only a few months before being connected in Spring 2021 to <a href="https://openai.com/blog/clip/">OpenAI's just-published CLIP.</a> The combo was published by Kevin Frans of MIT, who with collaborators, as a <a href="https://twitter.com/kvfrans/status/1409925269117362181?lang=en">Colab Notebook named CLIPDraw.</a> You can try it yourself without reading the associated paper, but you <a href="https://arxiv.org/abs/2106.14843">really should read it</a> -- the paper's full of good observations about the nature of current image datasets.

It's been straightforward to add SVG outputs to CLIPDraw, as well as contrain it with image priors, color palettes, etc. From there I can print at 20K pixels or even higher.

I'm hardly the first to look at extending CLIPDraw (that's kind of the _point_ in a Colab notebook): <a href="https://twitter.com/RiversHaveWings/status/1410020043178446848">this post by @RiversHaveWings</a> is an exceptional example using much denser collections of strokes.

A curious behavior, if you watch such a dense painting develop, is that CLIPDraw learns line placement very separately from line color. In fact it often hardly moves the strokes at all, prefering to hash-around colors to get a picture to match its desired goal.

You can see it in three stages of development of some rather bisquity-looking clouds for the painting below. I've added arrows showing two arcs in a very early stage: one thick bright curve, one dark squiggle below it. In later stages of the same image, those two strokes are still there -- almost unchanged save for their color.

<figure class="align-center">
<img alt="Cloud" src="https://www.botzilla.com/pix2021/cumulus_stack.jpg">
<figcaption>Accumulating Cumulus Clouds</figcaption>
</figure>

This is very unlike a human artist, especailly when building drawings from very thin lines (think: pencil or ballpoint pen, like the motorcycle drawing). The computer sometimes "gets" that collections of strokes can be used to build up color in cross-hatching and shading -- but not always.

<figure class="align-center">
<img alt="Cloud" src="https://www.botzilla.com/pix2021/cumulus_1000.jpg">
<figcaption>Final Reject: Bisquits Flying into the Sunset</figcaption>
</figure>

You can also see a habit the system has of "signing" paintings in the corners -- often writing out english words from the prompt, or even occasionally surprises like "Vincent." Most image databases, scraped from the internet, can contain bits of text and the computer happily learns to add text-like shapes in the typical locations. This one might have a hint of the <a href="https://www.artstation.com/?sort_by=community">Artstation</a> logo? Extra constraints need to be added to suppress the painter's ego, you might say.

<figure class="align-center">
<img alt="Cloud" src="https://www.botzilla.com/pix2021/cumulus-detail.jpg">
<figcaption>Near-Center Detail Showing Strokes</figcaption>
</figure>

Further experiments yet to come!

