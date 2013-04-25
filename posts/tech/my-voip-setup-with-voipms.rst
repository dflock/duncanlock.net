:title: My VOIP Setup, with VOIP.MS
:slug: my-voip-setup-with-voipms
:date: 2013-04-23 17:18:10
:tags: voip, howto
:category: tech

My wife and I currently live in Canada, and our families are back in the UK. We'd been using Skype to chat with people in the UK, but I was getting frustrated with Skype's limitations: it either ties you to a computer and Wifi, or running a battery hungry app which slows down your phone. It doesn't work very well over the 3G phone network here and while it's free to make Skype to Skype calls, it's fairly expensive calling real phones. I didn't really want to buy a dedicated Skype phone - we both already have mobile/cell phones. And, to top it all off, the Skype software for Linux is the poor cousin of the Windows one, especially if you run 64 bit Linux.

In addition to these Skype specific issues, our parents both live out in the English countryside, and their internet connections are pretty slow and unreliable. It would be better if they didn't have to use the internet on their end at all.

So, what I really wanted was something that I could easily use on my Android phone without having to run yet another app, and that was cheaper and easier to use. I also wanted something that could be used exactly like a regular local phone number -- just call it and ring a phone on the other side of the world.

What I wanted was a Magic Phone Number
======================================

After a lot of reading & research [#parlar]_, I decided that I wanted a :abbr:`VOIP (Voice Over IP)` [#voip_wiki]_ setup of some sort.

Unlike Skype, VOIP is an open standard, which means that anyone can create software and devices for it, not just one company. Amongst other things, this means that there are lots of VOIP soft-phones [#soft-phone]_ available for every platform and, even better, Android has built in support for making and receiving VOIP calls -- so it would just work on our existing phones.

There are also lots of VOIP services available that provide lots of other features, like :abbr:`DID (Direct Inward Dialling - i.e. real phone numbers)`, voice-mail, call forwarding, ring groups, :abbr:`IVR (Interactive Voice Response - i.e. Press One for..., Two for...)` etc...

I eventually chose http://voip.ms/, because of their extreme flexibility, `features <http://wiki.voip.ms/article/Features>`_ and very low wholesale-style costs.

Because it's so flexible, it easily allowed us to get what we needed, along with plenty of bonus extras, for almost no cost.

Getting a Real Phone Number
===========================

The first thing I wanted was a real UK phone number that people there could call, that would ring our phones in Canada. Ideally it would be a local number for our parents - familiar and free or cheap to call from a landline phone.

These are called :abbr:`DID (Direct Inward Dialling - i.e. real phone numbers)` numbers - and you can get one for `practically anywhere <https://www.voip.ms/intldids.php>`_. DID's for many places have a choice of either pay as you go, or monthly flat rate which includes unlimited inbound calls to that number; the UK ones only offer flat rate: $0 setup fee and $4 per month unlimited inbound calls. You just choose the area code you want and click Order.

Congratulations, you now have a UK phone number! The process for getting a phone number practically anywhere else in the world is the same. Now... you need to decide what happens when someone calls it:

Routing
-------

There are *lots* of options for routing your incoming calls: send them to voicemail, send them to a Digital Receptionist/:abbr:`IVR (Interactive Voice Response - i.e. Press One for..., Two for...)`, forward them to another number, play them a recording, etc...

I wanted to give people the option of being put through to either me, or my wife, so I wanted to prompt them to choose: 'Press 1 to call Duncan, Press 2 to...' -- so I needed to send callers to an IVR:

Interactive Voice Response (IVR)
--------------------------------

This is just a simple voice prompt system. It plays the caller a recording that you supply and then does things in response to them pressing different digits. You can route each option to anywhere you can route a normal call. I setup 1 to call me, 2 to call my wife, 3 to leave me a voicemail and 4 to leave one for my wife:

.. figure:: /static/images/simple-voip-uk-number-ivr-2013-04-24-18.38.41.jpg

   Simple UK IVR setup, works out to free calls, plus $4 per month flat rate.

Now I wanted the same thing, in reverse -- a local number that I could call in Canada that would let me call the UK.

Phone to Phone calling, via the Cloud
=====================================




Getting a Receptionist
======================

Bonus Features
==============


Footnotes & References:
----------------------------

.. [#parlar] http://parlar.ca/blog/2011/8/8/my-voip-setup-with-voipms.html
.. [#voip_wiki] What is VOIP: http://en.wikipedia.org/wiki/Voice_over_IP
.. [#soft-phone] A soft-phone is a piece of software, like Skype, that allows you to make phone calls on a computer. Unlike Skype, most of them support SIP, STUN and VOIP.
