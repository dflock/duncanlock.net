:title: The Marvellous & Incomplete Compendium of Reddit Automatons
:slug: the-marvellous-incomplete-compendium-of-reddit-automatons
:date: 2013-06-14 19:23:22
:tags: reddit, bots
:summary:

.. figure:: /static/images/reddit-bots-diagram.png

    How much does a a software bot weigh, anyway?

    The original public domain robot, courtesy of `johnny_automatic and openclipart <http://openclipart.org/detail/1654/robot-by-johnny_automatic>`_._

Reddit, the popular internet community, had 71,435,935 unique visitors last month, with over 2,360,783 people logged in [#stats]_.

I say people - but it turns out that not all of the denizens of Reddit are human. There are also 'bots. Lots and lots of them. How many? No-one really knows. [#bots]_

What is a reddit bot?
---------------------------

.. image:: /static/images/private-subreddit.png

A reddit bot is no different from any other reddit account, as far as reddit is concerned. The only difference is that rather than a human logging in to upvote cat pictures and post comments, this account is used by an automated computer script.

In the same way that computers can run scripts to automatically check weather data and `send you an email if you should take an umbrella with you today <https://ifttt.com/recipes/search?q=weather>`_, a computer can run scripts to automatically check reddit for certain activity - and post comments if certain conditions are met. [#qkme_transcriber_faq]_

This is an interesting and somewhat shadowy facet of the otherwise very public reddit community, so I thought I'd take a closer look.

Good bots, Bad bots
------------------------------

Bots that you can Summon with an Incantation
----------------------------------------------

These bots listen out for their summoning incantation to be posted somewhere on reddit, then turn up and do their thing in response:

JiffyBot
============

Purpose:
    Makes animated GIFs out of YouTube links
Known Haunts:
    - `/u/JiffyBot <http://www.reddit.com/user/JiffyBot>`_
    - `/r/JiffyBot <http://www.reddit.com/r/JiffyBot>`_
    - `JiffyBot Documentation <http://www.reddit.com/r/JiffyBot/comments/1fp9qh/how_do_i_summon_jiffy_bot/>`_
    - `JiffyBot in Action <http://www.reddit.com/r/JiffyBot/comments/1fvrsq/the_official_make_your_own_gif_verison_sfw/>`_

Summon by posting a link to a YouTube video, then writing ``Jiffy!`` followed by a start time and end time, in either of these forms:

.. code-block:: python

    Jiffy! 0:07-0:12
    /u/JiffyBot 0:00-0:15

The bot will respond by replying to your comment, with a comment of it's own - containing an imgur link to an animated GIF of that video, for the time period you specified. This is great for people on mobile devices - animated GIFs load much quicker than YouTube.

BitcoinTip
==============

Purpose:
    The bitcointip bot allows redditors to tip each other 'real' money, just by leaving a reddit comment or message.
Known Haunts:
    - `/u/bitcointip <http://www.reddit.com/user/bitcointip>`_
    - `/r/bitcointip <http://www.reddit.com/r/bitcointip>`_
    - `BitcoinTip Documentation <http://www.reddit.com/r/bitcointip/comments/13iykn/_bitcointipdocumentation/>`_

The bot scans user comments and messages for tips of the form:

.. code-block:: python

    +/u/bitcointip @RedditUsername $1
    +/u/bitcointip @Username $1usd
    +/u/bitcointip BitcoinAddress 1 millibit
    +/u/bitcointip Username ฿0.001 verify
    +/u/bitcointip $1 # This tips 1 usd to whoever posted the comments parent
    +/u/bitcointip BitcoinAddress ALL # This sends your entire balance to that bitcoin address
    +/u/bitcointip 2 internets # An "internet" is worth $0.25

You have to setup a bitcointip tip account in advance and put some funds into it. It then sends the specified amount of bitcoins from the sender's bitcointip account, to the receiver's bitcointip account. Supports lots of different currencies, which get converted to bitcoin automatically.

CHART_BOT
=============

Purpose:
    Automatically generate and post a chart of your posting history - or someone else's.
Known Haunts:
    - `/u/CHART_BOT <http://www.reddit.com/user/CHART_BOT>`_
    - `/r/CHART_BOT <http://www.reddit.com/r/CHART_BOT>`_

Making a submission `to this subreddit <http://www.reddit.com/r/CHART_BOT>`_ will cause CHART_BOT to automatically generate and post a chart of your reddit posting history. You can also request charts of other reddit users by putting their username prefixed with an @ in the title of your submission. The charts look like this - `here's mine <http://www.reddit.com/r/CHART_BOT/comments/1gdpu9/chart_me_up_baby/>`_:

.. image:: /static/images/duncan-locks-chart-bot-chart-june-2013.png
    :alt: Screenshot of CHART_BOTS output for duncanlock, as of June 2013.


Bots that just Turn Up, without human intervention
----------------------------------------------------

These bots ceaselessly watch the endless, mighty cataract of text that is reddit and leap in whenever they sense patterns in the noise that match their programming.

Metric System Converting bot
==============================
Purpose:
    Automatically generate and post a chart of your posting history - or someone else's.
Known Haunts:
    - `/u/CHART_BOT <http://www.reddit.com/user/CHART_BOT>`_
    - `/r/CHART_BOT <http://www.reddit.com/r/CHART_BOT>`_

Website Mirror bot
======================
Purpose:
    Mirrors websites if they go down due to being posted on reddit.
Known Haunts:
    - `/u/CHART_BOT <http://www.reddit.com/user/CHART_BOT>`_
    - `/r/CHART_BOT <http://www.reddit.com/r/CHART_BOT>`_


tabledresser
==================
Purpose:
    Automatically generates a summary table from an `AmA thread <http://www.reddit.com/r/IAmA/>`_, showing all answered questions, along with their answers.
Known Haunts:
    - `/u/tabledresser <http://www.reddit.com/user/tabledresser>`_
    - `/r/tabled <http://www.reddit.com/r/tabled>`_

It posts the first few rows in the actual AmA thread, with a link to the full table that it posts to `/r/tabled <http://www.reddit.com/r/tabled>`_. This provides a great way to quickly read a condensed summary of a complete AmA thread, `like this one <http://www.reddit.com/r/tabled/comments/1g9nja/table_iama_i_am_james_bamford_one_of_the/>`_. They look something like this:

.. image:: /static/images/tabledresserbot-example.png

qkme_transcriber
===================
Purpose:
    Automatically finds links to Quickmeme meme pics (quickmeme.com or qkme.me) and provides a plain-text transcript of the content of that meme in the comments section, so you don't have to click through to the Quickmeme site to get the 'joke'.
Known Haunts:
    - `/u/qkme_transcriber <http://www.reddit.com/user/qkme_transcriber>`_
    - `/r/qkme_transcriber <http://www.reddit.com/r/qkme_transcriber/>`_
    - `qkme_transcriber FAQ <http://www.reddit.com/r/qkme_transcriber/comments/o426k/faq_for_the_qkme_transcriber_bot/>`_

This bot tends to turn up in subreddits like `/r/AdviceAnimals/ <http://www.reddit.com/r/AdviceAnimals/>`_ and post comments that look like this:

.. image:: /static/images/qkme-transcriber-bot-example.png



----------------

Footnotes & References
--------------------------

.. [#stats] `About Reddit, including some mind boggling statistics <http://www.reddit.com/about/>`_.
.. [#bots] How many bots? Now one really knows. `How to create a Reddit bot <https://praw.readthedocs.org/en/latest/>`_. This being reddit, there's `a community <http://www.reddit.com/r/botwatch>`_ to keep an eye on them, too.
.. [#qkme_transcriber_faq] This is mostly quoted from the excellent qkme_transcriber bot's FAQ, `here <http://www.reddit.com/r/qkme_transcriber/comments/o426k/faq_for_the_qkme_transcriber_bot/>`_.