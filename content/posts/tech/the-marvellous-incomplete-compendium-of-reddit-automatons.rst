:title: The Marvellous & Incomplete Compendium of Reddit Automatons
:slug: the-marvellous-incomplete-compendium-of-reddit-automatons
:date: 2013-06-14 19:23:22
:tags: reddit, bots
:status: draft
:meta_description: Reddit had 71.4m visitors last month, with over 2.3m people logged in. I say people - but it turns out that not all of the denizens of Reddit are human. There are also 'bots. Lots and lots of bots...
:thumbnail: /static/images/reddit-bots-diagram.png

.. figure:: /static/images/reddit-bots-diagram.png

    How much does a a software bot weigh, anyway?

    I found the original public domain robot on `openclipart, posted by johnny_automatic <http://openclipart.org/detail/1654/robot-by-johnny_automatic>`_.

Reddit, the insanely popular internet community, had 71,435,935 unique visitors last month, with over 2,360,783 people logged in [#stats]_.

I say people - but it turns out that not all of the denizens of Reddit are human. There are also 'bots. Lots and lots of bots. How many? No-one really knows. [#bots]_

This is an interesting and somewhat shadowy facet of the otherwise very public reddit community, so I thought I'd take a closer look...

What *is* a reddit bot?
---------------------------

A reddit bot is no different from any other reddit account, as far as reddit is concerned. The only difference is that rather than a human logging in to upvote cat pictures and post comments, this account is used by an automated computer script.

In the same way that computers can run scripts to automatically check weather data and `send you an email if you should take an umbrella with you today <https://ifttt.com/recipes/search?q=weather>`_, a computer can run scripts to automatically check reddit for certain activity - and post comments if certain conditions are met. [#qkme_transcriber_faq]_

It's a Hard Bot Life
---------------------------

A major problem for any internet activity at scale is 'spam', or similar unwanted activity, in some form or other.

Reddit has scale coming out of it's ears, so needs aggressive, pervasive and rapid automated spam control algorithms - combined with extensive human flagging and moderation - just to survive.

These mechanisms come down on bots particularly hard, to prevent the place being overrun by implacable text hurling machines, who can type & post at the speed of light.

This is a `really nice /r/InternetAmA thread discussing the retirement of TicTacToeBot <http://www.reddit.com/r/InternetAMA/comments/1gescq/i_am_tictactoebot_i_derail_threads_and_i_am/>`_, which did exactly what you'd expect:

.. figure:: /static/images/reddit-bots-tictactoebot-example.png

   The only winning move is not to play.

Some quotes from TicTacToeBots developer:

    Q: Your account has only existed for 6 days. How have you already been banned from the subreddits?

    A: No clue. Every day I am banned from subreddits. I woke up today, looked at the mail. Banned from circlejerk, cats, and skyrim... Those aren't even default subs. I had to sub to new channels to be any active as a bot.

    Q: You actually got banned from circlejerk [#circlejerk]_? For derailing threads?!?

    A: Yes

TicTacToeBot got shot down for derailing threads - i.e. for being disruptive. It was `intentionally designed to randomly pop up and challenge people <http://www.reddit.com/r/todayilearned/comments/1fzgle/til_that_110_people_once_tied_for_second_prize_in/cafg3xj?context=2>`_ to a game - whimsical and fun, but also an uninvited disruption - albeit a harmless good natured one.

So unless they're careful, disruptive bots tend to have a fairly short life on reddit, quickly being hunted down and blocked by reddit's immune system -- even whimsical and seemingly harmless bots, like TicTacToeBot.

More circumspect bots, like JiffyBot_, CHART_BOT_ or Serendipity_ - either completely or largely confine themselves to their own subreddits, only turning up elsewhere when invited. This generally means that they'll be left alone to do their thing, because they're not interfering with anyone else. They're also completely upfront about what they do and provide a useful service to the reddit community.

Workin' on a Bot Farm
=======================

Bots also take resources to run - both to initially create & then to maintain the code - and also to provide a computer to run them on. Bots need a computer to host their code and to lavish CPU cycles running them - reddit doesn't do this, it's up to the bots creator to host them somewhere. This generally isn't free and can eat up quite a lot of computer resources, depending on what the bot does.

Bad Bots
==================
Some bots are designed to try to behave statistically more like human users, or to deliberately try to slip under the radar?

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

.. figure:: /static/images/reddit-bots-jiffybot-example.png

   JiffyBot in action: it can also do multiple GIFs!

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

.. figure:: /static/images/reddit-bots-bitcointip-example.png

   BitcoinTip in action: Adam Savage gets tipped. Yes `that Adam Savage <http://en.wikipedia.org/wiki/Adam_Savage>`_.


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


Bots that just Show Up, without human intervention
----------------------------------------------------

These bots ceaselessly watch the endless, mighty cataract of text that is reddit and leap in whenever they sense patterns in the noise & spume that match their programming.

Metric System Converting bot
==============================
Purpose:
    TODO
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

YTScreenShotBot
===================
Purpose:
    TODO
Known Haunts:
    - `/u/YTScreenShotBot <http://www.reddit.com/user/YTScreenShotBot>`_


Serendipity
===============
Purpose:
    Cross posts a popular submission from a random subreddit to `/r/Serendipity <http://www.reddit.com/r/Serendipity/>`_ every few hours
Known Haunts:
    - `/u/Serendipity <http://www.reddit.com/user/Serendipity>`_
    - `/r/Serendipity <http://www.reddit.com/r/Serendipity/>`_
    - `Source code on GitHub <https://github.com/umbrae/Serendipity>`_

.. figure:: /static/images/reddit-bots-serendipity-example.png

   Slice of life, reddit style.

I discovered this bot & subreddit combo while writing this article and it's quickly become one of my favourites. `/r/Serendipity <http://www.reddit.com/r/Serendipity/>`_ is a meta-subreddit meant to broaden the perspective of its subscribers. It takes a popular entry from a random subreddit and posts it every few hours, so if you subscribe to it, you get a broad, random, serendipitous sprinkling of great content from across reddit on your front page -- often surprising, wonderful things that you would otherwise never have come across. As the sidebar says:

    If you want to increase your exposure to niche subreddits, or just your perspective on things on the web in general, serendipity might help you do that. But it might not. It's a bot, after all.

Other Interesting Bots
-------------------------

I don't have time to cover all the multitude of great bots on reddit - here's some others to checkout:

-

Ex-Bots?
-------------

Some interesting bots who seem to be ex-bots -- or maybe they're just resting:

- http://www.reddit.com/user/Meta_Bot
- http://www.reddit.com/user/canhekickit
- http://www.reddit.com/user/QualityEnforcer
- http://www.reddit.com/user/PoliticalBot & http://www.reddit.com/r/AnalyzingReddit
- http://www.reddit.com/user/Match-Thread-Bot
-

----------------

Know of any more interesting & fun reddit bots? Let me know in the comments...

----------------

Footnotes & References
--------------------------

.. [#stats] `About Reddit, including some mind boggling statistics <http://www.reddit.com/about/>`_.
.. [#bots] How many bots? Now one really knows. `How to create a Reddit bot <https://praw.readthedocs.org/en/latest/>`_. This being reddit, there's `a community <http://www.reddit.com/r/botwatch>`_ to keep an eye on them, too.
.. [#qkme_transcriber_faq] This is mostly quoted from the excellent qkme_transcriber bot's FAQ, `here <http://www.reddit.com/r/qkme_transcriber/comments/o426k/faq_for_the_qkme_transcriber_bot/>`_.
.. [#circlejerk] `/r/circlejerk <http://www.reddit.com/r/circlejerk/top/>`_ is a subreddit dedicated entirely to reddit satire. It's full of parodies of 'karma whoring' posts and parodies of endless pun threads. The thought that they have rigorous standards and actually kick people out for breaking them is almost funny in itself.