#!/usr/bin/env python
# -*- coding: utf-8 -*- #

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys

# import main config
sys.path.append(os.curdir)
from pelicanconf import *

# Use real live URLs
SITEURL = 'http://duncanlock.net'
RELATIVE_URLS = False

# Generate Feeds
FEED_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'

# Always start over
DELETE_OUTPUT_DIRECTORY = True

# Articles have comments
DISQUS_SITENAME = "duncanlocknet"

# Output Google Analytics code
GOOGLE_ANALYTICS = "UA-1493291-9"
GOOGLE_ANALYTICS_UNIVERSAL = True

#################################
#
# Setting for plugins
#
#################################

# Which extra plugins to enable when publishing
PLUGINS = PLUGINS + ['gzip_cache', 'sitemap']

# Settings for the sitemap plugin
SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.8,
        'indexes': 0.7,
        'pages': 0.5
    },
    'changefreqs': {
        'articles': 'weekly',
        'indexes': 'daily',
        'pages': 'monthly'
    }
}