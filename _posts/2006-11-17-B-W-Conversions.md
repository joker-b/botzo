---
layout: post
title: "B&W Conversions"
categories: [GearHead]
tags: [_Phase1]
---


![bwConvIz.jpg]({{ 'https://www.botzilla.com/blog/pix2006/bwConvIz.jpg' | absolute_url }})

While my iTunes subscribes to it, I have to say that I'm not a huge fan of <a href="http://www.photoshopuser.com/">NAPP's</a> "Photoshop TV" video podcast. I subscribe in the hope that some of the tips on the show will be useful. At the same time I dread having to wade through the hosts' gossipy and self-congratulatory prattle. It's better to watch on iTunes than the iPod, mostly because it's easier to fast-forward and skip those sections on the PC. 

Another gripe: often the latest episode sometimes takes an hour to download on a broadband connection. Ugh.

This week, though, my pains were rewarded by a segment shot at the recent Photoshop World conference, featuring <a href="http://www.johnpaulcaponigro.com/">John Paul Caponigro</a> and his recommendations and method for converting color images to black and white. His method was different from what I have been using and I like it a lot. If you're used to working in Photoshop adjustment layers, the pic above tells almost the whole story... with more details below.

<!--more-->
What I've been doing (up to now, that is) is using a "channel mixer" layer with the 'monochrome' button checked to do my conversions, & quickly previewing all three channels (ctrl-1, ctrl-2, ctrl-3) before adding that layer. So does Caponigro. The tricky part for me has been getting the balance of the three R, G and B channels to look good (more effort than just hitting "grayscale" but a lot more control).

Caponigro's method depends on the "channel mixer," but he uses <i>two</i> layers where I had been using one &#151; for a lot more ease, speed, and flexibility. In this expanded method, just leave the "channel mixer" at its monochrome <i>default:</i> that is, check the "monochrome" box and leave the sliders set to 100% red, 0% green, and 0% blue. The resulting monochrome pic with therefore contain <i>only</i> the red channel. Rather than tweak the channel balancxes in the mixer, insert a "Hue/Saturation" layer immediately below the channel mixer layer, and play with the  input color balance by simply sliding "Hue" back and forth.

A big <i>Duh!</i> moment for me. This method is <i>so</i> much more fluid to use, lots of variations can be developed just by dragging around that single slider.



![bwHueVars.jpg]({{ 'https://www.botzilla.com/blog/pix2006/bwHueVars.jpg' | absolute_url }})




![bwLimits.jpg]({{ 'https://www.botzilla.com/blog/pix2006/bwLimits.jpg' | absolute_url }}){: .align-left}

I think I'd seen an article describing his method before, but the video really made it come alive for me &#151; and I realized it wasn't just useful for the landscapes typically used as examples.

The pic above shows a range of variations that can gained just from sliding "Hue" back and forth &#151; some cartoonish, some pretty standard and some Just Right.

If I felt like further noodling, all the other "Hue Saturation" controls could have been used too, including tweaks across specific color ranges (raising the saturation of just the reds, for example, could lighten the darker side of the face &#151; if I'd wanted that). For the sake of this example I've just stuck to a "straight" manipulation of only Hue.

The conversion happens independently from the two top Curve layers, which are optional. I use them (a) to give the overall picture a bit of a contrasty "S" characteristic tonal range that I like (that's the 'bwLimits' layer), and (b) to give the final B&W image some color tone by tweaking the blue channel only: boosting a wee bit in the shadows and pulling it back a wee bit in the highlights for a <i>slight</i> warm/cool effect (the "toneCurves" layer) (these layers would be the same regardless of the method I'd chosen for the basic B/W conversion from color).

In the pic at left you can see the "bwLimits" layer editor, which shows the "S" pretty clearly. It's not a <i>strong</i> "S" &#151; but it's there just the same, and the high and low points of the histogram are deliberately brought-in a little to give a full range between pure black and pure white.



![bwTone.jpg]({{ 'https://www.botzilla.com/blog/pix2006/bwTone.jpg' | absolute_url }}){: .align-right}

Below that we see the "toneCurves" editor, which is only applied to the blue channel to create that warm/cool effect (for a color image, as on the web. When printing B&W I currently prefer to use Roy Harrington's <a href="http://www.harrington.com/">Quadtone RIP,</a> which has its own warm/cool print style).

(Photoshop experts may point out that I could have done the work of <i>both</i> curves layers in a single layer. They're technically correct, though I prefer using two layers to do two different jobs)

In both cases, the 'curviness' of those curves applied is really very slight. The Hue/Saturation layer is where all the really bold action occurs.

This shot was just a quick grab from yesterday at the coffee shop. Iz was working with her laptop and didn't even realized that she'd set herself up with a cluster of papers on the tabletop supplying reflected fill beneath her face, which was already illuminated by a big soft-source picture window. The color image (shot quickly with the camera set to "P") doesn't really have the right feel, especially given the mixed-color nature of the light sources (the window was partially obscured by a tan sahde above her head, blue-gree anti-glare film near her face, but no film on the papers &#151; combined with incandescent lamps from the other side), but the B&W starts to approach the luminous glow I saw when shooting. Other than the conversion, there's not a bit of dodging or other alteration required for this one.
