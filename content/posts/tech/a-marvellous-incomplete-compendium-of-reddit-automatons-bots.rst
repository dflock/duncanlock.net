:title: A Marvellous & Incomplete Compendium of reddit Automatons & Bots
:slug: a-marvellous-incomplete-compendium-of-reddit-automatons-bots
:date: 2013-06-19 19:48:54
:tags: reddit, bots, web
:meta_description: reddit had 71.4m visitors last month, with over 2.3m people logged in. I say people - but it turns out that not all of the denizens of reddit are human. There are also bots. Lots and lots of bots...
:thumbnail: /static/images/posts/a-marvellous-incomplete-compendium-of-reddit-automatons-bots/reddit-bots-diagram.png
:schema: Article

.. contents:: Contents:

.. figure:: /static/images/posts/a-marvellous-incomplete-compendium-of-reddit-automatons-bots/reddit-bots-diagram.png

    How much does a a software bot weigh, anyway?

    Heavily modified & adapted from the original public domain robot on `openclipart, posted by johnny_automatic <http://openclipart.org/detail/1654/robot-by-johnny_automatic>`_.

reddit, the insanely popular internet community, had 71,435,935 unique visitors last month, with over 2,360,783 people logged in [#stats]_.

I say people - but it turns out that not all of the denizens of reddit are human. There are also bots. Lots and lots of bots. How many? No-one really knows. [#bots]_

This is an interesting and somewhat shadowy facet of the otherwise very public reddit community, so I thought I'd take a closer look...

What *is* a reddit bot?
---------------------------

A reddit bot is no different from any other user, as far as reddit is concerned. The only difference is that rather than a human logging in to upvote cat pictures and post comments, this account is used by an automated computer script.

reddit has a captcha system to help prevent automated signups - so the bot's human creator will need to create a new user account for the bot to use, then program the username and password into the bot, so it can use that account - just like a human would.

In the same way that computers can run scripts to automatically check weather data and `send you an email if you should take an umbrella with you today <https://ifttt.com/recipes/search?q=weather>`_, a computer can run scripts to automatically check reddit for certain activity - and post comments if certain conditions are met. [#qkme_transcriber_faq]_ A reddit bot does this by doing what your web browser does behind the scenes when you use websites - it makes requests and sends things to the reddit servers.

reddit also has an :abbr:`API (Application Programming Interface)` [#api]_ which makes it easier for automated external services (including bots) to talk to reddit. This allows bots & scrapers to do things in bulk, like "Show me all the new posts in the last hour" -- they can then go away, analyse this information and then take actions based on it.

It's a Hard Bot Life
---------------------------

A major problem for any internet activity at scale is 'spam', or similar unwanted activity, in some form or other.

reddit has scale coming out of it's ears, so needs aggressive, pervasive and rapid automated spam control algorithms - combined with extensive human flagging and moderation - just to survive.

These mechanisms come down on bots particularly hard, to prevent the place being overrun by an army of implacable text hurling machines, typing & posting at the speed of light.

This is a `really nice /r/InternetAmA thread discussing the retirement of TicTacToeBot <http://www.reddit.com/r/InternetAMA/comments/1gescq/i_am_tictactoebot_i_derail_threads_and_i_am/>`_, which did exactly what you'd expect:

.. figure:: /static/images/posts/a-marvellous-incomplete-compendium-of-reddit-automatons-bots/reddit-bots-tictactoebot-example.png

   The only winning move is not to play.

Some quotes from TicTacToeBots developer:

    Q: Your account has only existed for 6 days. How have you already been banned from the subreddits?

    A: No clue. Every day I am banned from subreddits. I woke up today, looked at the mail. Banned from circlejerk, cats, and skyrim... Those aren't even default subs. I had to sub to new channels to be any active as a bot.

    Q: You actually got banned from circlejerk [#circlejerk]_? For derailing threads?!?

    A: Yes

TicTacToeBot got shot down for derailing threads - i.e. for being disruptive. It was `intentionally designed to randomly pop up and challenge people <http://www.reddit.com/r/todayilearned/comments/1fzgle/til_that_110_people_once_tied_for_second_prize_in/cafg3xj?context=2>`_ to a game - whimsical and fun, but also an uninvited disruption - albeit a harmless good natured one.

So unless they're careful, disruptive bots tend to have a fairly short life on reddit, quickly being hunted down and blocked by reddit's immune system -- even whimsical and seemingly harmless bots, like TicTacToeBot.

More circumspect bots, like JiffyBot_, CHART_BOT_ or `Serendipity <#serendipitybot-r-serendipity>`_ - either completely or largely confine themselves to their own subreddits, only turning up elsewhere when invited. This generally means that they'll be left alone to do their thing, because they're not interfering with anyone else. They're also completely upfront about what they do and provide a useful service to the reddit community.

Workin' on a Bot Farm
=======================
Bots also take resources to run - both to initially create & then to maintain the code - but mainly to provide a computer to run them on [#bot_hosting]_. Bots need a computer to host their code and to lavish CPU cycles running them - reddit doesn't do this, it's up to the bots creator to host them somewhere. This generally isn't free and can eat up quite a lot of computer resources, depending on what the bot does. Bots can get shut down by their creators for lack of resources - time or money - or lack of interest. Pretty much all reddit bots are just created for fun, for learning, or both - sometimes the creator just wants to move on to another project.

Bad Bots, Sad Bots
==================
Some bots are designed to try to behave statistically more like human users [#impersonate]_, or to deliberately try to slip under the radar. Some bots are designed to boost the reddit karma [#what_is_karma]_ of their masters by pretending to be regular users and up-voting their masters posts and down-voting those who disagree with them. Some bots are designed to start flame wars and generally be mean, virtually.

This is pretty sad and pathetic... so I'm going to ignore them.

So, without further ado, here's the compendium, split into `Bots that you can Summon with an Incantation`_  and `Bots that just Show Up, without human intervention`_.

Bots that you can Summon with an Incantation
----------------------------------------------

These bots listen out for their summoning incantation to be posted somewhere on reddit, then turn up and do their thing in response:

JiffyBot
============

Purpose:
    Makes animated GIFs out of YouTube links
Creators:
    - `/u/DrKabob <http://www.reddit.com/user/DrKabob>`_
    - `/u/GoogaNautGod <http://www.reddit.com/user/GoogaNautGod>`
Home Base:
    - `/u/JiffyBot <http://www.reddit.com/user/JiffyBot>`_
    - `/r/JiffyBot <http://www.reddit.com/r/JiffyBot>`_
    - `JiffyBot Documentation <http://www.reddit.com/r/JiffyBot/comments/1fp9qh/how_do_i_summon_jiffy_bot/>`_
    - `JiffyBot in Action <http://www.reddit.com/r/JiffyBot/comments/1fvrsq/the_official_make_your_own_gif_verison_sfw/>`_
    - `JiffyBot FAQ <http://www.reddit.com/r/JiffyBot/comments/1fwo0y/jiffy_bot_feedback_and_questions_faq/>`_
    - `JiffyBot Source Code <https://github.com/l1am9111/JiffyBot>`_ - NB this is an orphaned fork of the original GitHub code repository; I'm currently trying to find out what happened to the original.
Current Karma:
    - 1 link karma
    - 30,173 comment karma
A Redditor for:
    16 days
Active Subreddits:
    +--------------------+---------------------+------------------+
    | Subreddit          | Submissions (karma) | Comments (karma) |
    +====================+=====================+==================+
    | /r/JiffyBot        | 0                   | 333 (391)        |
    +--------------------+---------------------+------------------+
    | /r/cringe          | 0                   | 92 (614)         |
    +--------------------+---------------------+------------------+
    | /r/tf2             | 0                   | 45 (315)         |
    +--------------------+---------------------+------------------+
    | /r/gaming          | 0                   | 40 (418)         |
    +--------------------+---------------------+------------------+
    | /r/youtubehaiku    | 0                   | 36 (173)         |
    +--------------------+---------------------+------------------+
    | /r/leagueoflegends | 0                   | 27 (73)          |
    +--------------------+---------------------+------------------+
    | /r/funny           | 0                   | 27 (434)         |
    +--------------------+---------------------+------------------+
    | /r/YouShouldKnow   | 0                   | 27 (28)          |
    +--------------------+---------------------+------------------+
    | /r/SeeThisShit     | 0                   | 22 (22)          |
    +--------------------+---------------------+------------------+
    | /r/DotA2           | 0                   | 17 (35)          |
    +--------------------+---------------------+------------------+
    | /r/starcraft       | 0                   | 15 (96)          |
    +--------------------+---------------------+------------------+
    | /r/hockey          | 0                   | 12 (7)           |
    +--------------------+---------------------+------------------+
    | /r/atheism         | 0                   | 10 (221)         |
    +--------------------+---------------------+------------------+
    | Plus 111 more...                                            |
    +--------------------+---------------------+------------------+

Summon by posting a link to a YouTube video, then writing ``Jiffy!`` followed by a start time and end time, in either of these forms:

.. code-block:: python

    Jiffy! 0:07-0:12
    /u/JiffyBot 0:00-0:15

The second form is apparently more reliable.

The bot will respond by replying to your comment, with a comment of it's own, containing an `imgur.com <http://imgur.com/>`_ link to an animated GIF of that video, for the time period you specified. This is great for people on mobile devices - animated GIFs load *much* quicker than YouTube.

.. figure:: /static/images/posts/a-marvellous-incomplete-compendium-of-reddit-automatons-bots/reddit-bots-jiffybot-example.png

   JiffyBot in action: it can also do multiple GIFs!

BitcoinTip
==============

Purpose:
    The bitcointip bot allows redditors to tip each other 'real' money, just by leaving a reddit comment or message.
Human Creator:
    - `/u/NerdfighterSean <http://www.reddit.com/user/NerdfighterSean>`_
Home Base:
    - `/u/bitcointip <http://www.reddit.com/user/bitcointip>`_
    - `/r/bitcointip <http://www.reddit.com/r/bitcointip>`_
    - `BitcoinTip Documentation <http://www.reddit.com/r/bitcointip/comments/13iykn/_bitcointipdocumentation/>`_
    - `BitcoinTip Quickstart Guide <http://imgur.com/CwDYZqW>`_
    - `Source Code <https://github.com/NerdfighterSean/bitcointip>`_ - rather out of date.
Current Karma:
    - 9 link karma
    - 11,906 comment karma
A Redditor for:
    1 year
Source Code:
    https://github.com/NerdfighterSean/bitcointip
Active Subreddits:
    +---------------------+---------------------+------------------+
    | Subreddit           | Submissions (karma) | Comments (karma) |
    +=====================+=====================+==================+
    | /r/Bitcoin          | 0                   | 368 (813)        |
    +---------------------+---------------------+------------------+
    | /r/GirlsGoneBitcoin | 0                   | 51 (59)          |
    +---------------------+---------------------+------------------+
    | /r/worldnews        | 0                   | 36 (133)         |
    +---------------------+---------------------+------------------+
    | /r/IAmA             | 0                   | 30 (81)          |
    +---------------------+---------------------+------------------+
    | /r/AskReddit        | 0                   | 30 (88)          |
    +---------------------+---------------------+------------------+
    | /r/bitcointip       | 0                   | 29 (49)          |
    +---------------------+---------------------+------------------+
    | /r/pics             | 0                   | 20 (136)         |
    +---------------------+---------------------+------------------+
    | /r/technology       | 0                   | 13 (134)         |
    +---------------------+---------------------+------------------+
    | /r/AdviceAnimals    | 0                   | 12 (23)          |
    +---------------------+---------------------+------------------+
    | /r/investing        | 0                   | 11 (43)          |
    +---------------------+---------------------+------------------+
    | /r/gaming           | 0                   | 11 (241)         |
    +---------------------+---------------------+------------------+
    | /r/tf2              | 0                   | 10 (145)         |
    +---------------------+---------------------+------------------+
    | /r/starcraft        | 0                   | 10 (205)         |
    +---------------------+---------------------+------------------+
    | Plus 155 more...                                             |
    +---------------------+---------------------+------------------+


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

Allows you to tip people for useful or awesome comments, in a very natural and low friction way:

.. figure:: /static/images/posts/a-marvellous-incomplete-compendium-of-reddit-automatons-bots/reddit-bots-bitcointip-example.png

   BitcoinTip in action: Adam Savage gets tipped. Yes `that Adam Savage <http://en.wikipedia.org/wiki/Adam_Savage>`_.


CHART_BOT
=============

Purpose:
    Automatically generates and posts a chart of your posting history - or someone else's.
Home Base:
    - `/u/CHART_BOT <http://www.reddit.com/user/CHART_BOT>`_
    - `/r/CHART_BOT <http://www.reddit.com/r/CHART_BOT>`_
Active SubReddits:
    Overwhelmingly active in it's own subreddit, but has been known to pop-up elsewhere, for the lulz:

    +--------------------------------+---------------------+------------------+
    | Subreddit                      | Submissions (karma) | Comments (karma) |
    +================================+=====================+==================+
    | /r/CHART_BOT                   | 1 (2)               | 931 (1063)       |
    +--------------------------------+---------------------+------------------+
    | /r/WTF                         | 0                   | 19 (13)          |
    +--------------------------------+---------------------+------------------+
    | /r/wheredidthesodago           | 0                   | 14 (-14)         |
    +--------------------------------+---------------------+------------------+
    | /r/science                     | 0                   | 13 (13)          |
    +--------------------------------+---------------------+------------------+
    | /r/TheLastAirbender            | 0                   | 12 (20)          |
    +--------------------------------+---------------------+------------------+
    | Plus 11 more...                                                         |
    +--------------------------------+---------------------+------------------+

Current Karma:
    - 3 link karma
    - 5,686 comment karma
A Redditor for:
    8 months

Making a submission `to this subreddit <http://www.reddit.com/r/CHART_BOT>`_ will cause CHART_BOT to automatically generate and post a chart of your reddit posting history. You can also request charts of other reddit users by putting their username prefixed with an @ in the title of your submission. The charts look like this - `here's mine <http://www.reddit.com/r/CHART_BOT/comments/1gdpu9/chart_me_up_baby/>`_:

.. image:: /static/images/posts/a-marvellous-incomplete-compendium-of-reddit-automatons-bots/duncan-locks-chart-bot-chart-june-2013.png
    :alt: Screenshot of CHART_BOTS output for duncanlock, as of June 2013.

CHART_BOT also produces some graphs of activity which are quite interesting. Here are the 'Posts Over Time' ones for me (on the left) and chartbot (on the right). You can clearly see the characteristic posting pattern of humans (irregular) vs. bots (regular):

.. figure:: /static/images/posts/a-marvellous-incomplete-compendium-of-reddit-automatons-bots/reddit-bots-duncanlock-chartbot-postings-over-time-graph.png
    :alt: Two scatter plots of reddit postings, over time. Left one for human user duncanlock, right one for chart_bot.

    Fairly typical human reddit user (left) vs bot (right).

    Bot scripts are often run on a regular schedule - e.g. once an hour, every 10 minutes, etc... - which explains the regular patterns of activity.



Bots that just Show Up, without human intervention
----------------------------------------------------

These bots ceaselessly scan the endless, mighty cataract of text that is reddit and leap in whenever they sense patterns in the noise & spume that match their programming.

raddit-bot
===========
Purpose:
    Shares (most of) the data about the posts it sees being used on `radd.it <http://radd.it/>`_. Currently it's sharing a combination of data from youtube, soundcloud, vimeo, last.fm, IMDb, and amazon; only comments in subreddits it's been invited to.
Human Creator:
    - `/u/radd_it <http://www.reddit.com/user/radd_it>`_
Home Base:
    - `/u/raddit-bot <http://www.reddit.com/user/raddit-bot>`_
    - `/r/raddit-bot <http://www.reddit.com/r/radd_it>`_
    - `raddit-bot FAQ <http://www.reddit.com/r/radd_it/comments/1gxa85/who_is_uradditbot_and_why_is_it_commenting_here/>`_
Current Karma:
    - 1915 link karma
    - 376 comment karma
A Redditor for:
    1 month
Active Subreddits:
    +---------------------+---------------------+------------------+
    | Subreddit           | Submissions (karma) | Comments (karma) |
    +=====================+=====================+==================+
    | /r/listentothis     | 0                   | 765 (1109)       |
    +---------------------+---------------------+------------------+
    | /r/FullMoviesOnline | 352 (764)           | 213 (215)        |
    +---------------------+---------------------+------------------+
    | /r/listentonew      | 51 (55)             | 0                |
    +---------------------+---------------------+------------------+
    | /r/VBT              | 0                   | 1 (1)            |
    +---------------------+---------------------+------------------+
    | /r/Music            | 0                   | 1 (2)            |
    +---------------------+---------------------+------------------+

Raddit-bot is a helpful bot that posts information when you post a link to a piece of media that's been on `radd.it <http://radd.it/>`_. It's posts look like this, sharing a wealth of links and information about things that people have linked to:

.. image:: /static/images/posts/a-marvellous-incomplete-compendium-of-reddit-automatons-bots/reddit-bots-radditbot-example.png

Discovered this bot while browsing `/r/listentothis <http://www.reddit.com/r/listentothis>`_ - which in turn led me to discover `radd.it <http://radd.it/>`_; I'm currently trying to resist getting distracted by radd.it itself.

haiku_robot
=============
Purpose:
    Watches reddit for comments that would qualify as Haiku [#haiku_definition]_ and posts a reply, with the original text reformatted into 3 lines of 5, 7 & 5 syllables.
Home Base:
    - `/u/haiku_robot <http://www.reddit.com/u/haiku_robot>`_
    - `haiku_robot FAQ <http://www.reddit.com/r/IAmA/comments/1fr7c5/beep_boop_beep_boop_bopiama_haiku_robotask_me/>`_
Current Karma:
    - 1 link karma
    - 104,473 comment karma
A Redditor for:
    1 year
Active Subreddits:
    +----------------------+---------------------+------------------+
    | Subreddit            | Submissions (karma) | Comments (karma) |
    +======================+=====================+==================+
    | /r/funny             | 0                   | 284 (2580)       |
    +----------------------+---------------------+------------------+
    | /r/pics              | 0                   | 199 (1239)       |
    +----------------------+---------------------+------------------+
    | /r/AdviceAnimals     | 0                   | 126 (619)        |
    +----------------------+---------------------+------------------+
    | /r/gaming            | 0                   | 90 (501)         |
    +----------------------+---------------------+------------------+
    | /r/WTF               | 0                   | 56 (618)         |
    +----------------------+---------------------+------------------+
    | /r/todayilearned     | 0                   | 25 (115)         |
    +----------------------+---------------------+------------------+
    | /r/IAmA              | 1 (8)               | 23 (99)          |
    +----------------------+---------------------+------------------+
    | /r/gifs              | 0                   | 23 (164)         |
    +----------------------+---------------------+------------------+
    | /r/videos            | 0                   | 22 (77)          |
    +----------------------+---------------------+------------------+
    | /r/leagueoflegends   | 0                   | 15 (404)         |
    +----------------------+---------------------+------------------+
    | /r/mildlyinteresting | 0                   | 15 (28)          |
    +----------------------+---------------------+------------------+
    | /r/gonewild          | 0                   | 10 (116)         |
    +----------------------+---------------------+------------------+
    | /r/technology        | 0                   | 10 (13)          |
    +----------------------+---------------------+------------------+
    | Plus 45 more...      |                     |                  |
    +----------------------+---------------------+------------------+

This seems to be quite popular, with lots of very highly upvoted comments - like this one:

.. image:: /static/images/posts/a-marvellous-incomplete-compendium-of-reddit-automatons-bots/reddit-bots-haikubot-example.png



Metric System Converting bot
==============================
Purpose:
    When it sees a post using Imperial/US units, it replies with a conversion to their Metric equivalents.
Human Creator:
    - `/u/xwcg <http://www.reddit.com/user/xwcg>`_
Home Base:
    - `/u/MetricConversionBot <http://www.reddit.com/user/MetricConversionBot>`_
    - `/r/MetricConversionBot <http://www.reddit.com/r/MetricConversionBot>`_
    - `MetricConversionBot FAQ <http://www.reddit.com/r/MetricConversionBot/comments/1f53fw/faq/>`_
Current Karma:
    - 239 link karma
    - 26,779 comment karma
A Redditor for:
    27 days
Active Subreddits:
    +------------------+---------------------+------------------+
    | Subreddit        | Submissions (karma) | Comments (karma) |
    +==================+=====================+==================+
    | /r/AdviceAnimals | 1 (285)             | 538 (4160)       |
    +------------------+---------------------+------------------+
    | /r/pics          | 0                   | 94 (1878)        |
    +------------------+---------------------+------------------+
    | /r/todayilearned | 0                   | 68 (625)         |
    +------------------+---------------------+------------------+
    | /r/gaming        | 0                   | 63 (65)          |
    +------------------+---------------------+------------------+
    | /r/videos        | 0                   | 44 (493)         |
    +------------------+---------------------+------------------+
    | /r/gifs          | 0                   | 15 (258)         |
    +------------------+---------------------+------------------+
    | /r/politics      | 0                   | 15 (230)         |
    +------------------+---------------------+------------------+
    | /r/progresspics  | 0                   | 10 (92)          |
    +------------------+---------------------+------------------+
    | Plus 53 more...                                           |
    +------------------+---------------------+------------------+

MetricConversionBot will convert the following units to their metric equivalents:

- Pounds (lbs) to Kilograms
- Miles to Kilometers
- Miles per hour to Kilometers per Hour
- Foot/Feet to Meters
- Kelvin to Celsius
- Fahrenheit to Celsius
- inch to cm
- yard to meters
- (US) fl. oz. to ml
- ounces to grams

and it leaves comments that look like this:

.. image:: /static/images/posts/a-marvellous-incomplete-compendium-of-reddit-automatons-bots/reddit-bots-metricconversionbot-example.png

This bot is a (`more popular <http://www.reddit.com/r/TheoryOfReddit/comments/1fop0k/why_is_umetricmonversionmot_succeeding_while_usi/>`_) successor to the deceased `SI_BOT <http://www.reddit.com/user/si_bot>`_. Interestingly, MetricConversionBot has attracted it's own parody bots, `MetricConversionNot <http://www.reddit.com/user/MetricConversionNot>`_ - which randomly makes similar looking, but factually inaccurate parody comments (somewhat similar to the older, inactive parody bot `Lord_Longbottom <http://www.reddit.com/user/Lord-Longbottom>`_) and `UselessConversionBot <http://www.reddit.com/user/UselessConversionBot>`_:

.. image:: /static/images/posts/a-marvellous-incomplete-compendium-of-reddit-automatons-bots/reddit-bots-uselessconversionbot-example.png

Website Mirror bot
======================
Purpose:
    Mirrors websites that go down from the traffic surge, due to being posted on reddit.
Home Base:
    - `/u/Website_Mirror_Bot <http://www.reddit.com/user/Website_Mirror_Bot>`_
    - `/r/Website_Mirror_Bot <http://www.reddit.com/r/Website_Mirror_Bot>`_
Current Karma:
    - 1 link karma
    - 9,946 comment karma
A Redditor for:
    20 days
Active Subreddits:
    +--------------------+---------------------+------------------+
    | Subreddit          | Submissions (karma) | Comments (karma) |
    +====================+=====================+==================+
    | /r/todayilearned   | 0                   | 29 (6391)        |
    +--------------------+---------------------+------------------+
    | /r/politics        | 0                   | 17 (870)         |
    +--------------------+---------------------+------------------+
    | /r/worldnews       | 0                   | 15 (1021)        |
    +--------------------+---------------------+------------------+
    | /r/technology      | 0                   | 8 (203)          |
    +--------------------+---------------------+------------------+
    | /r/Bitcoin         | 0                   | 4 (25)           |
    +--------------------+---------------------+------------------+
    | /r/atheism         | 0                   | 4 (2299)         |
    +--------------------+---------------------+------------------+
    | /r/starcraft       | 0                   | 4 (50)           |
    +--------------------+---------------------+------------------+
    | /r/conspiracy      | 0                   | 4 (15)           |
    +--------------------+---------------------+------------------+
    | /r/leagueoflegends | 0                   | 3 (109)          |
    +--------------------+---------------------+------------------+
    | Plus 63 more...                                             |
    +--------------------+---------------------+------------------+

Takes a (generally very tall) `screenshot <http://i.imgur.com/MyiPyDE.jpg>`_ of the page that was linked to, puts it on imgur.com and posts a link in a comment:

.. image:: /static/images/posts/a-marvellous-incomplete-compendium-of-reddit-automatons-bots/reddit-bots-websitemirrorbot-example.png

tabledresser
==================
Purpose:
    Automatically generates a summary table from an `AmA thread <http://www.reddit.com/r/IAmA/>`_, showing all answered questions, along with their answers.
Human Creator:
    - `/u/Helpful_Table_Maker <http://www.reddit.com/user/Helpful_Table_Maker>`_
Home Base:
    - `/u/tabledresser <http://www.reddit.com/user/tabledresser>`_
    - `/r/tabled <http://www.reddit.com/r/tabled>`_
Current Karma:
    - 4 link karma
    - 8,857 comment karma
A Redditor for:
    1 year
Active Subreddits:
    +----------------+---------------------+------------------+
    | Subreddit      | Submissions (karma) | Comments (karma) |
    +================+=====================+==================+
    | /r/tabled      | 1000 (9253)         | 0                |
    +----------------+---------------------+------------------+
    | /r/IAmA        | 0                   | 970 (4377)       |
    +----------------+---------------------+------------------+
    | /r/InternetAMA | 0                   | 19 (62)          |
    +----------------+---------------------+------------------+
    | /r/tf2trade    | 0                   | 2 (4)            |
    +----------------+---------------------+------------------+
    | Plus 9 more...                                          |
    +----------------+---------------------+------------------+

It posts the first few rows in the actual AmA thread, with a link to the full table that it posts to `/r/tabled <http://www.reddit.com/r/tabled>`_. This provides a great way to quickly read a condensed summary of a complete AmA thread, `like this one <http://www.reddit.com/r/tabled/comments/1g9nja/table_iama_i_am_james_bamford_one_of_the/>`_. They look something like this:

.. image:: /static/images/posts/a-marvellous-incomplete-compendium-of-reddit-automatons-bots/reddit-bots-tabledresserbot-example.png

VideoLinkBot
=================
Purpose:
    Posts a summary of all video links in a discussion, kept up to date as the discussion grows.
Human Creator:
    - `/u/shaggorama <http://www.reddit.com/user/shaggorama>`_
Home Base:
    - `/u/VideoLinkBot <http://www.reddit.com/user/VideoLinkBot>`_
    - `/r/VideoLinkBot <http://www.reddit.com/r/VideoLinkBot/>`_
    - `VideoLinkBot FAQ <http://www.reddit.com/r/VideoLinkBot/wiki/faq>`__
Current Karma:
    - 25 link karma
    - 49,423 comment karma
A Redditor for:
    4 months
Source Code:
    https://github.com/dmarx/VideoLinkBot
Active Subreddits:
    +--------------------------+---------------------+------------------+
    | Subreddit                | Submissions (karma) | Comments (karma) |
    +==========================+=====================+==================+
    | /r/videos                | 0                   | 126 (343)        |
    +--------------------------+---------------------+------------------+
    | /r/gaming                | 0                   | 93 (167)         |
    +--------------------------+---------------------+------------------+
    | /r/hiphopheads           | 1 (0)               | 48 (123)         |
    +--------------------------+---------------------+------------------+
    | /r/leagueoflegends       | 0                   | 47 (118)         |
    +--------------------------+---------------------+------------------+
    | /r/todayilearned         | 0                   | 41 (69)          |
    +--------------------------+---------------------+------------------+
    | /r/movies                | 0                   | 23 (66)          |
    +--------------------------+---------------------+------------------+
    | /r/nfl                   | 0                   | 21 (86)          |
    +--------------------------+---------------------+------------------+
    | /r/nba                   | 0                   | 18 (32)          |
    +--------------------------+---------------------+------------------+
    | /r/politics              | 0                   | 18 (19)          |
    +--------------------------+---------------------+------------------+
    | /r/Random_Acts_Of_Amazon | 4 (98)              | 13 (21)          |
    +--------------------------+---------------------+------------------+
    | /r/WhereDoIStart         | 0                   | 16 (36)          |
    +--------------------------+---------------------+------------------+
    | /r/hockey                | 0                   | 15 (39)          |
    +--------------------------+---------------------+------------------+
    | /r/SquaredCircle         | 0                   | 15 (43)          |
    +--------------------------+---------------------+------------------+
    | /r/worldnews             | 0                   | 14 (27)          |
    +--------------------------+---------------------+------------------+
    | /r/IAmA                  | 0                   | 12 (263)         |
    +--------------------------+---------------------+------------------+
    | /r/CFB                   | 0                   | 12 (33)          |
    +--------------------------+---------------------+------------------+
    | /r/DotA2                 | 0                   | 12 (28)          |
    +--------------------------+---------------------+------------------+
    | /r/tipofmytongue         | 0                   | 12 (14)          |
    +--------------------------+---------------------+------------------+
    | /r/teenagers             | 0                   | 11 (21)          |
    +--------------------------+---------------------+------------------+
    | /r/VideoLinkBot          | 11 (17)             | 0                |
    +--------------------------+---------------------+------------------+
    | /r/atheism               | 0                   | 10 (11)          |
    +--------------------------+---------------------+------------------+
    | /r/Guitar                | 0                   | 9 (45)           |
    +--------------------------+---------------------+------------------+
    | Plus 244 more...                                                  |
    +--------------------------+---------------------+------------------+


VideoLinkBot scans for comments containing supported video links. When it finds one, it scans the discussion that comment belongs to for video links. It then posts the aggregate links it has found to a comment. If it's already visited this discussion, it will update its existing comment with whatever new links it finds. Video links are sorted by the score of the comment they came from.

If the bot doesn't see a certain number of links or all the links the bot sees were posted by the same user, the it won't post a comment. Also, if a discussion has too few or too many comments, this bot will leave it alone.

This provides a useful summary of a wide ranging discussion, in a similar way to tabledresser_ does for AmA threads. The comments it leaves look like this:

.. image:: /static/images/posts/a-marvellous-incomplete-compendium-of-reddit-automatons-bots/reddit-bots-videolinkbot-example.png
    :alt: Screenshot of a comment made by VideoLinkBot, showing the table of aggregated video links, with links to the Source Comment & Video Link, showing the score of each original comment.

meme_transcriber
===================

.. note::
    reddit `banned quickmeme.com <http://www.reddit.com/r/AdviceAnimals/comments/1gvnk4/quickmeme_is_banned_redditwide_more_inside/>`_ for vote rigging on 22nd June 2013, which `ended the career of this bots former incarnation, qkme_transcriber <http://www.reddit.com/r/qkme_transcriber/comments/1gvz3z/about_the_banning_of_quickmeme_links/>`_.

Purpose:
    Automatically finds links to meme pics (memegen.com) and provides a plain-text transcript of the content of that meme in a comment, so you don't have to click through to the meme site to get the 'joke'. Useful on mobile devices or if the meme site goes down.
Home Base:
    - `/u/meme_transcriber <http://www.reddit.com/user/meme_transcriber>`_
    - `/r/meme_transcriber <http://www.reddit.com/r/meme_transcriber/>`_
    - `/u/qkme_transcriber <http://www.reddit.com/user/qkme_transcriber>`_
    - `/r/qkme_transcriber <http://www.reddit.com/r/qkme_transcriber/>`_
    - `meme_transcriber FAQ <http://www.reddit.com/r/qkme_transcriber/comments/o426k/faq_for_the_qkme_transcriber_bot/>`_
Current Karma:
    - 286 link karma
    - 340,954 comment karma
A Redditor for:
    1 year

This bot tends to turn up in subreddits like `/r/AdviceAnimals/ <http://www.reddit.com/r/AdviceAnimals/>`_ and post comments that look like this:

.. image:: /static/images/posts/a-marvellous-incomplete-compendium-of-reddit-automatons-bots/reddit-bots-meme-transcriber-bot-example.png


YTScreenShotBot
===================
Purpose:
    Creates a screenshot montage of a YouTube video and posts a link to it, in reply to posts containing YouTube links.
Home Base:
    - `/u/YTScreenShotBot <http://www.reddit.com/user/YTScreenShotBot>`_
Active SubReddits:
    +-----------+---------------------+------------------+
    | Subreddit | Submissions (karma) | Comments (karma) |
    +===========+=====================+==================+
    | /r/videos | 0                   | 420 (2551)       |
    +-----------+---------------------+------------------+
    | /r/pics   | 0                   | 300 (3843)       |
    +-----------+---------------------+------------------+
    | /r/gaming | 0                   | 280 (302)        |
    +-----------+---------------------+------------------+
Current Karma:
    - 1 link karma
    - 15,475 comment karma
A Redditor for:
    25 days

This bot allows you to get a quick overview of the video, just by viewing an image - much quicker than watching the video, especially on mobile devices. This is what it's comments look like:

.. image:: /static/images/posts/a-marvellous-incomplete-compendium-of-reddit-automatons-bots/reddit-bots-ytscreenshotbot-example.png

and this is what the montage looks like:

.. image:: /static/images/posts/a-marvellous-incomplete-compendium-of-reddit-automatons-bots/M2XOpjb.jpg


JordanTheBrobot
===================
Purpose:
    A sophisticated Multi-purpose bot that patrols reddit looking for scams, misleading links, mistakes in markup, kindness, flash content, etc...
Home Base:
    - `/u/JordanTheBrobot <http://www.reddit.com/user/JordanTheBrobot>`_
    - `JordanTheBrobot HQ <http://jordanthebrobot.com/>`_
Current Karma:
    - 1 link karma
    - 36,879 comment karma
A Redditor for:
    8 months
Active Subreddits:
    +------------------+---------------------+------------------+
    | Subreddit        | Submissions (karma) | Comments (karma) |
    +==================+=====================+==================+
    | /r/gaming        | 0                   | 193 (4614)       |
    +------------------+---------------------+------------------+
    | /r/videos        | 0                   | 71 (1808)        |
    +------------------+---------------------+------------------+
    | /r/todayilearned | 0                   | 36 (221)         |
    +------------------+---------------------+------------------+
    | /r/gonewild      | 0                   | 32 (34)          |
    +------------------+---------------------+------------------+
    | /r/pics          | 0                   | 27 (277)         |
    +------------------+---------------------+------------------+
    | /r/AdviceAnimals | 0                   | 14 (212)         |
    +------------------+---------------------+------------------+
    | /r/ginger        | 0                   | 14 (33)          |
    +------------------+---------------------+------------------+
    | /r/Bitcoin       | 0                   | 13 (80)          |
    +------------------+---------------------+------------------+
    | /r/worldnews     | 0                   | 13 (68)          |
    +------------------+---------------------+------------------+
    | /r/movies        | 0                   | 12 (49)          |
    +------------------+---------------------+------------------+
    | /r/brobot        | 5 (36)              | 3 (3)            |
    +------------------+---------------------+------------------+
    | Plus 360 more...                                          |
    +------------------+---------------------+------------------+

This bots most user visible function is to detect when people have got the markdown syntax for links the wrong way round (a very common mistake), and if they don't correct it themselves within a few minutes, leave a reply with the corrected links:

.. image:: /static/images/posts/a-marvellous-incomplete-compendium-of-reddit-automatons-bots/reddit-bots-jordanthebrobot-example.png

It also detects 'spam/affiliate marketing' links and leaves a reply warning people:

    **Spam Link**

    The comment above contains a link to a spam site, click with caution, your clicks will earn a spammer money and give them motivation to continue.

This bot also has `moderator functionality <http://jordanthebrobot.com/moderators>`_, if you add it as a moderator of a subreddit, it will automatically:

- Follows all links posted to all subreddits to identify dangerous redirect chains
- Scans comments/submissions/redirect chains for spam domains
- Detects and warns users of mismatched domains in reddit link markup IE: [http://test.com](http://not-really-test.com)
- Detects and waits 6 minutes to post a fix of mistakes in reddit link markup (for ease of clicking)
- Warns users of unapparent links to flash content

It also upvotes the original commenter if it corrects you links and upvotes you if you thank it - which might help it's popularity. It also has a real time `dashboard <http://jordanthebrobot.com/>`_ which lets you see what it's up to.

SerendipityBot & /r/Serendipity
================================
Purpose:
    Cross posts a popular submission from a random subreddit to `/r/Serendipity <http://www.reddit.com/r/Serendipity/>`_ every few hours
Home Base:
    - `/u/serendipitybot <http://www.reddit.com/user/serendipitybot>`_
    - `/r/Serendipity <http://www.reddit.com/r/Serendipity/>`_
Current Karma:
    - 37,027 link karma
    - 2,641 comment karma
A Redditor for:
    2 years
Source Code:
    https://github.com/umbrae/Serendipity

.. figure:: /static/images/posts/a-marvellous-incomplete-compendium-of-reddit-automatons-bots/reddit-bots-serendipity-example.png

   Slice of life, reddit style.

I discovered this bot & subreddit combo while writing this article and it's quickly become one of my favourites. `/r/Serendipity <http://www.reddit.com/r/Serendipity/>`_ is a meta-subreddit meant to broaden the perspective of its subscribers. It chooses a popular post from a completely random subreddit and posts it every few hours, so if you subscribe to it, you get a broad, random, serendipitous sprinkling of great content from across reddit on your front page -- often surprising, wonderful things that you would otherwise never have come across. As the sidebar says:

    If you want to increase your exposure to niche subreddits, or just your perspective on things on the web in general, serendipity might help you do that. But it might not. It's a bot, after all.

**NB**: Occasionally, just by chance, a random post might be :abbr:`NSFW (Not Safe for Work)` or :abbr:`NSFL (Not Safe for Life - i.e. ugh, wish I could un-see.)`, but not very often. I asked the bots creator, `/u/umbrae <http://www.reddit.com/user/umbrae>`_, if it did any filtering - this is what he said:

.. epigraph::

   It's actually a bit complicated: It does technically filter out NSFW subreddits, but does not necessarily filter out NSFW posts from subreddits that are not marked NSFW. So you'll occasionally get a NSFW post here and there. There are also a few subs that have asked to be opted out for privacy /audience concerns.

   -- `/u/umbrae <http://www.reddit.com/user/umbrae>`_, in `this comment <http://www.reddit.com/r/explainlikeimfive/comments/1icm90/eli5_how_do_bots_on_reddit_work_how_are_they/cb3l4av>`_

Other Interesting Bots
-------------------------

I don't have time to cover all the multitude of great bots on reddit - here's some other useful or fun ones to checkout:

- `SmileBot <http://www.reddit.com/user/SmileBot>`_
- `DollarSignBot <http://www.reddit.com/user/DollarSignBot>`_
- `F1-Bot <http://www.reddit.com/user/F1-Bot>`_
- `RideItBot <http://www.reddit.com/user/smidsy_bot>`_
- `SimilarImage <http://www.reddit.com/user/SimilarImage>`_
- `original-finder <http://www.reddit.com/user/original-finder>`_
- `Australian_Translate <http://www.reddit.com/user/Australian_Translate>`_ and his Arch Nemesis: `FIXES_YOUR_COMMENT <http://www.reddit.com/user/FIXES_YOUR_COMMENT>`_
- `RepostConspiracyBot <http://www.reddit.com/user/RepostConspiracyBot>`_
- `CaptionBot <http://www.reddit.com/user/CaptionBot>`_

Another whole *category* of bots, that I didn't have time to go into, are Moderator Bots - designed to assist the human moderators of reddit with their ceaseless work, by automating some of the mechanical stuff:

- `AutoModeratorBot <http://www.reddit.com/user/automoderator>`_ - very widely used now & also open source: `more information here <https://github.com/Deimos/AutoModerator/wiki/Features>`_.
- `moderator-bot <http://www.reddit.com/user/moderator-bot>`_
- `atheismbot <http://www.reddit.com/r/atheismbot>`_ & `atheismbot FAQ <http://reddit.com/r/atheismbot/wiki/faq>`_
- `DeltaBot <http://www.reddit.com/u/DeltaBot>`_ is part of the bot moderation team at `/r/changemyview <http://www.reddit.com/r/changemyview/>`_. It adds a special feature to the subreddit that allows users to awards deltas (∆) to each other.

Ex-Bots?
-------------

Some interesting bots who seem to be ex-bots -- or maybe they're just resting:

- `Meta_Bot <http://www.reddit.com/user/Meta_Bot>`_
- `canhekickit <http://www.reddit.com/user/canhekickit>`_
- `QualityEnforcer <http://www.reddit.com/user/QualityEnforcer>`_
- `PoliticalBot <http://www.reddit.com/user/PoliticalBot>`_ & `AnalyzingReddit <http://www.reddit.com/r/AnalyzingReddit>`_
- `Match-Thread-Bot <http://www.reddit.com/user/Match-Thread-Bot>`_
- `LinkFixerBot <http://www.reddit.com/user/linkfixerbot>`_
- `tweet_poster <http://www.reddit.com/user/tweet_poster>`_
- `Karmangler <http://www.reddit.com/user/Karmangler>`_
- `autotldr <http://www.reddit.com/user/autotldr>`_
- `CONGRATS_GUY <http://www.reddit.com/user/CONGRATS_GUY>`_
- `qkme_transcriber <http://www.reddit.com/r/qkme_transcriber/comments/1gvz3z/about_the_banning_of_quickmeme_links/>`_

----------------

Know of any more interesting & fun reddit bots? Let me know in the comments...

----------------

Footnotes & References
--------------------------

.. [#stats] `About reddit, including some mind boggling statistics <http://www.reddit.com/about/>`_.
.. [#bots] How many bots? No one really knows. `How to create a reddit bot <https://praw.readthedocs.org/en/latest/>`_. This being reddit, there's `a community <http://www.reddit.com/r/botwatch>`_ to keep an eye on them, too - and `/r/TheoryOfReddit <http://www.reddit.com/r/TheoryOfReddit/>`_ do `sometimes <http://www.reddit.com/r/TheoryOfReddit/comments/187n3n/reddit_has_bots_but_what_kinds_of_bots_are_there/>`_ `discuss <http://www.reddit.com/r/TheoryOfReddit/comments/1586yk/should_reddit_regulate_bots/>`_ bots. Well, `actually <http://www.reddit.com/r/TheoryOfReddit/comments/m5t1s/a_worrying_trend_for_reddits_bots/>`_ they `talk <http://www.reddit.com/r/IAmA/comments/kglw8/we_are_the_creators_of_the_automated_bots_on/>`_ `about <http://www.reddit.com/r/TheoryOfReddit/comments/k7xjw/lets_talk_about_bots/>`_ bots `quite a lot <http://www.reddit.com/r/TheoryOfReddit/search?q=bot&restrict_sr=on>`_.
.. [#qkme_transcriber_faq] This is mostly quoted from the excellent qkme_transcriber bot's FAQ, `here <http://www.reddit.com/r/qkme_transcriber/comments/o426k/faq_for_the_qkme_transcriber_bot/>`_.
.. [#api] **API**: An agreed way for one piece of software to talk to another. Often consists of functions you can call with parameters, that return different peices of information - or perform different actions - depending on the value of the parameters. In the case of websites, the functions map to URL's - pages that you can request, with the parameters on the end of the URL. **Why does reddit have an API?** Well, people would find a way to get the same information somehow - often by brute force (acting like a very fast human making lots of requests) - which puts more strain on reddit's servers than just giving the data out in one go, on request - it also means that they get to set the rules when they make the API.
.. [#circlejerk] `/r/circlejerk <http://www.reddit.com/r/circlejerk/top/>`_ is a subreddit dedicated entirely to reddit satire. It's full of 'parodies' of 'karma whoring' posts and 'parodies' of endless pun threads. The thought that they have rigorous standards and actually kick people out for breaking them is almost funny in itself.
.. [#bot_hosting] `/r/redditdev/ thread: Where do you all host your python-based bots? <http://www.reddit.com/r/redditdev/comments/1ixqu0/praw_where_do_you_all_host_your_pythonbased_bots/>`_ - turns out YTScreenhostBot is hosted on an old laptop.
.. [#impersonate] `How easily could a computer program emulate the average reddit commenter? <http://www.reddit.com/r/TheoryOfReddit/comments/tiqqg/how_easily_could_a_computer_program_emulate_the/>`_
.. [#what_is_karma] Internet Points! reddit has a system called `Karma <http://www.reddit.com/wiki/faq#wiki_what_is_that_number_next_to_usernames.3F_and_what_is_karma.3F>`_ : "The number next to a username is called that user's "karma." It reflects how much good the user has done for the reddit community. The best way to gain karma is to submit links that other people like and vote for."
.. [#haiku_definition] `Haiku <http://en.wikipedia.org/wiki/Haiku>`_: In English, Haiku are traditionally three line verses, each line having 5, 7 & 5 syllables respectively.