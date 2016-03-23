:title: I finally figured out my mysterious 418/Unused HTTP Status Code
:slug: finally-figured-out-my-mysterious-418unused-http-status-code-dreamhost
:date: 2016-03-22 22:21:19
:tags: web, apache, hosting, dreamhost
:category: tech
:meta_description: I've had a mysterious broken page on this site for a while - but been too busy to look into it. I finally made the time to figure it out.
:thumbnail:

I've had a mysterious broken page on this site for a while - but been too busy to look into it. My `Comprehensive Linux Backups with etckeeper & backupninja <{filename}./comprehensive-linux-backups-with-etckeeper-backupninja.rst>`_ article has been refusing to load, and returning a weird HTTP 418 Unused status code instead. I finally made the time to figure out the cause.

.. figure:: {filename}/images/posts/finally-figured-out-my-mysterious-418unused-http-code-dreamhost/extra_web_security-nq8.png
   :align: right

   Well, mostly reccomended.

It turned out that this was being caused by the apache/php ``mod_security`` module. This is a static website - there's no PHP anywhere - so why would that be a problem? Well, so far I've been very happily hosting the site on my old DreamHost shared hosting account - which comes with Apache & PHP installed whether you want it or not. At some point I must have checked the `'Extra Web Security?' option in the DreamHost control panel <https://help.dreamhost.com/hc/en-us/articles/215947927>`_ for this domain.


Checking the Logs
===================

I `SSH'd in to my account <http://wiki.dreamhost.com/SSH>`_ on the shared server to `look at the logs <http://wiki.dreamhost.com/Error_log>`_. The apache ``error.log`` for the site had lots of the following entries:

.. class:: wrap
.. code-block:: log

  [Tue Mar 22 01:17:39 2016] [error] [client 24.84.4.121] ModSecurity: Access denied with code 418 (phase 4). Pattern match "(?:<title>[^<]*?(?:\\\\b(?:(?:c(?:ehennemden|gi-telnet)|gamma web shell)\\\\b|imhabi
  rligi phpftp)|(?:r(?:emote explorer|57shell)|aventis klasvayv|zehir)\\\\b|\\\\.::(?:news remote php shell injection::\\\\.| rhtools\\\\b)|ph(?:p(?:(?: commander|-terminal)\\\\b|remot ..." at RESPONSE_BODY. [
  file "/dh/apache2/template/etc/mod_sec2/modsecurity_crs_45_trojans.conf"] [line "34"] [id "950922"] [msg "Backdoor access"] [severity "CRITICAL"] [tag "MALICIOUS_SOFTWARE/TROJAN"] [hostname "duncanlock.net"]
   [uri "/blog/2013/08/27/comprehensive-linux-backups-with-etckeeper-backupninja/index.html"] [unique_id "VvD-o9BxuqUAAGqPBDYAAAAA"]


Line 34 of the ``.conf`` file that it references:

.. code-block:: plain

  /dh/apache2/template/etc/mod_sec2/modsecurity_crs_45_trojans.conf

looks like this:

.. class:: wrap
.. code-block:: apache

  SecRule RESPONSE_BODY "(?:<title>[^<]*?(?:\b(?:(?:c(?:ehennemden|gi-telnet)|gamma web shell)\b|imhabirligi phpftp)|(?:r(?:emote explorer|57shell)|aventis klasvayv|zehir)\b|\.::(?:news remote php shell injection::\.| rhtools\b)|ph(?:p(?:(?: commander|-terminal)\b|remoteview)|vayv)|myshell)|\b(?:(?:(?:microsoft windows\b.{,10}?\bversion\b.{,20}?\(c\) copyright 1985-.{,10}?\bmicrosoft corp|ntdaddy v1\.9 - obzerve \| fux0r inc)\.|(?:www\.sanalteror\.org - indexer and read|haxplor)er|php(?:konsole| shell)|c99shell)\b|aventgrup\.<br>|drwxr))" \
          "phase:4,ctl:auditLogParts=+E,deny,log,auditlog,msg:'Backdoor access',id:'950922',tag:'MALICIOUS_SOFTWARE/TROJAN',severity:'2'"


This rather large regular expression *just happened* to match a prefectly innocent peice of text in my `Comprehensive Linux Backups with etckeeper & backupninja <{filename}./comprehensive-linux-backups-with-etckeeper-backupninja.rst>`_ article - specifically, this directory listing matched the ``|drwxr))`` bit at the end of that regex:

.. code-block:: console

    $ sudo ls -lah /etc/backup.d/

    total 40K
    drwxrwx---   2 root root 4.0K May 19 16:54 .
    drwxr-xr-x 154 root root  12K May 19 15:25 ..
    -rw-------   1 root root 1.4K May 19 16:54 10-little-things.sh
    ...

This caused Apache's ``mod_security`` to eat requests for that page, and `DreamHost to return a 418 error instead <http://wiki.dreamhost.com/Mod_security>`_:

  **418 I'm a teapot (RFC 2324)**

  This code was defined in 1998 as one of the traditional `IETF <https://en.wikipedia.org/wiki/Internet_Engineering_Task_Force>`_ `April Fools' jokes <https://en.wikipedia.org/wiki/April_Fools%27_Day_RFC>`_, in `RFC 2324 <https://tools.ietf.org/html/rfc2324>`_, `Hyper Text Coffee Pot Control Protocol <https://en.wikipedia.org/wiki/Hyper_Text_Coffee_Pot_Control_Protocol>`_, and is not expected to be implemented by actual HTTP servers. The RFC specifies this code should be returned by tea pots requested to brew coffee. This HTTP status is used as an easter egg in some websites, including Google.com.

I guess it's easy to see in logs and is unlikely to be caused by anything else. Took me a while to figure out where it was coming from, though.

Fixing it
==================

The simplest fix for this is to just uncheck the `'Extra Web Security?' option in the DreamHost control panel <https://help.dreamhost.com/hc/en-us/articles/215947927>`_ for this domain. You have to wait a few minutes for the change to happen, but after that, the page should start working.

What I *actually* decided to do was to take advantage of the static nature of the site - and experiment with hosting this blog directly on Amazon s3. I'll cover that in another article, if I decide to stick with it.
