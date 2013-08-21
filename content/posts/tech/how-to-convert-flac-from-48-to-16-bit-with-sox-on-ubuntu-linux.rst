:title: How to convert FLAC files from 24/48 bit to 16 bit on Ubuntu Linux
:slug: how-to-convert-flac-files-from-24-48-bit-to-16-bit-on-ubuntu-linux
:date: 2013-08-19 22:40:59
:tags: music, convert, howto, flac, linux, sonos
:category: tech
:meta_description: How to convert FLAC files from 24/48bit to 16bit - converting all the files in a folder, preserving the metadata.

I recently needed to convert some FLAC music files from the increasingly common 48 bit encoding, down to 16 bit at 44100 kHz, so that they'll play on my Sonos. Here's how to do it:

If you don't already have ``sox`` installed, do this to install it:

.. code-block:: console

    $ sudo apt-get install sox

Then run this to do the conversion, in the folder with music in:

.. code-block:: bash

    $ mkdir resampled
    $ for flac in *.flac; do sox -S "${flac}" -r 44100 -b 16 ./resampled/"${flac}"; done

And that's it - it will convert all the ``.flac`` files in that folder to 16 bit at 44100 kHz and put the result into the ``./resampled`` subfolder, preserving the metadata.
