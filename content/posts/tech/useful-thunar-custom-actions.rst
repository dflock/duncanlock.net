:title: Useful Thunar Custom Actions
:slug: useful-thunar-custom-actions
:date: 2013-06-20 17:25:43
:tags: linux, xfce, config, howto, xubuntu, thunar
:status: draft
:thumbnail: /static/images/thunar-icon.png

.. contents:: Contents:

.. image:: /static/images/thunar-icon.png
    :alt: Thunar's icon, a beautifully rendered, stylized version of Thor's hammer, Mjölnir.

http://docs.xfce.org/xfce/thunar/custom-actions

My Custom Actions
---------------------------

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

Rename to lower-case
====================
Description:
    Rename the currently selected files, making the filenames lower-case.
Command:
    .. code-block:: bash

        for file in %F; do rename 'y/A-Z/a-z/' $file; done
File Pattern:
    ``*``
Appears if selection contains:
    *All*

Copy Contents to Clipboard
==========================
Description:
    Copies the contents of the selected file to the clipboard.
Command:
    .. code-block:: bash

        cat %F | xclip -i -selection clipboard
File Pattern:
    ``*``
Appears if selection contains:
    Text Files

Compress with PNGOUT
====================
Description:
    Runs PNGOUT on each of the selected PNG Files, with default options.
Command:
    .. code-block:: bash

        for file in %F; do pngout $file; done
File Pattern:
    ``*.png``
Appears if selection contains:
    Image Files

Compare
====================
Description:
    Compares selected files or folders in Meld
Command:
    .. code-block:: bash

        meld %F
File Pattern:
    ``*``
Appears if selection contains:
    Directories, Text Files