:title: How I built this website, using Pelican: Part 2 - Themes
:slug: how-i-built-this-website-using-pelican-part-2-themes
:date: 2013-07-11 14:06:18
:tags: web, pelican, python, tutorial
:category: tech
:_parts:  How I built this website, using Pelican
:meta_description: A complete breakdown showing you how to build a professional grade Pelican theme, using this site's theme as an example.
:status: draft

The Pelican quickstart site that we created in `Part 1 <|filename|how-i-built-this-website-using-pelican-part-1-setup.rst>`_ used the default theme - which you will probably want to change or, at least, customize. In this post I break down the Pelican theme I created for this site and show you exactly how it's built. I'll be going through each part of the theme in depth, explaining why I did things that way and how each part works.

The theme for this site is professional grade - high quality, polished and responsive. It puts the `focus on the reader and is 100% easy to read <http://ia.net/blog/100e2r/>`_. It also takes into account best practices for both social media and :abbr:`SEO (Search Engine Optimization)`, so that you can make the most of your writing.

The Structure of a Pelican Theme
=================================

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
- use filename no query param for name