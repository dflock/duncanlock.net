:title: How I upgraded this website to Pelican 3.6
:slug: how-i-upgraded-this-website-to-pelican-36
:date: 2016-03-05 01:51:54
:tags: howto, pelican, web
:category: tech
:meta_description: This site has been generated using Pelican 3.3 for over two years. I finally found some time to upgrade to the current version of Pelican, 3.6.3. This is how I did the upgrade.
:thumbnail:

This site has been generated using Pelican 3.3 for over two years - and I finally found some time to upgrade to the current version of Pelican, 3.6.3. This is how I did the upgrade.

I decided to be lazy and do the upgrade in-place, instead of creating a new ``virtualenv`` and copying the content & settings over. Luckily, this worked out OK, after a bit of fiddling around.

I also decided, rather cavalierly, to upgrade all the packages in the ``virtualenv`` to their latest versions while I was at it. To do this, I upgraded ``pip``, then used `pip-review <https://pypi.python.org/pypi/pip-review>`_. To upgrade ``pip`` & install ``pip-review`` system wide, run this on the command line:

.. code-block:: console

    $ sudo -H pip install --upgrade pip
    $ sudo -H pip install pip-review

Then upgrade eveything in the sites ``virtualenv``:

.. code-block:: console

    $ sudo apt-get install libjpeg-dev
    $ workon duncanlock.net
    $ pip-review --auto
    $ pip freeze > requirements.txt

Installing `libjpeg-dev` was a requirement for upgrading Pillow, I think.

Upgrade Settings
-----------------

I then tried to generate the site -- and got this:

.. code-block:: console

    $ pelican content

    WARNING: PLUGIN_PATH setting has been replaced by PLUGIN_PATHS, moving it to the new setting name.
    WARNING: Defining PLUGIN_PATHS setting as string has been deprecated (should be a list)
    WARNING: Deprecated setting ARTICLE_DIR, moving it to ARTICLE_PATHS list
    WARNING: Deprecated setting PAGE_DIR, moving it to PAGE_PATHS list

These are all warnings about deprecated settings in my ancient ``pelicanconf.py`` settings file. I fixed those by making these changes:

.. code-block:: diff

    -ARTICLE_DIR = ('posts')
    -PAGE_DIR = ('pages')
    +ARTICLE_PATHS = ['posts']
    +PAGE_PATHS = ['pages']

    -PLUGIN_PATH = '../pelican-plugins'
    +PLUGIN_PATHS = ['../pelican-plugins']

Upgrade Plugins
-----------------

I'm sourcing my plugins from a git checkout of the `pelican-plugins repository <https://github.com/getpelican/pelican-plugins>`_, so I pulled that up to date like this:

.. code-block:: console

    $ cd ../pelican-plugins/
    $ git fetch origin
    $ git co master
    $ git pull --recurse-submodules && git submodule update --recursive

The only change precipitated by this was a minor tweak to use the ``serial`` plugin instead of the deprecated ``multipart`` one. I made this change to the theme:

.. code-block:: diff

  --- a/templates/article-sidebar-multipart.html
  +++ b/templates/article-sidebar-multipart.html
  @@ -1,9 +1,9 @@
  -{% if article.metadata.parts_articles %}
  +{% if article.series %}
       <div class="row-fluid">
           <nav>
               <p>This post is part of a series:</p>
               <ol class="parts">
  -            {% for part_article in article.metadata.parts_articles %}
  +            {% for part_article in article.series.all %}
                   <li {% if part_article == article %}class="active"{% endif %}>
                       {% if part_article == article %}
                       {{ part_article.title }}
  @@ -15,4 +15,4 @@
               </ol>
           </nav>
       </div>
  {% endif %}

and changed my config to load the ``serial`` plugin instead:

.. code-block:: python

  # Which plugins to enable
  PLUGINS = [
      'better_figures_and_images',
      'assets',
      'related_posts',
      'extract_toc',
      'post_stats',
      'series'
  ]



Minor tweak to syntax highlighting in blueptint theme
-----------------------------------------------------------

As my pygments module had got a `major version bump from 1.6 to 2.1.2 <http://pygments.org/docs/changelog/>`_, I updated the pygments CSS files included with the theme. To do this, I ran this at the command line, in the website folder, then merged the result into the existing ``pygments-monokai.css`` file in the blueprint themes `static/css` folder:

.. code-block:: console

    $ pygmentize -S monokai -f html -a .highlight | sort > pygments-monokai.css

I also had an existing ``pygments.css`` in there for some reason, which had a few extra styles in. I merged these into ``pygments-monokai.css`` and deleted it, so I could just load that one file.

New feature: Caching
---------------------------

Pelican 3.6 now has build caching, which 3.3 didn't. To take advantage of this, I set these properties in my settings file:

.. code-block:: python

    #################################
    #
    # Cache Settings
    #
    #################################

    CACHE_CONTENT = True
    CHECK_MODIFIED_METHOD = 'mtime'
    LOAD_CONTENT_CACHE = True
    GZIP_CACHE = False

Doing this cut the generation time for this site roughly in half -- from ~13 seconds, down to ~7 seconds - a worthwhile improvement. Symlinking the ``./cache`` folder to my SSD instead of the regular HD... didn't make much difference to the time. Symlinking it to a folder on `a tmpfs RAM disk <https://wiki.archlinux.org/index.php/Tmpfs>`_ didn't seem to make much difference either -- so for this little site, the caching doesn't seem very IO bound, which was a little unexpected. Maybe this is because the source files are still on a regular HD?
