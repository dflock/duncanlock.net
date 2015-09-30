:title: What would a UNIX Music collection look like?
:slug: what-would-a-unix-music-collection-look-like
:date: 2015-08-12 12:02:18
:tags: tech, music, linux, unix
:meta_description:
:status: draft

What would a unixy music collection actually look like, if we could start from scratch?

Everything Is A File
======================

- Everything is a file - including metadata
- Separate music data from meta data
- Separate static metadata from dynamic 'play' metadata - playcounts, last played time, etc...
- Each 'thing' in a collection: an album, an artist, a track - becomes a folder

Hierarchical Folder Structure
-----------------------------

.. code-block:: sh

    Music/
    -- library-meta.yml
    -- Collections/
    ---- global-collections-meta.yml
    ---- By Artist/
    ------ by-artist-collection-meta.yml
    ------ ABBA/
    -------- artist-meta.yml
    -------- artist-photo.jpg
    -------- Waterloo/
    ---------- album-meta.yml
    ---------- cover.jpg
    ---------- back.jpg
    ---------- booklet.pdf
    ---------- playlist-mp3.m3u
    ---------- playlist-flac.m3u
    ---------- 01 - Waterloo/
    ---------- 02 - Sitting in the Palmtree/
    ------------ track-meta-static.yml
    ------------ track-meta-play.yml
    ------------ Sitting in the Palmtree.flac
    ------------ Sitting in the Palmtree.mp3
    ---------- 03 - ....
    ...
    ---- By Decade/
    ------ 70s/
    -------- ABBA/
    ---------- Waterloo/ (symlink)

- could have a FUSE file system to make this look like a regular music collection, or vice versa
- possible multiple versions of anything at any node - multiple version of a track, of artist (lineup)
- Meta data is inherited/combined up the tree to the Library level when playing
- can use standard tools to add/edit metadata in bulk
- can easily write scripts to process library
- can write scripts to create new collections from existing collections & metadata, eg: - by Genre, by BPM, etc...

The Music Is The DB & Don't Repeat Yourself
============================================
- Can do collections via symlinks
- Can do compilation albums via symlinks to the tracks (if you already have them), as we've separated out the metadata
- No artwork or tags inside music files.

Classical Music?
================

Allowing multiple versions of things helps - different orchestras, different conductors is just a different version of the same piece?

Questions
=========

- Does this remove the need for players, mostly? Or just make the library view == the file system?
- Can you point existing players at this a have it just work? Would making some of the files .dotfiles help?
- Classical music? Does this really help with their actual issues?
- Would this give you anything that regular people might actually care about?
- Is there an existing standard for external metadata? External replaygain data?
- Which metadata file format to use - YAML? JSON?
- Would a read-only FUSE (that stitches the metadata & music back together) filesystem be a pre-requisite for a player to work well using this system?
- Discuss why the UNIX way of thinking about things is powerful
- Good collection of existing tools that can generate metadata and dump to a file?

How To...
=========

Install Pre-requisites
-----------------------

.. code-block:: bash

    $ sudo apt-get install python-mutagen
    $ git clone git@github.com:dflock/unix-music.git ~/bin

Dump tags from an audio file to a yml file
------------------------------------------

.. code-block:: bash

    $ mid3v2 --list test.mp3 > metadata.txt
    # TODO: Convert to yml


Clear all the tags from an audio file
-------------------------------------

.. code-block:: sh

    $ mid3v2 --delete-all test.mp3

Extract embeded images from an audio file
-------------------------------------------

.. code-block:: sh

  $ python export_apic2.py test.mp3

  2 images found.
  test-albumart-1.jpg
  test-albumart-2.jpg


Remove embedded images from an audio file
---------------------------------------------

.. code-block:: sh

    $ mid3v2 --delete-frames=APIC test.mp3

Disadvantages?
==============

- Existing players won't work as well out of the box - expect tags inside music files.
