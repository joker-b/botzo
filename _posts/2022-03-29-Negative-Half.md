---
layout: post
title: "Negative Half-Life"
categories: [Hacking]
tags: [Featured, Essay, _Phase4]
image:
  path: https://www.botzilla.com/pix2022/bjorke-Half-1-1.jpg
  thumbnail: https://www.botzilla.com/pix2022/bjorke-Half-1-1.jpg
---
<br>

In 1907 Ernest Rutherford realized that certain materials in certain rocks were slowly decaying into other materials. Specifically, the newly-discovered radium degenerated into the stable isotope lead-206. He realized that this decay's speed was exponential: faster at first and slower as it progressed, leaving less and less radium. In his equations he labeled the time it would take for half of a radium sample to decay into lead as its _half-life._

From this realization he and others could compare the amounts of a specific isotope of decaying radium or (even better) uranium to the amount of stable lead in a mineral sample, and use this proportion to estimate the rock's age. By the end of the 1920's they'd managed to show reliably that the age of the earth was at least 3.4 billion years old.

The idea works great for rocks. Also, for software & development.

<!--more-->

The term "half life" has been used in other fields.  Investors may talk about the half life of a loan, meaning the time it takes to pay back half of the principal. The term gained everyday popularity as the name of a Valve videogame, then as a series of games.

That hit video game itself has a sales decay: in 1999 _Half-Life_ sold 445,123 copies in the US, while in 2000 it sold 286,593 -- from those two samples we can estimate that _Half Life's_ half life is about a year and a half, with many of those gamer sales decaying into _Counter-Strike_ or _Half-Life: Alyx_ or an orange box.

For someone who is skilled at playing _Half Life,_ their skills likewise decay when they are exposed to those new titles. The keystrokes of WASD and firing might be preserved (unless you move to a game console or HMD), but the player's skilled notions about speed, about the maps, about the distribution and nature of opponents human or automated, are all subject to revision or need to be completely discarded.

For a new or decaying atom, the state changes nearly instantly: the exit of protons, gamma particles and so forth are so quick that a new kind of imaging was needed to even identify them clearly (see <a href="{% post_url 2018-12-17-Hough %}">this previous entry</a>). After the shift, the next bump in a nucleus's half life might be half a trillion years away into the future. Quick change, long stability. Sometimes.

This simplicity isn't entirely shared by the decay of a skill (or a loan). A skill doesn't only have a gently-grading exponential decay: like a single atom, a single learned skill is either trained, or untrained. Both learning and unlearning have fixed, non-gradient costs (Loans might have fixed costs relating to lump sums, down payments, prepayments...).

Human learning, despite improvements in technology, despite <a href="https://fs.blog/learning/">best practices,</a> overall continues to run at about the same clock rate, decade after decade. Even the fastest learner can't reduce the cost to zero. Part of this comes from the irreducible non-zero cost of <i>practice:</i> you can read about tennis, but to play tennis, you need court time.

Learning to walk takes about a year. The skill of walking's half-life of usefulness is probably over a century. Learning to move around effectively in the early-edition _Half Life_ takes a few minutes or hours with an expected play time of maybe 15 hours. If your subsequent gaming decays into _Counter Strike_ or _Team Fortress,_ then those basic skills might retain utility for another five or ten years. 

Gameplay is designed to have "a low on-ramp" to basic skill. There's an incentive for the game maker to create it this way, it encourages everyone to keep exploring and buying more games. This is not, however, the nature of game _making._

The skills involved in creating video games are largely shared by other kinds of software efforts: developers need to learn ever-mutating specialized languages; the shapes of APIs for graphics and networking and storage and financial operations; cognitive psychology and phenomenology; game AI, probability, statistics; the mathematics of optics ands newtonian physics and (usually) exponential decay, and surely more in the future as the scope of gaming continues to expand.

The acquisition of these skills takes time, and often a team of particular individuals is required to share the burden of learning different specialties. This pattern is not at all unique to game building: it's true for nearly every technically-intensive field: energy, aviation, and medicine to name only three. As computers accelerate and data storage grows, the half-lives of many skills shrink.

Decay events happen suddenly for a single atom, and so too, sometimes, for skills -- especially if those skills are contingent on externalities such as the existence of a specific tool vendor. Early in my animation career, such a sudden decay occured when I realized that the creaky IMI-500 workstation I'd been using and learning on was to be replaced, along with all of the associated software, due to the studio and its proprietary software going bust, which in turn was allegedly due to a bank fraud in another country, external to "animation" _per se._ Just as I was starting to feel accomplished at using it, I thought. _Start over._

Around the point of this misfortune, I had the complementary good fortune (probably due to older colleagues) to realize that _it will always be like this._ And it always has. Learning the specifics about technology is a hazardously-limited business. It's essential to expect and _embrace change,_ not to rest on accomplishment.

The correct response to having lots of now-useless skills is to get very good at learning. A benefit: there's a real joy in it. As Isaac Asimov commented: "The true delight is in the finding out rather than in the knowing."

