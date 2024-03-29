---
layout: post
title: "Fuji/Chrome 2020: Storage"
image:
  path: https://www.botzilla.com/pix2020/P1090143-p20.JPG
  thumbnail: https://www.botzilla.com/pix2020/P1090143-p20.JPG
categories: [GearHead]
tags: [Fujifilm, Software, _Phase4]
---

It's been almost three years since the <a href="{{ site.baseurl }}{% post_url 2017-07-19-The-New-Fuji-Chrome-Fujifilm-X-and-Chromebook %}">previous post on using a Chromebook with Fujifilm cameras.</a> How are things today, in 2020, after several newly-released cameras, OS editions, and improved Chromebooks? What about... iPad? Have other camera brands started to catch up?

In this other posts I'll be looking at the current options and will describe how I'm integrating ChromeOS into my photography (and general) workflows.

This small series was triggered by the recent addition of the <a href="https://www.samsung.com/us/computing/chromebooks/galaxy-chromebook/">Samsung Galaxy Chromebook</a> to my working kit. Like Samsung's other premiere Chromebooks, it arrives with a touchscreen, pressure-sensitive integrated pen, micro-SD reader (now supporting the high-speed UHS protocol), and support for Android apps. On the Galaxy, you get a solid aluminum frame that's  _lighter_ than the Macbook Air, a 4K OLED display, and at last Samsung has shipped a top-tier Intel-powered (<a href="https://ark.intel.com/content/www/us/en/ark/products/195436/intel-core-i5-10210u-processor-6m-cache-up-to-4-20-ghz.html">i5-10210U</a>) Chromebook with offical support for Linux.

Basically: the machine I've been waiting for since 2017. Did I mention it's orange?

In this 2020 post, we'll look at moving photos from camera or SD cards to Chromebook, or to somewhere nearby.

<!--more-->

> ## Executive Summary
> 
> The addition of robust Linux is a big step up for ChromeOS workflows, as are other recent additions such as improved **Files** app, Android applications from vendors like Adobe, and the advent of wireless self-archiving drives and SSD's. Due to overlapping security concerns between _The Three Storage Domains_ -- Chrome, Android, and Linux apps -- the storage methods are not always obvious, and depend on your needs. Some Android import applications, particularly **Lightroom,** are still lagging behind their Mac, Windows, and iOS siblings, but good inexpensive alternatives exist.

We'll compare a few different archiving methods:

* **Google Drive** backup 
* Just copy the camera DCIM folder via **Files** 
* Wireless drive (e.g., Western Digital Wireless Pro), Gnarbox, etc
* Linux command-line apps like <a href="{{ site.baseurl }}{% post_url 2020-04-09-kbImport %}">**kbImport**</a>
* **Adobe Lightroom** import
* **Fujifilm Camera Remote**

## Starting with the Worst Case: Direct Backup to Google Drive Cloud

Before we can edit photos on computer we need to get them there. Let's begin by paging the camera calendar back to 2012, and transfer the first batch of test photos not from a modern Fuji but an aging yet still-functional Lumix LX7 (<a href="https://blog.mingthein.com/2013/03/25/leica-d-lux-6-panasonic-lx7/">aka Leica DLux-6,</a> for all practical purposes), shot using its cornea-blistering <a href="https://www.dpreview.com/reviews/panasonic-lumix-dmc-lx7/5">"Impressive Art Mode"</a> and with RAW backup files. Our first test will look at 614MB of mixed jpeg and raw files, stashed on a vintage SDHC Class-4 card.

When you add such a drive to the Chromebook (or rather, to a USB-C hub: I used a Letscom USBC02), Google's **Files** app will open, and offer to backup your pictures to **Google Drive.** I habitually ignore this offer, but for the sake of this article, I wondered: "how slow can it be?"

The answer: _very, **very** slow._

Backing up those 108 files to **Google Drive** burned nearly _two hours:_ 116 minutes.

