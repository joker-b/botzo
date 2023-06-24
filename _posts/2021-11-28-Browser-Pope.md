---
layout: post
title: "The Browser and the Pope"
image:
  path: https://www.botzilla.com/pix2021/westphalia-labberton-1884.jpg
  thumbnail: https://www.botzilla.com/pix2021/westphalia-labberton-1884.jpg
categories: [Hacking]
tags: [Machine Learning, 3D, Games, Digital, Math, History, Media, TechBiz, NVIDIA, Featured]
---

The excitement of 2021 about "the metaverse" hinges on hardware, but probably not in the way you think.

The metaverse's enabling device is not a perfect future headset or muscular neuron sensing or brain-machine interface. No memex is required. Instead, as an explanation I'd like to offer some very noisy graphs and a map of 1648 Europe to spell out what's really going on.

<figure class="align-center">
<img alt="Noise obscures the signal" src="https://www.botzilla.com/pix2021/compute-rg20-Noisy.png">
<figcaption>The Signal: It's in There</figcaption>
</figure>

_There's no such thing as <a href="https://en.wikipedia.org/wiki/Psychohistory_(fictional)">psychohistory</a>,_ but there are some useful models. Sometimes models overlap: the above graph overlaps the story of the 30 Years' War...

<!--more-->

<hr/>

First, let's consider that noisy graph. Hidden underneath the noise, it's three "simple" curves describing the computation that's available for different kinds of tasks, and how that compute availability changes over generations of hardware. Precise values of _how fast_ and _by how much_ are speculations, but stick with me here, the core idea remains the same regardless of scaling.

If we remove the noise, the split between different kinds of computation environment becomes clearer.

<figure class="align-center">
<img alt="Unobscured the signal" src="https://www.botzilla.com/pix2021/compute-rg20-Smooth.png">
<figcaption>Noiseless: Though We Know that the World's a Noisy Place</figcaption>
</figure>

The smooth center of those graphs represents the _core computational capacity_ of the available hardware over calendar time: over months, over years. The essential message of Moore's Law is that chip capacity grows more or less exponentially. That exponent is driven by the nature of the geometry of the chips, the materials used, and the tasks they're assigned to calculate. The noise portion of the graph (a mix of absolute fixed-value and relative-value noises) represents varying individual applications (is Excel faster than Visicalc?), regulations, clever coders, etc. When variation between platform capabilities are small, these noisy factors dominate.

There are many kinds of computer but for clarity I've split this idea into three curves, where the capacities of a single local computer are outpacing the capacities of a browser running Javascript on that same computer, and above them the power of parallel, throughput-focused datacenter-based HPC (High Performance Computing), which outpaces everything else. While the specific exponents of growth might historically vary, the basic orderings of these relationships aren't controversial.

