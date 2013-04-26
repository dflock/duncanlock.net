:title: How I built this site, using Pelican
:slug: how-i-built-this-site-using-pelican
:date: 2013-04-26 14:37:34
:tags: web, pelican, python
:category: tech


Basic Setup
--------------------
- Install, quick start
- Theme
- Link to: using incron, when I figure that out with virtualenvs post
- Link to: Apache vitual server setup post


Gotchas
----------------------
- The config file is a python script; the setting here http://docs.getpelican.com/en/3.1.1/settings.html#basic-settings aren't
- 'WARNING: Could not process...' - other stuff in the pelican root folder
	- Using ARTICLE_DIR = ('posts') & PAGE_DIR = ('pages') to tell it where to look; that these are relative to PATH = ('.')

Images
-------------------
- Link to: Better Figures and Images Plugin post
- Compression Using PNGOUT::

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

Deployment
--------------------

