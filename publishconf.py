#!/usr/bin/env python
# -*- coding: utf-8 -*- #

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *

SITEURL = 'http://duncanlock.net'
RELATIVE_URLS = False

# FEED_RSS = 'feeds/all.rss.xml'
# CATEGORY_FEED_RSS = 'feeds/%s.rss.xml'

# FEED_ATOM = 'feeds/all.atom.xml'
# CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'

FEED_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'

DELETE_OUTPUT_DIRECTORY = True

# Following items are often useful when publishing

DISQUS_SITENAME = "duncanlocknet"
GOOGLE_ANALYTICS = "UA-1493291-9"
GOOGLE_ANALYTICS_UNIVERSAL = True

#################################
#
# Setting for plugins
#
#################################

# Where to look for plugins
PLUGIN_PATH = '../pelican-plugins'
# Which plugins to enable
PLUGINS = ['better_figures_and_images', 'assets', 'gzip_cache', 'sitemap']

# Setting for the better_figures_and_images plugin
RESPONSIVE_IMAGES = True

# Settings for the sitemap plugin
SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.5,
        'indexes': 0.5,
        'pages': 0.5
    },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'daily',
        'pages': 'monthly'
    }
}