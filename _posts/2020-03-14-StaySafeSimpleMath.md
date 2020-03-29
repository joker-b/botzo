---
layout: post
title: "Staying Safe: Simple Math"
image:
  path: http://www.botzilla.com/pix2020/bjorke_Empty_KBXF7884d.jpg
  thumbnail: http://www.botzilla.com/pix2020/bjorke_Empty_KBXF7884d.jpg
categories: [Botzilla]
tags: [Health, Epidemic, Math, Algorithms, Python]
---

_How can I avoid being infected by the current pandemic? What's my risk? How safe is "safe"? What are realistic safety margins?_ Let's find out! It's not difficult with a little focused thought.

The internet today is full of confusing information, but on this page you can get the math yourself to decide what's best for you, the people you care about, and to keep _yourselves_ safe.

## **TL;DR:**
* The epidemic is big, but your personal decisions about your safety can give you control. Don't be a statistic.
* The best way to win is to avoid losing.
* "Common Sense" and intuitions will be very wrong for this uncommon situation.
* Early choices have big benefits. Small risks over time can become big risks, so keep them all small.
* Things will be changing rapidly day-to-day in a couple of weeks, even if it's not immediately obvious: there are delays between infection and illness.
* Testing is only a small part of the solution.
* Friends and family matter.
* You can do this.
<!--more-->

### The Simple Math

The math of epidemics is based on statistics, and you take your bets. But just like any game of chance, _sometimes you can cheat._ This article looks at the math, and tells you when -- and how -- to cheat. You can cheat by being deliberate about your risks on a day-to-day basis, by managing over many days, and by working wisely with accomplices. You don't have to be a statistic.

Maybe you hated high school math. That's okay -- if you're reading this, you have a computer. You're covered: let the computer do it. _You don't have to read equations to benefit from them._

If you do want the equations, here's <a href="https://colab.research.google.com/drive/1hMDK4EIDLYARerGvokSK2se-smFZ2RpQ">my original notebook on Google Colaboratory</a> (I don't work for Google, it's just a great tool). I very much welcome comments and suggestions for improvement.

The math you'll find here, hidden behind the graphs and available to anyone who wants to improve it, repurpose it, or see for themselves, never uses basic concepts more complex than middle-school arithmetic -- just a lot of them chained together.

### Common Sense is not Enough

_"Common sense" might not be best in uncommon situations._ I'm writing this in the hope it spreads a little sense about how your personal safety can be managed in these times when "common sense" and "moderation" -- excellent most of the time -- might get you in trouble.

In particular, what feels low-risk in the moment might be high-risk if it's repeated during the day, and over many days. 

### You Win By Not Losing, Over and Over

_"What's my risk?"_ is similar to the high school math-class question: _"How many times can you flip a coin without hitting tails?"_ For one toss, obviously, the chances are fifty-fifty. What about four times? If you'd hit tails on the first go, you're done. But on the next toss, if you had heads at first, the odds for _that_ second toss alone are: again, fifty-fifty. So, you still have about a 25% of throwing heads twice. You can keep multiplying the chances of _not_ hitting tails for each subsequent toss, and there will always be some slim _possible_ chance that you can toss heads ten times in a row. Even 100 times in a row. But don't count on it! 

There's a simple formula to figure out your chances for figuring your chance for tossing heads ten times: just multiply the chances of _not_ tossing heads, ten times. Or in Math notation,

> `pow(chanceOfTails,numberOfTosses)`

and subtract that result from 100%.

<figure class="align-center">
<img alt="coin flips: avoid losing" src="http://botzilla.com/pix2020/safe-01.png">
</figure>

So much for coin tosses.

We can apply the very same method to understand, for any given day and based on how many people we might encounter each day, the likelihood we'll encounter any infected people, based on just a few numbers: how many people we encounter that day, the total population, and the known number of cases.

To determine our personal risk for a single day: multiply _"chanceUnifected"_ by itself, _"numberOfPeople"_ times. If 80% of people are uninfected (only 20% _are_ infected) and you encounter five random people during the day, then your chance that none of them were infected is<br/>&nbsp;&nbsp;&nbsp;&nbsp;80%&nbsp;x&nbsp;80%&nbsp;x&nbsp;80%&nbsp;x&nbsp;80%&nbsp;x&nbsp;80%<br/>which is only 32%(!), giving you a 68% chance of being exposed that day -- worse than fifty-fifty, though the amount of infection might have seemed "low."

You can figure out the _"chanceUninfected"_ by just dividing the number of infected people by the population and subtracting that from 1. That's defined by what you hear on the news. It is what it is. But:

**Cheat #1: it's _up to you to decide_ the _"numberOfPeople"_ you encounter for any given day.** This is the most powerful cheat. How many people is a good number? Read on.

