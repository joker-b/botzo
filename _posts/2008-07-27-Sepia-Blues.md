---
layout: post
title: "Sepia Blues"
categories: [GearHead]
tags: [B&W, Methods, Digital, Lumix]
---


![Sepia Image + 3 component channels]({{ 'https://www.botzilla.com/blog/pix2008/SepiaWai.jpg' | absolute_url }})


[Almost two years ago]({{ site.baseurl }}{% post_url 2006-08-27-Are-Sepia-Images-Better %}) I wrote an entry about in-camera sepia, wondering if in fact a sepia transformation could provide a photo with more tonalities than a tyical 8-bit black and white.


<!--more-->
At the time, I assumed that the crucial yes or no part of that answer would involve the B&W conversion -- if it was done before the sepia rotation of the color space, or after -- that is, if the # of B&W values was fixed to 256 and <i>then</i> rotated, or if it was in a higher precision RAW format, rotated, and then quantized to eight bit. In the latter case, you'd have more tones.

I was half right, and it was the poor half. Looking closely at LX2 sepia images like the one above, it's become clear that the B&W is converted and quantized first. And the part I was wrong about I didn't expect -- that the LX2 creates sepia images not through a matrix transform in RGB color space, but simply by adding a color to the B&W image. The color appears to be (+30R,-18G,-38B). That is, raise red, and drop green and blue, by a simple addition.

Since the values are already clipped to 8-bit, this means a loss of highlights in the red channel and a loss of shadow detail for green and blue. Since all three are made from the same B&W original, it's possible to rebuild that original B&W 8-bit picture by adding (-30R,+18G,+38B) and then selectively using the shadow detail from the red channel and the highlights from the green or blue channels. The result, in Photoshop, is the same as if the pic had just been shot in B&W to start with (barring JPEG artifacts).

So why does it <i>seem</i> to have more tonality? I'm guessing that it simply looks better on the small, contrasty camera LCD.

It's a tragedy that the B&W image is already clipped to 8-bit before sepia conversion. If the image was unclipped, the sepia conversion realy <i>would</i> be better, with and increased number of shadow tones in red and highlights in blue and green. It is what it is, though.

At least for web use, this is suggesting to me the following work approach for high quality B&W from JPEGs (when time demands preclude shooting in RAW):

&bull; count on spatial resolution as a stand-in for pixel depth detail. Given some level of pixel noise, 4x4 8-bit pixels should be better than one 12-bit pixel. For a reduction from a 4K image down to a 500-pixel web snap, there are a lot of input pixels for every final output pixel.

&bull; with this in mind, set the camera to a low-contrast image, to compact as much of the original RAW range into the 8-bit jpeg, and then feel free to beat on it using levels and curves later on -- knowing that even if precision is lost per-pixel, a lot of it will be made up in the size reduction step.

I'll report on some results soon.

