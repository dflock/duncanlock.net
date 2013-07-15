:title: Magic Phone Numbers: My VOIP Setup, with voip.ms
:slug: magic-phone-numbers-my-voip-setup-with-voipms
:date: 2013-05-31 14:46:45
:tags: voip, howto, telephony
:category: tech
:meta_description: I wanted something better than Skype, exactly like a regular local phone number - just call it and ring a phone on the other side of the world, for free.
:thumbnail: /static/images/posts/magic-phone-numbers-my-voip-setup-with-voipms/magic-number-diagram.png

.. figure:: /static/images/posts/magic-phone-numbers-my-voip-setup-with-voipms/magic-number-diagram.png
   :alt: Schmatic diagram showing two phones, linked by a magic cloud, calling from the UK to Canada - via the cloud - for free.

   In an ideal world, I'd like something like this - and vice versa, please.

My wife and I currently live in Canada, and our families are back in the UK. We'd been using Skype to chat with people in the UK, but I was getting frustrated with Skype's limitations: it either ties you to a computer and WiFi, or running a battery hungry app which slows down your phone. It doesn't work very well over the 3G phone network here and while it's free to make Skype to Skype calls, it's fairly expensive calling real phones. I didn't really want to buy a dedicated Skype phone - we both already have mobile/cell phones. And, to top it all off, the Skype software for Linux is the poor cousin of the Windows one, or pretty much unusable if you run 64-bit Linux.

In addition to these Skype specific issues, our parents both live out in the English countryside, and their internet connections are pretty slow and unreliable. It would be better if they didn't have to use the internet on their end at all.

So, what I really wanted was something that I could easily use on my Android phone without having to run yet another app, and that was cheaper and easier to use. I also wanted something that could be used exactly like a regular local phone number -- just call it and ring a phone on the other side of the world.


What I wanted was a Magic Phone Number
======================================