<figure class="align-center">
<img alt="cheat #1" src="http://botzilla.com/pix2020/safe-02.png">
</figure>

Assuming that infected people continue randomly walking around on the street, you can see that even for a lot of cases within a population (I'm using today's rough population of Sonoma County), the odds that any given person is infected can look low. This is where your choices about _"numberOfPeople"_ come into play.

Let's compare results for different numbers of random people you encounter daily: do you encounter 1 person, 2, 5, 10, 30, or 100 people?

<figure class="align-center">
<img alt="risks from number of daily interactions" src="http://botzilla.com/pix2020/safe-03.png">
</figure>

I hope you can see where this leads! The brown line at the top is for 100 people, the blue one at bottom for just one. The more people you encounter each day, there's a _big_ difference in the chances that at least one of them is infected. This matters even when the infection rates are miniscule. Are there 30 people in your workplace? Look at that purple line. Five? Look at the green. Are you staying isolated at home, using the phone and video chat? Your chances of encountering an infected person are much, much, less.

> _To be clear: by "encounter" I don't mean "you'll be infected." You could be entirely safe, prudently far from them, just noticing as folks go by outside your window. Be smart in all the regular ways, regardless. Wash your hands. We're just estimating randomized risk._

Why think about this per-day? Because every day is different. The present epidemic in the US is growing by about 30% every day. A big change day-to-day, as it grows.

Currently, the 14th of March, our county has had ony one local person-to-person case. We'll get to that a bit later, but I'll include these cruise ship numbers for now -- they won't make much difference later (Because there are so few cases here in Sonoma County, it's hard to know if we're currently in week one of the charts below, week two, or even week three -- I'll be tracking and updating in the future). We can use what we know today and start to get a grasp of how things might go for ourselves as risk of exposure grows over several weeks:

<figure class="align-center">
<img alt="risk growth" src="http://botzilla.com/pix2020/safe-04.png">
</figure>

Again, the brown line at the top -- that is, the one peaking early -- shows the risk for people who have a lot of exposure to others each day. The lowest one on the right: just one person per day.

Here's an estimate of the early weeks of infection, up to where it's levelling-off some and you can _start_ to feel a bit safer:

<figure class="align-center">
<img alt="early weeks" src="http://botzilla.com/pix2020/safe-05.png">
</figure>

There's a line that's missing in these charts: __*the zero option.*__ If you're not encountering _anyone,_ none of them have an opportunity to infect you that day, other than indirectly via dirty surfaces, shared plumbing and ventilation, etc. 

_Remember Cheat #1: Interact with as few people, as carefully as possible, and right from the start. Don't wait to be exposed before trying to stay isolated._

**Cheat #2: If you need to interact with people, do it early.**

Let them know you won't be available in person if the epidemic grows. If you work on a team, say your temporary goodbyes (or switch to remote work) in week one, not week two. If you absolutely must be in your workplace, can you stagger work hours to minimize the daily contacts? And yes, if you can, shop early and don't go back to the store.

## Where "Common Sense" Fails: from Risk-per-Day to Risk-per-Epidemic

Remember, the values above are for understanding you personal _per-day_ risk factors. Just for one day! The risk goes up over time, but you want to stay safe over the epidemic as a whole.

Just as with our coin-toss example, we really want to calculate the ongoing likelihood that you will _not_ encounter an opportunity for infection over many days. You want that likelihood to be absolutely as low as possible! Even without a growing epidemic, let's look at the likelihhood of exposure over the same time range, if there's only a _one percent_ per-day likelihood:

That's `pow(0.99, 56)` for 99% safe over 56 days -- which leaves a dismal 43% likelihood of safety of the period.

<!-- 
<figure class="align-center">
<img alt="one percent not so good" src="http://botzilla.com/pix2020/safe-06.png">
</figure>
-->

Not so great -- little better than fifty-fifty. But... our initial risk values were actually lower than one percent. A lot lower. What if we restrict ourselves to the expected exposure on "the blue line" after one week from the start, which is a tiny 0.0037648% of risk:


<!--
<figure class="align-center">
<img alt="better" src="http://botzilla.com/pix2020/safe-07.png">
</figure>
-->

Or `pow((1-0.000037648) ,56)` which comes out to **99.78938932742998% safe.**

_That's so much better!_ This is our blue line value for the first week -- randomly encountering no more than _one_ random person per day, and somehow maintaining the same level of risk. Low risk today, low risk tomorrow.

Of course, we know the risk varies over time. It gets a lot worse for a while, and then subsides as the population reaches its maximum level of infection (eventually, the virus runs out of people to infect, either because they've stayed home and dodged the bullets or they've already had the disease).

