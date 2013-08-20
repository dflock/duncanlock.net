:title: How I built this website, using Pelican: Part 2 - Themes
:slug: how-i-built-this-website-using-pelican-part-2-themes
:date: 2013-07-11 14:06:18
:tags: web, pelican, python, tutorial
:category: tech
:_parts:  How I built this website, using Pelican
:meta_description: A complete breakdown showing you how to build a professional grade Pelican theme, using this site's theme as an example.
:status: draft

The Pelican quickstart site that we created in `Part 1 <|filename|how-i-built-this-website-using-pelican-part-1-setup.rst>`_ used the default theme - which you will probably want to change or, at least, customize. In this post I break down the Pelican theme I created for this site and show you exactly how it's built. I'll be going through each part of the theme in depth, explaining why I did things that way and how each part works.

The theme for this site is professional grade - high quality, polished and responsive. It puts the `focus on the reader and is 100% easy to read <http://ia.net/blog/100e2r/>`_ and works flawlessly on any screen size, including mobiles & tablets. It also takes into account best practices for both social media and :abbr:`SEO (Search Engine Optimization)`, so that you can make the most of your writing.

Before We Begin, a Word About Editing Workflow
==============================================

I'm going to assume that you're `carrying on from Part 1 <|filename|how-i-built-this-website-using-pelican-part-1-setup.rst>`_ - so we're using a python ``virtualenv`` & ``virtualenvwrapper``, for example. With that in mind, here's the workflow I'd recommend for working on your site. Open a text editor, open a browser and point it at your local site, then, in a Terminal window run the following:

.. code-block:: console

    $ workon duncanlock.net-pelican
    $ pelican -rs pelicanconf.py

    --- AutoReload Mode: Monitoring `content`, `theme` and `settings` for changes. ---
    -> Modified: content, theme, settings. re-generating...
    Done: Processed 13 articles and 1 pages in 5.83 seconds.


This should just sit there and monitor the site for changes and automatically rebuild it whenever anything changes. To test it, open ``pelicanconf.py`` in your text editor and just save it - this should trigger an automatic rebuild.

Standing on the Shoulders of Giants
===================================

My theme - which I'm currently calling Blueprint - wasn't created from scratch. It was based on an existing theme, from the pelican-themes repository. To checkout this repository and see what themes are available, just check it out from github with ``git``:

.. code-block:: console

    $ git clone --recursive git@github.com:getpelican/pelican-themes.git

Note that this repository uses sub-modules, so you need to use ``\-\-recursive`` when cloning. In order to pull the latest changes in the future, you need to do this:

.. code-block:: console

    $ cd pelican-themes
    $ git pull --recurse-submodules

Once you've done this, you can try out the different themes by creating or changing the following setting in your ``pelicanconf.py`` file:

.. code-block:: python

    # Which theme to use
    THEME = '../pelican-themes/built-texts'

Just point this to a different theme folder and re-generate your site to see what it looks like. If you're using the editing workflow mentioned above, just saving the file should rebuild the site automatically.

My theme was based on the theme called `'Built Texts' by Abhishek L <http://theanalyst.github.com>`_ - you can see this theme in action at his site. You can definitely see the family resemblance, but the two themes have already diverged quite a bit.

I suggest that you try the different themes in the pelican-themes repository and either find one you like and stop reading, or find one you almost-sorta-like -- and want to use as a base for your theme.

Forking or Copying to a New Theme
---------------------------------
You now have some options - you can either fork the ``pelican-plugins`` repository on github, then copy the theme folder you wish to start from and rename it - or you can just copy the theme folder somewhere else - such as your sites ``./themes`` folder - and work on it separately.

I'm not going to explain in depth how to use github here - they have excellent help documentation. If you want to

The Structure of a Pelican Theme
=================================

You can find the minimum requirements for a working pelican theme `here <https://pelican.readthedocs.org/en/latest/themes.html>`_, but my theme expands on this a bit, to add extra features. The current structure of the blueprint theme looks like this.

.. code-block:: console

    ├── themes
        ├── blueprint
            ├── static
            │   ├── css
            │   │   ├── fontello.css
            │   │   ├── main.css
            │   │   ├── print.css
            │   │   ├── pygments.css
            │   │   └── pygments-monokai.css
            │   ├── font
            │   │   ├── fontello.eot
            │   │   ├── fontello.svg
            │   │   ├── fontello.ttf
            │   │   └── fontello.woff
            │   └── js
            │       └── html5.js
            └── templates
                ├── analytics.html
                ├── archives.html
                ├── article.html
                ├── article-sidebar.html
                ├── article-sidebar-multipart.html
                ├── article-sidebar-toc.html
                ├── author.html
                ├── base.html
                ├── categories.html
                ├── category.html
                ├── colophon.html
                ├── disqus.html
                ├── googleplus.html
                ├── index.html
                ├── page.html
                ├── pagination.html
                ├── period_archives.html
                ├── tag.html
                ├── tags.html
                └── twitter.html

