:title: How I upgraded this website to Pelican 3.3
:slug: how-i-upgraded-this-website-to-pelican-33
:date: 2013-10-18 17:08:14
:tags: howto, pelican, web
:meta_description: A few of the changes in Pelican 3.3 might mean making some changes to your site in order to upgrade. Here's how I upgraded my site from Pelican 3.2 to 3.3.

There are `quite a few changes <https://github.com/getpelican/pelican/issues?milestone=5&state=closed>`_ in `Pelican 3.3 <http://blog.getpelican.com/pelican-3.3-released.html>`_ - most of them minor, but a few which might mean making some changes to your site in order to upgrade. This is what I did to move my site from Pelican 3.2 to 3.3.

The change that had the biggest impact and took the most work was around image linking - caused by a combination of things. I think I was doing it wrong before and things changed in a way that meant this no longer worked. I also had to update my `Better Figures & Images plugin <{filename}/posts/tech/better-figures-and-images-plugin-for-pelican.rst>`_ to take this into account.

Previously, I'd been linking to my images like this, both in my content and in my theme:

.. code-block:: css

    /* Theme CSS Image Link */
    background: #2C71B8 url(/static/images/blueprint-background.png) repeat;

.. code-block:: html+jinja

    {# Theme HTML/Jinja image link #}
    <meta name="twitter:image" content="{{ SITEURL }}/static/images/favicon-128x128.png">

.. code-block:: rst

    .. image:: /static/images/dunc_smiling_192x192.jpg

    .. figure:: /static/images/pages/404-error.png

This is linking to the output location of the final images, in the ``/output/static/images`` folder. I don't think this is the way you're supposed to do it - and it doesn't appear to work with Pelican 3.3.

The way you're supposed to do it, I think, is to use a place-holder for the first bit of the path and, effectively, link to the source location of the file, not the destination. The `relevant documentation is here <http://docs.getpelican.com/en/3.3.0/getting_started.html#linking-to-internal-content>`_ - and the above examples now look like this:

.. code-block:: css

    /* Theme CSS Image Link - not processed, so no place-holder */
    background: #2C71B8 url(/images/blueprint-background.png) repeat;

.. code-block:: html+jinja

    {# Theme HTML/Jinja image link - not processed, so no place-holder #}
    <meta name="twitter:image" content="{{ SITEURL }}/images/favicon-128x128.png">

.. code-block:: rst

    .. image:: {filename}/images/dunc_smiling_192x192.jpg

    .. figure:: {filename}/images/pages/404-error.png

Theme Changes
-------------

The theme changes were the same: I removed the ``/static`` from the start of any image links. Because the theme files aren't content, they don't get processed by Pelican, so you don't use the ``{filename}`` place-holder here. All the changes looked something like this:

.. code-block:: diff

    - <meta name="twitter:image" content="{{ SITEURL }}/static/images/test.png">
    + <meta name="twitter:image" content="{{ SITEURL }}/images/test.png">

You can see the Git commit with all the theme changes `here <https://github.com/dflock/blueprint/commit/bae678828b4535fcece8327c0f2dbae63bf4c92f>`_, `in the Blueprint Theme Repository <https://github.com/dflock/blueprint>`_.

Content Changes
---------------

.. epigraph::

    The syntax for linking to source content has been changed in order to ensure compatibility with Markdown and reST extensions. For example, the new syntax for Markdown: ``[a link relative to content root]({filename}/article1.md)``
    The previous ``|filename|/article1.md`` syntax will continue to be supported for backwards compatibility.

    -- `Pelican Blog <http://blog.getpelican.com/pelican-3.3-released.html>`_

Again, this is the related to image linking - and is the same change as above. This:

.. code-block:: rst

    .. image:: /static/images/dunc_smiling_192x192.jpg

    .. figure:: /static/images/pages/404-error.png
        :target: /static/images/pages/404-error.png


becomes this:

.. code-block:: rst

    .. image:: {filename}/images/dunc_smiling_192x192.jpg

    .. figure:: {filename}/images/pages/404-error.png
        :target: {filename}/images/pages/404-error.png

You need to do this in every post that has images. Fortunately this was simple to search & replace. On some posts I also have an extra piece of metadata called ``thumbnail``, that also needed updating. This isn't processed by Pelican, so no place-holder here:

.. code-block:: diff

     -:thumbnail: /static/images/posts/post-name/image.jpg
     +:thumbnail: /images/posts/post-name/image.jpg


Configuration Changes
---------------------

Since the ``FILES_TO_COPY`` setting has been deprecated, you should replace it with the ``STATIC_PATHS`` and ``EXTRA_PATH_METADATA`` `settings <http://docs.getpelican.com/en/3.3.0/settings.html#basic-settings>`_. The relevant part of my settings file changed like this:

.. code-block:: diff

     # static paths will be copied under the same name
    -STATIC_PATHS = ["images"]
    +STATIC_PATHS = [
    +    'images',
    +    'extras'
    +]

     # A list of extra files to copy from the source to the destination
    -FILES_TO_COPY = (
    -    ('extras/.htaccess', '.htaccess'),
    -    ('extras/robots.txt', 'robots.txt'),
    -    ('extras/favicon.ico', 'favicon.ico'),
    -)
    +EXTRA_PATH_METADATA = {
    +    'extras/.htaccess': {'path': '.htaccess'},
    +    'extras/robots.txt': {'path': 'robots.txt'},
    +    'extras/favicon.ico': {'path': 'favicon.ico'},
    +}

You can see the Git commit with all the `content & configuration changes here <https://github.com/dflock/duncanlock.net/commit/bcee8b830d45daad00ea9428a339459689a27cf5>`_, in the `site repository <https://github.com/dflock/duncanlock.net>`_.

Plugin Changes
--------------

A special case for me is the `Better Figures & Images plugin <{filename}/posts/tech/better-figures-and-images-plugin-for-pelican.rst>`_. I use this plugin and I also wrote it - and it stopped working.

In order to debug it, I first added in some logging support. I added this at the top with the other imports:

.. code-block:: python

    import logging
    logger = logging.getLogger(__name__)


and then some of this further down to output the paths that the plugin was seeing:

.. code-block:: python

    logger.debug('Better Fig. PATH: %s', instance.settings['PATH'])
    logger.debug('Better Fig. img.src: %s', img['src'])

This made it easier to figure out what I needed to change. The path handling code in the plugin was never very good, so I changed it from this mess:

.. code-block:: python

    # TODO: Pretty sure this isn't the right way to do this, too hard coded.
    # There must be a setting that I should be using?
    src = instance.settings['PATH'] + '/images/' + os.path.split(img['src'])[1]

    #src = instance.settings['PATH'] + '/images/' + os.path.split(img['src'])[1]

    # The method mentioned above is only working if the images are really in the "images" folder.
    # It's also not working on subdirectories inside the image folder
    # Both issues are fixed:
    # Changed the static "/images/" string to the proper path which is extracted from the 'split' tuple
    # The first 7 letters are cutted ("/static") to get a valid link.
    # Somehow the static folder isn't created in the output folder. It's only on the server after 'make ftp_upload'
    src = instance.settings['PATH'] + os.path.split(img['src'])[0][7:] + '/' + os.path.split(img['src'])[1]


to this slightly more robust mess:

.. code-block:: python

    logger.debug('Better Fig. PATH: %s', instance.settings['PATH'])
    logger.debug('Better Fig. img.src: %s', img['src'])

    img_path, img_filename = path.split(img['src'])

    logger.debug('Better Fig. img_path: %s', img_path)
    logger.debug('Better Fig. img_fname: %s', img_filename)

    # Strip off {filename}, |filename| or /static
    if img_path.startswith(('{filename}', '|filename|')):
        img_path = img_path[10:]
    elif img_path.startswith('/static'):
        img_path = img_path[7:]
    else:
        logger.warning('Better Fig. Error: img_path should start with either {filename}, |filename| or /static')

    # Build the source image filename
    src = instance.settings['PATH'] + img_path + '/' + img_filename

    logger.debug('Better Fig. src: %s', src)
    if not (path.isfile(src) and access(src, R_OK)):
        logger.error('Better Fig. Error: image not found: {}'.format(src))

This code basically strips the leading ``{filename}``, ``|filename|`` or ``/static`` from the image path, then looks for the original source image inside the current content folder (as set by the ``PATH`` setting in your config). This new code also contains lots more logging for debugging and reporting any errors or warnings. You can see the complete Git commit for the `plugin changes here <https://github.com/dflock/pelican-plugins/commit/259147e4da6474c128c4dd09c3a51c64453343af>`_.