If we glue-together our graphs of changing population risks plus our personal risk management, we'll get something like the following:

<figure class="align-center">
<img alt="Worst Case" src="http://botzilla.com/pix2020/safe-13.png">
<figcaption>Worst: 100 Encounters per Day</figcaption>
</figure>

<figure class="align-center">
<img alt="Better" src="http://botzilla.com/pix2020/safe-08.png">
<figcaption>Better: Only One Encounter per Day</figcaption>
</figure>

With only _one_ random encounter per day, we're only getting to 20% risk of exposure at the same time our worst performer, with 100 contacts, is essentially at 100%.

Yet eventally, after a couple of weeks' growth, even the low-contact model gets to the top.

Again, we've left-out **zero encounters.** And this is where your friends come in.

## You are not a Random Number

And neither are the people around you. We tend to collect in groups: teams, families, friends. If you are only interacting with a small group, then the randomness of your life is... less random!

But remember this important rule of thumb: **the risk for all people in a close group will be set by the maximum risk of any single member of the group.**

If you stay isolated with your uninfected family and no one goes out for many days, your risk during that time is close to zero. If one person goes to the grocery store, their risk in doing that is shared by everyone. If the whole family goes to the grocery store, the risk will be even slightly higher.

(A note about "hidden encounters": at trafficked locations like grocery stores, there are places where nearly everyone will touch the same object -- the automated checkout machine or ATM, the doors of refrigerators, doors of the store, rails on the stairs, basket and shopping-cart handles, or the grip on the filling-station pump on your drive to the market. You may never see the people who might have left viruses on these objects, but consider it an "encounter" just the same. Remember to wear gloves and to wash your hands whenever you touch items outside your home safe-zone).

**Cheat #3: Isolate Close to People You Love, and Coordinate.**

If you can stay isolated but together, you will be happiest. You'll help each other be healthy, happy, and you'll even be helping everyone else, in your own collective bits.

_What if one of us gets infected?_ Isolate them as best you can, get medical professionals involved. Discuss how you might divide your living areas _in advance_ so that everyone knows what to do if this happens.

**Cheat #4: Stay Aware and Follow Your Plan.**

Your plan doesn't need to be perfect, but it can be good. Resist the urges to make exceptions, or to believe things you wish were true (like: "maybe it will just get better if the weather turns hot" -- this is just hopeful speculation, there's no evidence of it and some evidence that it's wrong). Situations will change so looking ahead at the range of possibilities will help you stay calm and make good decisions when you need them.

### What About Testing, and Isolating Sick People?

When someone gets a positive virus test and is isolated at home (or in bad cases, at the hospital), it's true that they're now less-likely to spread the illness and that's a great thing!

The problem comes from _delays._ On average, people don't have any symptoms for three to five days. In five days, with the current growth rate, and even with perfect universal instant testing, the actual number of infected people will be _nearly four times the number of people showing symptoms._

Even with perfect testing, the daily risk is only reduced by about one-quarter or less. It is important to do, and will get treatment to people who need it, but testing and isolating sick people will only have limited effect on the overall growth of the illness.

Likewise, I've left out recovered cases because it can take many weeks to recover -- recovered patients don't become a major factor until we're already past the peak.

## How Can I Help This to End Quickly?

Glad you asked! The same measures you take to keep yourself safe, to keep safe your
family and everyone dear to you, are _the same measures that will end the epidemic
for everyone._

If you get infected, there's a risk you will infect others. But back to **Cheat #1** and the **Zero Option:** _you won't lose a game if you don't play._

The more people who can fight back by staying in control of their daily exposure will not only be healthier, they'll reduce the number of hosts for the virus to exploit. The size of the pot will shrink, and the game will end safely all the sooner.
 
## Where "Common Sense" Wins: Remember What's Really Important

**Cheat #5: Don't Spend All Your New "Free Time" Anxiously Clicking Links.** 

It will stress you out. Stress will mess with your immune system, and rob you of sleep. Follow your plan. You're in your own personal army for the duration. That plan should include a positive attitude.

Whether you're at home alone or with your safe-crew people, spend your time constructively. Call your parents, call your kids. Call your neighbors and your snowboarding buddies who you missed during the Year of No Spring Break. Keep calling them. Learn to use video chat programs if you can. Spend time being creative: it's hard to draw or play piano or create that cool new web app you've dreamed about if you're being interupted all the time, but for the next few weeks, you might have just the opportunity.

In the 1660's Isaac Newton created his famous Three Laws of Motion at home, isolated from a plague that had shut down most of England (including his school). You don't need to be a genius to use this time to get closer to your loved ones and yourself. But you'd be a fool not to try!

## **You can do this.**

