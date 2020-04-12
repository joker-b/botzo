---
layout: post
title: "Fuji/Chrome 2020: Storage"
image:
  path: http://www.botzilla.com/pix2020/P1090143-p20.JPG
  thumbnail: http://www.botzilla.com/pix2020/P1090143-p20.JPG
categories: [GearHead]
tags: [Books,Fujifilm,Digital,Chromebook,Samsung,Linux,Lumix,Leica,iOS]
---

It's been almost three years since the <a href="{{ site.baseurl }}{% post_url 2017-07-19-The-New-Fuji-Chrome-Fujifilm-X-and-Chromebook %}">previous post on using a Chromebook with Fujifilm cameras.</a> How are things today, in 2020, after several newly-released cameras, OS editions, and improved Chromebooks? What about... iPad? In this and following posts I'll be looking at the current options and will describe how I'm integrating ChromeOS into my photography (and general) workflows.

This small series was triggered by the recent addition of the <a href="https://www.samsung.com/us/computing/chromebooks/galaxy-chromebook/">Samsung Galaxy Chromebook</a> to my working kit. Like Samsung's other premiere Chromebooks, it arrives with a touchscreen, pressure-sensitive integrated pen, micro-SD reader (now supporting the high-speed UHS protocol), and support for Android apps. For the Galaxy, you get a solid aluminum frame that's  _lighter_ than the Macbook Air, 4K OLED display, and finally Samsung has shipped a top-tier Chromebook that sports an Intel processor (<a href="https://ark.intel.com/content/www/us/en/ark/products/195436/intel-core-i5-10210u-processor-6m-cache-up-to-4-20-ghz.html">i5-10210U</a>) with support for both Android apps _and_ native Linux.

Basically: the machine I've been waiting for since 2017. Did I mention it's orange?


In this first 2020 post, we'll look at moving photos from SD cards to Chromebook, or to somewhere nearby.

<!--more-->

> ## Executive Summary
> 
> The addition of robust Linux is a big step up for ChromeOS workflows, as are other recent additions such as improved **Files** app, Android applications from vendors like Adobe, and the advent of wireless self-archiving drives and SSD's. Due to overlapping security concerns between _The Three Domains_ -- Chrome, Android, and Linux -- the storage methods are not always obvious, and depend on your needs. Some Android import applications, particularly **Lightroom,** are still lagging behind their Mac, Windows, and iOS siblings.

## Starting with a Worst Case: Direct Backup to Cloud

Before we can edit photos on computer we need to get them there. Let's begin by stepping back to the days before Cameras with Wifi, and transfer the first batch of test photos not from a modern Fuji but an aging yet still-functional PanaLeica Lumix LX7 (aka Leica DLux-6, for all practical purposes), set in its cornea-blistering <a href="https://www.dpreview.com/reviews/panasonic-lumix-dmc-lx7/5">"Impressive Art Mode"</a> (but with RAW backup files). Our first test will look at 614MB of mixed jpeg and raw files, stashed on a vintage SDHC Class-4 card mounted to a Letscom USBC02 USB-C hub.

When you add such a drive to the Chromebook, Google's **Files** app will open, and offer to backup your SD files to Google Drive. I habitually ignore this offer, but for the sake of this article, I wondered: "how slow can it be?"

The answer: _very, very slow._

Backing up those 108 files to Google Drive burned nearly _two hours:_ 116 minutes.

The test files appeared in a Google Drive folder named `My Drive/Chrome OS Cloud backup/2020-04-10` -- Google Drive's web page showed thumbnails for all of the images, though it had some hidden issue related to the raw (`.RW2`) files in web preview. They _do_ open but the web page also announces some unseen error. If you're just using Google Cloud as a transfer/backup mechanism to share with other computers, this might not be a big deal.

In the Chromebook **Files** app, the raw files appear normally, except that they're mysteriously listed as TIFF files. **Files** lets you define default applications for each file type, so I set the `.RW2` default to <a href="https://rawtherapee.com/">**RawTherapee,**</a> a very capable Linux-based RAW processor.

