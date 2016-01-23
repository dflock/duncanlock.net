:title: How I upgraded this website to Pelican 3.6
:slug: how-i-upgraded-this-website-to-pelican-36
:date: 2015-11-19 22:44:24
:tags: howto, pelican, web
:category: tech
:meta_description:
:thumbnail:

This site has been generated using Pelican 3.3 for over two years - and I finally found some time to upgrade to the current version of Pelican, 3.6. This is how I did the upgrade.

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
    $ git fetch upstream
    $ git co master
    $ git pull --recurse-submodules && git submodule update --recursive

I also got this, as fallout from the upgraded `BeautifulSoup <http://www.crummy.com/software/BeautifulSoup/>`_ module:

.. code-block:: console

    /home/duncan/venv/duncanlock.net/local/lib/python2.7/site-packages/bs4/__init__.py:166:
    UserWarning: No parser was explicitly specified, so I'm using the best available HTML
    parser for this system ("lxml"). This usually isn't a problem, but if you run this
    code on another system, or in a different virtual environment,
    it may use a different parser and behave differently.

    To get rid of this warning, change this:

     BeautifulSoup([your markup])

    to this:

     BeautifulSoup([your markup], "lxml")
      markup_type=markup_type)

This turned out to be caused by my plugins - two of which are using BeautifulSoup: ``post_stats`` and ``better_figures_and_images``. To fix this, I just did what the warning said:

This was the change for ``better_figures_and_images``:

.. code-block:: diff

    - soup = BeautifulSoup(content)
    + soup = BeautifulSoup(content, "lxml")

... and this was the very similar change for ``post_stats``:

.. code-block:: diff

    - raw_text = BeautifulSoup(content).getText()
    + raw_text = BeautifulSoup(content, "lxml").getText()

Minor tweak to syntax highlighting in blueptint theme
-----------------------------------------------------------

As my pygments module had got a `major version bump from 1.6 to 2.0.2 <http://pygments.org/docs/changelog/>`_, I updated the pygments CSS files included with the theme. To do this, I ran this at the command line, in the theme folder, then merged the result into the existing ``pygments-monokai.css`` file:

.. code-block:: console

    $ pygmentize -S monokai -f html -a .highlight > pygment.css

I also had an existing ``pygments.css`` in there for some reason, which had a few extra styles in. I merged these into ``pygments-monokai.css`` and deleted it, so I could just load that one file.

Currently Unresolved: Problem with the assets plugin
------------------------------------------------------

Finally, I was getting this error when trying to generate the site:

.. code-block:: console

  CRITICAL: BundleError: '/home/duncan/dev/duncanlock.net/output/theme/css/fontello.css' does not exist

This is caused by the `assets <https://github.com/getpelican/pelican-plugins/tree/master/assets>`_ plugin, which I was using in my `bluprint theme <https://github.com/dflock/blueprint>`_ to minify and concatenate the css stylesheets:

.. code-block:: jinja

    {% assets filters="cssprefixer,cssmin", output="css/final-%(version)s.css", "css/fontello.css", "css/main.css", "css/pygments-monokai.css" %}
      <link rel="stylesheet" media="all" href="{{ SITEURL }}/{{ ASSET_URL }}">
    {% endassets %}

For now, I've just disabled this in my settings file:

.. code-block:: python

    # Which plugins to enable
    PLUGINS = [
        'better_figures_and_images',
        # 'assets',
        'related_posts',
        'extract_toc',
        'post_stats',
        'multi_part'
    ]

and fallen back to loading the stylesheets individualy, unminified:

.. code-block:: jinja

    {# Comment this out until I fix the BundleError:
    {% assets filters="cssprefixer,cssmin", output="css/final-%(version)s.css", "css/fontello.css", "css/main.css", "css/pygments-monokai.css" %}
    <link rel="stylesheet" media="all" href="/{{ ASSET_URL }}">
    {% endassets %}
    #}
    <link href="{{ SITEURL }}/theme/css/fontello.css" rel="stylesheet">
    <link href="{{ SITEURL }}/theme/css/main.css" rel="stylesheet">
    <link href="{{ SITEURL }}/theme/css/pygments.css" rel="stylesheet">
    <link href="{{ SITEURL }}/theme/css/pygments-monokai.css" rel="stylesheet">

This will make the site slightly slower to load, but I'll have to live with that for now.

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

Doing this cut the generation time for this site roughly in half -- from ~13 seconds, down to ~7 seconds - a worthwhile improvement. Symlinking the ``./cache`` folder to my SSD instead of the regular HD... didn't make much difference to the time. Symlinking it to a folder on `a tmpfs RAM disk <https://wiki.archlinux.org/index.php/Tmpfs>`_ didn't seem to make much difference either -- so for this little site, the caching dosn't seem very IO bound, which was a little unexpected. Maybe this is because the files it needs to check - i.e. the rest of the site - are still on a regular HD?
