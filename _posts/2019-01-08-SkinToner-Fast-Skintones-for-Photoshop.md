---
layout: post
title: "SkinToner: Fast Easy Skin Tones in Photoshop"
categories: [GearHead]
tags: [Analog,Digital,Darkroom,Printing]
markdown: kramdown
---

<img alt="SkinToner Sample" src="http://www.botzilla.com/img/pix2019/skinTonerBJRK7403ocs.jpg" class="align-center"  />

I've seen a few video tutorials about getting good skintones in Photoshop, and while some were [illuminating](https://youtu.be/Wvr8LCSuFjE) or even [inspiring,](https://youtu.be/yMjb7sMiAsg) all of them were more involved than they needed to be: using numeric templates or eyedropper-tool tricks in concert with the info panel and a calculator, etc. Time for an easy tool: <a href="http://www.botzilla.com/blog/archives/SkinToner.jsx"><strong><em>SkinToner</em></strong></a>

<!--more-->
_SkinToner_ works in any recent version of Photoshop, and should be able to present you with great-looking neutral skin tones for photos of anyone regardless of their complexion or ethnicity.

### Installation

Like [ChartThrob,]({{ site.baseurl }}{% post_url 2006-10-24-ChartThrob-A-Tool-for-Printing-Digital-Negatives %}) *SkinToner* is a Photoshop _script_ rather than an Action or PlugIn &mdash; you trigger it from the Photoshop _"File->Scripts"_ menu.

If you just download <a href="http://www.botzilla.com/blog/archives/SkinToner.jsx">_SkinToner.jsx_</a> (right-click on the link and choose "Save Link As...") to any old place on your hard drive, you can find it from within Photoshop by using Photoshop's _"File->Script->Browse..."_ menu item.

An easier and faster way to use it is to copy the `SkinToner.jsx` file specifically to the `Presets/Scripts` folder within your particular flavor of Photoshop. For my Mac circa January 2019 that's in `/Applications/Adobe Photoshop CC 2019/Presets/Scripts/` &mdash;  put the script there, restart Photoshop, and then _SkinToner_ will just appear directly as part of your Photoshop _"File->Scripts"_ menu, as part of Photoshop itself. It's faster to use and can even be incorporated into keyboard shortcut actions.

### Usage

To apply, just load any RGB picture, select a sample area of the existing skintone, and run the _SkinToner_ script.

The script will add a Curves adjustment layer named "SkinToner" to your Photoshop document. That new layer will map the color found in your sample selection to a more-convincing skin tone.

_Done._

----

#### Fancier Usage

Because the curves layer is... well, a _layer,_ it comes with a layer mask. The Curves adjustment created by _SkinToner,_ by default, affects the entire image. If you want it to only affect a limited region, Just invert the mask (that is, make the mask black) and then paint-in (using white on the mask) the areas of skin you'd like corrected.

#### What Might Go Wrong

_SkinToner_ will present you an alert warning of some common error cases:

* _SkinToner_ only works on RGB-mode pictures.
* It needs you to select some area(s) of skintone for sampling before you run the script.
* It wants to look directly at pixels, so be sure a picture layer is selected, not a layer group or similar editing tool.

It's also possible that _SkinToner_ can deliver odd results in a few special circumstances:

* If the image selection is over-exposed or under-exposed, the correction can end up "pinned" -- some channels will get forced to 100% or 0% in parts of the picture. Sometimes this can be fixed by using a layer mask, but sometimes... sorry, there are limits!
* Likewise, if the photo is strongly de-saturated, the resulting color shifts can be too strong. _SkinToner_ likes simple, middle-of-the-color-range photos as source material. It can't do anything with a black and white photo.
* Be careful to select areas of smooth consistent skin color, avoiding shiny highlights and makeup. Those highlights are not skin color, and they will pollute the color correction! In the sample above, I selected an area around the neck and clavicle, rather than the face, to get a highlight-free tone.
* There will be photos where the skin color varies a lot because of multi-colored lighting: different lights from different sides of the subject. An example might be a portrait of someone lit by a warm interior lamp while standing near a cool-toned window. _SkinToner_ will do its best, but if you correct a magenta image to be more green on one side, it will be more green on the _other_ side, too. One option in these cases, if you want to get more uniform skin tones everywhere, is to just run _SkinToner_ multiple times: run it once with, say, one part of the face selected, then hide (and potentially rename) the SkinToner layer, reselect your picture layer, select another part of the face (lit by an opposing light), and run _SkinToner_ again. The script will add another curves layer. Repeat as you like. By mixing these curve layers together via their layer masks, you can quickly rebalance the photo any way you'd like.

#### More Info

_SkinToner_ is part of [this github repository.](https://github.com/joker-b/PhotoshopScripts) I always appreciate feeback and pull requests for improvement!

