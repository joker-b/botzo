---
layout: post
title: "Contrast Curves for Leica Monochrom"
image:
  path: https://www.botzilla.com/pix2021/mono-bouq-trio.jpg
  thumbnail: https://www.botzilla.com/pix2021/mono-bouq-trio.jpg
categories: [GearHead]
tags: [Leica, _Phase4]
---

Adobe Camera Raw (ACR) has supported Leica Monchrom files for most of the past decade, yet the support seems to have been pretty modest -- a linear mapping of the grayscale-source DNG values. Setting your preferences for "Camera Matching" has essentially no effect - the contrast adjustments in the Monochrom are ignored.

The pic above shows three versions. On the left, what ACR will deliver directly from the sensor: a full range but with flat tones. The center is what the EVF showed, and is the in-camera JPG. The right image is something getting closer to my final edit, based on a higher-contrast version like that at the center: closer to the EVF view than what was delivered by ACR.

I couldn't find any publicly-available curves or presets for Monochrom DNGs to match the contrast ranges you might see in the EVF or JPGs. So: I made some. You can find the link below:

<!--more-->

## <a href="https://www.botzilla.com/assets/2021/Monochrom-Contrast-Presets.zip">CLICK HERE TO DOWNLOAD PRESETS AND CURVE FILES</a>

The linked file is a `.zip` folder containing another zip (`Monochrom Contrast - Botzilla.zip`), along with a folder with three Photoshop curves files.

These curves are presets are _specifically for Leica Monochrom cameras_ -- not for creating black and white images from RGB ones.

To load the presets into ACR (and thus both Photoshop and Lightroom), just use ACR's "Import" item in the presets pane, and select the `Monochrom Contrast - Botzilla.zip` file directly.

These curves were originally made for a Monochrom Typ 246 and tested against some old photos made with the M9M -- the curves will work with all Monochrom cameras.

If you prefer to import linear DNGs into Photoshop and use Photoshop's Curves tools, the curve files provided are exact matches to the Camera Raw preset versions. To install, drop them in the Photoshop `Presets/Curves` folder before starting Photoshop.

I've only provided three presets & curves for the Standard, High, and Low Contrast settings of the Monochrom, even though the camera has five settings. The missing "medium low" and "medium high" settings dont seem that crucial if you're already opening the RAW file. Instead, you should use these curves and presets as a launching point for your own subsequent editing. If all you wanted was the JPG, why not just use the JPG?


