---
layout: post
title: "Let's Get Small"
categories: [Nuke Em from Orbit]
---
<i>(A few years ago, I wrote a number of internal documents for <a href="http://www.squaresoft.com/" target="_blank">Square,</a> describing important aspects of digital imaging and production for the crew of <a href="http://www.imdb.com/title/tt0173840/" target="_blank"><u>Final Fantasy: The Spirits Within</u></a> and the <a href="http://www.intothematrix.com/" target="_blank"><u>Animatrix.</u></a> After Square closed their Hawaii production operations, those documents disappeared &#151; for fun, I'll be revisiting the ideas from some of them. Wish I could find the originals...)</i>

When you see an object (spacecraft, character, monster, sinking ship...) rendered in 3D by computer, chances are good that the visual quality surface is defined by three basic sets of data: the <i>geometry</i> that describes the surface; <i>texture maps</i> (essentailly form-fitting painted decals that cover that surface); and the <i>shader</i> (a snip of code within the rendering program that describes how light bounces off a particular kind of material &#151; as a simple example, think of how different a piece of gold looks compared to gold-hued plastic (or gold-colored carpeting). They're the same basic color, but their physical properties are different and they <i>look</i> different &#151; a shader is the computer's way of defining those physical/optical properties). These chunks of "art assets" tell you if you're looking at the side of a barn, a battleship, or someone's cheek.

One of the toughest ongoing problems in all computer graphics (as in painting, btw) is the issue of <i>scale.</i> At a distance of 6km, a large enemy star cruiser can be adequately represented by a single triangle &#151; from 10 meters away, we expect to see every rivet. 

Photographs play an increasingly-large role in the creation of texture maps for games and movies
