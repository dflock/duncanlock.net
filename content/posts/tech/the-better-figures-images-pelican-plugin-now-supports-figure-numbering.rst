:title: The Better Figures & Images Pelican plugin now supports Figure Numbering
:slug: the-better-figures-images-pelican-plugin-now-supports-figure-numbering
:date: 2013-10-19 22:08:26
:tags: pelican, plugin, python
:figure_numbers: true

.. figure:: {filename}/images/posts/better-figures-images-plugin-for-pelican/dummy-200x200.png
    :alt: A dummy placeholder image, 200x200 pixels square.

    This figure has automatic figure numbering.

I had a feature request for automatic figure numbering, like latex. As I was revamping this plugin for Pelican 3.3 anyway - and this didn't seem too hard - so I decided to add it.

So, the `Better Figures & Images plugin <{filename}/posts/tech/better-figures-and-images-plugin-for-pelican.rst>`_ now supports automatic figure numbering. To enable this for all posts, just add this to your config file:

.. code-block:: python

    FIGURE_NUMBERS = True

If you want to enable this per post, just add this to the metadata at the top of the post:

for restructuredText add this:

.. code-block:: rst

    :figure_numbers: true

and for Markdown add this:

.. code-block:: markdown

    figure_numbers: true

.. caution:: Can you have Figures in Markdown?

    I use reStructuredText for this site, and I'm not sure if you can even *have* Figures in markdown documents - and I haven't tested it, so caveat emptor.

It adds this:

.. code-block:: html

    <span class="fig_num" id="fig_X">Figure X: </span>

to the start of the figure captions, where ``X`` is the current figure number. It only does this to figures that already have captions - it'll skip figures without. It completely ignores images, even it they have captions - it only affects figures.

The markup it outputs look like this:

.. code-block:: html

    <div class="figure" style="width: 250px; max-width: 100%; height: auto;">
        <img style="width: 250px; max-width: 100%; height: auto;" alt="" src="/static/images/image.jpg" />
        <p class="caption">
            <span class="fig_num" id="fig_1">Figure 1: </span>This is the caption of the figure.
        </p>
        <div class="legend">
            Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod
            tempor incididunt ut labore et dolore magna aliqua.
        </div>
    </div>

.. note:: Automatic Figure numbering is new and isn't upstream yet - check out the ``figure_numbers`` branch from my git repo, `here <https://github.com/dflock/pelican-plugins/tree/figure_numbers>`_ if you want to use it.

    While we're on that subject, this plugin `does work with Pelican 3.3 <{filename}/posts/tech/how-i-upgraded-this-website-to-pelican-33.rst>`_, but that's not upstream yet either - the ``figure_numbers`` branch includes those fixes too.


The results look like this
==========================

Here are a few working examples, showing the results of using the plugin. The original rst source for these are available in the plugins ``/test`` folder:

.. figure:: {filename}/images/posts/better-figures-images-plugin-for-pelican/dummy-800x300.png

    This image is wider than the column it's in - try resizing the browser window.

    Because of the max-width: 100%, the image is resized to fit the column.

Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod
tempor incididunt ut labore et dolore magna aliqua.

.. figure:: {filename}/images/posts/better-figures-images-plugin-for-pelican/dummy-200x200.png
    :alt: A dummy placeholder image, 200x200 pixels square.

    This image is only 200px wide - smaller that the column it's in.

    The max-width: 100% doesn't stretch the image, because it's also got a width: 200px - making it shrink to fit.

Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod
tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam,
quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo
consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse
cillum dolore eu fugiat nulla pariatur.

.. figure:: {filename}/images/posts/better-figures-images-plugin-for-pelican/dummy-250x300.png
    :alt: map to buried treasure 2
    :align: right

    This is the third image caption.

    Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod
    tempor incididunt ut labore et dolore magna aliqua.

Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod
tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam,
quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo
consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse
cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non
proident, sunt in culpa qui officia deserunt mollit anim id est laborum.

.. image:: {filename}/images/posts/better-figures-images-plugin-for-pelican/dummy-200x200.png

Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod
tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam,
quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo
consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse
cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non
proident, sunt in culpa qui officia deserunt mollit anim id est laborum.

.. figure:: {filename}/images/posts/better-figures-images-plugin-for-pelican/dummy-250x300.png
    :alt: map to buried treasure 3
    :align: right

    This is the fourth image caption.

    Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod
    tempor incididunt ut labore et dolore magna aliqua.

Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod
tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam,
quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo
consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse
cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non
proident, sunt in culpa qui officia deserunt mollit anim id est laborum.

.. figure:: {filename}/images/posts/better-figures-images-plugin-for-pelican/dummy-250x300.png
    :alt: map to buried treasure 3
    :align: left

Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod
tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam,
quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo
consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse
cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non
proident, sunt in culpa qui officia deserunt mollit anim id est laborum.