After a lot of reading & research [#parlar]_, I decided that I wanted a :abbr:`VOIP (Voice Over IP)` [#voip_wiki]_ setup of some sort.

Unlike Skype, VOIP is an open standard, which means that anyone can create software and devices for it, not just one company. Amongst other things, this means that there are lots of VOIP soft-phones [#soft-phone]_ available for every platform and, even better, Android has built in support for making and receiving VOIP calls -- so it would just work on our existing phones, without needing to install anything.

There are also lots of VOIP services available that provide lots of other features, like :abbr:`DID (Direct Inward Dialling - i.e. real phone numbers)`, voice-mail, call forwarding, ring groups, :abbr:`IVR (Interactive Voice Response - i.e. Press One for..., Two for...)` etc...

I eventually chose http://voip.ms/, because of their extreme flexibility, `features <http://wiki.voip.ms/article/Features>`_ and very low wholesale-style costs.

Because it's so flexible, it easily allowed us to get what we needed, along with plenty of bonus extras, for almost no cost.

Getting a Real Phone Number
===========================

The first thing I wanted was a real UK phone number that people there could call, that would ring our phones in Canada. Ideally it would be a local number for our parents - familiar and free or cheap to call from a landline phone.

These are called :abbr:`DID (Direct Inward Dialling - i.e. real phone numbers)` numbers - and you can get one for `practically anywhere <https://www.voip.ms/intldids.php>`_. DID's for many places have a choice of either pay as you go, or monthly flat rate which includes unlimited inbound calls to that number; the UK ones only offer flat rate: $0 setup fee and $4 per month unlimited inbound calls. You just choose the area code you want and click Order.

Congratulations, you now have a UK phone number! The process for getting a phone number practically anywhere else in the world is the same. Now you just need to decide what happens when someone calls it.

Routing
-------

There are *lots* of options for routing your incoming calls: send them to voicemail, send them to a Digital Receptionist/:abbr:`IVR (Interactive Voice Response - i.e. Press One for..., Two for...)`, forward them to another number, play them a recording, etc...

I wanted to give people the option of being put through to either me, or my wife, so I wanted to prompt them to choose: 'Press 1 to call Duncan, Press 2 to...' -- so I needed to send callers to an IVR:

Interactive Voice Response (IVR)
--------------------------------

This is just a simple voice prompt system. It plays the caller a recording that you supply and then does things in response to them pressing different digits. You can route each option anywhere you can route a normal call. I setup 1 to call me, 2 to call my wife, 3 to leave me a voicemail and 4 to leave one for my wife:

.. figure:: /static/images/posts/magic-phone-numbers-my-voip-setup-with-voipms/uk-voip-diagram.png
   :alt: Schematic blueprint style diagram showing a UK caller, calling a local UK landline, being routed to an IVR menu in the 'magic cloud', having a choice of calling or leaving a message.

   Simple UK IVR setup, works out to free calls, plus $4 per month flat rate.

Now I wanted the same thing, in reverse -- a local number that I could call in Canada that would let me call the UK.

Phone to Phone calling, via the Cloud
=====================================

So I purchased another DID number, a local Vancouver number, that we could call for free from our cell phones. I then created another IVR, so that when we called that number it would give us a menu of people in the UK to call:

.. figure:: /static/images/posts/magic-phone-numbers-my-voip-setup-with-voipms/screenshot-13-05-31_03-30-35-pm.png

   Building an IVR menu in voip.ms.

   On the right - the digit the caller pressed, on the left, the destination. As you can see, there are lots of different options on the left - these are all the different places you can send callers.

Because our cell phone plan gives us unlimited included/free talk time to local numbers, this means that we can call our local DID number for free and talk to people in the UK (or anywhere else), for as long as we like - no data connection required.

There are two different plans available for the Vancouver DID number: either $1.99 per month plus 0.0149¢ per minute, or $5.95 per month flat rate. The flat rate plan is cheaper if you're using more than 400 minutes per month - we're currently using less than that, so we're on the $1.99 plan.

Counting the Cost
===================

Last month, we spent a total of **14 hours, 24 minutes, 55 seconds** calling people in the UK and spent a total of **$12.59**. That's... *a lot* of talking, for not very much cash.

This gives us what we wanted - magic numbers that we can use to call anyone in the world from our cell phones - and that anyone can use to call us - at very low prices.

But wait, there's more...
==========================

This just scratches the surface of the things you can do using VOIP & voip.ms. Here's a taster of some of the other things that you can do, some of this we're already using and some we might use in the future:

`Free Voicemail for anything <http://wiki.voip.ms/article/Voicemail>`_
	You can route any call to voicemail to take a message. The system can then email the recording (as a .wav file attachment) to any inbox.

`CallerID <http://wiki.voip.ms/article/Caller_ID>`_
	You can pass-through the CallerID from your phone when you use DID numbers to make outbound calls if you want, or you can set them yourself. You can also have the system report CallerID's on incoming calls, so that your phone will tell you who's calling.

VOIP to VOIP calling, VOIP to Phone calling (aka free long distance)
	You don't have to use the :abbr:`POTS (Plain Old Telephone System)` at all - you can make pure data calls over the internet, either to regular phones or SIP/VOIP numbers. This means that you can use WiFi to make calls without using your cell phone minutes at all, or indeed having a SIM card or a phone - you can use a softphone on any computer or laptop to make calls.

`SMS text messaging <http://wiki.voip.ms/article/SMS>`_
	I haven't figured this out yet, but you can send & receive SMS text messages, using your DID numbers. This is a new feature currently US only (and free) - will be 1¢ per text from 2014.

`DISA - Direct Inward System Access <http://wiki.voip.ms/article/DISA>`_
	This allows you to make outgoing calls, to anyone, with no setup. You just dial to your DID number, provide a 4 digit PIN, then you can dial out to any number in the world, using `voip.ms's cheap termination rates <http://www.voip.ms/rates.php>`_.

`Callback <http://wiki.voip.ms/article/Callback>`_
	You can define a number to be called back by voip.ms, in order to receive a dial tone and place outgoing calls. This could be useful if you want to place a call and you are not at home or don't have access to your voip device: you call the number, hang up and it calls the predefined number. You pickup and you get a dial tone - and you can then dial any phone number.

`CallerID Filtering <http://wiki.voip.ms/article/CallerID_Filtering>`_
	Allows you to filter the incoming calls to your DID numbers that came from specific numbers, area code or even anonymous numbers. For example, if you receive annoying incoming calls from a telemarketing company you can create a filter to route all the calls to a recording that plays the message "That number is no longer in service, please hang-up and try again", amongst several other options. You can also flip this around and filter out everyone except certain numbers, creating a private line that's impervious to telemarketers.

There are also loads of 'professional' type features designed for big offices - calling cues, ring groups, failover, time conditions, etc... Lots more details here: http://wiki.voip.ms/article/Features.

If you're sold on voip, here's the `voip.ms getting started guide <http://wiki.voip.ms/article/Getting_Started>`_ -- and if you've got any questions, please just ask in the comments!

-------------------

Footnotes & References:
----------------------------

.. [#parlar] Thanks very much to Jay Parlar, who wrote up his voip setup `here <http://parlar.ca/blog/2011/8/8/my-voip-setup-with-voipms.html>`_.
.. [#voip_wiki] What is VOIP: http://en.wikipedia.org/wiki/Voice_over_IP
.. [#soft-phone] A soft-phone is a piece of software, like Skype, that allows you to make phone calls on a computer. Unlike Skype, most of them support SIP, STUN and VOIP.
