:title: Useful Thunar Custom Actions
:slug: useful-thunar-custom-actions
:date: 2013-06-28 14:11:43
:tags: linux, xfce, config, howto, xubuntu, thunar, png
:thumbnail: /static/images/posts/useful-thunar-custom-actions/thunar-icon.png
:meta_description: Thunar has a simple mechanism that allows you to easily add new commands to the right click menu of files and folders. Here's how to do it.

.. contents:: Contents:

.. image:: /static/images/posts/useful-thunar-custom-actions/thunar-icon.png
    :alt: Thunar's icon, a beautifully rendered, stylized version of Thor's hammer, Mjölnir.

Thunar - XFCE & XUbuntu's small but perfectly formed file manager - has a simple mechanism that allows you to easily add new commands to the right click menu of files and folders. These are called `Custom Actions <http://docs.xfce.org/xfce/thunar/custom-actions>`_ and are easy to create... here's how to do it.

Click the **Edit** menu, then click '**Configure custom actions...**'. This will take you to the Custom Actions Manager, where you can create, edit or delete your custom actions.

You can enter anything into the command box, including complex bash scripts, names of scripts or executables on the PATH, or the full path and filename of the command you want to run.

.. image:: /static/images/posts/useful-thunar-custom-actions/thunar-custom-actions-edit-1.png

On the '**Appearance Conditions**' tab, you tell Thunar when you want your item to appear in the right click menu:

.. figure:: /static/images/posts/useful-thunar-custom-actions/thunar-custom-actions-edit-3.png
    :align: right

    Now, when I right click on a text file, I have extra options in my menu.

I've included my custom actions below - and you can find `more around the web <https://www.google.ca/search?q=thunar+custom+actions>`_. I've only included ones here that aren't commonly listed elsewhere.

My Thunar Custom Actions
---------------------------

To use these yourself, just copy and paste these names, descriptions & commands into new actions in your Custom Actions Manager:

Share Folder
============
Description:
    Shares the currently selected folder, giving everyone read access.
Command:
    .. code-block:: bash

        net usershare add %n %f "" Everyone:R guest_ok=y
File Pattern:
    ``*``
Appears if selection contains:
    Directories


Flatten Folder
==============
Description:
    Moves all files from subfolders to parent (current) folder, then removes all empty folders inside the current folder.
Command:
    .. code-block:: bash

        find . -mindepth 2 -type f -exec mv "{}" . \; && find . -type d -empty -delete
File Pattern:
    ``*``
Appears if selection contains:
    Directories

Rename to lower-case
====================
Description:
    Rename the currently selected files, making the filenames lower-case.
Command:
    .. code-block:: bash

        for file in %F; do rename 'y/A-Z/a-z/' "$file"; done
File Pattern:
    ``*``
Appears if selection contains:
    *All*

Copy Contents to Clipboard
==========================
Description:
    Copies the contents of the selected file to the clipboard. This requires ``xclip`` - which you may need to install using your distribution's package manager.
Command:
    .. code-block:: bash

        cat %F | xclip -i -selection clipboard
File Pattern:
    ``*``
Appears if selection contains:
    Text Files


Compare
====================
Description:
    Compares selected files or folders in `Meld <http://meldmerge.org/>`_
Command:
    .. code-block:: bash

        meld %F
File Pattern:
    ``*``
Appears if selection contains:
    Directories, Text Files


Compress with Advpng
====================

Description:
    Runs `Advpng <http://en.wikipedia.org/wiki/Advpng>`_ on each of the selected PNG Files.
Command:
    .. code-block:: bash

        for file in %F; do advpng -z -4 -q $file; done
File Pattern:
    ``*.png``
Appears if selection contains:
    Image Files


Quantize with pngnq
====================

Description:
    Reduce to 8bit colour, by running `pngnq <https://github.com/stuart/pngnq>`_ on each of the selected PNG Files.
Command:
    .. code-block:: bash

        for file in %F; do pngnq -s1 $file; done
File Pattern:
    ``*.png``
Appears if selection contains:
    Image Files
