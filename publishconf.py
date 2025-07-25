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
SITESCHEME = "https"
SITEURL = SITESCHEME + "://duncanlock.net"
RELATIVE_URLS = False

# Send the published output to a different folder, so It doesn't
# overwrite the dev site. It's just used for staging before uploading, really.
OUTPUT_PATH = "published_output/"
# Leave the cache alone when publishing
CACHE_CONTENT = False
LOAD_CONTENT_CACHE = False

#
# Generate Feeds
#
RSS_FEED_SUMMARY_ONLY = False
# The domain prepended to feed URLs. Since feed URLs should always be absolute,
# it is highly recommended to define this.
FEED_DOMAIN = SITEURL

FEED_ATOM = "feeds/all.atom.xml"
CATEGORY_FEED_ATOM = "feeds/{slug}.atom.xml"

FEED_RSS = "feeds/all.rss.xml"
CATEGORY_FEED_RSS = "feeds/{slug}.rss.xml"

# Always start over
DELETE_OUTPUT_DIRECTORY = True

# Articles have comments
# DISQUS_SITENAME = "duncanlocknet"

# Output Google Analytics code
# GOOGLE_ANALYTICS_ID = "UA-1493291-9"
# v4
# GOOGLE_ANALYTICS_ID = "G-PTKBWTS0KG"
# GOOGLE_ANALYTICS_UNIVERSAL = False
# GOOGLE_ANALYTICS_V4 = True

# ARTICLE_TWEET_BUTTON = True

# WITH_FUTURE_DATES = True
# CACHE_CONTENT = False

#################################
#
# Setting for plugins
#
#################################

# Which extra plugins to enable when publishing
PLUGINS = PLUGINS + ["gzip_cache", "sitemap"]

# Settings for the sitemap plugin
SITEMAP = {
    "format": "xml",
    "priorities": {"articles": 0.8, "indexes": 0.7, "pages": 0.5},
    "changefreqs": {"articles": "daily", "indexes": "weekly", "pages": "monthly"},
}