In recent years, it's become common to see cases where the half-life of utility for technologies is becoming <i>even less than the time required to learn them deeply.</i> That is, for a new student of, say, the GulpJS package manager, the half-life of GulpJS's usefulness may be _negative._

This doesn't mean the new skill is entirely useless, but that its utility is already dwindling even as you begin.

Sometimes a quick decline can spell quick extinction, as in, say, YouCoin or TurtleGold. Your skill (and maybe money) will tank.

Other times the value might be there, but it either fades to fog or becomes very narrow in use. A quick check of LinkedIn this morning revealed new-today opportuniies for COBOL developers. But the audience for COBOL skill is dwindling and the rate of change in those markets (e.g., long-lived government contracts) is very unlikely to reward innovation or even exceptional competence.

The speculative half-life of COBOL skill is probably somewhere around forty or even sixty years. COBOL has outlived languages like Algol and MUMPS and Pascal, probably in part because its closely aligned with slow-moving entities like central banks and state benefits agencies. The half-life of Maya MEL or Vue, tied to TV and gaming and retail, is surely much less.

How can we estimate the half-life, or expected utility, or a skill? A reasonable approach is to exploit the Lindy Effect, named after a NY diner where a group of writers would discuss changes in their corner of the mass media. The basic gist: if you don't know anything else about a medium or a show or a technology, assume that you are probably at the mid-point of its life. There might be additional info that you can use to refine the guess, but: assume that _right now_ is the midpoint.

COBOL has been around since 1959. Will it finally expire around 2085? React has been around for a decade: React17 for about a year and a half. If that's _all the info you have,_ what should you guess about ongoing usefulness? What info might make your estimations clearer? Should developers, HR departments, and managers think they _know?_

Ignorance of this nature of technology is evident in the way many companies address their product plans, staffing needs, and quarterly budgets. It's likewise, sadly, how many developers, artists, doctors and other might mistakenly define themselves. Recruiters may work from a cryptic-to-them checklist. Item one: we need a React17 developer (at the extreme, someone with the impossible "5+ years of React17 experience").

It's not unusual to hear former animation and VFX colleagues lamenting that there just aren't many good 3DS Max jobs around any more, because "I'm a skilled Max user" (I suppress the urge to shout: "the job should never have been about Max!").

Sadly, it's very, very rare to see jobs, even in the most dynamic of work environments, where learning and the ability to learn is considered a qualification. And as for job _listings:_ forget it. Rather, the opposite: the idea that someone would be spending time actively re-learning and discarding their qualifications is  actively discouraged. Or if it's expected, that learning should be done after work hours.

In medicine, there's a partial acknowledgement of this (life or death) problem. Clinical practioners are expected to spend at least part of each year learning new procedures and changes in standard practices. This situation in professions like medicine is probably due to the fact that a doctor and their hospital can be sued for malpractice if they treat a patient with an obsolete or dangerous procedure. In software, no one will sue you for using less-performant and tired tools like Angular or PHP or Rails, even if maybe you should carefully reconsider their future usefulness. Companies would often rather just shuffle-off old tech and hire new faces than, say, grow the company's ability to use, say, Rust or LIGO.

In recent Silicon Valley practice (by "Silicon Valley" I mean online-related tech in general), this acceleration problem has spread to non-developer jobs as well. The typical time that developers and managers spend at their current Silicon Valley company is now hovering around two years. In practice it's normal to see managers sweep from company to company in much less time.

A product manager colleague asked me, around 2017: "I'm coming up on my second anniversary... do you think that's too long at one company?" They were concerned that if they weren't actively company-hopping it would make them look stagnant to potential future recruiters. It didn't matter if they were enjoying the work or accomplishing things.

A serious hazard, for such a revolving-door culture, is that such managers can't reliably make decisions for longer time frames. As the investment aphorism goes: "you can't expect long-term results from short-term people."

The way many companies are currently structured, there's a strong individual incentive _toward_ bad decision-making when it comes to long-term impact. It's a pattern I've seen repeatedly: a new-hire manager arrives with a copy of _Your First 90 Days_ tucked under their arm, they declare "the new plan" which invalidates the work of "the old plan" while indicating to their manager that they are full of ideas and action. They're praised for their chaos-inducing foresight but before their New Plan has actually (not) shipped they've moved to the next bigger paycheck and a new face arrives with their own copy of _90 Days._

This sort of corrosive feedback loop is one of the many ways companies can become disaster factories. The incentives for middle managers are away from having skin in the game, when they can so handily avoid any negative consequences from their decisions.

Is there a way out of this, a way to improve accountability and to foster continuing growth?

Contingent bonus completion contracts might offer one method. Stock options are sometimes useful first-choice from VCs but rarely effective if the stock's not being traded or seems to be lingering at close to or below the option price. These transactional ideas have a flaw: they don't really address learning or connection or responsible action once the checks have been printed.

There is another way. It's a bit radical, but it goes like this: the people are not a collection of skills, they are not the company's greatest "resource." _The people are the company._ As the people grow, the company can likewise grow. If the people are locked in place, the enterprise is on its way to self-strangulation.

When these ideas are aligned, changing tech, learning as a company, and effective long-term decision making are possible. Without it: you might be trapped below zero. Good luck.