Metadata & Microdata
======================

Metadata like ``title`` and ``description`` have always been important for your site's appearance in search results and for SEO generally - so the blueprint theme is very careful to provide complete support for all the traditional metadata - plus a few newer ones like favicons for phones & tablets.

Microdata is becoming more and more important and is increasingly being used by large services like Twitter, Google+ and, crucially, Google Search. Marking up your content with mircodata is a simple and unobtrusive way of adding machine readable metadata to your content - giving you an advantage when your content appears on services that can use this data.

The blueprint theme fully supports the following microdata:

Twitter Cards
-------------

.. epigraph::

   Twitter cards make it possible for you to attach media experiences to Tweets that link to your content. Simply add a few lines of HTML to your webpages, and users who Tweet links to your content will have a "card" added to the Tweet that’s visible to all of their followers.

   -- https://dev.twitter.com/docs/cards

This is what this looks like in action:

.. image:: /static/images/posts/how-i-built-this-website-using-pelican-part-2-themes/twitter-card-example.png



Authorship
-----------
.. epigraph::

   Google is piloting the display of author information in search results to help users discover great content.

   -- https://support.google.com/webmasters/answer/1408986?hl=en

This is what this looks like in a Google Search result when this is setup and working:

.. image:: /static/images/posts/how-i-built-this-website-using-pelican-part-2-themes/google-authorship-microdata-results.png

Google In-depth Articles
-------------------------

This feature prefers articles which use schema.org Article microdata, specifically the following items:

- headline
- alternativeHeadline
- image
- description
- datePublished
- articleBody

See `here for more information about Google In-depth articles <https://support.google.com/webmasters/answer/3280182>`_.

Supporting ``image`` also has other benefits, notably Google+ and Facebook, which will both default that image in as the thumbnail if you post a link:

.. image:: /static/images/posts/how-i-built-this-website-using-pelican-part-2-themes/google-plus-image-thumbnail-example.png
.. image:: /static/images/posts/how-i-built-this-website-using-pelican-part-2-themes/facebook-image-thumbnail-example.png



The Main Theme Components
=========================

base.html
---------

index.html
----------

article.html
------------


The Supporting Cast
===================

article-sidebar.html
--------------------



The Devil is in the Detail
==========================

Mention


A Multitude of Favicons
-------------------------

Put this into the ``<head>`` section of ``base.html``:

.. code-block:: html+jinja

    {# Favicons #}
        <meta itemprop="image" content="{{ SITEURL }}/static/images/favicon-128x128.png">
        <link rel="shortcut icon" href="{{ SITEURL }}/favicon.ico">
        <link rel="apple-touch-icon" href="{{ SITEURL }}/static/images/apple-touch-icon.png">
        <link rel="apple-touch-icon" sizes="72x72" href="{{ SITEURL }}/static/images/apple-touch-icon-72x72.png">
        <link rel="apple-touch-icon" sizes="114x114" href="{{ SITEURL }}/static/images/apple-touch-icon-114x114.png">

Google Analytics Integration
------------------------------

This goes into your ``publishconf.py`` file:

.. code-block:: python

    # Output Google Analytics code
    GOOGLE_ANALYTICS_ID = "UA-XXXXXXX-X"
    GOOGLE_ANALYTICS_UNIVERSAL = True

This goes at the bottom of ``base.html``:

.. code-block:: html_jinja

    {% include "analytics.html" %}

    </body>
    </html>

and ``analytics.html`` looks like this:

.. code-block:: html+jinja

    {% if GOOGLE_ANALYTICS_ID %}
        {% if GOOGLE_ANALYTICS_UNIVERSAL %}
            <script>
              (function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
              (i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
              m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
              })(window,document,'script','//www.google-analytics.com/analytics.js','ga');

              ga('create', '{{GOOGLE_ANALYTICS_ID}}', 'duncanlock.net');
              ga('send', 'pageview');
            </script>
        {% else %}
            <script>var _gaq=[['_setAccount','{{GOOGLE_ANALYTICS_ID}}'],['_trackPageview']];(function(d,t){var g=d.createElement(t),s=d.getElementsByTagName(t)[0];g.src='//www.google-analytics.com/ga.js';s.parentNode.insertBefore(g,s)}(document,'script'))</script>
        {% endif %}
    {% endif %}

Plugins I use, which affect the theme
=======================================

webassets
--------------
- rearrange theme files
- first name in list of output is actual output filename
- use filename not query param for name