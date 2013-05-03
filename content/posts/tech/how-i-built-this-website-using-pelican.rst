:title: How I built this website, using Pelican
:slug: how-i-built-this-website-using-pelican
:date: 2013-04-29 17:19:53
:tags: web, pelican, python, tutorial
:category: tech

As I `mentioned previously <|filename|/posts/news/new-site-built-on-pelican.rst>`_, this site was put together using `Pelican <http://getpelican.com/>`_ - a static site generator, written in Python.

.. figure:: /static/images/pelecanus-occidentalis-diagram.png
    :alt: Blueprint style diagram showing a brown Pelican, flying. The diagram point out it's Yellow Head, Large beak and pouch for fishing, long neck, white chest and grey body.

    Pelecanus Occidentalis - the Brown Pelican.

    Image Credit: Original clipart `Flying Pelican from OpenClipart, by molumen, Public Domain <http://openclipart.org/detail/2798/flying-pelican-by-molumen>`_. More on `Pelican, the bird <http://en.wikipedia.org/wiki/Brown_Pelican>`_.

Static site generators take your content, pour it into your templates and output the result as static pre-generated HTML, CSS, JS & image files. You can then just upload the resulting folder of output to your server and you're done. All you need on the server is a web server of some sort, like Apache or Nginx - anything really - all it's doing is serving static pages.

The huge advantage of this setup is simplicity:
--------------------------------------------------

#. You can write your content in Markdown [#markdown]_, reStructuredText [#rest]_ or AsciiDoc [#asciidoc]_ - all simple text formats, designed to facilitate writing and get out of your way. You can use any writing tool you prefer, as long as it can output plain text files.
#. Whenever you make changes, Pelican can automatically regenerate the site, so you can see your changes immediately.
#. When you're done, Pelican can automatically upload the site to your web server, or you can do it, just by uploading a folder.
#. The web server generally requires no setup - all you need is a web server that can serve static content (which is all of them) - no extra software or configuration; no PHP, no database, no nothing - much less to go wrong.
#. Because you've only got one thing running on the server, you have much less exposure to security problems - no WordPress, no PHP - just the OS & the web server.
#. Because the server is only serving pre-generated static content, a Pelican site is very lightweight, using very few server resources.


Installation & Basic Setup
-----------------------------

I'm using Linux, but doing this on Windows or Mac is quite similar - you'll need the same things installed, but the details of installing them will be different. Installing ``python-dev`` and python packages that want to build C extensions on Windows... won't work - I suggest you give ActiveState's Binary Package manager a try if you're on Windows: http://code.activestate.com/pypm/

Install
^^^^^^^^^^^^^^^^^^^^^^^^^^

Pelican uses Python, so you'll need that installed. If you're on Mac or Linux, you'll already have this, but you'll probably need to `install it on Windows <http://www.activestate.com/activepython/downloads>`_. Pelican supports Python 2 or 3, so use whichever you like.

First, I'm going to install ``pip`` [#pip]_, ``virtualenv`` [#virtualenv]_ and ``virtualenvwrapper`` [#virtualenvwrapper]_. These tools make working on python projects *much* easier. Later, we're going to install some python packages that will attempt to build their C extensions during install, so we also need ``python-dev``:

.. code-block:: console

    sudo apt-get install python-dev python-pip python-virtualenv virtualenvwrapper

Next, I'm going to tell ``virtualenvwrapper`` where I want it to put stuff, by adding this to my ``~/.bashrc`` file:

.. code-block:: bash

    # virtualenvwrapper config
    export PROJECT_HOME=~/dev
    export WORKON_HOME=~/dev/virtualenvs

Now either do ``source ~/.bashrc`` or close and re-open your terminal. This will trigger a one-time setup for virtualenvwrapper. Then run:

.. code-block:: console

    mkproject duncanlock.net-pelican

which should do something like this:

.. code-block:: console

    New python executable in duncanlock.net-pelican/bin/python
    Installing distribute.........done.
    Installing pip...............done.
    virtualenvwrapper.user_scripts creating
    [...]
    Creating /home/duncan/dev/duncanlock.net-pelican
    Setting project for duncanlock.net-pelican to /home/duncan/dev/duncanlock.net-pelican

You will now have a self-contained python virtual environment installed in ``~/dev/virtualenvs/duncanlock.net-pelican`` and a new folder in ``~/dev/duncanlock.net-pelican``, to put your project files. Your command prompt will change while this virtualenv is active - gaining a ``(duncanlock.net-pelican)`` at the beginning, so you know which virtualenv you're in.

