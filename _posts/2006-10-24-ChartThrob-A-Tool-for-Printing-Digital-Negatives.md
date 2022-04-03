---
layout: post
title: "ChartThrob: A Tool for Printing Digital Negatives"
categories: [GearHead]
tags: [Analog,Digital,Darkroom,Printing]
markdown: kramdown
---
![The ChartThrob Chart]({{ 'https://www.botzilla.com/blog/pix2007/CT107.jpg' | absolute_url }}){: .align-center }

_Updated Jan 2019_

In 2006, at a <a href="http://www.pacificartleague.org/">Pacific At League</a> meeting, I met <a href="http://www.luminaryarts.com/">Thomas Howard,</a> and saw how he was using charts to hand-profile his process to make <a href="http://luminaryarts.com/Reference/Articles/PPDN/">digital negatives for platinum-process contact printing.</a>

I figured this labor-intensive process could be automated, so: I automated it, and made a tool called <a href="https://www.botzilla.com/blog/archives/ChartThrob.jsx"><strong><em>ChartThrob,</em></strong></a> which runs right inside _Adobe Photoshop._ It's available for public, free-for-everyone <s>ab</s>use.

<!--more-->

<h3>Version: 1.15 &mdash; Jan 2019 </h3>

<strong><em>ChartThrob</em></strong> is a a JSX-format javascript for <a href="http://www.adobe.com/">Adobe Photoshop.</a> It works with all versions of Photoshop since Photoshop CS2. It works for both Windows and Mac versions of Photoshop. Since 2006 thousands of photgraphers have used ChartThrob to make terrific prints. It's used in college photo curricula and can even be used to optimize picture quality in self-published photo books through services like Blurb and Lulu. And: It's free.

<strong>ChartThrob</strong> creates profiles for <strong>your</strong> process, for <strong>your</strong> printer, and lets you create consistently-beautiful digital negatives from <strong>your</strong> pictures &#151; every single time.

<h3>Downloading and Installing <em>ChartThrob</em></h3>

<a href="https://www.botzilla.com/blog/archives/ChartThrob.jsx"><strong>Right-Mouse-Click and Select "Save Link As..." Here for the Current Version of <em>ChartThrob.</em></strong></a>

Typically, "Save As..." this (for Windows - Mac is similar):<br /><tt>C:\Program Files\Adobe\\[Current_Photoshop\]\Presets\Scripts\ChartThrob.jsx</tt><br />where "Current_Photoshop" is any installed version from CS2 to the latest CC 2019.

_That's it!_ The next time you start Photoshop, <em>ChartThrob</em> will appear as an option under Photoshop's "File&#8212;>Scripts" menu.

<em>The very latest ChartThrob and updates are <a href="https://github.com/joker-b/ChartThrob">also available on GitHub.</a></em> The version here on Botzlla should be current with the GitHub master branch. You may also find more info and alternative branches on the git repo, if you are wise in the ways of git..