Despite all the best attempts at adding WASM, WebWorkers, WebGPU, and other tools, the browser simply can't keep up with its own local hardware while remaining general enough to be considered a browser. It wasn't designed for that -- which is one reason why most of the bigger advances in web technology over the past decade or so have been about _developer_ productivity using tools like React, not about improving browser compute ability (we'll get back to that).

If we extend the time scale, the absolute noise mostly vanishes and the three signals start to show their differences clearly.

<figure class="align-center">
<img alt="Unobscured the signal" src="https://www.botzilla.com/pix2021/compute-rg100-Noisy.png">
<figcaption>Regardless of Specific Exponents and Noise Scales, You'll Get a Graph Like This Eventually</figcaption>
</figure>

Over time, the _relative_ noise -- that is, variation based on compute capability itself -- for that top track eventually becomes larger than the _entire_ range of the lower curves.

The left side of this longer chart is important -- compared to the later growth, it's nearly flat. The variation in capabilities, and the noise, barely register. The first graph was a close-up of those early years, where the noise dominates. Later on, it's a completely different story. A big and contentious question: how far along are we now, where on this graph is _today?_

These relations do have limits, and sometimes noisy variations can even point _down_ -- the introduction of larger 4K and 8K monitors slowed down web browsers, for instance. Restrictions like Amdahl's Law, the limits of fabbing, network latencies, consumption of compute and network bandwidth by freeloading advertisers, supply chain issues, political constraints on shipping -- they have impacts, but over time each of them fade. 

## _But what does this have to do with the Thirty Years' War?_

Quick history recap: The Thirty Years' War essentially shredded the internals of the Holy Roman Empire. Some parts of the Empire saw as many as 50% of the local population dead. The Holy Roman Empire had been set up and crowned way back in 800 AD by the Pope, and declared the only "true legal inheritor" of the Roman Empire. After 30 years of nearly everyone in Europe fighting everyone else, the Empire was reduced to a fraction of its size and, importantly, the Pope was no longer calling the shots. The war dragged on, in many ways, because _the Vatican knew what was coming_ and by 1648's Peace of Westphalia they'd realized they could not stop it. After that, it was the Kings and Princes who decided which versions of God and Church were to be allowed or disallowed. Adios, Papa.

The thing is, the Pope and Catholicism didn't ever fully _disappear_ -- their authority was reduced, and has kept shrinking through history as Napoleon feels okay arresting Pius VI in 1769 and Pius VII in 1809 or Mussolini isolating Pius XI's authority to only two square miles around the Vatican in 1929.

Likewise the Holy Roman Empire limped on for quite a while, but in such a reduced state that Voltaire could mock it in his essay _Customs_ as "neither Holy nor Roman, nor an Empire."

In a similar way, browsers won't completely disappear right away -- but over time their value continues to decline, being reduced to a framework for retailers and a few small games, all of which see the _real_ action being performed offscreen on the growing arrays of servers and compute clusters.

## Another Parallel: Radio

If European history isn't a good analogy for you, consider instead radio and television. Amazingly, _television came first_ -- George Carey's "Selenium camera" of 1876 was already in _Scientific American_ for the June 5, 1880 edition, years before Marconi was giving demonstrations. Images sent over radio waves were a real thing by the 1920's but the experience was expensive and not all that great. Radio media dominated, but Farnsworth's 1927 invention of _electronic_ television (that directed the pixels using elecromagnets rather than mechanical beam-aiming) put the technology on an exponential curve of improvements.

The big split between radio and TV at home happened around 1950, as these charts from <a href="https://saylordotorg.github.io/text_understanding-media-and-culture-an-introduction-to-mass-communication/s12-01-the-evolution-of-television.html">Saylor</a> and <a href="https://www.sciencedirect.com/topics/social-sciences/radio-listeners">Science Direct</a> reveal.

<figure class="align-center">
<img alt="The Shift, seen from a Sales angle" src="https://www.botzilla.com/pix2021/tv-adoption-saylordotorg.jpg" width="50%">
<figcaption>from <i>The Evolution of Television:</i> US Households with Televisions</figcaption>
</figure>

<figure class="align-center">
<img alt="The Shift, seen from a consumption angle" src="https://www.botzilla.com/pix2021/radio-listeners-science-direct.gif" width="80%">
<figcaption>from the <i>Encyclopedia of International Media and Communications:</i> Declining Radio Time</figcaption>
</figure>

It's all TV from there on out.

Radio didn't entirely go away -- but today it's mostly an automotive accessory.

In the early days of TV's success, program content followed radio formats closely -- some radio programs like _Gunsmoke_ even jumped the divide when the audiences were moving. Over times, we've seen those formats mutate. Episodic radio shows have nearly vanished, and TV quickly developed its new forms and rituals: Saturday Morning Cartoons, daytime soap operas, the decline of baseball in favor of football and basketball, and later the youtubes and HBOs. Ideas that really don't make sense for radio.

## So Where Does That Leave the Browser?

Depending on where you think we are on the graph, and how the scales shake out, things don't look good, in the long long term, for the browser. And maybe not even in the short term. The rise of computationally-intensive ideas like Deep Learning, Crypto currencies, and Metaverse applications indicate to me that we're already passing into the steeper part of the chart where capabilities are peeling apart faster than software product cycles can adapt (this was true even a decade ago in some quarters: when I was at Nvidia, we passed the point where it took longer to create a AAA video game than the product cycles of AAA game hardware).

Yet weirdly when people are encouraged to learn to code, we give them: Javascript.

It's where some jobs are _now,_ I get it. Or worse, maybe it's where the jobs _were_ when the training website was prepared in 2013. But the long-term returns for getting locked-into JS's mentality and the browser DOM model are questionable.

While the browser isn't vanishing instantly, there are many applications for which the browser's contribution is already reduced to noise:

* High end gaming
* Machine Learning (especially training)
* Crypto
* Microbiology
* Machine Vision
* High-speed and automated Trading
* Logistics Automation and robotics of all kinds
* _The Metaverse_

I'm sure you can think of many more.

For that last one, "the Metaverse" -- whether hi-def or low-def -- is much deeper than what you see on the screen or in your goggles. Those increased demands are largely what makes it more than just another walled-garden game. Physics needs to be calculated, poses estimated, textures and patterns recalculated, loads balanced and synchronized... The computation that's required beyond the visible pixels has to be deep, fast, connected, secure, and able to scale to a very wide range of complexity.

The truth is, "the metaverse" might just be a blip in the course of this history. Right now lots of people have identified a range of computational possibilities and have wrapped a little ribbon around them labelled "metaverse." The truth of what can be accomplished may be far more amazing.

_Hardly anything has been invented yet._

<hr/>

### Footnotes

* _On Moore's Law and Exponents:_ It's entirely possible that what Gordon Moore realized in the 1960's was not an exponential curve but the start of a long logistic one (or a series of logistic curves). If you want to learn a lot about the consequences of logistic curves and improvement, I highly recommend Vaclav Smil's book <a href="http://vaclavsmil.com/">_Growth._</a> If various kinds of computation _are_ on long logistic curves, the basic assertion of this article is probably still true, because each kind of task and platform will have its own limiting factors, which are likely to kick in at different times. In fact I'd even go so far as to say browser computation is already suffering from the limits of its architecture and has been since well before ES6.

* _Try it Yourself:_ As mentioned, the ideas behind this simple set of graphs are in a <a href="https://colab.research.google.com/drive/1NKcdC_18ZQ-GntNhbeRHx1nsU-CRe4XK?usp=sharing">Colab notebook</a> and you can fiddle with them yourself. It's really _very_ simple math, though unintuitive for human brains that don't deal well with exponents. So try it yourself -- see how much noise or variations in the signals can affect your own results. And if you think this model is just full of beans, I'd appeciate your comments!

* The Thirty Years' War lasted about the same in duration as the time from the first web browser until today. Probably nothing.

* _**The Missing Graph Line:**_ One key piece of computational hardware that hasn't changed appreciably since the invention of electrical circuits is the human brain. Tools like React are trying to help you out, but it's... a losing battle. Human computation limits would be drawn as a flat horizontal line on graphs like the ones above. You can decide for yourself where you think that line might should be drawn: high, or low? YMMV, but thinking through some of the possible personal impacts of different line heights might be worth your while. My hunch is that it's low, but hard to make out in the noise: especially since once computation is above human understanding, how can you recognize the quiet shift?

> _This is how the Singularity comes_<br/>
> _This is how the Singularity comes_<br/>
> _This is how the Singularity comes_<br/>
> _Not with a bang but a whisper._
