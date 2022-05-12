---
layout: post
title: "SkinToner: Fast Easy Skin Tones in Photoshop"
categories: [GearHead]
tags: [Tools, Digital, Darkroom, Printing, Portrait, Methods, Photoshop]
markdown: kramdown
---

<img alt="SkinToner Sample" src="https://www.botzilla.com/img/pix2019/skinTonerBJRK7403ocs.jpg" class="align-center"  />

I've seen a few video tutorials about getting good skintones in Photoshop. Some were [illuminating,](https://youtu.be/Wvr8LCSuFjE) some even [inspiring](https://youtu.be/yMjb7sMiAsg) &mdash; but all were more involved than they needed to be: using numeric templates or eyedropper-tool tricks in concert with the info panel and a calculator, etc.

Time for an easy select-click-done tool: <a href="https://www.botzilla.com/blog/archives/SkinToner.jsx"><strong><em>SkinToner</em></strong></a>

<div class="notice">
<p><img alt="Monk Skintone Scale" src="https://www.botzilla.com/pix2022/monk-hsl.jpg" class="align-center"  /></p>
<p><i>May 2022 Update:</i> The new publication of the <a href="https://skintone.google/get-started">Monk Skin Tone (MST) Scale</a> is a big step forward in rendering great skin tones for everyone. The illustration of the scale above, along with HSL hue values, show that unlike the common Photoshop folklore, skin hues are _not_ always uniform in hue, not even linearly changing from light to dark.</p><p>Tones can become further complicated when multiple people appear in the frame. The <em>SkinToner</em> tool offered here is thus crude in two respects: it only offers a single adjustment per image, and it may apply that (potentially close but imperfect) adjustment to all faces in the frame. The good news is: <em>SkinToner</em> creates adjustable layers so if you chose to ask or alter them, it's still easy and fast.</p></div>

<!--more-->

<em>SkinToner</em> works in any recent version of Photoshop, and should be able to present you with great-looking neutral skin tones for photos of anyone regardless of their complexion or ethnicity.

### Installation

Like [ChartThrob,]({{ site.baseurl }}{% post_url 2006-10-24-ChartThrob-A-Tool-for-Printing-Digital-Negatives %}) *SkinToner* is a Photoshop _script_ rather than an Action or PlugIn &mdash; you trigger it from the Photoshop _"File->Scripts"_ menu. If you already know how to install Photoshop scripts, you can skip down to **Usage**

If you just download <a href="https://www.botzilla.com/blog/archives/SkinToner.jsx">_SkinToner.jsx_</a> (right-click on the link and choose "Save Link As...") to any old place on your hard drive, you can find it from within Photoshop by using Photoshop's _"File->Script->Browse..."_ menu item.

An easier and faster way to use it is to copy the `SkinToner.jsx` file specifically to the `Presets/Scripts` folder within your particular flavor of Photoshop. For my Mac circa January 2019 that's in `/Applications/Adobe Photoshop CC 2019/Presets/Scripts/` &mdash;  put the script there, restart Photoshop, and then _SkinToner_ will just appear directly as part of your Photoshop _"File->Scripts"_ menu, as part of Photoshop itself. It's faster to use and can even be incorporated into keyboard shortcut actions.

### Usage

Load any RGB picture, select a sample area of the existing skintone pixels, and run the _SkinToner_ script.

_Done._

The script will add a Curves adjustment layer named "SkinToner" to your Photoshop document. That new layer will map the color found in your sample selection to a more-convincing skin tone.

----

#### Fancier Usage

Because the curves layer is... well, a _layer,_ it comes with a layer mask. The Curves adjustment created by _SkinToner,_ by default, affects the entire image. If you want it to only affect a limited region, Just invert the mask (that is, make the mask black) and then paint-in (using white on the mask) the areas of skin you'd like corrected.

Sharing the correction between documents is also easy &mdash; you can copy and paste the adjustments layer freely to get one good skin tone for an entire photo shoot.

#### What Might Go Wrong

Occasionally photos won't work with _SkinToner,_ but it can catch many common cases before they occur. The script will present you an alert warning of common error cases like these:

* _SkinToner_ only works on RGB-mode pictures.
* It needs you to select some area(s) of skintone for sampling before you run the script.
* It wants to look directly at pixels, so be sure a picture layer is selected, not a layer group or similar editing tool.

It's also possible that _SkinToner_ can deliver odd results in a few special circumstances:

* **Exposure:** If the image selection is over-exposed or under-exposed, the correction can end up "pinned" -- some channels will get forced to 100% or 0% in parts of the picture. Sometimes this can be fixed by using a layer mask, but sometimes... sorry, sometimes there's just not a good color in there to start from.
* **Saturation:** Likewise, if the photo is strongly de-saturated, the resulting color shifts can be too strong. _SkinToner_ likes simple, middle-of-the-color-range photos as source material. It can't do anything with a black and white photo.
* **Selected Areas:** Be careful to select areas of smooth consistent skin color, avoiding shiny highlights and makeup. Those highlights are not skin color, and they will pollute the color correction! In the sample above, I selected an area around the neck and clavicle, rather than the face, to get a highlight-free tone.
* **Mixed-Color Lighting:** There are lots of great photos where the skin color varies from multi-colored lighting from different sides of the subject. An example might be a portrait of someone lit by a warm interior lamp while standing near a cool-toned window. _SkinToner_ will do its best, but if you correct an image to be, say, more green on one side of the face, it will be more green on the _other_ side, too. One option in these cases, if you want to get more uniform skin tones everywhere, is to just run _SkinToner_ multiple times: run it once with, say, one part of the face selected, then hide (and potentially rename) the SkinToner layer, reselect your picture layer, select another part of the face (lit by an opposing light), and run _SkinToner_ again. The script will add another curves layer. Repeat as you like. By mixing these curve layers together via layer masks, you can quickly rebalance the photo any way you'd like.

#### More Info

_SkinToner_ is part of [this github repository.](https://github.com/joker-b/PhotoshopScripts) I always appreciate feeback and pull requests for improvement!

