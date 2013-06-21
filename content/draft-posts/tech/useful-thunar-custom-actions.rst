:title: Useful Thunar Custom Actions
:slug: useful-thunar-custom-actions
:date:
:tags: linux, xfce, config, howto, xubuntu, thunar

Document yours, plus howto

http://docs.xfce.org/xfce/thunar/custom-actions

Share Folder
------------

.. code-block:: bash

    net usershare add %n %f "" Everyone:R guest_ok=y

File Pattern:
    *
Appears if selection contains:
    Directories

Rename to lowercase
-------------------

.. code-block:: bash

    for file in %F; do rename 'y/A-Z/a-z/' $file; done

File Pattern:
    *
Appears if selection contains:
    All

Copy Contents to Clipboard
--------------------------

.. code-block:: bash

    cat %F | xclip -i -selection clipboard

File Pattern:
    *
Appears if selection contains:
    Text Files

Compress with PNGOUT
--------------------

Runs PNGOUT on each of the selected PNG Files, with default options.

.. code-block:: bash

    for file in %F; do pngout $file; done

File Pattern:
    *.png
Appears if selection contains:
    Image Files