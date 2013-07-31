:title: How to setup a Secure Ubuntu LAMP Server & Website on a RamNode VPS
:slug: how-to-setup-a-secure-ubuntu-lamp-server-website-on-a-ramnode-vps
:date: 2013-05-29 21:06:44
:tags: ramnode, vps, linux, lamp, howto
:status: draft

I've recently setup websites on several RamNode :abbr:`VPS (Virtual Private Server)`'s, so I thought I'd document the process for anyone who's doing this for the first time -- providing a quick start guide to setting up a website on a RamNode VPS, from nothing to a fully working, public facing website.

This guide assumes that you've got some version of Ubuntu installed on the VPS - this is easy to do by choosing a version of Ubuntu during setup/purchase.

This guide will start you off with reasonably secure defaults - we'll be taking some basic steps to secure the root account, ssh and setting up a firewall - but this is not magically 'secure' - security is an ongoing process and as server Admin this is part of your responsibility - this guide is just intended to get you started properly.

http://blog.al4.co.nz/2011/05/setting-up-a-secure-ubuntu-lamp-server/


*************
Initial Setup
*************

If you don't already have one, go and `get a RamNode VPS <https://clientarea.ramnode.com/aff.php?aff=565>`_. Don't forget to `use a coupon - up to 30% off for life <http://serverbear.com/9756/ramnode#view-coupons>`_.

Purchasing & Choices during setup
=================================

.. figure:: /static/images/posts/how-to-setup-a-secure-ubuntu-lamp-server-website-on-a-ramnode-vps/ramnode-setup-configure-step.png

   When you get to this point in the RamNode checkout process, you need to make some choices: pick an OS and pick a hostname.

   How about ``axiom`` and 'Ubuntu <highest number> 32-bit'?

Choosing a hostname
===================

We'll be setting up a proper DNS setup for this website later, so the hostname isn't very important. I would suggest that you set it to the name of the website, without the ``www`` or ``.com`` parts - i.e. don't use a :abbr:`FQND (Fully Qualified Domain Name)` - it's potentially confusing.

If you plan to host multiple websites or other things on this VPS, then I suggest just choosing a memorable name or `generating one <http://computernamer.com/>`_. I would also suggest that the name be short, lower case, with no spaces or punctuation - keep it simple.

How about ``axiom``?

Choosing an OS
===================
Unless you have a special reason not to (i.e > 4GB RAM), I would suggest installing the latest version of Ubuntu - but choosing the 32bit version.

There *are* some security and speed advantages to 64bit systems but they *do* use more RAM than an equivalent 32bit system - so in a VPS environment where RAM is at a premium, I would stick with 32bit systems.

Logging In
==========

Once you've ordered your VPS, you'll get an email containing all the login details. You need this section:

.. code-block:: text

    SSH Access Information
    =============================
    Main IP Address: 123.123.123.123
    Username: root
    Password: qwRAUiGEXB3I (Change this immediately)
    Port: 22



**************
Basic Security
**************

Stop using the `root` account
==============================

Many naïve attacks focus on the ``root`` account. A simple way to sidestep these is to set a very strong password on the root account - and then stop using it. You don't have to remember the root password because we won't be using the root account, so you can make it very strong.

To create a super strong password, use ``pwgen`` - which you might have to install:

.. code-block:: console

    $ sudo apt-get install pwgen

You can then run it in a terminal to generate some highly random, secure passwords:

.. code-block:: console

    $ pwgen -sycn 50

    uJfApg3wMox9by5g+$-D2`Kg{KN!<#i=sUG2`@w-kc:QB%|aHD
    _sJddY9l>Y|)P+@V/|e$R!g;$Th0~x<~#AkWKtM7aUi.e?7)nf
    0uS<++KWn/=D?RDxQQ5iE{:>a}bbR}QQG~Z3'oN-T39mOT@%(G
    r=a&Y-4]Y:'.s\gNu:!sy3IKCqPh]m;}o^%8&g+LZ[)\*#dch1
    t_-@?XUe`Zg!i/Iz@uliwpMKDN+8qhoth40>M!n_t5p=MA"_z2
    K4)QL"MmaKW=VFI^{?0bU{5%JH6rdNRMxz\R4x(Fa.P#r"A#n=
    ...


Create a New Admin account instead
----------------------------------

Stop using passwords for SSH
============================

Hardening SSH a little
======================

We will disable root logins & restrict access to only the new admin user we just created. Disabling the ``root`` account defeats many simple dictionary attacks, and restricting access to your own user means that accounts created for other purposes don't accidentally get granted ssh access. These two things taken together default most simple username & password 'guessing' attacks.

**********************************
Pointing a Domain Name at your VPS
**********************************


Register a Domain Name
======================

If there are no Name Servers, point them somewhere
==================================================

ClouFlare will give you an error message and won't add the domain if it doesn't have any name servers defined in it's DNS record.

Register with CloudFlare
========================

Setup the DNS using CloudFlare
==============================

*********************************************************
Copying things from your computer using SSH, SCP or SSHFS
*********************************************************

