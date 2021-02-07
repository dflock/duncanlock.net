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
SITESCHEME = 'http'
SITEURL = SITESCHEME + '://' + 'duncanlock.test'
SITE_DOMAIN = 'duncanlock.net'
RELATIVE_URLS = False

SITE_TITLE = 'Duncan Locks personal site'
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
# Cache Settings
#
#################################

CACHE_CONTENT = True
CHECK_MODIFIED_METHOD = 'mtime'
LOAD_CONTENT_CACHE = True
GZIP_CACHE = False

#################################
#
# Setting for Feeds
#
#################################

# Feed generation is usually not required when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

FEED_ALL_RSS = None
CATEGORY_FEED_RSS = None
TRANSLATION_FEED_RSS = None

# Generate Feeds
# FEED_DOMAIN = SITEURL

# FEED_ATOM = 'feeds/all.atom.xml'
# CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'

# FEED_RSS = 'feeds/all.rss.xml'
# CATEGORY_FEED_RSS = 'feeds/%s.rss.xml'


#################################
#
# Setting for Paths
#
#################################

# static paths will be copied under the same name
STATIC_PATHS = [
    'images',
    'extras',
    'files'
]

# A list of extra files to copy from the source to the destination
EXTRA_PATH_METADATA = {
    'extras/.htaccess': {'path': '.htaccess'},
    'extras/robots.txt': {'path': 'robots.txt'},
    'extras/favicon.ico': {'path': 'favicon.ico'},
    'extras/google9b8f9c7f2338fb3e.html': {'path': 'google9b8f9c7f2338fb3e.html'},
    'extras/keybase.txt': {'path': '.well-known/keybase.txt'},
}

# Do we want to wipe the /output folder every build,
# or just accumulate new stuff?
DELETE_OUTPUT_DIRECTORY = True


#################################
#
# Footer Links & Menu's
#
#################################

# Blogroll
# (anchor-text, icon-name, URL)
LINKS = (
    ('CV/Resume', 'user', '/pages/duncan-locks-resume.html'),
    ('LinkedIn', 'linkedin-squared', 'http://ca.linkedin.com/in/duncanlock/'),
    ('SO Careers', 'stackoverflow', 'http://careers.stackoverflow.com/duncanlock'),
    ('Codeistry', 'globe', 'http://codeistry.com/'),
    ('E-Numbers', 'user', '/pages/e-numbers-food-additives.html'),
)

# Social widget
# (anchor-text, icon-name, URL)
SOCIAL = (
    ('Twitter', 'twitter', 'http://twitter.com/duncanlock'),
    ('GitHub', 'github-circled', 'http://github.com/dflock'),
    ('Stack Overflow', 'stackoverflow', 'http://stackoverflow.com/users/259698/duncan-lock')
)

# Extra Header Menu links
# (anchor-text, icon-name, URL)
# HEADER_LINKS = (
#     ('about', '', '/pages/about.html'),
# )

TWITTER_USERNAME = 'duncanlock'
TWITTER_ACCOUNT_ID = '1512952557'
TWITTER_CARD = True

ARTICLE_TWEET_BUTTON = False
ARTICLE_GOOGLEPLUS_BUTTON = False

DEFAULT_PAGINATION = 8
DEFAULT_ORPHANS = 1

OPEN_GRAPH_METADATA = True
DUBLIN_CORE_METADATA = True

DEFAULT_PAGESCHEMA = 'BlogPost'

# Switch Typogrify on, to get fancier Typography
# See here for more: https://github.com/mintchaos/typogrify
TYPOGRIFY = True
# TYPOGRIFY_IGNORE_TAGS = ['pre', 'code', 'tty']

# Which theme to use
THEME = '../blueprint'

# Where should Pelican look for content?
PATH = ('content')
# These are relative to PATH, above
ARTICLE_PATHS = ['posts']
PAGE_PATHS = ['pages']


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

# Don't bother generating an Author page - we've only got one author
AUTHOR_SAVE_AS = False

# Do we want all our pages displayed in the theme's header?
DISPLAY_PAGES_ON_MENU = False

# Disqus sitename for comments. If not set, comments won't be shown.
# DISQUS_SITENAME = "duncanlocknet"


# Set Colophon variables, which can be output by the theme.
COLOPHON = True
COLOPHON_TITLE = 'About'
COLOPHON_CONTENT = """<a href="/pages/duncan-locks-resume.html">
An adaptable and enthusiastic developer with broad experience
and an artistic back&shy;ground. Strong graph&shy;ical
com&shy;munication, design, creative
<span class="amp">&amp;</span> prob&shy;lem solving
skills &mdash; and an eye for detail.</a>"""

#################################
#
# Social Settings
#
#################################

# ARTICLE_TWEET_BUTTON = True
# ARTICLE_GPLUS_BUTTON = True

#################################
#
# Setting for plugins
#
#################################

# Where to look for plugins
PLUGIN_PATHS = ['../pelican-plugins']
# PLUGIN_PATH = '../pelican-plugins-integration'
# Which plugins to enable
PLUGINS = [
    'asciidoc_reader',
    'better_figures_and_images',
    'assets',
    'related_posts',
    'extract_toc',
    'post_stats',
    'series'
]

ASCIIDOC_OPTIONS = ['-a source-highlighter=rouge', '-a rouge-style=monokai', '-r asciidoctor-html5s', '-b html5s']
# ASCIIDOC_OPTIONS = ['-a source-highlighter=rouge', '-a rouge-style=monokai', '-r asciidoctor-html5s', '-b html5s', '-T ~/dev/asciidoctor-html5s']

# Settings for the better_figures_and_images plugin
RESPONSIVE_IMAGES = True
# FIGURE_NUMBERS = True

# Settings for the related_posts plugin
RELATED_POSTS_MAX = 4


#################################
#
# Custom Jinja Filters
#   see: http://jinja.pocoo.org/docs/templates/#filters
#
#################################


def suffix(d, wrap=True):
    tmp = 'th' if 11 <= d <= 13 else {1: 'st', 2: 'nd', 3: 'rd'}.get(d % 10, 'th')
    if wrap:
        return '<span class="day_suffix">' + tmp + '</span>'
    else:
        return tmp


def tagsort(tags):
    return sorted(tags, key=lambda x: len(x[1]))


def custom_strftime(format, t):
    return t.strftime(format).replace('{S}', str(t.day) + suffix(t.day))


def month_name(month_number):
    import calendar
    return calendar.month_name[month_number]


def archive_date_format(date):
    return custom_strftime('{S} %B, %Y', date)


def sidebar_date_format(date):
    return custom_strftime('%a {S} %B, %Y', date)


def dump(thing):
    import pprint
    pp = pprint.PrettyPrinter(indent=4)
    return pp.pformat(thing)


# Which custom Jinja filters to enable
JINJA_FILTERS = {
    "month_name": month_name,
    "archive_date_format": archive_date_format,
    "sidebar_date_format": sidebar_date_format,
    "tagsort": tagsort,
    "dump": dump,
}
