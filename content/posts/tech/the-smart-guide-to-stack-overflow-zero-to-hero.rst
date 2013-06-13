:title: The Smart Guide to Stack Overflow: Zero to Hero
:slug: the-smart-guide-to-stack-overflow-zero-to-hero
:date: 2013-06-10 19:19:40
:tags: howto, stack overflow, site guide
:meta_description: How to use Stack Overflow effectively, how to build reputation and become a valued member of the site.
:status: draft

.. figure:: /static/images/stackoverflow-logo-is-made-of-people-diagram.png

	StackOverflow is made of people. Lots and lots of people.

Seemingly like everything else in the world, Stack Overflow is getting more & more competitive as time passes. Generating a good reputation - and even finding good questions to answer - is becoming harder and harder, as more and more people compete for less unanswered questions.

This is *great* if you want to find an answer - but makes it much harder for newcomers to get started and build a reputation on the site.

This guide will help you jump-start your reputation on StackOverflow and get more out of the site.

How to find questions you can answer
======================================

Ignored & Favourite Tags
--------------------------

.. figure:: /static/images/stack-overflow-ignored-tags.png
	:align: right
	:alt: Screenshot of part of my (very long) ignored tags list from Stack Overflow

	I don't know jack: Screenshot of part of my (long) ignored tags list from Stack Overflow


Use the `no answers <http://stackoverflow.com/unanswered/tagged/?tab=noanswers>`_ page, but make sure you add plenty of Ignored Tags. Whenever you see a question that you don't know anything about, add it's tags to your Ignored Tags list. This fades questions with these tags, making it much easier to skim through the list finding things that you *can* answer.

Don't be afraid to add lots of ignored tags - it's not an admission of failure - there will always be lots of things that you aren't an expert on.

Add some favourite tags too - this highlights questions with these tags, again, helping you to sort the wheat from the chaff.

Wildcards
---------------

.. image:: /static/images/stack-overflow-ignored-tags-add-with-wildcard.png

Both Ignored and Favourite Tags can use wild cards - just put an asterisk at the end of the tag when you enter it - so ``xcode*`` would match both ``xcode`` and ``xcode4.5``, for example. This significantly reduces the number of tags you need.

Follow Tags & Automate
-------------------------

You can also follow a single tag - one of your Favourite tags, for example - just click on it in your sidebar and you'll see a `filtered version of the Questions pages, just for that tag <http://stackoverflow.com/questions/tagged/mysql%2A>`_. This also works for wildcards, so clicking on a wildcard tag in your sidebar will filter by all matching tags.

.. image:: /static/images/stack-overflow-follow-tags-feed-with-wildcard.png

