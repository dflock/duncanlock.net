:title: How to create thumbnails for PDFs with ImageMagick on Linux
:slug: how-to-create-thumbnails-for-pdfs-with-imagemagick-on-linux
:date: 2013-11-18 20:05:38
:tags: linux, pdf, imagemagick, howto

To create image thumbnails from a PDF document, run this in a terminal window:

.. code-block:: bash

    convert -thumbnail x300 -background white -alpha remove input_file.pdf[0] output_thumbnail.png

The parameters to `convert <http://www.imagemagick.org/script/command-line-options.php>`_ do the following things:

+--------------------------+-------------------------------------------------------------------------------+
| Parameter                | Effect                                                                        |
+==========================+===============================================================================+
| ``-thumbnail``           | Similar to -resize, but optimized for speed and strips metadata.              |
+--------------------------+-------------------------------------------------------------------------------+
| ``x300``                 | Make the thumbnail 300px tall, and whatever width maintains the aspect ratio. |
+--------------------------+-------------------------------------------------------------------------------+
| ``-background white``    | Sets the thumbnail background to white.                                       |
+--------------------------+-------------------------------------------------------------------------------+
| ``-alpha remove``        | Removes the alpha channel from the thumbnail output.                          |
+--------------------------+-------------------------------------------------------------------------------+
| ``input_file.pdf``       | The PDF file to use as input.                                                 |
+--------------------------+-------------------------------------------------------------------------------+
| ``[0]``                  | The page number of the input file to use for the thumbnail.                   |
+--------------------------+-------------------------------------------------------------------------------+
| ``output_thumbnail.png`` | The output thumbnail file to create.                                          |
+--------------------------+-------------------------------------------------------------------------------+

If you want larger thumbnails, just change the ``x300`` parameter to match. If you want to output .jpg's (or anything else, like .gif), just change the file extension on the ``output_thumbnail.png`` parameter. If you leave the ``[0]`` off the end of the input filename, you'll get a thumbnail for each page, not just the first; setting it to ``[1]`` will get you a thumbnail of the second page, and so on...

Do a whole folder at a time
---------------------------

To create thumbnails for a whole folder of PDF's, do this:

.. code-block:: bash

    for f in *.pdf; do convert -thumbnail x300 -background white -alpha remove "$f"[0] "$f".png; done

This will create thumbnails with filenames that match the input PDF's, except with an extra ``.pdf`` extension.

Requirements
------------

This requires ImageMagick and Ghostscript, which you can install like this:

.. code-block:: bash

    sudo apt-get install imagemagick ghostscript

This technique should also work on a Mac, provided you have these both installed.