Next, we're going to install Pelican and it's dependencies into our virtual environment:

.. code-block:: console

    pip install pelican

This should install the following things for you:

feedgenerator
    to generate the Atom feeds
jinja2
    for templating support
pygments
    for syntax highlighting
docutils
    for supporting reStructuredText as an input format
pytz
    for timezone definitions
blinker
    an object-to-object and broadcast signaling system
unidecode
    for ASCII transliterations of Unicode text

Check that worked by running ``pelican ----version`` - currently this should print out ``3.2.0`` - then run ``pip freeze`` - which prints out a list of the python modules installed in your current virtualenv.

I also suggest you install some extra python modules to support bonus functionality provided by some Pelican plugins that we'll be using later:

.. code-block:: console

    pip install Pillow beautifulsoup4 cssmin cssprefixer cssutils pretty six smartypants typogrify webassets

Once this is done, I suggest you run this, to get pip to make a list of all the things you've got installed in this virtualenv:

.. code-block:: console

    pip freeze > requirements.txt

This allows you to re-install everything in one go if you move machines, just by running ``pip install -r requirements.txt`` -- or to check for & install updates to all the modules at once, just by running ``pip install ----upgrade -r requirements.txt``, amongst other things. We're also going to check this lot into ``git`` later and this allows you to keep the list of requirements under version control too, which is nice.

Quick Start
^^^^^^^^^^^^^^^^^^^^^^^

Now that we've got everything installed, run this to create a basic skeleton site for you to modify:

.. code-block:: console

    pelican-quickstart

- Theme
- Link to: using incron, when I figure that out with virtualenvs post

Apache Setup
^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: apacheconf

    # domain: duncanlock.test

    <VirtualHost *:80>

        # Admin email, Server Name (domain name) and any aliases
        ServerAdmin webmaster@duncanlock.test
        ServerName  duncanlock.test
        ServerAlias www.duncanlock.test


        # Index file and Document Root (where the public files are located)
        DirectoryIndex index.php index.html
        DocumentRoot /home/duncan/dev/duncanlock.net-pelican/

    </VirtualHost>

Then add that domain to our /etc/hosts:

.. code-block:: text

    127.0.0.1  duncanlock.test

Then enable the new virtual host in Apache:

.. code-block:: console

    sudo a2ensite duncanlock.test
    sudo service apache2 reload

Git
----------------------

Create a ``.gitignore`` file in your website folder, with this in it:

.. code-block:: text

    output/*
    *.py[cod]


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

- be careful with rsync_upload - quicker but will make folders match deleting anything on the server that isn't on local
- Feeds

Footnotes & References:
----------------------------

- https://github.com/getpelican/pelican/wiki/Tips-n-Tricks
- http://blog.xlarrakoetxea.org/posts/2012/10/creating-a-blog-with-pelican/

.. [#markdown] **Markdown** is a text-to-HTML conversion tool for web writers. Markdown allows you to write using an easy-to-read, easy-to-write plain text format, then convert it to structurally valid XHTML (or HTML): http://daringfireball.net/projects/markdown/
.. [#rest] **reStructuredText** is an easy-to-read, what-you-see-is-what-you-get plaintext markup syntax and parser system. It is useful for in-line program documentation (such as Python docstrings), for quickly creating simple web pages, and for standalone documents: http://en.wikipedia.org/wiki/ReStructuredText
.. [#asciidoc] **AsciiDoc** is a text document format for writing notes, documentation, articles, books, ebooks, slideshows, web pages, man pages and blogs. AsciiDoc files can be translated to many formats including HTML, PDF, EPUB, man page: http://www.methods.co.nz/asciidoc/
.. [#pip] **Pip** is a package management system used to install and manage software packages written in the programming language Python. Many packages can be found in the Python Package Index (PyPI): http://en.wikipedia.org/wiki/Pip_(Python)
.. [#virtualenv] **virtualenv** is a tool to create isolated Python environments: http://www.virtualenv.org/en/latest/ & http://www.clemesha.org/blog/modern-python-hacker-tools-virtualenv-fabric-pip/
.. [#virtualenvwrapper] **virtualenvwrapper** is a set of extensions to Ian Bicking’s ``virtualenv`` tool. Includes wrappers for creating & deleting virtual environments and managing development workflow, making it easier to work on more than one project at a time without introducing conflicts in their dependencies. http://virtualenvwrapper.readthedocs.org/en/latest/