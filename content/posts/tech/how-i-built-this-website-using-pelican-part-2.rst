:title: How I built this website, using Pelican: Part 2
:slug: how-i-built-this-website-using-pelican-part-2
:date: 2013-05-20 10:35:21
:tags: web, pelican, python, tutorial
:category: tech
:status: draft

Themes
-----------------------
The Pelican quickstart site uses the default theme

Go through my theme and explain each bit
---------------------------------------------

Mention http://ia.net/blog/100e2r/

Go through my config and explain each bit
---------------------------------------------

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

.. code-block:: console

    $ find . -iname "*png" -print0 | xargs -0 --max-procs=4 -n 1 pngout

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

- be careful with rsync_upload - quicker but will make folders match deleting anything on the server that isn't on local
- Feeds


- Link to: using incron, when I figure that out with virtualenvs post
- https://github.com/getpelican/pelican/wiki/Tips-n-Tricks
- http://blog.xlarrakoetxea.org/posts/2012/10/creating-a-blog-with-pelican/
