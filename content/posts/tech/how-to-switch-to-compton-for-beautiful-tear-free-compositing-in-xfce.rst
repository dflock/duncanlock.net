:title: How to switch to Compton for beautiful tear free compositing in XFCE
:slug: how-to-switch-to-compton-for-beautiful-tear-free-compositing-in-xfce
:date: 2013-06-07 00:05:59
:tags: xfce, compositing, compton, config, howto, linux
:meta_description: How to quickly & easily swap compositor in XFCE for beautiful, tear free, glassy smooth window dragging, drop shadows, etc...

I switched my XFCE machines over to use Compton for window compositing today - and it's a noticeable improvement.

A compositor glues your stacks of windows together to form the final image that you see on screen. It's responsible for any fancy effects like drop-shadows, as well drawing windows while dragging, resizing and minimizing or maximizing them. [#compositor]_

Compton does this *beautifully*. It does one thing and it does it well. It provides glassy smooth, tear free compositing and supports a few tasteful effects - drop shadows, fades and transparency.

I stumbled across this while searching for something else and found a great guide in the NeoWin forums [#neowin]_, where most of this info comes from, so thanks ViperAFK.

Switch off the existing compositor
------------------------------------

.. image:: /static/images/posts/how-to-switch-to-compton-for-beautiful-tear-free-compositing-in-xfce/xfce-applications-menu-settings-manager.png
    :align: right
    :alt: Screenshot of the XFCE Applications menu, with the Settings Manager highlighted.

You'll need to switch of any existing compositing you've got running, otherwise this won't work. Unless you know differently, this will be the default one, built into the XFCE window manager, xfwm4.

To switch this off, go into the Applications menu and click 'Settings Manager':

Then click 'Window Manager Tweaks', then the 'Compositor' tab, and un-tick the 'Enable Display Compositing' box:

.. image:: /static/images/posts/how-to-switch-to-compton-for-beautiful-tear-free-compositing-in-xfce/xfce-settings-manager-window-manager-tweaks-disable-compositing.png
  :alt: Screenshot of the XFCE Settings Manager - Window Manager Tweaks window, with 'Enable Display Compositing un-ticked'

Once you've switched off any existing compositor, you can install Compton.

Install Compton
---------------------

To do that, run the following commands in a terminal window. These will add the official Compton PPA [#compton]_ and then install it:

.. code-block:: console

    $ sudo apt-add-repository ppa:richardgv/compton
    $ sudo apt-get update
    $ sudo apt-get install compton

Configure Compton
----------------------------

Once it's installed, create a text file in ``~/.config/`` called ``compton.conf`` with the following contents:

.. code-block:: linux-config

    # Shadow
    shadow = true; # Enabled client-side shadows on windows.
    no-dnd-shadow = true; # Don't draw shadows on DND windows.
    no-dock-shadow = true; # Avoid drawing shadows on dock/panel windows.
    clear-shadow = true; # Zero the part of the shadow's mask behind the window (experimental).
    shadow-radius = 5;
    shadow-offset-x = -5;
    shadow-offset-y = -5;
    shadow-opacity = 0.5;
    # Set if you want different colour shadows
    # shadow-red = 0.0;
    # shadow-green = 0.0;
    # shadow-blue = 0.0;
    shadow-exclude = [ "name = 'Notification'", "name *= 'VLC'", "name *= 'compton'", "class_g = 'Conky'", "name *= 'Chromium'", "name *= 'Chrome'", "class_g ?= 'Cairo-dock'", "class_g ?= 'Notify-osd'", "name = 'Kupfer'", "name = 'xfce4-notifyd'" ];
    shadow-ignore-shaped = false;

    # Opacity
    menu-opacity = 1;
    inactive-opacity = 1;
    active-opacity = 1;
    frame-opacity = 1;
    inactive-opacity-override = false;
    alpha-step = 0.06;
    # inactive-dim = 0.2;
    # inactive-dim-fixed = true;
    # blur-background = true;
    # blur-background-frame = true;
    blur-background-fixed = false;
    blur-background-exclude = [ "window_type = 'dock'", "window_type = 'desktop'" ];

    # Fading
    fading = true;
    fade-delta = 4;
    fade-in-step = 0.03;
    fade-out-step = 0.03;
    # no-fading-openclose = true;
    fade-exclude = [ ];

    # Other
    backend = "glx";
    mark-wmwin-focused = true;
    mark-ovredir-focused = true;
    use-ewmh-active-win = false;
    detect-rounded-corners = true;
    detect-client-opacity = true;
    refresh-rate = 0;
    vsync = "opengl-swc";
    dbe = false;
    paint-on-overlay = true;
    sw-opti = false;
    unredir-if-possible = true;
    focus-exclude = [ ];
    detect-transient = true;
    detect-client-leader = true;
    invert-color-include = [ ];

    # GLX backend
    glx-no-stencil = true;
    glx-copy-from-front = false;
    # glx-use-copysubbuffermesa = true;
    # glx-no-rebind-pixmap = true;
    glx-swap-method = "undefined";

    # Window type settings
    wintypes:
    {
            tooltip =
            {
                    fade = true;
                    shadow = false;
                    opacity = 0.85;
                    focus = true;
            };
    };

Details on what each of these options does can be found `here <https://github.com/chjj/compton/blob/master/man/compton.1.asciidoc>`_. Some of them might need adjusting if you have crappy graphics drivers but should work for anyone with reasonable, up to date drivers & some kind of 3D graphics card.

It worked perfectly for me, on both my desktop dual monitor setup on an NVidia 8800GTS using the current xorg-edgers driver, 313.30 [#xorg-edgers]_ - and also on my laptop with a somew sort of crappy Mobility Radeon. By the look of the documentation, the most likely settings that might cause problems with drivers would be ``vsync`` and ``backend``.

Start Compton for the Current Session
-------------------------------------

Now we're going to make sure this is all working by starting compton. Press Alt+F2, type ``compton`` in the Application Launcher box, then press enter:

.. image:: /static/images/posts/how-to-switch-to-compton-for-beautiful-tear-free-compositing-in-xfce/xfce-application-finder-launching-compton.png
  :alt: Screenshot of the XFCE Applications Filder launching Compton.

Your screen will flicker and you should now have glassy smooth, tear free window dragging, with drop shadows and beautiful fading on window open/close & desktop switching, etc... Try dragging and few windows around, switching workspaces and open and closing things. Bathe in the smoothness.

Set Compton to auto-start
----------------------------

Assuming that worked, we'll make Compton start at startup. Go into the Applications menu and click 'Settings Manager', then click 'Session and Startup', then select the 'Application Autostart' tab:

.. figure:: /static/images/posts/how-to-switch-to-compton-for-beautiful-tear-free-compositing-in-xfce/xfce-settings-manager-session-and-startup-add-application.png
  :alt: Screenshot of the XFCE Settings Manager - Session and Startup window, showing the filled in 'Add application' box.

  Click the 'Add' button, then fill in the boxes like this.

Excluding some windows using xwininfo and shadow-exclude
-----------------------------------------------------------

.. figure:: /static/images/posts/how-to-switch-to-compton-for-beautiful-tear-free-compositing-in-xfce/xfce-notify-osd-window-corner.png
    :align: right

    Notice the square background behind the rounded corners on this volume notification.

You probably don't want shadows on every window - they don't work very well on notification popups, for example:

To exclude certain types of window, or certain applications, from having shadows, you can set the ``shadow-exclude`` setting. This setting is a list of conditions to match windows to. The simplest one is a wildcard match on the window name, which is done something like this: ``name *= 'Firefox'``.

Here's an example from my config file. It excludes various notification popups, VLC, Chrome, Kupfer [#kupfer]_, Cairo Dock and Conky:

.. code-block:: linux-config

    shadow-exclude = [
        "name *= 'compton'",

        "class_g ?= 'Notify-osd'",
        "name = 'Notification'",
        "name = 'xfce4-notifyd'",

        "name *= 'VLC'",
        "name *= 'Chromium'",
        "name *= 'Chrome'",
        "name = 'Kupfer'",

        "class_g = 'Conky'",
        "class_g ?= 'Cairo-dock'"
    ];

To add to this, you will need to know either the name or the class that X11 uses to refer to the window. There's a handy utility called ``xwininfo`` that will tell you this. To use it, run this from a console window:

.. code-block:: console

    $ xwininfo -stats -wm

Your mouse cursor will turn into a little cross-hair. Use this to click on the window you want to know about and ``xwininfo`` will print out some information about it:

.. code-block:: console

    xwininfo: Window id: 0x9a00073 "xfce4-notifyd"

      Absolute upper-left X:  1390
      Absolute upper-left Y:  16
      Relative upper-left X:  0
      Relative upper-left Y:  0
      Width: 274
      Height: 76
      Depth: 32
      Visual: 0xec
      Visual Class: TrueColor
      Border width: 0
      Class: InputOutput
      Colormap: 0x9a00003 (not installed)
      Bit Gravity State: NorthWestGravity
      Window Gravity State: NorthWestGravity
      Backing Store State: NotUseful
      Save Under State: no
      Map State: IsViewable
      Override Redirect State: no
      Corners:  +1390+16  -2064+16  -2064-1060  +1390-1060
      -geometry 274x76+1390+16

      Window manager hints:
          Client accepts input or input focus: No
          Initial state is Normal State
          Displayed on all desktops
          Window type:
              Notification
          Window state:
              Sticky
              Skip Pager
              Skip Taskbar
              Above
          Process id: 23420 on host duncan-desktop
          Frame extents: 0, 0, 0, 0


The window name is on the end of the first line ("xfce4-notifyd" in this case) and the class and type are further down. `Click here for more information about Compton conditionals <https://github.com/chjj/compton/blob/master/man/compton.1.asciidoc#format-of-conditions>`_. You can use this information to add exclusions for these windows to your config.

All done. If you have any improvements on this setup, let me know in `the comments <#article-comments-section>`_.

----------------

Footnotes & References
--------------------------

.. [#compositor] Some window managers have Compositing built in and some don't. `See here for more info <http://en.wikipedia.org/wiki/Compositing_window_manager>`_.
.. [#neowin] Most of this information came from this `great guide by ViperAFK on the NeoWin formus <http://www.neowin.net/forum/topic/1148464-using-compton-for-tear-free-compositing-in-xfce/>`_.
.. [#compton] Compton code is on `GitHub <https://github.com/chjj/compton>`_ and the PPA is on `Launchpad <https://launchpad.net/~richardgv/+archive/compton>`_.
.. [#xorg-edgers] xorg-edgers: "Packages for those who think development versions, experimental and unstable are for old ladies. We want our crack straight from upstream git! Well, straight, we want it built and packaged so we don't need to know what we're doing, except that we will break our X and put our computers on fire." `Use at your own risk! <https://launchpad.net/~xorg-edgers>`_
.. [#kupfer] `Kupfer: An extremely lightweight quick launcher, like Gnome DO <https://live.gnome.org/Kupfer>`_, "a convenient command and access tool", is a program that can launch applications and open documents, and access different types of objects and act on them.