At the bottom of each of these filtered lists is a link to an Atom Feed [#atomfeed]_ that you can subscribe to in a News/Feed Reader [#feedreader]_ - this will alert you whenever new questions are posted with that tag.

You can also use `IFTTT to automatically notify <https://ifttt.com/recipes/search?q=stackoverflow>`_ [#ifttt]_ you when new questions appear, when your reputation changes, etc - it can even send you an SMS.


Mercenary Reputation Building 101
======================================

Most of these reputation building techniques are win-win, thanks to Stack Overflow's masterful gamification [#gamification]_ architecture - but some of them are a little bit... mercenary:

Answers in the comments are just asking for it
--------------------------------------------------

For some reason, people often answer questions in the comments, rather than submitting an actual Answer - this is wrong for lots of reasons:

- It makes the answers hard to find for other people & adds to the noise on the site.
- It means that an answer can never be accepted, so other people won't be able to tell if the question has an answer - and the question will appear in the Unanswered lists forever.
- You get no credit for answers supplied in the comments
- Formatting and space is intentionally very limited in comments.

If people are stupid enough to do this, then they deserve to be punished (a little tiny bit). Copy their answer out of the comment into a real Answer. Expand on it in the extra space you now have, improve the formatting, add example code, etc... - and wait for the reputation points to roll in.

Answer questions from experienced users
-------------------------------------------

.. figure:: /static/images/screenshot-13-06-06-07-43-18-pm.png

   Except this guy.

Everything else being equal, answer questions asked by users with higher reputation. They know how the site works, they know to accept and upvote answers. New users often don't, or they'll ask a question and never some back - so it's much more likely that you'll get no reward for answering their questions.

New users also tend to ask more crappy questions, which get closed more often, than experienced users.

Sadly this is hard on new users, so if they've asked a well articulated, valid question and have a real looking username, I would suggest taking a chance and answering the question anyway. Even if the asker never comes back, you can still get upvotes from other users.

Speculate to Accumulate: Answer lots of questions, well
--------------------------------------------------------
This seems obvious, but the more questions you answer well, the more reputation you'll gain - but not just at the time you answer: forever. Good answers keep building reputation over time as new people discover them and upvote them - and the more of your answers are out there, the more you'll gain from this on an ongoing basis.

.. figure:: /static/images/screenshot-13-06-06-07-27-10-pm.png

	`This answer <http://stackoverflow.com/questions/2675323/mysql-load-null-values-from-csv-data/5968530#5968530>`_ was posted in May 2011, this screenshot was taken in June 2013.

Once you've got the top voted answer on a popular question, you will gain occasional upvotes and reputation from it without you actively doing anything. The more of this you have and the more popular those questions and answers, the more you gain - with `top users <http://stackoverflow.com/users/1288/bill-the-lizard?tab=reputation>`_ sometimes hitting the daily reputation cap of +200 without doing anything.

Come back and improve your popular answers
---------------------------------------------

If you find that one of your answers keeps receiving upvotes over time, then come back and improve on it. Edit your answer - improve the formatting, add better example code and answer any comments people have left - by improving the answer to address them. This increases the amount of upvotes that your improved answer will get over time and improves the quality of the site overall.
It also bumps that question back up in search results and lists, making it more visible, increasing the likelihood of upvotes, and so on.

However - don't do this *too* often. Only make edits that are worthwhile and add value to the answer - if you edit your answers too much, they'll become `Community Wiki posts <http://meta.stackoverflow.com/questions/11740/what-are-community-wiki-posts>`_ and stop generating reputation altogether.

Get in First
-------------------
Being the first answer is often surprisingly important. There are lots of other people looking through the unanswered questions list for questions to answer - as soon as a question has an answer it disappears from this list. Being the first correct answer to a question also makes it more likely that other people visiting the question will upvote your answer and move on, looking for something else to answer. Answers are sorted by votes, so the answer with the first upvote will move to the top, thus getting more attention and re-enforcing the cycle -- answers with an early lead will often maintain it.

So, if you see a question that you know the answer to off the top of your head, answer it immediately. Get the gist of the answer down and submit it. Then, read through your answer, think about it some more, then edit it - expanding on your answer, adding more detail, improving it with examples and Markdown formatting.

Quick answers are also good for the asker - they get the answer they need quickly and can start working on their solution and perhaps making follow-up comments while you're further polishing your answer.

Preferentially answer questions with bounties
------------------------------------------------
Again, obvious - questions with `bounties <http://stackoverflow.com/helpcenter/bounty>`_ give you the bounty as reputation if you post the accepted (or highest voted) answer.

.. image:: /static/images/screenshot-13-06-06_07-12-23-pm.png


Use the `Featured list <http://stackoverflow.com/questions?pagesize=50&sort=featured>`_ to see all questions with bounties. Your ignored and favourite tags work here too.

Even if the person who places the bounty never bothers to come back and award it - half of it will get awarded to the highest voted answer (created after the bounty started with at least 2 upvotes) when the bounty closes. This means that you're only guaranteed to land the bounty if you can get the top spot, so answering questions with an outstanding bounty - but several existing answers with lots of votes - generally isn't such a good investment of time. Unless you think you can provide an answer that's sufficiently good to beat the existing ones before the bounty closes.

Getting Badges
--------------

.. image:: /static/images/screenshot-13-06-06_07-14-59-pm.png

You will accumulate badges in the course of using the site, but there are ways to increase your accumulation rate slightly without going out of your way too much.

Preferentially answering older, un-answered questions is a good way to get `Necromancer <http://stackoverflow.com/badges/17/necromancer?userid=259698>`_, `Revival <http://stackoverflow.com/badges/837/revival?userid=259698>`_ and `Excavator <http://stackoverflow.com/badges/1287/excavator?userid=259698>`_ badges - and using ignored tags is a great way to filter out the noise in the No Answers list, allowing you to quickly zip back to the older un-answered questions that you can answer. There's also less competition to answer these poor, neglected questions.

Ask Good Questions
========================

You can also get reputation by *asking* questions: +5 for each upvote your question gets.

How to ask good questions? The `official guide is here <http://stackoverflow.com/helpcenter/asking>`_. In addition to this, my tips for good questions are:

Search first
-----------------------------
Someone has almost certainly asked your question before and the answer is just there waiting for you. Search with Google & directly on Stack Overflow.

Think before you post
-----------------------------
Don't just ask questions for the sake of it - or for the reputation. Ask when you're *genuinely* stuck. Try to solve the problem yourself - but if you really can't, ask. Mention your attempted solutions in the question, so that people know what you've already tried and eliminated.

Explain carefully
-----------------------------

Carefully layout your problem, in detail, so that someone without any prior knowledge of your situation can understand the problem. They're not telepathic - you need to explain yourself succinctly and thoughtfully if you want a good answer.

Include a relevant simplified example
---------------------------------------

Boil your problem down to it's essence and include a simplified example - with any required code and data - in your question. Try and make this as short as possible without leaving out anything essential.

A working example, using `jsfiddle <http://jsfiddle.net/>`_, `sqlfiddle <http://sqlfiddle.net/>`_, `rubyfiddle <http://rubyfiddle.net/>`_, etc... is the gold standard. Put the simplified example code into your question as normal, but also upload it to the relevant \*fiddle site and add the link to your question.

Use Markdown formatting
----------------------------

This goes for both asking questions and answering them. Stack Overflow `supports Markdown for formatting your posts <http://stackoverflow.com/editing-help>`_ - use it! It will make you questions easier to read and understand, you'll get more upvotes and better answers.

Read before posting, then read it again afterwards
-----------------------------------------------------
Read you question through a few times before posting. Make sure that it's well phrased, well formatted and spelt correctly. Make sure that your example code and data is clear and concise and includes everything you would need to reproduce the problem.

Once you've posted it, read the live version and edit out the mistakes you missed before posting.

----------------

Footnotes & References
--------------------------

.. [#atomfeed] **Atom Feeds** (like RSS Feeds) can be used to allow users to subscribe to updates from a website: http://en.wikipedia.org/wiki/Atom_(standard)
.. [#feedreader] A **Feed Reader** is a piece of software (Desktop, Mobile or Web based) that allows users to collect/aggregate and read their Feeds, manage subscriptions and send notifications: http://en.wikipedia.org/wiki/Feed_reader
.. [#gamification] **Gamification** is the use of game thinking and game mechanics in a non-game context in order to engage users and solve problems: http://en.wikipedia.org/wiki/Gamification
.. [#ifttt] **IFTTT** enables you to create and share "recipes" that fit the simple statement: "if this then that". The "this" part of a recipe is a trigger. Some example triggers are "I’m tagged in a photo on Facebook" or "I check in on Foursquare." The "that" part of a recipe is an action. Some example actions are "send me a text message" or "create a status message on Facebook.": http://en.wikipedia.org/wiki/IFTTT