---
layout: post
title: "Nub is in the Details"
categories: [Hacking]
tags: [3D, Games, Digital, Methods, Photoshop, NVIDIA]
---
This is a little game development (or general graphics) tip that I've been thinking about for the past couple of nights, with additional applications for photographic and other images.

It's really a simple observation, followed by some implementation tricks. The dumb observation is that people like noisy pictures. This has been well known, of course, in famous older papers like Rob Cook's 1985/86 paper <a href="http://graphics.pixar.com/StochasticSampling/paper.pdf">Stochastic Sampling in Computer Graphics (PDF).</a> And for many years photographers have been keen on using grain as a means to elicit a sense of sharpness that may be actually greater than what's really in the picture. This isn't really news, but in playing with noise I've found a really simple trick or two that have pretty broad uses.

First, we're going to make a texture.


<!--more-->
&bull; Start up Photoshop, and create a new image that's twice as wide as it is high &#151; preferably both values will be powers of two. In this example, I'll use 512 by 256, RGB.

&bull; Set the foreground color to middle gray (128/128/128 or #808080), select-all, then shift-F5 to get the fill dialog and fill with the Foreground color at 100%. You image is now gray.

&bull; Select <i>only</i> the red channel by selecting it in the channels palette or hitting ctrl-1 (or cmd-1 on a Mac). You should see a plain gray rectangle and the select-all marching dots are still active.

&bull; Select from the Menu bar: Filter -> Noise -> Add Noise.... and set it to 15% and "Gaussian." (Note that if you squint so the at the image is out-of-focus, and click the "Preview" checkbox on and off, the overall gray value doesn't change).

&bull; Now select the Green channel.

&bull; Apply noise in exactly the same way as before.

&bull; Jump back to RGB display, and you should see something pretty similar to this:



![512 x 256 with 15% independant gaussian noise in red and green channels]({{ 'https://www.botzilla.com/blog/archives/512noise.jpg' | absolute_url }})


&bull; We're going to save this as a DDS texture. You'll need the <a href="http://developer.nvidia.com/object/photoshop_dds_plugins.html">NVIDIA Texture Tools DDS plugin</a> if you haven't got it already (if you are a game artist, you almost surely do).

&bull; When the dialog appears, select the "Use existing <a href="http://en.wikipedia.org/wiki/Mip_map">MIP</a> Maps" option and save.

&bull; Close the window.

&bull; Open the resultant DDS file and click "Load MIP Maps" to see all the data.



![noiseMipped.jpg]({{ 'https://www.botzilla.com/blog/pix2007/noiseMipped.jpg' | absolute_url }})


What happened? The DDS exporter assumed the right half of the original image was filled with an image pyramid &#151; the data in the black area was thrown away, since it's not used. We now have a MIP data set where all layers of the MIP stack have noise of roughly the same statistical characteristics for each and every level (rather than each level being a scaled-down vesion of the layer above it). 

What this means is that if this texture is applied to a 3D model, the on-screen frequency of the noise will tend to be constant, regardless of scaling. The texture mapping hardware will always select a level appropriate to the current pixel's screen size, and that level will always have noise of about the frequency we see here on the screen.

Let's try it out on everyone's favorite teapot:



![NoiseMip texture mapped onto teapot]({{ 'https://www.botzilla.com/blog/pix2007/noisepots.jpg' | absolute_url }})


Whether near or far, you can see that the texture feature size &#151; that is, the <i>on-screen</i> size of the noisy "blobs" &#151; is about the same regardless of whether near or far.

I call this approach "constant frequency noise."

If you're experienced in game shading, you may already suspect why we added noise to the red and green channels, but left the blue channel alone.



![Noise mips as tangent space normals]({{ 'https://www.botzilla.com/blog/pix2007/noisebumppots.jpg' | absolute_url }})


Applying this as a tangent space normal maps, you can see that the nubbly detail maintains its on-scren size regardless of whether the pot is near or far. This is different from typical MIP map behavior (which would degenerate towards a smooth surface &#151; see the example below), and while not "physically correct," gives a better consistent <i>feeling</i> to the nature of the rough but shiny material, regardless of rotation, scaling, or distance.

As long as we've got this noise texture, let's try something else. Here are two teapots, one with a standard color texture and one with our noise-mips added to the texture UV values:



![texture and texture with noisy UV offsets.jpg]({{ 'https://www.botzilla.com/blog/pix2007/offsetNoise1.jpg' | absolute_url }})


In areas where textures are greatly over-extended, this method can be used as a variation of "detail texturing" so that instead of soft linear-interpolated blobs, we get little bits of noise.



![Closeup showing stretched texture and detailed offsets to replace aliasing with noise]({{ 'https://www.botzilla.com/blog/pix2007/CloseupOffset.jpg' | absolute_url }})


Of course, in this application we <i>don't</i> want to offset the texture too much when we're not super-close, so rather than using constant-frequency noise, we can just make a square texture, rather than a rectangular one, and let the DDS exporter "Generate MIP maps" insteead &#151; the lower maps will smooth to a center, zero value, so that at a distance there's no visible offset.

Here's an example. As you can see, it's identical at the largeest MIP but smooths quickly to middle gray at the smaller sizes. In this case, where we are using the channels as signed values, middle gray equals zero: no offset, no bump.



![Noise texture the usual way: sclaing-down the top level]({{ 'https://www.botzilla.com/blog/archives/noiseMipped2.jpg' | absolute_url }})


The noise-offset-as-faux-detail technique can be applied to still pictures, too. In Photoshop, you may be familiar with the idea of using the "add noise" filter to cover-up the defects of a picture that's out of focus or enlarged too much.

Let's take the thumbnail of <a href="https://www.botzilla.com/photo/Sampler/5RT.html">this photo</a> as a sample. If we blow up the thumbnail, it looks pretty soft (especially if using bilinear filtering, which is typical for realtime applications like games).

But if we "add noise" (here quite a lot &#151; the same amount we used when creating the noise texture), the effect is "Grainy" rather than "Muddy," as we can see in these side-by-side views:



![Adding noise to an inflated thumbnail]({{ 'https://www.botzilla.com/blog/pix2007/AddNoise.jpg' | absolute_url }})


Alternatively, we can apply the same noise pattern offset method we used for 3D detail texturing to the 2D image.

&bull; Make a red/green noise pattern as before, but the same image size as our soft enlarged image. Save if as a .PSD file &#151; say, "imgOffsets.psd."

&bull; Then go back to the soft enlargement, select "Filter->Distort->Displace..." In this example, the scale was set to 4, the wrap mode was on, and no stretching (since the images were the same size). When the file dialog appears, select our just-created "imgOffsets.psd" as the offset sourcefile.



![Adding noisy pixel offsets to an inflated thumbnail]({{ 'https://www.botzilla.com/blog/pix2007/AddNoiseOffset.jpg' | absolute_url }})


This version creates an illusion of small detail even though there is none &#151; and without altering the colors directly. Some of the obviously-aliased details, such as the highlight on the lower lip, really look far better this way.

Both approaches can be combined &#151; offsets and also a smaller bit of color noise to enhance the apparent sharpness. Another option might be to make the offset image a smaller size and then stretch it in the offset filter, so that the "clumps" are larger than single pixels.

Understanding these uses of noise can extend well beyond Photoshop. An obvious application that would join together these techniques would be better, more sophisticted video scaling performed in real time on a GPU.

Here's a last combined-noise version with clumpy offsets, followed by a sharp version (the thumbnail was a scaled-down version of this) for comparison.



![both luminance and clumping noise]({{ 'https://www.botzilla.com/blog/pix2007/both.jpg' | absolute_url }})




![image based on original slide]({{ 'https://www.botzilla.com/photo/Sampler/5RT.jpg' | absolute_url }})