<figure class="align-center">
<img alt="RawTherapee" src="http://botzilla.com/pix2020/RawTherapee-Sample1.jpg">
<figcaption><b>RawTherapee</b> in action, editing a slightly-less-eye-burning edition of the photo from the top of this article (result at the article's end). The results can either be saved directly, or passed on (via the little gear icon at the bottom) to another app for further processing. In this case, that extra app was <b>GIMP.</b></figcaption>
</figure>

It's very evident that the Chrome team have been improving the filesystem connections between "the three domains" in ChromeOS -- the standard ChromeOS file system (which includes both local storage and Google Drive), the storage available for Android apps, and the storage available for Linux. When opening an image via **Files** you often don't need to care too much about domain boundaries. The context menu for a `.RW2` file on my system shows that you can "Open with..." a half-dozen different applications, some of which are linux-based even though the source drive is _not_ tagged "Share with Linux." **Files** manages the cross-domain transport for you as it pulls the daata from the cloud.

<figure class="align-center">
<img alt="Files App" src="http://botzilla.com/pix2020/Files-Context1.jpg">
<figcaption>ChromeOS's <b>Files</b> app showing JPG and RW2 images saved on Google Drive, and contextual menu choices for <tt>RW2</tt> files.</figcaption>
</figure>

This type mapping doesn't _always_ work for local files -- for my local drive, `.RW2` files were recognized not as TIFF but as "RW2 Image" and I'd have to open them from **RawTherapee** in a more-manual manner (see "File Shuffling" at the end of this article).

Android app access from **Files** is slightly hidden under "More actions" in the context menu, and offers tools like Snapseed, Adobe Lightroom, or even a direct posting to Instagram, straight from the file browser.

Which is all great, despite Google-Drive-backup's very slow start.

So let's look at our options for local storage, which are typically 100 times faster.

## Local Storage

As before, my preferred case is to work from an external SSD -- today's tests will use a 1TB SanDisk "Extreme Portable SSD" SDSSDE6-1TOO. In some simple preliminary testing to compare the speed of this SSD to that of the internal storage, copying from an external SD card to either internal or external SSD took about the same time. The Chromebook's internal SSD is 256GB, and you can augment it with the integrated micro-SD card slot. That slot supports the new Samsung UFS high-speed format, if you can find such a card. Testing against a current 256GB EVO card resulted in transfer times pretty similar to the internal or external SSDs.

### Structured or Unstructured Storage

Ask ten photographers aboout their filing systems, and you'll probably get a dozen different answeres, even if three of those photographers report "I don't have one."

Some automated backup systems decide for you: as described above Google Drive sorts by date, ignoring the structure of the original camera's `DCIM` folder and subfolders -- in our test case, a single `DCIM/PANA_109/` to contain all the test shots of the day.

(SD-card layout can get even more complicated for video, especially on older cameras that use the complex `AVCHD` standard)

In this article we'll mention just a few:

* DCIM direct copy: just copy for DCIM folders via **Files**
* Google Drive backup (already described, again via **Files**)
* Western Digital automated backup
* Adobe Lightroom import
* My own custom format

#### My Custom Format

This isn't a sales pitch: I have a personal, idiosyncratic format that I've used for a long time, across many different cameras and computers, varying media types, even for film storage. In fact it started wilth labels on individual bulk-loaded film rolls.

In my library, primary hard drives are rotated every year or two, and duplicated separately so that if one is accidentally lost there's a better chance for backup survival. Within each drive, there are three folders for photos, video, and audio, and those are further arranged by data and "job name." Individual pictures also get relabelled for ownership and job name. Here's a saved image path from the current test:

`Pix/2020/2020-04-Apr/2020_04_10_LX7/bjorke_LX7_P1090129.RW2`

where "LX7" is the job name and `bjorke` is the owner. The dates and job names are redundant so that if images are shared there's a chance that the path back to the original file can be found.

In the camera original, it was in `DCIM/PANA_109/P1090129.RW2`

This complicated shuffling would be hard to manage by hand, so I wrote a <a href="https://github.com/joker-b/kbImport">python script called **kbImport**</a> that manages imports and relabeling in a single go, on a variety of computers: Linux, Mac, or Windows.

Not everyone needs structured copying, and it's easy to just let a tool do it (before writing my own tool, I often used Adobe Bridge for this, too). Structured copying is usually slightly slower than simple copying, but it can save time later.

#### Comparing Performance: SD card to SSD (or internal)

* **kbImport** copy, rename, and filing: 65 seconds
* **Files** direct copy: about 40 seconds

#### Western Digital Wireless Pro

Wireless, standalone devices can provide storage without the computer being turned on. They range from the luxury <a href="https://www.gnarbox.com/">Gnarbox SSD</a> to inexpensive spinning disks like my <a href="https://shop.westerndigital.com/products/portable-drives/wd-my-passport-wireless-pro-hdd#WDBVPL0010BBK-NESN">Western Digital Wireless Pro</a>, which trades speed and weight for price (the Gnarbox also provides "folder presets" to allow custom structured-in-import storage like the system I described above).

The WD Pro has a simple backup mechanism: turn it on, put in the SD card, and press the backup button. Like Google Drive, it sorts imports into simple folders ordered by time-of-import.

* *WD Wireless Pro* hard drive SD backup: 75 seconds

After backing up, the hard drive can be connected to the Chromeboook either wirelessly or via wired connection. In theory, you could use apps like **kbImport** or **Files** to copy from SD to a connected WD drive, but there doesn't seem to be any advantage to that approach unless you want structured folders.

Western Digital's **My Cloud** Android app is one wireless mechanism for bringing files from the drive into ChromeOS. It requires disconnecting from the internet to use it, and for a device like a Chromebook with working USB ports, it feels like more trouble than it would usually be worth. A better solution for some tasks, which is a bit buried in WD's lengthy manual, is to use your Chrome browser, rather than the app, and aim it at `http://192.168.60.1` while your Chromeboook's wifi is attached to the drive. You can then set up a connection between the drive and your home wifi, and access the drive as a netowrk device via your usual network:

<figure class="align-center">
<img alt="WD Wireless Pro" src="http://botzilla.com/pix2020/WD-wifi.jpg">
<figcaption>Accessing the **WD Wireless Pro** via web browser when the drive is connected as a wifi server, and linking it to a home Wifi rouuter</figcaption>
</figure>

the WD has a range of connection features that go well beyond the scope of this already-long article, you can easily use it as a wireless NAS or a media server, too. Suffice to say that it's a powerful device, but fiddly to set up -- that complexity (not helped much by the obscure tech-jargon in the manual) might be enough to encourge you to drop the extra $850 for a Gnarbox.

#### Lightroom

There are multiple methods for bringing photos into **Lightroom** on Chromeboook: you can use LR's own "Add" operation, or alternatively select the images in **Files** and share as "Add to Lightroom." Neither is especially quick, and when sending lots of images to LR from **Files** it can be hard to know what's going on -- you'll see nothing happening for many seconds, then a popup saying how many images have been sent or that failed to send, without much more detail than that. Once they're sent, you're all set for standard Android **Lightroom** operations.

Moving the sample photo set from the local drive (already transfered from SD) took about... two minutes? With poor reporting of status, it's hard to say exactly.

After a while, **Lightroom Mobile** also presented a popup asking if I'd like to move its storage to the microSD card. Nice touch, and only added a one-shot process that completed in only a couople of minutes, _except_... it lost all image previews -- they all turned black. Restoring them might have been a simple process: editing any photo, however lightly, would restore the preview image, _but_ Android **Lightroom**'s lack of batch editing (unlike other LR editions) means that every single photo in the catalog needed to be opened by hand and edited or reverted to refresh the preview. _Every. Single. Photo._

<figure class="align-center">
<img alt="Lightroom Mobile" src="http://botzilla.com/pix2020/Lightroom-edit.jpg">
<figcaption><b>Lightroom Mobile</b> Android Edition</figcaption>
</figure>

The lack of batch editing in Android is a bit of a mystery -- it's generally a strength of **Lightroom,** and available in the iOS version. More mysterious still, the help menu aims the user (or, attempted user) to doc web pages and tutorials... for the iOS edition.

#### Fujifilm Camera Remote

As we've seen, most photo-import strategies for Chromebook can apply to SD card data from any camera. **Fujifilm Camera Remote** is an Android application for transfering photos wirelessly from the camera to phone or Chrome. **Camera Remote** also provides remote camera control while shooting.

While the app is invaluable for transfers and camera control on a phone, it's a bit less useful on Chromebook, mostly because it transfers _only_ jpeg files -- never the `.RAF` RAW file, nor `.MP4` video data. This is great for most phone usage, but less-so for a laptop, where you typically have access to the SD card itself, which you can access without needing to disconnect the laptop from Wifi.

Those caveats aside, it works well.

For laptop use, you may want to turn resizing off. This is a _camera_ setting, not on the app! For example, on the X-Pro2, when in playback mode, press the `Menu` button and then navigate to the `wrench` icon, then `CONNECTION SETTING`, then `WIRELESS SETTINGS`, and `RESIZE IMAGE FOR SMARTPHONE [3M]` -- turn it OFF to keep the transfered images their original sizes.

If your goal is to send your photo out on the web, **3M** might be okay. The savings in file size (and thus time spent transfering) can be significant. Consider the X-Pro2 photo below: the full-size "normal" jpg is 9.9MB, while the resized **3M** version is less than 979KB. Roughly a 10x difference! 

<figure class="align-center">
<img alt="Fujifilm Camera Remote" src="http://botzilla.com/pix2020/bjorke_remote_acros_lg.jpg">
<figcaption>X-Pro2 image transfered via **Fujifilm Camera Remote.**</figcaption>
</figure>

#### File Shuffling

ChromeOS, Android, and Linux all have different expectations about privacy. Linux users tend to want access to _everything,_ while ChromeOS and Android app-makers prefer a lot of control and privacy considerations, which don't entirely align between those two systems.

This has led to the model I call _The Three Domains:_ every folder and file has a default location within these domains. A few special locations within **Files** are allowed to cross domains easily (Google Drive for instance, or the internal SD card). Others may occasionally need to have files explicitly shared or copied via **Files** -- the most common cases for this are when you want to move pictures from an Android app like **Snapseed** to linux. Without considerabe gymnastics, you're better-off just copying it to a Linux-accesible location, like your home directory or SD card.

(To professional Android developers: yes, you can also put an Android phone into Developer mode and then log-into it via <a href="https://developer.android.com/studio/command-line/adb">`adb shell`</a> to get a linux prompt inside the phone. Let's just not go there for this article, okay?)

##### Android apps and the Micro-SD card

Some Android (err, "Google Play") apps can write their data to the internal micro-SD slot. That drive can also be marked "Share with Linux" in the **Files** app, so the SD makes a handy place for interchange between Android and Linux. I've set up both **Lightroom** and **Fujifilm Camera Remote** this way.

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

The next article in this series will cover some explorations relating to different image-editing tools available for Chromebook, followed by some ideas about printing and export to the web or services like WeChat and Instagram. Thanks for getting this far!

<figure class="align-center">
<img alt="Header from RAW" src="http://botzilla.com/pix2020/P1090143r.jpg">
<figcaption>Edited by <b>RawTherapee</b> and <b>GIMP</b>, a less-painful edition of the top photo.</figcaption>
</figure>