(Tiny aside: if you update to a new version of Photoshop, you'll need to move the ChartThrob.jsx to your new application)

<h3>Using <em>ChartThrob</em> </h3>

<em>ChartThrob</em> is really two scripts in one: First, it's a script for creating grayscale calibration charts, which you can print using amost any grayscale process. Second, it's a tool for automatically evaluating scanned prints of those charts and setting up appropriate profiles depending on the nature of your printing process.

The <em>ChartThrob</em> workflow for digital negatives has a few basic steps:

  - <strong>Create</strong> a Grayscale chart in <em>ChartThrob.</em>
  - <strong>Print</strong> a digtial negative from that chart (on Pictorico material etc).
  - <strong>Contact-print</strong> that negative onto your medium of choice (platinum, mimeo, silver-gelatine paper, sun prints, etc).
  - <strong>Scan</strong> the resultant positive print.
  - <strong>Crop</strong> the scan back to the original chart boundaries.
  - <strong>Analyze</strong> the chart in <em>ChartThrob</em> &#151; the result will be a new Curves layer containing a Printing Curve, which you can use on the spot or save for repeated use later.
  - <strong>Apply</strong> that curve to any B&W images you like, before printing them to digital negatives. The curve will correct the original image grayscale values to neatly fit to the grayscale range of your chosen medium.

So let's begin!

<h4>Create a Chart</h4>

From any Photoshop session, you can start-up <em>ChartThrob</em> by selecting "File&#8212;>Scripts&#8212;>ChartThrob."

<img alt="ctCreate106.jpg" src="https://www.botzilla.com/blog/pix2006/ctCreate106.jpg" class="align-center"  />

If you have no documents open and call <em>ChartThrob,</em> you should see a dialog box similar to the one above (if you have documents open, the dialog will be more complex, but will still contain this info) (The illustrations in this doc page show both Windows and Mac examples). Pressing <strong>"Help"</strong> will provide you with step-by-step instructions, or pressing <strong>"Build New Chart Now"</strong> will do exactly that &#151; it will create a new document and start filling it with profiling information. Photoshop draws very quickly, but this will typically take several seconds &#151; especially if you have the 'Numbers' option checked. The result will look like the picture below (with or without the numeric labels).

<img alt="ChartThrobTemp.jpg" src="https://www.botzilla.com/blog/pix2006/ChartThrobTemp.jpg" class="align-center"/>

This is a <em>positive</em> chart &#151; that is, you'll either have to invert it when you print it to a negative, or before (depending on your printer). The text at the bottom reads: <strong>"THIS IS A POSITIVE IMAGE WITH DARK TEXT ON WHITE."</strong> Keep that in mind, because <em>ChartThrob</em> creates and analyzes <em>positive</em> images.

<h4>Print (A Fresh Chart)</h4>

You may want to resize the chart when printing, by default it's pretty large, paper-wise. You should be able to resize it according to your own printing habits. Then print to a (typically transparent) negative, and contact-print that negative according to whatever process suits your fancy: silver-gelative, old xerox, woodburytype, cyanotype, whatever, so that once again you have a positive print that looks like the original chart. Be sure that you have a solid, dependable printing process so that you can repeat your results later. The chart print doesn't need to be huge, just big enough to see the individual patches (platinum printers will probably be happy to hear that, considering they pay by the droplet...).

If you have a good grasp of your printing already, try to print so that the midtones are as properly-exposed as you think you can get them. The blacks and pure whites will work themselves out.

Also, be sure that your printing is uniform across the entire size of the chart &#151; if the exposure varies from one side to the other, or from the center of your prints to the edges, there won't be any way for the calibrator to second-guess that. You'll just get junk.

<h4>Scan (Your Print)</h4>

Okay, so now you've made a positive print from the chart. Let it dry, and then scan it, making sure you have a linear (gamma 1.0) scan with the full grayscale range  (see the <a href="#faq">FAQ</a> below on how to do this).

<h4>Crop (Your Scan)</h4>

Back in Photoshop with your scan, crop the scan back to the boundaries of the chart, and you'll have something perhaps like the image here. 

<img alt="ChartThrobScan.jpg" src="https://www.botzilla.com/blog/pix2006/ChartThrobScan.jpg" class="align-center" />

<h4>Analyze (A Scanned, Cropped Chart)</h4>

With this new scanned print loaded, call <em>ChartThrob</em> again. The dialog box will still let you create a new chart if you want one, but now it also contains options for analysing a scanned printed chart.

<img alt="ctScanDialog.gif" src="https://www.botzilla.com/blog/archives/ctScanDialog.gif" class="align-center" />

If we hit <strong>&lt;return&gt;</strong> or press <strong>"Analyze,"</strong> that's exactly what <em>ChartThrob</em> will do: analyze the scanned chart, adjusting for paper tone and process color and evaluating every patch. When done, it will display a brief report telling you everything's okay, and will add a new curves layer to your scanned chart document, titled "Print Curve."

<img alt="ctCurve.gif" src="https://www.botzilla.com/blog/pix2006/ctCurve.gif" class="align-right" align="right" />


If we double-click select the "Print Curve" in the Photoshop Layers palette to view the resultant curve, it would look like the one shown here (we're just showing the curve rather than the whole dialog, to save web-page space).


The new curve layer is _hidden_ in our current document, because the curve isn't meant for adjusting the scan itself &#151; instead, it's to be used for adjusting <em>other</em> B&W images so that they can be printed using the same process that you used to create the scan.

<h4>Apply (to A New Photo)</h4>

When a <em>ChartThrob</em> curve is applied to a B&W image, the image's original gray values will be remapped so that they will print to match the grayscale range of the target printing medium, as long as you're consistent in the print exposure and processing. So if you expose a silver-gelatin contact print for 30 seconds, then as long as you expose and process all subsequent prints the same amount, they should print consistently and the curves will adjust them perfectly to that tonal range.

You can apply the curve to other images either by saving & loading it as a Photoshop .csv file, or just drag the curves layer from the layers palette onto another picture if it's opened in Photoshop.

<img alt="IMG_7240-180x120-trio.jpg" src="https://www.botzilla.com/blog/pix2006/IMG_7240-180x120-trio.jpg" class="align-center" />

With the curve applied, _the image may now look dull and washed out on the monitor,_ but those tones are what's needed to hit the darkest blacks and whitest whites that the particular printing process can handle &#151;  at least the tones that were in the printed chart. If the chart is strongly over or under exposed, <em>ChartThrob</em> will still make a curve, though it will tell you if the midtones seem to be strongly skewed.

Your photo is ready to print. Create your print using the same method you used to make the printed chart, being as precise as you can -- you should now have a full-range print.

<h4><strong>Double-Checking Your Curve (on a Chart)</strong></h4>

If things have gone well, you can take your original chart (as created by <em>ChartThrob</em>), apply that correction curve to it, print again and you should get a full range of grays from the new corrected print.

<!-- SPACER ----------------------------------------- -->

---

<h2><a name="faq">The <em>ChartThrob</em> FAQ</a> </h2>

<dl>
<dt>Will <em>ChartThrob</em> work with 16-bit images? I keep giving it 16-bit scans but  it reduces them to 8-bit.</dt>
  <dd>Yes. You can absolutely apply a printing curve made by <em>ChartThrob</em> to 16-bit  images. Just apply the curve in the usual ways. <em>ChartThrob</em> does all of its calibration work in 8-bit, but unless you have an extremely narrow and contrasty process (say, rubber stamps), that should be plenty of precision for the purpose. Applying the resultant curve to a 16-bit image will still give you a 16-bit image.</dd>

<dt>What about 32-bit  images?</dt>
  <dd>Do you have a 32-bit printer? Call me...</dd>

<dt>Can <em>ChartThrob</em> be ued to calibrate B&W images printed by bookprint services like <a href="http://www.lulu.com/">Lulu</a> and <a href="http://www.blurb.com/">Blurb,</a> or on my local newspaper's press?</dt>
  <dd>If the printer is reasonably consistent from run to run, then absolutely yes.</dd>

<dt>How do I contact you to make a report or tell you my great idea for an enhancement or to send you money?</dt>
  <dd><em>ChartThrob is free.</em> You are, however, welcome to buy my photos. You can contact me here at PhotoRant as either 'kevin' or 'bjorke' at photorant.com.</dd>

<dt>How can I be notified of new versions of <em>ChartThrob?</em></dt>
   <dd>Click "Watch" on <a href="https://github.com/joker-b/ChartThrob" target="blank">the GitHub page.</a></dd>

<dt>Does<em>ChartThrob</em> work with Photoshop CS3, now that it's out?</dt>
   <dd>Yes.</dd>

<dt>I only have Photoshop 5 (or 7, or CS). Will you change <em>ChartThrob</em> to work with my old version of Photoshop?</dt>
   <dd>Nope. <em>ChartThrob</em> uses UI tools that were introduced with CS2, and Photoshop pre-7 didn't have scripting at all.</dd>

<dt>Why doesn't <em>ChartThrob</em> set curve points for <em>all</em> of the patches? It only seems to set about a dozen points on the curve.</dt>
   <dd>This is a limitation of Photoshop, but 14 points (along a parametric curve) seem to be plenty for real-world printing. The full range of patches are there for <em>you</em> to see.</dd>

<dt>What do all those extra check boxes do?</dt>
   <dd>Try them out!</dd>

<dt>Can you make <em>ChartThrob</em> as an Action instead? I don't like having to call scripts from the 'File' menu, I'd rather see it in the actions palette and attach it to a hot key.</dt>
   <dd>Actions can't do everything scripts can do, especially the stuff that <em>ChartThrob</em> does. You <em>can</em> create an Action that will start-up <em>ChartThrob.</em> That's easy, do it the normal way. The Action won't see the stuff you click in the <em>ChartThrob</em> dialogue boxes, though. That seems to be a limitation of the current Photoshop.</dd>

<dt>I resized the chart scan to be really, really small and now I'm getting junky values from <em>ChartThrob</em>.</dt>
   <dd>The program averages-out an area of the scanned chart and samples this average. It does this to compensate for grain and paper texture. If the scan is too small to get a good average, the quality of the curve will suffer. In general, don't let your scanned-chart image get smaller than, say, 600 pixels across.</dd>

<dt>The defaut chart size is 4 inches at 300 dpi. I want 7.3 inches at 1440 dpi. Can you resize it?</dt>
   <dd>You can use Photoshop's 'Image Size' command for now. I'm considering adding more print-size options, though they will make the dialog box more complicated.</dd>

<dt>Should I be setting stuff up using "Relative Colormetric" in the print dialog? What color space should I use?</dt>
   <dd>It doesn't really matter what your print settings are, as long as they are always the same each time you make a printing negative. In general, try to avoid anything in your printing or scanning processes described as "automatic," since such functions may be changing stuff behind your back &#151; and be sure that your scan is in the same color space (particularly w.r.t. gamma) as the B&W images you plan to print.<br />&nbsp;<br />Be sure that your scan covers the full print range from darkest to lightest within the <em>straight-line portion</em> of the scan. Some scanners will "roll-off" the shadows and/or highlights. This sort of compression of the original print values will give <em>ChartThrob</em> a distorted input.<br /><img alt="ChartScan-WrongRight.jpg" src="https://www.botzilla.com/blog/pix2006/ChartScan-WrongRight.jpg" class="align-center" /><br /><em><small class="align-center">You want the <strong>full range</strong> when scanning. These dialogs from EpsonScan&#8482;<br />show that the Automatic exposure of a printed ChartThrob chart<br />distorts the grayscale values. Instead, <strong>manually</strong> set the max and min pointers <br />to beyond the brightest and darkest vales, &amp; <strong>set the gamma to 1.00.</strong><br />Note that the entire grayscale will thus be linear: the "shoulder" &amp; "toe" buttons will be ignored.<br />&nbsp;</small></em></dd>

<dt>I have a fax scanner and the quality is not so great. I'm losing light (or dark) tones in the printed chart! I can see them, but my scanner can't</dt>
<dd>Either get a better scanner, borrow a better scanner, or try creating a "camera scan" &#151; take a glare-free, evenly-lit photo of the printed chart using a good-quality digital camera &#151; this may also be a solution for printing materials where the dark tones are more reflective than the light tones, thus "fooling" the scanner and not scanning well.</dd>

<dt>Why isn't the generated chart a negative, since I'll be printing it as a negative? It hurts my hand to have to press &lt;Ctrl-I&gt; to invert the chart before printing.</dt>
   <dd>Get a better grip on your printing! Some people print directly from a positive image to a negative and let their print driver do the inversion for them. Others need to print from an inverted image. <em>ChartThrob</em> can't know if you are a negative person or a positive person. So it looks on the bright side and assumes that everyone is positive.</dd>

<dt>Why does <em>ChartThrob</em> use the font 'Myriad Pro,' which I don't have? I have to click lots of stupid 'okay' dialog boxes when I generate a new chart.</dt>
   <dd>First: <em>Upgrade your version of (free) ChartThrob and/or (not free but worth it) Photoshop.</em> <em>ChartThrob</em> doesn't actually use "Myriad" &#151; it only uses "Arial." I'm told it's "an Adobe Thing" which was also updated in Photoshop CS3. That was a _long_ time ago! <em>IFF</em> you get those (annoying but harmless) "font not found" messages: Just upgrade to V1.06 or later. <em>Or,</em> if you're insanely determined to use an old version, install 'Myriad' and those dialog boxes will vanish forever.</dd>

<dt>Where can I find out more about <em>ChartThrob,</em> and compare results with other users?</dt>
   <dd>See <a href="http://www.hybridphoto.com/forums/showthread.php?t=36">this discussion thread</a> at HybridPhoto.com. In addition, check out this page by Michael Koch-Schulte, who has done additional work in understanding how to get the most out of the varying color sensitivities of different alt-process materials: <a href="http://www.inkjetnegative.com/images/RNP/quick_guide_to_making_digital_ne.htm"><em>A Quick Guide to Making Digital Negatives with RNP-Arrays and ChartThrob.</em></a> Or just poke it into Google &#151; it's been encouraging to see that <em>ChartThrob</em> users have cropped up all over the net.</dd>

<dt>Sometimes <em>ChartThrob</em> seems to take a long time to run. How do I know that it's working at all?</dt>
   <dd>Leave the 'Histogram,' 'History,' or 'Info' panels open, and you'll see just how fast and furious <em>ChartThrob's</em> drawing and analysis really is. It's edu-taining!</dd>
</dl>
