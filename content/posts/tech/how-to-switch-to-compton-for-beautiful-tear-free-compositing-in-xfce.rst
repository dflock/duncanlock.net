:title: How to switch to Compton for beautiful tear free compositing in XFCE
:slug: how-to-switch-to-compton-for-beautiful-tear-free-compositing-in-xfce
:date: 2013-06-07 00:05:59
:tags: xfce, compositing, compton, config, howto, linux
:meta_description: How to quickly & easily setup & configure Compton in XFCE for beautiful, tear free, glassy smooth window dragging, drop shadows, etc...
:schema: Article

.. contents:: Contents:

I switched my XFCE machines over to use Compton for window compositing today - and it's a noticeable improvement.

A compositor glues your stacks of windows together to form the final image that you see on screen. It's responsible for any fancy effects like drop-shadows, as well drawing windows while dragging, resizing and minimizing or maximizing them. [#compositor]_

Compton does this *beautifully*. It does one thing and it does it well. It provides glassy smooth, tear free compositing and supports a few tasteful effects - drop shadows, fades and transparency.

I stumbled across this while searching for something else and found a great guide in the NeoWin forums [#neowin]_, where most of this info comes from, so thanks ViperAFK.

Switch off the existing compositor
------------------------------------

.. image:: {filename}/images/posts/how-to-switch-to-compton-for-beautiful-tear-free-compositing-in-xfce/xfce-applications-menu-settings-manager.png
    :align: right
    :alt: Screenshot of the XFCE Applications menu, with the Settings Manager highlighted.

You'll need to switch of any existing compositing you've got running, otherwise this won't work. Unless you know differently, this will be the default one, built into the XFCE window manager, xfwm4.

To switch this off, go into the Applications menu and click 'Settings Manager':

Then click 'Window Manager Tweaks', then the 'Compositor' tab, and un-tick the 'Enable Display Compositing' box:

.. image:: {filename}/images/posts/how-to-switch-to-compton-for-beautiful-tear-free-compositing-in-xfce/xfce-settings-manager-window-manager-tweaks-disable-compositing.png
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

.. code-block:: ini

    #################################
    #
    # Backend
    #
    #################################

    # Backend to use: "xrender" or "glx".
    # GLX backend is typically much faster but depends on a sane driver.
    backend = "glx";

    #################################
    #
    # GLX backend
    #
    #################################

    glx-no-stencil = true;

    # GLX backend: Copy unmodified regions from front buffer instead of redrawing them all.
    # My tests with nvidia-drivers show a 10% decrease in performance when the whole screen is modified,
    # but a 20% increase when only 1/4 is.
    # My tests on nouveau show terrible slowdown.
    # Useful with --glx-swap-method, as well.
    glx-copy-from-front = false;

    # GLX backend: Use MESA_copy_sub_buffer to do partial screen update.
    # My tests on nouveau shows a 200% performance boost when only 1/4 of the screen is updated.
    # May break VSync and is not available on some drivers.
    # Overrides --glx-copy-from-front.
    # glx-use-copysubbuffermesa = true;

    # GLX backend: Avoid rebinding pixmap on window damage.
    # Probably could improve performance on rapid window content changes, but is known to break things on some drivers (LLVMpipe).
    # Recommended if it works.
    # glx-no-rebind-pixmap = true;


    # GLX backend: GLX buffer swap method we assume.
    # Could be undefined (0), copy (1), exchange (2), 3-6, or buffer-age (-1).
    # undefined is the slowest and the safest, and the default value.
    # copy is fastest, but may fail on some drivers,
    # 2-6 are gradually slower but safer (6 is still faster than 0).
    # Usually, double buffer means 2, triple buffer means 3.
    # buffer-age means auto-detect using GLX_EXT_buffer_age, supported by some drivers.
    # Useless with --glx-use-copysubbuffermesa.
    # Partially breaks --resize-damage.
    # Defaults to undefined.
    glx-swap-method = "undefined";

    #################################
    #
    # Shadows
    #
    #################################

    # Enabled client-side shadows on windows.
    shadow = true;
    # Don't draw shadows on DND windows.
    no-dnd-shadow = true;
    # Avoid drawing shadows on dock/panel windows.
    no-dock-shadow = true;
    # Zero the part of the shadow's mask behind the window. Fix some weirdness with ARGB windows.
    clear-shadow = true;
    # The blur radius for shadows. (default 12)
    shadow-radius = 5;
    # The left offset for shadows. (default -15)
    shadow-offset-x = -5;
    # The top offset for shadows. (default -15)
    shadow-offset-y = -5;
    # The translucency for shadows. (default .75)
    shadow-opacity = 0.5;

    # Set if you want different colour shadows
    # shadow-red = 0.0;
    # shadow-green = 0.0;
    # shadow-blue = 0.0;

    # The shadow exclude options are helpful if you have shadows enabled. Due to the way compton draws its shadows, certain applications will have visual glitches
    # (most applications are fine, only apps that do weird things with xshapes or argb are affected).
    # This list includes all the affected apps I found in my testing. The "! name~=''" part excludes shadows on any "Unknown" windows, this prevents a visual glitch with the XFWM alt tab switcher.
    shadow-exclude = [
        "! name~=''",
        "name = 'Notification'",
        "name = 'Plank'",
        "name = 'Docky'",
        "name = 'Kupfer'",
        "name = 'xfce4-notifyd'",
        "name *= 'VLC'",
        "name *= 'compton'",
        "name *= 'Chromium'",
        "name *= 'Chrome'",
        "name *= 'Firefox'",
        "class_g = 'Conky'",
        "class_g = 'Kupfer'",
        "class_g = 'Synapse'",
        "class_g ?= 'Notify-osd'",
        "class_g ?= 'Cairo-dock'",
        "class_g ?= 'Xfce4-notifyd'",
        "class_g ?= 'Xfce4-power-manager'"
    ];
    # Avoid drawing shadow on all shaped windows (see also: --detect-rounded-corners)
    shadow-ignore-shaped = false;

    #################################
    #
    # Opacity
    #
    #################################

    menu-opacity = 1;
    inactive-opacity = 1;
    active-opacity = 1;
    frame-opacity = 1;
    inactive-opacity-override = false;
    alpha-step = 0.06;

    # Dim inactive windows. (0.0 - 1.0)
    # inactive-dim = 0.2;
    # Do not let dimness adjust based on window opacity.
    # inactive-dim-fixed = true;
    # Blur background of transparent windows. Bad performance with X Render backend. GLX backend is preferred.
    # blur-background = true;
    # Blur background of opaque windows with transparent frames as well.
    # blur-background-frame = true;
    # Do not let blur radius adjust based on window opacity.
    blur-background-fixed = false;
    blur-background-exclude = [
        "window_type = 'dock'",
        "window_type = 'desktop'"
    ];

    #################################
    #
    # Fading
    #
    #################################

    # Fade windows during opacity changes.
    fading = true;
    # The time between steps in a fade in milliseconds. (default 10).
    fade-delta = 4;
    # Opacity change between steps while fading in. (default 0.028).
    fade-in-step = 0.03;
    # Opacity change between steps while fading out. (default 0.03).
    fade-out-step = 0.03;
    # Fade windows in/out when opening/closing
    # no-fading-openclose = true;

    # Specify a list of conditions of windows that should not be faded.
    fade-exclude = [ ];

    #################################
    #
    # Other
    #
    #################################

    # Try to detect WM windows and mark them as active.
    mark-wmwin-focused = true;
    # Mark all non-WM but override-redirect windows active (e.g. menus).
    mark-ovredir-focused = true;
    # Use EWMH _NET_WM_ACTIVE_WINDOW to determine which window is focused instead of using FocusIn/Out events.
    # Usually more reliable but depends on a EWMH-compliant WM.
    use-ewmh-active-win = true;
    # Detect rounded corners and treat them as rectangular when --shadow-ignore-shaped is on.
    detect-rounded-corners = true;

    # Detect _NET_WM_OPACITY on client windows, useful for window managers not passing _NET_WM_OPACITY of client windows to frame windows.
    # This prevents opacity being ignored for some apps.
    # For example without this enabled my xfce4-notifyd is 100% opacity no matter what.
    detect-client-opacity = true;

    # Specify refresh rate of the screen.
    # If not specified or 0, compton will try detecting this with X RandR extension.
    refresh-rate = 0;

    # Set VSync method. VSync methods currently available:
    # none: No VSync
    # drm: VSync with DRM_IOCTL_WAIT_VBLANK. May only work on some drivers.
    # opengl: Try to VSync with SGI_video_sync OpenGL extension. Only work on some drivers.
    # opengl-oml: Try to VSync with OML_sync_control OpenGL extension. Only work on some drivers.
    # opengl-swc: Try to VSync with SGI_swap_control OpenGL extension. Only work on some drivers. Works only with GLX backend. Known to be most effective on many drivers. Does not actually control paint timing, only buffer swap is affected, so it doesn’t have the effect of --sw-opti unlike other methods. Experimental.
    # opengl-mswc: Try to VSync with MESA_swap_control OpenGL extension. Basically the same as opengl-swc above, except the extension we use.
    # (Note some VSync methods may not be enabled at compile time.)
    vsync = "opengl-swc";

    # Enable DBE painting mode, intended to use with VSync to (hopefully) eliminate tearing.
    # Reported to have no effect, though.
    dbe = false;
    # Painting on X Composite overlay window. Recommended.
    paint-on-overlay = true;

    # Limit compton to repaint at most once every 1 / refresh_rate second to boost performance.
    # This should not be used with --vsync drm/opengl/opengl-oml as they essentially does --sw-opti's job already,
    # unless you wish to specify a lower refresh rate than the actual value.
    sw-opti = false;

    # Unredirect all windows if a full-screen opaque window is detected, to maximize performance for full-screen windows, like games.
    # Known to cause flickering when redirecting/unredirecting windows.
    # paint-on-overlay may make the flickering less obvious.
    unredir-if-possible = true;

    # Specify a list of conditions of windows that should always be considered focused.
    focus-exclude = [ ];

    # Use WM_TRANSIENT_FOR to group windows, and consider windows in the same group focused at the same time.
    detect-transient = true;
    # Use WM_CLIENT_LEADER to group windows, and consider windows in the same group focused at the same time.
    # WM_TRANSIENT_FOR has higher priority if --detect-transient is enabled, too.
    detect-client-leader = true;

    #################################
    #
    # Window type settings
    #
    #################################

    wintypes:
    {
        tooltip =
        {
            # fade: Fade the particular type of windows.
            fade = true;
            # shadow: Give those windows shadow
            shadow = false;
            # opacity: Default opacity for the type of windows.
            opacity = 0.85;
            # focus: Whether to always consider windows of this type focused.
            focus = true;
        };
    };

Details on what each of these options does can be found `here <https://github.com/chjj/compton/blob/master/man/compton.1.asciidoc>`_. Some of them might need adjusting if you have crappy graphics drivers but should work for anyone with reasonable, up to date drivers & some kind of 3D graphics card.

It worked perfectly for me, on both my desktop dual monitor setup on an NVidia 8800GTS using the current xorg-edgers driver, 313.30 [#xorg-edgers]_ - and also on my laptop with a some sort of crappy Mobility Radeon. By the look of the documentation, the most likely settings that might cause problems with drivers would be ``vsync`` and ``backend``.

Start Compton for the Current Session
-------------------------------------

Now we're going to make sure this is all working by starting compton. Press Alt+F2, type ``compton`` in the Application Launcher box, then press enter:

.. image:: {filename}/images/posts/how-to-switch-to-compton-for-beautiful-tear-free-compositing-in-xfce/xfce-application-finder-launching-compton.png
  :alt: Screenshot of the XFCE Applications Filder launching Compton.

Your screen will flicker and you should now have glassy smooth, tear free window dragging, with drop shadows and beautiful fading on window open/close & desktop switching, etc... Try dragging and few windows around, switching workspaces and open and closing things. Bathe in the smoothness.

Set Compton to auto-start
----------------------------

Assuming that worked, we'll make Compton start at startup. Go into the Applications menu and click 'Settings Manager', then click 'Session and Startup', then select the 'Application Autostart' tab:

.. figure:: {filename}/images/posts/how-to-switch-to-compton-for-beautiful-tear-free-compositing-in-xfce/xfce-settings-manager-session-and-startup-add-application.png
  :alt: Screenshot of the XFCE Settings Manager - Session and Startup window, showing the filled in 'Add application' box.

  Click the 'Add' button, then fill in the boxes like this.

Excluding some windows using xwininfo and shadow-exclude
-----------------------------------------------------------

.. figure:: {filename}/images/posts/how-to-switch-to-compton-for-beautiful-tear-free-compositing-in-xfce/xfce-notify-osd-window-corner.png
    :align: right

    Notice the square background behind the rounded corners on this volume notification.

You probably don't want shadows on every window - they don't work very well on notification popups, for example.

To exclude certain types of window, or certain applications, from having shadows, you can set the ``shadow-exclude`` setting. This setting is a list of conditions to match windows to. The simplest one is a wild card match on the window name, which is done something like this: ``name *= 'Firefox'``.

Here's an example from my config file. It excludes various notification popups, VLC, Chrome, Kupfer [#kupfer]_ and other problem apps:

.. code-block:: ini

    shadow-exclude = [
        "! name~=''",
        "name = 'Notification'",
        "name = 'Plank'",
        "name = 'Docky'",
        "name = 'Kupfer'",
        "name = 'xfce4-notifyd'",
        "name *= 'VLC'",
        "name *= 'compton'",
        "name *= 'Chromium'",
        "name *= 'Chrome'",
        "name *= 'Firefox'",
        "class_g = 'Conky'",
        "class_g = 'Kupfer'",
        "class_g = 'Synapse'",
        "class_g ?= 'Notify-osd'",
        "class_g ?= 'Cairo-dock'",
        "class_g ?= 'Xfce4-notifyd'",
        "class_g ?= 'Xfce4-power-manager'"
    ];

To add to this, you will need to know either the name or the class that X11 uses to refer to the window. There's a handy utility called ``xwininfo`` that will tell you this. To use it, run this from a console window:

.. code-block:: console

    $ xwininfo -stats -wm

Your mouse cursor will turn into a little cross-hair. Use this to click on the window you want to know about and ``xwininfo`` will print out some information about it. For example, clicking on an XFCE notification bubble will print something like this:

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
.. [#neowin] Some of this information here came from this `great guide by ViperAFK on the NeoWin formus <http://www.neowin.net/forum/topic/1148464-using-compton-for-tear-free-compositing-in-xfce/>`_ and `this one by screaminj3sus on ubuntuforums.org <http://ubuntuforums.org/showthread.php?t=2144468>`_, as suggested by Saravanan Kumar in the comments.
.. [#compton] Compton code is on `GitHub <https://github.com/chjj/compton>`_ and the PPA is on `Launchpad <https://launchpad.net/~richardgv/+archive/compton>`_.
.. [#xorg-edgers] xorg-edgers: "Packages for those who think development versions, experimental and unstable are for old ladies. We want our crack straight from upstream git! Well, straight, we want it built and packaged so we don't need to know what we're doing, except that we will break our X and put our computers on fire." `Use at your own risk! <https://launchpad.net/~xorg-edgers>`_
.. [#kupfer] `Kupfer: An extremely lightweight quick launcher, like Gnome DO <https://live.gnome.org/Kupfer>`_, "a convenient command and access tool", is a program that can launch applications and open documents, and access different types of objects and act on them.
