:title: Setting your Compose Key to Caps Lock on XFCE/Xubuntu
:slug: setting-your-compose-key-to-caps-lock-on-xfcexubuntu
:date: 2013-05-03 15:40:46
:tags: linux, xfce, configuration, tutorial, xubuntu
:category: tech


.. figure:: /static/images/compose-key-diagram.png
    :alt: Blueprint style diagram showing the compose key sequence for the Euro currency symbol.

    Just hold down your chosen compose key, then press the other keys in turn: [compose key] + e + = gets you a Euro symbol.

The compose key on Linux if *incredibly* useful, but not configured by default - and on XFCE there's currently no graphical UI to change it. However, it's pretty simple to change... here's how to make the Caps Lock key your compose key:

In the file ``/etc/default/keyboard``, change ``XKBOPTIONS`` to look like this:

.. code-block:: ini

    XKBOPTIONS="compose:caps"

Save the file. You can now either reboot, restart X, or see `Activating your change without rebooting`_, below.

If you don't want to use Caps Lock as your compose key, there are some other options in this file: ``/usr/share/X11/xkb/rules/xorg.lst`` - search for 'compose', they're listed towards the end.

Using the Compose Key
--------------------------

Try holding down the Caps Lock key and type the letter ``l``, followed by a dash you should get a British Pound symbol: £ - magic!

Generally you can just hold down your compose key then type a combo that kinda 'looks like' the symbol you want, if they were drawn on top of each other. For example, ``e`` followed by ``=`` will get you a Euro symbol: €, ``o`` followed by ``c`` will get you a copyright symbol: © - and ``1`` followed by ``2`` gets you a half fraction: ½.

These work anywhere you can type things. There's a list of some common ones `here <http://en.wikipedia.org/wiki/Compose_key#Common_compose_combinations>`_, and a `full list here <http://www.hermit.org/Linux/ComposeKeys.html>`_.

Activating your change without rebooting
-------------------------------------------------

Like it says at the top of that file, check ``/usr/share/doc/keyboard-configuration/README.Debian`` for what to do after you've modified it. Mine currently says:

    After modifying ``/etc/default/keyboard``, you can apply the changes to the Linux
    console by running ``setupcon``. If X is configured to use that file too, then the
    changes will become visible to X only if

    ``udevadm trigger \-\-subsystem-match=input \-\-action=change``

    is called, or the system is rebooted.

When it says Console, it means it -- not a terminal window, an actual login console -- try pressing ``Ctrl + Alt + F1`` and logging in, then running:

.. code-block:: console

    $ setupcon
    $ udevadm trigger --subsystem-match=input --action=change

These don't print anything out when they run, disconcertingly. Once you've run them in the Console, ``Ctrl + Alt + F7`` should get you back to the default console session you were in before.
