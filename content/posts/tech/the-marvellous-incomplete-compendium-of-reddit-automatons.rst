:title: The Marvellous & Incomplete Compendium of Reddit Automatons
:slug: the-marvellous-incomplete-compendium-of-reddit-automatons
:date: 2013-06-19 19:48:54
:tags: reddit, bots
:meta_description: Reddit had 71.4m visitors last month, with over 2.3m people logged in. I say people - but it turns out that not all of the denizens of Reddit are human. There are also bots. Lots and lots of bots...
:thumbnail: /static/images/reddit-bots-diagram.png

.. figure:: /static/images/reddit-bots-diagram.png

    How much does a a software bot weigh, anyway?

    Heavily modified & adapted from the original public domain robot on `openclipart, posted by johnny_automatic <http://openclipart.org/detail/1654/robot-by-johnny_automatic>`_.

Reddit, the insanely popular internet community, had 71,435,935 unique visitors last month, with over 2,360,783 people logged in [#stats]_.

I say people - but it turns out that not all of the denizens of Reddit are human. There are also bots. Lots and lots of bots. How many? No-one really knows. [#bots]_

This is an interesting and somewhat shadowy facet of the otherwise very public reddit community, so I thought I'd take a closer look...

What *is* a reddit bot?
---------------------------

A reddit bot is no different from any other user, as far as reddit is concerned. The only difference is that rather than a human logging in to upvote cat pictures and post comments, this account is used by an automated computer script.

In the same way that computers can run scripts to automatically check weather data and `send you an email if you should take an umbrella with you today <https://ifttt.com/recipes/search?q=weather>`_, a computer can run scripts to automatically check reddit for certain activity - and post comments if certain conditions are met. [#qkme_transcriber_faq]_

It's a Hard Bot Life
---------------------------

A major problem for any internet activity at scale is 'spam', or similar unwanted activity, in some form or other.

Reddit has scale coming out of it's ears, so needs aggressive, pervasive and rapid automated spam control algorithms - combined with extensive human flagging and moderation - just to survive.

These mechanisms come down on bots particularly hard, to prevent the place being overrun by an army of implacable text hurling machines, typing & posting at the speed of light.

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

More circumspect bots, like JiffyBot_, CHART_BOT_ or `Serendipity <#serendipitybot-r-serendipity>`_ - either completely or largely confine themselves to their own subreddits, only turning up elsewhere when invited. This generally means that they'll be left alone to do their thing, because they're not interfering with anyone else. They're also completely upfront about what they do and provide a useful service to the reddit community.

Workin' on a Bot Farm
=======================
Bots also take resources to run - both to initially create & then to maintain the code - but mainly to provide a computer to run them on. Bots need a computer to host their code and to lavish CPU cycles running them - reddit doesn't do this, it's up to the bots creator to host them somewhere. This generally isn't free and can eat up quite a lot of computer resources, depending on what the bot does. Bots can get shut down by their creators for lack of resources - time or money - or lack of interest. Pretty much all reddit bots are just created for fun, for learning, or both - sometimes the creator just wants to move on to another project.

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
Home Base:
    - `/u/JiffyBot <http://www.reddit.com/user/JiffyBot>`_
    - `/r/JiffyBot <http://www.reddit.com/r/JiffyBot>`_
    - `JiffyBot Documentation <http://www.reddit.com/r/JiffyBot/comments/1fp9qh/how_do_i_summon_jiffy_bot/>`_
    - `JiffyBot in Action <http://www.reddit.com/r/JiffyBot/comments/1fvrsq/the_official_make_your_own_gif_verison_sfw/>`_
Current Karma:
    - 1 link karma
    - 30,173 comment karma
A Redditor for:
    16 days

Summon by posting a link to a YouTube video, then writing ``Jiffy!`` followed by a start time and end time, in either of these forms:

.. code-block:: python

    Jiffy! 0:07-0:12
    /u/JiffyBot 0:00-0:15

The bot will respond by replying to your comment, with a comment of it's own, containing an `imgur.com <http://imgur.com/>`_ link to an animated GIF of that video, for the time period you specified. This is great for people on mobile devices - animated GIFs load *much* quicker than YouTube.

.. figure:: /static/images/reddit-bots-jiffybot-example.png

   JiffyBot in action: it can also do multiple GIFs!

BitcoinTip
==============

Purpose:
    The bitcointip bot allows redditors to tip each other 'real' money, just by leaving a reddit comment or message.
Home Base:
    - `/u/bitcointip <http://www.reddit.com/user/bitcointip>`_
    - `/r/bitcointip <http://www.reddit.com/r/bitcointip>`_
    - `BitcoinTip Documentation <http://www.reddit.com/r/bitcointip/comments/13iykn/_bitcointipdocumentation/>`_
Current Karma:
    - 9 link karma
    - 11,906 comment karma
A Redditor for:
    1 year
Source Code:
    https://github.com/NerdfighterSean/bitcointip

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

.. figure:: /static/images/reddit-bots-bitcointip-example.png

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
    | ...lots more with 1 comment... | 0                   | 1                |
    +--------------------------------+---------------------+------------------+

Current Karma:
    - 3 link karma
    - 5,686 comment karma
A Redditor for:
    8 months

Making a submission `to this subreddit <http://www.reddit.com/r/CHART_BOT>`_ will cause CHART_BOT to automatically generate and post a chart of your reddit posting history. You can also request charts of other reddit users by putting their username prefixed with an @ in the title of your submission. The charts look like this - `here's mine <http://www.reddit.com/r/CHART_BOT/comments/1gdpu9/chart_me_up_baby/>`_:

.. image:: /static/images/duncan-locks-chart-bot-chart-june-2013.png
    :alt: Screenshot of CHART_BOTS output for duncanlock, as of June 2013.

CHART_BOT also produces some graphs of activity which are quite interesting. Here are the 'Posts Over Time' ones for me (on the left) and chartbot (on the right). You can clearly see the characteristic posting pattern of humans (irregular) vs. bots (regular):

.. figure:: /static/images/reddit-bots-duncanlock-chartbot-postings-over-time-graph.png
    :alt: Two scatter plots of reddit postings, over time. Left one for human user duncanlock, right one for chart_bot.

    Fairly typical human reddit user (left) vs bot (right).

    Bot scripts are often run on a regular schedule - e.g. once an hour, every 10 minutes - which explains the regular patterns of activity.



Bots that just Show Up, without human intervention
----------------------------------------------------

These bots ceaselessly scan the endless, mighty cataract of text that is reddit and leap in whenever they sense patterns in the noise & spume that match their programming.

Metric System Converting bot
==============================
Purpose:
    When it sees a post using Imperial/US units, it replies with a conversion to their Metric equivalents.
Home Base:
    - `/u/MetricConversionBot <http://www.reddit.com/user/MetricConversionBot>`_
    - `/r/MetricConversionBot <http://www.reddit.com/r/MetricConversionBot>`_
    - `FAQ <http://www.reddit.com/r/MetricConversionBot/comments/1f53fw/faq/>`_
Current Karma:
    - 239 link karma
    - 26,779 comment karma
A Redditor for:
    27 days

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

.. image:: /static/images/reddit-bots-metricconversionbot-example.png

This bot is a (`more successful <http://www.reddit.com/r/TheoryOfReddit/comments/1fop0k/why_is_umetricmonversionmot_succeeding_while_usi/>`_) successor to the deceased `SI_BOT <http://www.reddit.com/user/si_bot>`_. Interestingly, MetricConversionBot has attracted it's own parody bot, called `MetricConversionNot <http://www.reddit.com/user/MetricConversionNot>`_ - which randomly makes similar looking, but factually inaccurate parody comments; somewhat similar to the older, inactive parody bot `Lord_Longbottom <http://www.reddit.com/user/Lord-Longbottom>`_.

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

Takes a (generally very tall) `screenshot <http://i.imgur.com/MyiPyDE.jpg>`_ of the page that was linked to, puts it on imgur.com and posts a link in a comment:

.. image:: /static/images/reddit-bots-websitemirrorbot-example.png

tabledresser
==================
Purpose:
    Automatically generates a summary table from an `AmA thread <http://www.reddit.com/r/IAmA/>`_, showing all answered questions, along with their answers.
Home Base:
    - `/u/tabledresser <http://www.reddit.com/user/tabledresser>`_
    - `/r/tabled <http://www.reddit.com/r/tabled>`_
Current Karma:
    - 4 link karma
    - 8,857 comment karma
A Redditor for:
    1 year

It posts the first few rows in the actual AmA thread, with a link to the full table that it posts to `/r/tabled <http://www.reddit.com/r/tabled>`_. This provides a great way to quickly read a condensed summary of a complete AmA thread, `like this one <http://www.reddit.com/r/tabled/comments/1g9nja/table_iama_i_am_james_bamford_one_of_the/>`_. They look something like this:

.. image:: /static/images/reddit-bots-tabledresserbot-example.png

VideoLinkBot
=================
Purpose:
    Posts a summary of all video links in a discussion, kept up to date as the discussion grows.
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

VideoLinkBot scans for comments containing supported video links. When it finds one, it scans the discussion that comment belongs to for video links. It then posts the aggregate links it has found to a comment. If it's already visited this discussion, it will update its existing comment with whatever new links it finds. Video links are sorted by the score of the comment they came from.

If the bot doesn't see a certain number of links or all the links the bot sees were posted by the same user, the it won't post a comment. Also, if a discussion has too few or too many comments, this bot will leave it alone.

This provides a useful summary of a wide ranging discussion, in a similar way to tabledresser_ does for AmA threads. The comments it leaves look like this:

.. image:: /static/images/reddit-bots-videolinkbot-example.png
    :alt: Screenshot of a comment made by VideoLinkBot, showing the table of aggregated video links, with links to the Source Comment & Video Link, showing the score of each original comment.

qkme_transcriber
===================
Purpose:
    Automatically finds links to Quickmeme meme pics (quickmeme.com or qkme.me) and provides a plain-text transcript of the content of that meme in a comment, so you don't have to click through to the Quickmeme site to get the 'joke'. Useful on mobile devices.
Home Base:
    - `/u/qkme_transcriber <http://www.reddit.com/user/qkme_transcriber>`_
    - `/r/qkme_transcriber <http://www.reddit.com/r/qkme_transcriber/>`_
    - `qkme_transcriber FAQ <http://www.reddit.com/r/qkme_transcriber/comments/o426k/faq_for_the_qkme_transcriber_bot/>`_
Current Karma:
    - 286 link karma
    - 340,954 comment karma
A Redditor for:
    1 year

This bot tends to turn up in subreddits like `/r/AdviceAnimals/ <http://www.reddit.com/r/AdviceAnimals/>`_ and post comments that look like this:

.. image:: /static/images/qkme-transcriber-bot-example.png

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

.. image:: /static/images/reddit-bots-ytscreenshotbot-example.png

and this is what the montage looks like:

.. image:: /static/images/M2XOpjb.jpg


JordanTheBrobot
===================
Purpose:
    Detects spam comments and fixes link syntax, Bro.
Home Base:
    - `/u/JordanTheBrobot <http://www.reddit.com/user/JordanTheBrobot>`_
Current Karma:
    - 1 link karma
    - 36,879 comment karma
A Redditor for:
    8 months

This bot detects when people have got the markdown syntax for links the wrong way round (a very common mistake), and leaves a reply with the corrected links:

.. image:: /static/images/reddit-bots-jordanthebrobot-example.png

It also detects 'spam/affiliate marketing' links and leaves a reply warning people:

    **Spam Link**

    The comment above contains a link to a spam site, click with caution, your clicks will earn a spammer money and give them motivation to continue.

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

.. figure:: /static/images/reddit-bots-serendipity-example.png

   Slice of life, reddit style.

I discovered this bot & subreddit combo while writing this article and it's quickly become one of my favourites. `/r/Serendipity <http://www.reddit.com/r/Serendipity/>`_ is a meta-subreddit meant to broaden the perspective of its subscribers. It chooses a popular post from a completely random subreddit and posts it every few hours, so if you subscribe to it, you get a broad, random, serendipitous sprinkling of great content from across reddit on your front page -- often surprising, wonderful things that you would otherwise never have come across. As the sidebar says:

    If you want to increase your exposure to niche subreddits, or just your perspective on things on the web in general, serendipity might help you do that. But it might not. It's a bot, after all.

**NB**: It doesn't seem to filter much, so occasionally, just by chance, the random post might be :abbr:`NSFW (Not Safe for Work)` or :abbr:`NSFL (Not Safe for Life - i.e. ugh, wish I could un-see.)`, but not very often.

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

Another whole *category* of bots, that I didn't have time to go into, are Moderator Bots - designed to assist the human moderators of Reddit with their ceaseless work, by automating some of the mechanical stuff:

- `AutoModeratorBot <http://www.reddit.com/user/automoderator>`_ - very widely used now & also open source: `more information here <https://github.com/Deimos/AutoModerator/wiki/Features>`_.
- `moderator-bot <http://www.reddit.com/user/moderator-bot>`_
- `atheismbot <http://www.reddit.com/r/atheismbot>`_ & `atheismbot FAQ <http://reddit.com/r/atheismbot/wiki/faq>`_

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

----------------

Know of any more interesting & fun reddit bots? Let me know in the comments...

----------------

Footnotes & References
--------------------------

.. [#stats] `About Reddit, including some mind boggling statistics <http://www.reddit.com/about/>`_.
.. [#bots] How many bots? No one really knows. `How to create a Reddit bot <https://praw.readthedocs.org/en/latest/>`_. This being reddit, there's `a community <http://www.reddit.com/r/botwatch>`_ to keep an eye on them, too - and `/r/TheoryOfReddit <http://www.reddit.com/r/TheoryOfReddit/>`_ do `sometimes <http://www.reddit.com/r/TheoryOfReddit/comments/187n3n/reddit_has_bots_but_what_kinds_of_bots_are_there/>`_ `discuss <http://www.reddit.com/r/TheoryOfReddit/comments/1586yk/should_reddit_regulate_bots/>`_ bots. Well, `actually <http://www.reddit.com/r/TheoryOfReddit/comments/m5t1s/a_worrying_trend_for_reddits_bots/>`_ they `talk <http://www.reddit.com/r/IAmA/comments/kglw8/we_are_the_creators_of_the_automated_bots_on/>`_ `about <http://www.reddit.com/r/TheoryOfReddit/comments/k7xjw/lets_talk_about_bots/>`_ bots `quite a lot <http://www.reddit.com/r/TheoryOfReddit/search?q=bot&restrict_sr=on>`_.
.. [#qkme_transcriber_faq] This is mostly quoted from the excellent qkme_transcriber bot's FAQ, `here <http://www.reddit.com/r/qkme_transcriber/comments/o426k/faq_for_the_qkme_transcriber_bot/>`_.
.. [#circlejerk] `/r/circlejerk <http://www.reddit.com/r/circlejerk/top/>`_ is a subreddit dedicated entirely to reddit satire. It's full of 'parodies' of 'karma whoring' posts and 'parodies' of endless pun threads. The thought that they have rigorous standards and actually kick people out for breaking them is almost funny in itself.
.. [#impersonate] `How easily could a computer program emulate the average Reddit commenter? <http://www.reddit.com/r/TheoryOfReddit/comments/tiqqg/how_easily_could_a_computer_program_emulate_the/>`_
.. [#what_is_karma] Internet Points! Reddit has a system called `Karma <http://www.reddit.com/wiki/faq#wiki_what_is_that_number_next_to_usernames.3F_and_what_is_karma.3F>`_ : "The number next to a username is called that user's "karma." It reflects how much good the user has done for the reddit community. The best way to gain karma is to submit links that other people like and vote for."