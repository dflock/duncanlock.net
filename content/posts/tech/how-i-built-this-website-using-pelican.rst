:title: How I built this website, using Pelican
:slug: how-i-built-this-website-using-pelican
:date: 2013-04-29 17:19:53
:tags: web, pelican, python, tutorial
:category: tech

As I `mentioned previously <|filename|/posts/news/new-site-built-on-pelican.rst>`_, this site was put together using `Pelican <http://getpelican.com/>`_ -- a static site generator, written in Python.

.. figure:: /static/images/pelecanus-occidentalis-diagram.png
    :alt: Blueprint style diagram showing a brown Pelican, flying. The diagram point out it's Yellow Head, Large beak and pouch for fishing, long neck, white chest and grey body.

    Pelecanus Occidentalis - the Brown Pelican.

    Image Credit: Original clipart `Flying Pelican from OpenClipart, by molumen, Public Domain <http://openclipart.org/detail/2798/flying-pelican-by-molumen>`_. More on `Pelican, the bird <http://en.wikipedia.org/wiki/Brown_Pelican>`_.

Static site generators take your content, pour it into your templates and output the result as static pre-generated HTML, CSS, JS & image files. You can then just upload the result to your server and you're done. All you need on the server is a web server of some sort, like Apache or Nginx - anything really - all it's doing is serving static pages.

The huge advantage of this setup is simplicity:
--------------------------------------------------

1. You can write your content in Markdown, reStructuredText or AsciiDoc - all simple text formats, designed to facilitate writing and get out of your way. You can use any writing tool you prefer, as long as it can output plain text.
2. Whenever you make changes, Pelican can automatically regenerate the site, so you can see your changes immediately.
3. When you're done, Pelican can automatically upload the site to your web server, or you can do it, just by uploading a folder.
4. The web server generally requires no setup - all you need is a web server that can serve static content (which is all of them) -- and no extra software or configuration; no PHP, no database, nothing.
5. Because the server is only serving pre-generated static content, a Pelican site is very lightweight, using very few server resources.
6. Because you've only got one thing running on the server, you have much less exposure to security problems - no WordPress, no PHP - just the OS & the web server.

Installation & Basic Setup
-----------------------------

Pelican uses Python, so you'll need that installed.

- Install, quick start
    - Python, pip, virtualenv & wrapper
- Theme
- Link to: using incron, when I figure that out with virtualenvs post
- Link to: Apache vitual server setup post

Date based posts
----------------------

.. code-block:: python

    ARTICLE_URL = 'blog/{date:%Y}/{date:%m}/{date:%d}/{slug}/'
    ARTICLE_SAVE_AS = 'blog/{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'

    YEAR_ARCHIVE_SAVE_AS = 'blog/{date:%Y}/index.html'
    MONTH_ARCHIVE_SAVE_AS = 'blog/{date:%Y}/{date:%m}/index.html'
    DAY_ARCHIVE_SAVE_AS = 'blog/{date:%Y}/{date:%m}/{date:%d}/index.html'

    ARCHIVES_SAVE_AS = 'blog/index.html'


Gotchas
----------------------
- The config file is a python script; the setting here http://docs.getpelican.com/en/3.1.1/settings.html#basic-settings aren't
- 'WARNING: Could not process...' - other stuff in the pelican root folder
    - Using ARTICLE_DIR = ('posts') & PAGE_DIR = ('pages') to tell it where to look; that these are relative to PATH = ('.')

Images
-------------------
- Link to: Better Figures and Images Plugin post
- Compression Using PNGOUT

.. code-block:: bash

    find . -iname "*png" -print0 | xargs -0 --max-procs=4 -n 1 pngout

Final Optimizations
-------------------

- Apache .htaccess
    - Steal from here: https://github.com/h5bp/html5-boilerplate/blob/master/.htaccess
    - use gzip, not deflate
    - gzipcache
- webassets
    - rearrange theme files
    - first name in list of output is actual output filename
    - use filename no query param for name
- favicon
- Google analytics integration
- Sitemap

.. code-block:: python

    PATH = ('content')
    ARTICLE_DIR = ('posts')
    PAGE_DIR = ('pages')

    # DISQUS_SITENAME = "duncanlocknet"

    SITEMAP = {
        'format': 'xml',
        'priorities': {
            'articles': 0.5,
            'indexes': 0.5,
            'pages': 0.5
        },
        'changefreqs': {
            'articles': 'monthly',
            'indexes': 'weekly',
            'pages': 'monthly'
        }
    }

Deployment
--------------------
- Editing the makefile
- moving content into a /content folder, or edit the makefile::

    make ssh_upload
    pelican /home/duncan/dev/duncanlock.net-pelican/content -o /home/duncan/dev/duncanlock.net-pelican/output -s /home/duncan/dev/duncanlock.net-pelican/publishconf.py
    Traceback (most recent call last):
      File "/home/duncan/dev/virtualenvs/duncanlock.net-pelican/bin/pelican", line 8, in <module>
        load_entry_point('pelican==3.2', 'console_scripts', 'pelican')()
      File "/home/duncan/dev/virtualenvs/duncanlock.net-pelican/src/pelican/pelican/__init__.py", line 317, in main
        pelican = get_instance(args)
      File "/home/duncan/dev/virtualenvs/duncanlock.net-pelican/src/pelican/pelican/__init__.py", line 303, in get_instance
        settings = read_settings(args.settings, override=get_config(args))
      File "/home/duncan/dev/virtualenvs/duncanlock.net-pelican/src/pelican/pelican/settings.py", line 124, in read_settings
        return configure_settings(local_settings)
      File "/home/duncan/dev/virtualenvs/duncanlock.net-pelican/src/pelican/pelican/settings.py", line 151, in configure_settings
        raise Exception('You need to specify a path containing the content'
    Exception: You need to specify a path containing the content (see pelican --help for more information)
    make: *** [publish] Error 1

- be careful with rsync_upload - quicker but will make folders match deletung anything on the server that isn't on local
- Feeds

References
----------

- https://github.com/getpelican/pelican/wiki/Tips-n-Tricks
- http://blog.xlarrakoetxea.org/posts/2012/10/creating-a-blog-with-pelican/