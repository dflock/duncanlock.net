#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
from datetime import date

#################################
#
# Basic Settings
#
#################################

AUTHOR = 'Duncan Lock'
SITENAME = 'duncanlock.net'
SITEURL = 'http://duncanlock.test'
SITE_DOMAIN = 'duncanlock.net'
RELATIVE_URLS = False

SITE_DESCRIPTION = 'Duncan Locks personal site. Includes my blog, colitis resources, SCD recipes, portfolio and CV/Resume.'

TIMEZONE = 'America/Vancouver'

DEFAULT_LANG = 'en'
# Use the date of the file from the filesystem for the article date
# DEFAULT_DATE = 'fs'

COPYRIGHT_FROM = 1998
COPYRIGHT_UNTIL = date.today().year

SUMMARY_MAX_LENGTH = 80

#################################
#
# Setting for Feeds
#
#################################

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# FEED_RSS = 'feeds/all.rss.xml'
# CATEGORY_FEED_RSS = 'feeds/%s.rss.xml'

# FEED_ATOM = 'feeds/all.atom.xml'
# CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'


# static paths will be copied under the same name
STATIC_PATHS = ["images"]

# A list of files to copy from the source to the destination
FILES_TO_COPY = (
    ('extras/.htaccess', '.htaccess'),
    ('extras/robots.txt', 'robots.txt'),
    ('extras/favicon.ico', 'favicon.ico'),
    ('extras/google9b8f9c7f2338fb3e.html', 'google9b8f9c7f2338fb3e.html')
)

# Do we want to wipe the /output folder every build, or just accumulate new stuff?
DELETE_OUTPUT_DIRECTORY = True

# Blogroll
# (anchor-text, icon-name, URL)
LINKS = (
    ('CV/Resume', 'user', '/pages/duncan-locks-resume.html'),
    ('LinkedIn', 'linkedin-squared', 'http://ca.linkedin.com/in/duncanlock/'),
    ('Codeistry', 'globe', 'http://codeistry.com/'),
)

# Social widget
# (anchor-text, icon-name, URL)
SOCIAL = (
    ('Twitter', 'twitter', 'http://twitter.com/duncanlock'),
    ('GitHub', 'github-circled', 'http://github.com/dflock'),
    ('Stack&#8203;Overflow', 'stackoverflow', 'http://stackoverflow.com/users/259698/duncan-lock'),
    ('Google+', 'gplus-squared', 'https://plus.google.com/108110520114045131522'),
)

TWITTER_USERNAME = 'duncanlock'
TWITTER_ACCOUNT_ID = "1512952557"

ARTICLE_TWEET_BUTTON = False
ARTICLE_GOOGLEPLUS_BUTTON = False

DEFAULT_PAGINATION = 8
DEFAULT_ORPHANS = 1

# Switch Typogrify on, to get fancier Typography
# See here for more: https://github.com/mintchaos/typogrify
TYPOGRIFY = True

# Which theme to use
THEME = 'themes/blueprint'

# Where should Pelican look for content?
PATH = ('content')
# These are relative to PATH, above
ARTICLE_DIR = ('posts')
PAGE_DIR = ('pages')

MARKUP = (('rst', 'html'))


# Use filsystem folders for categories
USE_FOLDER_AS_CATEGORY = True

# What do we want article URLs to look like?
ARTICLE_URL = 'blog/{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = 'blog/{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'

# What do we want archive URLs to look like?
YEAR_ARCHIVE_SAVE_AS = 'blog/{date:%Y}/index.html'
MONTH_ARCHIVE_SAVE_AS = 'blog/{date:%Y}/{date:%m}/index.html'
DAY_ARCHIVE_SAVE_AS = 'blog/{date:%Y}/{date:%m}/{date:%d}/index.html'

# Do something if people visit /blog
ARCHIVES_SAVE_AS = 'blog/index.html'

# Do we want all our pages displayed in the theme's header?
DISPLAY_PAGES_ON_MENU = False

# Disqus sitename for comments. If not set, comments won't be shown.
# DISQUS_SITENAME = "duncanlocknet"


# Set Colophon variables, which can be output by the theme.
COLOPHON = True
COLOPHON_TITLE = 'About'
COLOPHON_CONTENT = '<a href="/pages/duncan-locks-resume.html">An adaptable and enthusiastic writer <span class="amp">&amp;</span> developer with broad experience and an artistic background. Strong graph&shy;ical com&shy;munication, design, creative <span class="amp">&amp;</span> prob&shy;lem solving skills &mdash; and an eye for detail.</a>'


#################################
#
# Setting for plugins
#
#################################

# Where to look for plugins
PLUGIN_PATH = '../pelican-plugins'
# PLUGIN_PATH = '../pelican-plugins-integration'
# Which plugins to enable
# PLUGINS = ['assets', 'related_posts', 'extract_toc', 'post_stats']
PLUGINS = ['better_figures_and_images', 'assets', 'related_posts', 'extract_toc', 'post_stats']

# Setting for the better_figures_and_images plugin
RESPONSIVE_IMAGES = True

# Settings for the related_posts plugin
RELATED_POSTS_MAX = 4


#################################
#
# Custom Jinja Filters
#   see: http://jinja.pocoo.org/docs/templates/#filters
#
#################################

def month_name(month_number):
    import calendar
    return calendar.month_name[month_number]


def suffix(d, wrap=True):
    tmp = 'th' if 11 <= d <= 13 else {1: 'st', 2: 'nd', 3: 'rd'}.get(d % 10, 'th')
    if wrap:
        return '<span class="day_suffix">' + tmp + '</span>'
    else:
        return tmp


def custom_strftime(format, t):
    return t.strftime(format).replace('{S}', str(t.day) + suffix(t.day))


def archive_date_format(date):
    return custom_strftime('{S} %B, %Y', date)


def sidebar_date_format(date):
    return custom_strftime('%a {S} %B, %Y', date)


# Which custom Jinja filters to enable
JINJA_FILTERS = {
    "month_name": month_name,
    "archive_date_format": archive_date_format,
    "sidebar_date_format": sidebar_date_format,
}
