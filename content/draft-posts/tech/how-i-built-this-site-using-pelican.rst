:title: How I built this site, using Pelican
:slug: how-i-built-this-site-using-pelican
:date: 2013-04-26 14:37:34
:tags: web, pelican, python
:category: tech


Link to & update: https://github.com/getpelican/pelican/wiki/Tips-n-Tricks

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
- Editing the makefile

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

