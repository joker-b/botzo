---
layout: post
title: "Away from the Desk: WD Wireless Pro"
published: false
image:
  path: https://www.botzilla.com/pix2020/bjorke_Putnam_KBXF7797.jpg
  thumbnail: https://www.botzilla.com/pix2020/bjorke_Putnam_KBXF7797.jpg
categories: [GearHead]
tags: [Fujifilm, Digital, Chromebook, Samsung, Linux, Lumix, Leica, Android, iOS, Mac, Windows, Review]
---

Wireless, standalone devices can provide camera archive storage without a laptop. They range from the luxury <a href="https://www.gnarbox.com/">Gnarbox SSD</a> to inexpensive spinning disks like my <a href="https://shop.westerndigital.com/products/portable-drives/wd-my-passport-wireless-pro-hdd#WDBVPL0010BBK-NESN">Western Digital Wireless Pro</a>, which trades speed and weight for price (the Gnarbox also provides "folder presets" to allow custom structured-on-import storage like the system I described <a href="{{ site.baseurl }}{% post_url 2020-04-09-kbImport %}">here</a>).

For my use, this is all good, and the WD can even function as an _ad hoc_ NAS.

<!--more-->

The WD isn't terribly expensive: around $150 for my 2TB spinning disk. An SSD version is available for $800 -- lighter, (maybe) more rugged, and faster -- at a cost. The smaller 1TB Gnarbox 2 is currently about $900.

The WD Pro has a simple backup mechanism: turn it on, put in the SD card, and press the backup button. It sorts imported files into simple folders ordered by time-of-import.

You can also connect most Fuji and other cameras directly to the drive via USB without removing the card from the camera, and copy media in the same way: push the button, wait for the LEDs to indicate you're done. Speed varies a bit depending on the specific camera.

## Accessing Your Pictures

After backing up, the hard drive can be connected to the Chromeboook either wirelessly or via wired connection. In theory, you could use apps like <a href="https://www.botzilla.com/gearhead/2020/04/09/kbImport.html"><b>kbImport</b></a> or **Files** to copy from an SD card connected to your computer to a WD drive also connected to the same computer, but there doesn't seem to be much advantage to that approach unless you want structured folders.

Western Digital's **My Cloud** Android app is one wireless mechanism for bringing files from the drive into ChromeOS. You can get the app for iOS as well. But there is a better way: mounting the drive as a network share. This method works very well for Mac or Windows, right in the finder window, and can also work on phones with a helper app (but for such a case, you may as well use **My Cloud**). Chromebook's **Files** app has built-in "SMB" support to connect the WD, but I've had better results with the helper extension, <a href="https://chrome.google.com/webstore/detail/file-system-for-windows/mfhnnfciefdpolbelmfkpmhhmlkehbdf?hl=en">**File System for Windows.**</a>

<figure class="align-center">
<img alt="Mac Access" src="https://botzilla.com/pix2020/WD-Network-on-Mac.jpg">
<figcaption>Network access from the Mac Finder: mounted as "MyPassport"</figcaption>
</figure>

You can connect any device directly to the WD's own wifi server, `http://192.168.60.1` -- but that can be fiddly. It's simpler to connect to the WD this way just _once,_ and use the controls found in the "admin" panel there to connect it back to your main network. You can then reconnect your computer back to the main network and access the WD either by name ("MyPassport") or local IP address (for my network, `192.168.1.32` is today's dynamic address. You can also set a static address: <a href="https://media.flixcar.com/f360cdn/Western_Digital-2411667979-eng_user_manual_4779-705151.pdf">here's the manual</a>). 

<figure class="align-center">
<img alt="WD Wireless Pro" src="https://botzilla.com/pix2020/WD-wifi.jpg">
<figcaption>Accessing the **WD Wireless Pro** via web browser when the drive is connected as a wifi server, and linking it to a home Wifi router</figcaption>
</figure>

The WD has a range of connection features that go well beyond the scope of this article: you can use it as a Plex media server for your TV or stereo. It can charge your phone. You can log-in via `ssh` and tweak it as a tiny linux machine. Suffice to say that it's a powerful, complex device -- that complexity (not helped much by the obscure tech-jargon in the manual) might be enough to encourge you to drop the extra $750 for a half-sized Gnarbox. Or not, if the WD handles what you need?

<figure class="align-center">
<img alt="Files Access" src="https://botzilla.com/pix2020/files_extensions.jpg" width="484" height="368">
<figcaption>Network access from Chromebook <b>Files</b> using an IP address<br/>(Dropbox can be accessed by a similar extension, btw)</figcaption>
</figure>

