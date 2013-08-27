:title: Windows is Screwed in a Post Desktop Future
:slug: windows-is-screwed-in-a-post-desktop-future
:date: 2013-07-10 00:07:01
:tags: windows, linux
:meta_description: If you're building something that needs an OS - like a rocket (SpaceX) or a console (Valve) - you HAVE to use Linux, nothing else makes sense.
:status: draft

If you're building something that needs an :abbr:`OS (Operating System)` -  like a rocket (SpaceX) or a games console (Valve) - you HAVE to use Linux, nothing else makes sense. Nothing.

Windows is closed source software - only Microsoft can change the code, you just get to use the final product. You can either like it, or not, but you can't change the way it works.

Because Microsoft has only built Windows to work on generic PC compatible hardware - desktop and laptop computers - if you need something different to this, you're out of luck.

.. epigraph::

   Linux is used for everything at SpaceX. The Falcon, Dragon, and Grasshopper vehicles use it for flight control, the ground stations run Linux, as do the developers' desktops. SpaceX is "Linux, Linux, Linux"

   -- Robert Rose, SpaceX: "Lessons Learned Developing Software for Space Vehicles" [#SpaceX]_

If you're building a product that needs an operating system - which is pretty much anything with electronics in - and your product doesn't resemble a generic PC compatible desktop or laptop computer, you can't use Windows as your OS - end of story.

What are you going to do - ask Microsoft do you a custom Windows for Rockets? Hey, Microsoft, could we have a good volume deal on a custom version of Windows for our new XBox competitor? Yeah, sure.

http://arstechnica.com/information-technology/2013/07/99-arm-based-pc-runs-either-ubuntu-or-android/

RasberryPi

Fat & Expensive
---------------

Even if you could customize Windows so that it works on your hardware, it often makes little commercial sense to do so. Microsoft charge money for Windows licenses per device - which adds an extra fixed cost to each one that you sell.

[Embedded Windows]
[Windows is to big]

Both of these problems get worse in the wrong direction for most consumer devices, too - the smaller and cheaper your hardware, the greater the proportion of your costs are made up of the Windows license for it -- and the more problems you'll have squeezing it on there in the first place.

Late & Stuck
--------------

Microsoft were a decade late waking up to *the trend* - one in which they were instrumental in helping to start in IT in the 80's - the democratization / amateurization of everything [#amateurization]_. They hugely assisted - and profited from - the transition from giant mainframe computers, managed by professional IT gurus, to a PC on every desk, managed by you (whether you liked it or not).

But then they got stuck.

They were slow to realize that the trend continued, out the office door, all the way home, into your pocket & online. They got stuck where their money lived - in the office. They didn't react fast enough to the wave of consumer devices, proliferating at home - and then coming back into the office and cannibalizing that market.

Why does my office look like this: [pic of ancient dell desktop] and my home look like this: [pic of new apple gear]

By getting married to big business, Microsoft was unable to serve the home consumer market well - think Zune vs. iTunes:

.. figure:: /static/images/posts/windows-is-screwed-in-a-post-desktop-future/microsoft-revenue-diagram.png

    Microsoft Revenue & Profits, June 2011 - 2012, broken down by division, then consumer vs. business. [#ms_revenue]_

    Their revenue/turnover from the consumer market is ~17%, but it's either loss-making, or not very profitable, so only equates to ~1% of overall profits.


It may well turn out that Microsoft's total domination of the business computing market throughout the last ~30 years was the best gift Apple ever got. They couldn't beat Microsoft at their own game and almost died trying, several times. They were eventually forced to learn to play a different game - the consumer market. They eventually got quite good at it. Microsoft never did - they didn't *have to*, they had plenty of existing revenue they could fall back on.

It's really hard to turn around a company as big as Microsoft. They currently employ 94,290 people [#ms_info]_ worldwide - almost all of whom have been hired, trained and have worked for the last ~30 years to focus *completely* on the business desktop PC market. It's woven very deeply into their corporate DNA.

Why MS is in cul-de-sac and apple isnt:

http://stratechery.com/2013/if-steve-ballmer-ran-apple/

Transition to Multi-screen world
----------------------------------------

Seemingly quite suddenly, after decades of dominance, the desktop PC is facing incredible competition from new kinds of devices - principally smart phones & tablets. Unlike laptops, these new devices don't use shrunk down PC compatible parts inside - they're a little bit different. They use hardware that Windows historically doesn't run on *at all*. They're also quite different from each other - different tablets and phones use wildly different chipsets, processors, screens, etc... - and they change all this every year.

MS don't give the source code out, so OEMs can't customize Windows for their devices - so they have to use something else.
The only way MS can compete is to make the Hardware too - hence Surface.

So, they become a crappy version of Apple and their market share slowly dwindles to match.

http://qz.com/118337/steve-ballmers-retirement-could-unlock-the-talent-and-resources-now-dormant-at-microsoft/

Surface & Windows RT
----------------------

WTF?

http://tech.slashdot.org/story/13/07/19/1456220/microsofts-surface-rt-was-doomed-from-day-one
http://slashdot.org/topic/cloud/microsofts-surface-rt-doomed-from-day-one/
http://techcrunch.com/2013/08/10/microsoft-doesnt-want-to-admit-windows-rt-is-dead/

Embedded Windows
----------------------------
Refs:

* http://www.omgubuntu.co.uk/2013/04/microsofts-market-dominance-is-coming-to-an-end-say-leading-analysts


----------------

Footnotes & References
=========================

.. [#SpaceX] Quote taken from here: `Lessons Learned Developing Software for Space Vehicles <http://lwn.net/Articles/540368/>`_
.. [#amateurization] **Mass Amateurization** refers to the capabilities that new technology have given to non-professionals and the ways in which those non-professionals have applied those capabilities in order to create and distribute content & solve problems in ways that compete with larger, professional institutions. `The Mass Amateurization Of Everything <http://en.wikipedia.org/wiki/Mass_amateurization>`_
.. [#ms_revenue] Figures taken from here: `Where does Microsoft make money? (Updated 2012) <http://www.tannerhelland.com/4273/microsoft-money-updated-2012/>`_
.. [#ms_info] From the horses mouth: `Facts About Microsoft <http://www.microsoft.com/en-us/news/inside_ms.aspx>`_