The test files appeared in a **Google Drive** folder named `My Drive/Chrome OS Cloud backup/2020-04-10` -- **Google Drive's** web page showed thumbnails for all of the images, though it had some hidden issue related to the raw (`.RW2`) files in web preview. They _do_ open but the web page also announces some unseen error. If you're just using Google Cloud as a transfer/backup mechanism to share with other computers, this might not be a big deal: the files are fine, it's just the webpage being wonky.

In the Chromebook **Files** app, the raw files appear normally, except that they're mysteriously listed as TIFFs. **Files** lets you define default applications for each file type, so I set the `.RW2` default to <a href="https://rawtherapee.com/">**RawTherapee,**</a> a very capable Linux-based RAW processor.

<figure class="align-center">
<img alt="RawTherapee" src="https://botzilla.com/pix2020/RawTherapee-Sample1.jpg">
<figcaption><b>RawTherapee</b> in action, editing a slightly-less-eye-burning edition of the photo from the top of this article (result at the article's end). The results can either be saved directly, or passed on (via the little gear icon at the bottom) to another app for further processing. In this case, that extra app was <b>GIMP.</b></figcaption>
</figure>

It's evident that the Chrome team have been improving the filesystem connections between "the three domains" in ChromeOS: (1) the standard ChromeOS file system (which includes both local storage and **Google Drive**), (2) the storage available for Android apps, and (3) the storage available for Linux. When opening an image via **Files** you often don't need to care too much about domain boundaries, especially from cloud file sources. The context menu for a cloud-based `.RW2` file on my system shows that you can "Open with..." a half-dozen different applications, some of which are linux-based even though the source drive is _not_ tagged "Share with Linux." **Files** manages the cross-domain transport for you as it pulls the data from the cloud.

<figure class="align-center">
<img alt="Files App" src="https://botzilla.com/pix2020/Files-Context1.jpg">
<figcaption>ChromeOS's <b>Files</b> app showing JPG and RW2 images saved on **Google Drive**, and contextual menu choices for <tt>RW2</tt> files.</figcaption>
</figure>

This type mapping doesn't _always_ work for local files -- `.RW2` files on the local SSD were recognized not as TIFF but as "RW2 Image" and I'd have to open them from **RawTherapee** in a more-manual manner (see "File Shuffling" at the end of this article).

Android app access from **Files** is slightly hidden under "More actions" in the context menu, and offers tools like Snapseed, Adobe Lightroom, or even a direct posting to Instagram, straight from the file browser.

Which is all great, despite Google-Drive-backup's very slow initial transfer speed.

So let's look at our options for local storage, which are typically 100 times faster.

## Local Storage

My preferred approach for photo storage is to work from an external SSD -- today's tests will use a 1TB SanDisk "Extreme Portable SSD" SDSSDE6-1TOO. In testing I found that copying from an external SD card to either Chromebook internal storage or this external SSD took about the same time. The Chromebook's internal SSD is 256GB, and you can augment it with the integrated micro-SD card slot. That slot supports the Samsung UFS high-speed format, if you can find such a still-rare new-style card. Testing against a current 256GB EVO card resulted in transfer times pretty similar to the internal or external SSDs.

If you just want to move camera files quickly, the fastest way is to just drag the folders in the **Files** app. Slow on Linux, but quick locally. Using Linux-native apps will be slower due to file-translation overhead. That's true for structured-copy apps like <a href="{{ site.baseurl }}{% post_url 2020-04-09-kbImport %}">**kbImport**</a> or even just `cp -r` from the command line.

This is different from a machine like the Mac, where command-line copying is faster -- much faster -- than using the Finder GUI.

#### Comparing Performance: SD card to SSD (or internal)

* **Files** direct copy: about 40 seconds
* **kbImport** copy, rename, and filing: 65 seconds
* **WD Wireless Pro** spinning-hard drive SD backup: 75 seconds

Comparing to my Macs and a Windows 10 desktop, Chromebook is... slower. The champion thus far is to use my old Macbook Air from 2013, which has a built-in SD slot. Newer Macs, including my 2018 Macbook Pro, are slower with an adapter, as the Windows machine. Within Linux, `cp -r` is faster than **kbImport** -- this seems to be an issue with the current edition of python for Chromebook's linux. I log occasonal tests <a href="https://github.com/joker-b/kbImport/blob/master/README.md">here.</a> In general, `cp -r` is 6-8x faster than **kbImport** on Chrombook, but **kbImport** is 5x faster than _that,_ on Mac. Windows is in between, and again lower if you use a linux container for Windows 10. The oddly-slowest results come from the Mac too, though, when dragging folders in the Finder.

#### Western Digital Wireless Pro

Wireless, standalone devices can provide storage without the computer being turned on. They range from the luxury <a href="https://www.gnarbox.com/">Gnarbox SSD</a> to inexpensive spinning disks like the Western Digital Wireless Pro.

The general usage for all such drives: plug in the card, press "backup," and let it work. Later, access the drive either wirelessly or with a cord.

#### Lightroom

There are multiple methods for bringing photos into **Lightroom** on Chromeboook: you can use LR's own "Add" operation, or alternatively select the images in **Files** and share as "Add to Lightroom." Neither is especially quick, and when sending lots of images to LR from **Files** it can be hard to know what's going on -- you'll see nothing happening for many seconds, then a popup saying how many images have been sent or that failed to send, without much more detail than that. Once they're sent, you're all set for standard Android **Lightroom** operations.

Moving the sample photo set from the local drive (already transfered from SD) took about... two minutes? With poor reporting of status, it's hard to say exactly.

After a while, **Lightroom Mobile** also presented a popup asking if I'd like to move its storage to the microSD card. Nice touch, and only added a one-shot process that completed in only a couople of minutes, _except_... it lost all image previews -- they all turned black. Restoring them might have been a simple process: editing any photo, however lightly, would restore the preview image, _but_ Android **Lightroom**'s lack of batch editing (unlike other LR editions) means that every single photo in the catalog needed to be opened by hand and edited or reverted to refresh the preview. _Every. Single. Photo._

<figure class="align-center">
<img alt="Lightroom Mobile" src="https://botzilla.com/pix2020/Lightroom-edit.jpg">
<figcaption><b>Lightroom Mobile</b> Android Edition</figcaption>
</figure>

The lack of batch editing in Android is a bit of a mystery -- it's generally a strength of **Lightroom,** and available in the iOS version. More mysterious still, the help menu aims the user (or, attempted user) to doc web pages and tutorials... for the iOS edition.

#### What about DarkTable, or Digikam?

The linux app <a href="http://darktable.org">**DarkTable**</a> is similar to "real" **Lightroom** but doesn't try to copy files as you add them to **DarkTable's** catalog(s) -- so it needs you to transfer the files (if an expert has a counter-example, please share!). **DarkTable** also works on Mac or Windows.

**DigiKam** is a file-management app for photographers but thus far it hasn't worked for me on Chromebook linux -- after installation it emitted tons of errors about missing GTK methods (which oddly, are probably also used by other apps that _do_ work, like **VS Code** or **Sublime Text** or... **DarkTable**). If I do manage to get it into a useful state, I'll add a note here.

#### Fujifilm Camera Remote

As we've seen, most photo-import strategies for Chromebook can apply to SD card data from any camera. **Fujifilm Camera Remote** is an Android application for transfering photos wirelessly specifically from Fuji cameras to phone or Chrome. **Camera Remote** also provides tether-like remote camera control while shooting, complete with a live view and (if autofocus is active) touch-to-focus control.

While the app is invaluable for transfers and camera control on a phone, it's a bit less useful on Chromebook, mostly because it transfers _only_ jpeg files -- never the `.RAF` RAW file, nor `.MP4` video data. This is great for everyday phone usage, but less-so for permanent archiving, where you typically have access to the SD card itself, which you can access without needing to disconnect the laptop from Wifi so that it can be connected to the camera's transmitter (newer Fuji's -- my newest is X100F -- also have bluetooth to avoid this last issue).

Those caveats aside, it works well.

For laptop use, you may want to turn resizing off. This is a _camera_ setting, not on the app! To alter it on the X-Pro2, when in playback mode, press the `Menu` button and then navigate to the `wrench` icon, then `CONNECTION SETTING`, then `WIRELESS SETTINGS`, and `RESIZE IMAGE FOR SMARTPHONE [3M]` -- turn it OFF to keep the transfered images their original sizes. Other cameras will have similar menu options.

If your goal is to send your photo out on the web, the smaller **3M** size will usually be okay. The savings in file size (and thus time spent transfering) can be significant. Consider the stay-at-home X-Pro2 photo below: the full-size "normal" jpg is 9.9MB, while the resized **3M** version is less than 979KB. Roughly a 10x difference! 

<figure class="align-center">
<img alt="Fujifilm Camera Remote" src="https://botzilla.com/pix2020/bjorke_remote_acros_lg.jpg">
<figcaption>X-Pro2 image transfered via **Fujifilm Camera Remote.**</figcaption>
</figure>

#### File Shuffling

ChromeOS, Android, and Linux all have different expectations about privacy. Linux users tend to want access to _everything,_ while the makers of ChromeOS and Android apps prefer a lot of security fencing, so that no app can access another's data except through controlled APIs -- _if_ both apps allow the transaction.

This has led to the ChromeOS file-storage model I call _The Three Domains:_ every folder and file has a default location within these domains. **Files** has access to all of them. A few special locations within **Files** are allowed to overlap domains easily (**Google Drive** for instance, or the internal SD card). Others may occasionally need to have files explicitly shared or copied between locations -- the most common cases for this are when you want to move pictures from an Android app like **Snapseed** to linux. Without considerabe gymnastics, you're better-off just copying it to a Linux-accesible location, like your home directory or SD card.

(To professional Android developers: yes, you can also put an Android phone into Developer mode and then log-into it via <a href="https://developer.android.com/studio/command-line/adb">`adb shell`</a> to get a linux prompt inside the phone. Let's just not go there for this article, okay?)

##### Android apps and the Micro-SD card

Some Android (err, "Google Play") apps can write their data to the internal micro-SD slot. That drive can also be marked "Share with Linux" in the **Files** app, so the SD makes a handy place for interchange between Android and Linux. I've set up both **Lightroom** and **Fujifilm Camera Remote** this way.

**Advanced Users:**

Android has its own way to manage disk space, but it's not especially difficult to navigate from Linux. You can even set up symbolic links to locations on the SD card, and **Files** will happily follow them for quicker browsing.

To find those files in the bash shell:

```
SD=/mnt/chromeos/removable/evo256 # your SD card may have a different name than "evo256"
#
echo Fujifilm Camera Remote files on SD card:
ls ${SD}/Android/data/com.fujifilm_dsc.app.remoteshooter/files/fujifilm/Camera\ Remote\(SD\)/
#
echo Lightroom Mobile Files on SD card: camera data and shared proxies
echo All files from all days:
ls ${SD}/Android/data/com.adobe.lrmobile/files/carouselDocuments/*/Originals/*/*/*/
```

Lightroom catalogs follow a structured-storage approach not unlike the one used by **kbImport**: `year/month/day/files....`

Here's a sample, assuming that you have files for 10 April 2020, and using some more bash variables for readability:

```
LR_ID=`/bin/ls ${SD}/Android/data/com.adobe.lrmobile/files/carouselDocuments`
echo Every machine/user/catalog may have a different ID, in this case: ${LR_ID}
LR_PIX=${SD}/Android/data/com.adobe.lrmobile/files/carouselDocuments/${LR_ID}/Originals
LR_YEAR=2020
LR_MONTH=${LR_YEAR}-04
LR_DAY=${LR_MONTH}-10
echo For the day ${LR_DAY}:
ls ${LR_PIX}/${LR_YEAR}/${LR_MONTH}/${LR_DAY}/
```

#### Next Up: Photo Editing on Chromebook, Printing, and Publishing

The next parts of this series will cover some explorations relating to different image-editing tools available for Chromebook, followed by some ideas about printing and export to the web or services like WeChat and Instagram. Thanks for getting this far!

<figure class="align-center">
<img alt="Header from RAW" src="https://botzilla.com/pix2020/P1090143r.jpg">
<figcaption>Edited by <b>RawTherapee</b> and <b>GIMP</b>, a less-painful edition of the top photo.</figcaption>
</figure>

