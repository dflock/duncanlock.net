#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Duncan Lock'
SITENAME = u'duncanlock.net'
SITEURL = 'http://duncanlock.test'
SITE_DOMAIN = u'duncanlock.net'

SITE_DESCRIPTION = u'Duncan Locks personal site. Includes my blog, colitis resources, SCD recipes, portfolio and CV/Resume.'

TIMEZONE = 'America/Vancouver'

DEFAULT_LANG = u'en'
DEFAULT_DATE = (None)

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
    ('extras/favicon.png', 'favicon.png'),
)

# DELETE_OUTPUT_DIRECTORY = True

# Blogroll
LINKS = (
    ('About', '/pages/about.html'),
    ('Codeistry', 'http://codeistry.com/'),
)

# Social widget
SOCIAL = (
    ('twitter', 'http://twitter.com/duncanlock'),
    ('github', 'http://github.com/dflock'),
    ('stack-overflow', 'http://stackexchange.com/users/95334/dflock?tab=accounts'),
    ('google-plus', 'https://plus.google.com/108110520114045131522'),
)
ARTICLE_TWEET_BUTTON = False
TWITTER_USERNAME = 'duncanlock'

DEFAULT_PAGINATION = 10
DEFAULT_ORPHANS = 1

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

TYPOGRIFY = True

THEME = './themes/duncs-v1'

PATH = ('content')
ARTICLE_DIR = ('posts')
PAGE_DIR = ('pages')

USE_FOLDER_AS_CATEGORY = True
ARTICLE_URL = 'blog/{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = 'blog/{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'

YEAR_ARCHIVE_SAVE_AS = 'blog/{date:%Y}/index.html'
MONTH_ARCHIVE_SAVE_AS = 'blog/{date:%Y}/{date:%m}/index.html'
DAY_ARCHIVE_SAVE_AS = 'blog/{date:%Y}/{date:%m}/{date:%d}/index.html'

ARCHIVES_SAVE_AS = 'blog/index.html'

DISPLAY_PAGES_ON_MENU = False
# DISQUS_SITENAME = "duncanlocknet"

SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.5,
        'indexes': 0.5,
        'pages': 0.5
    },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'weekly',
        'pages': 'monthly'
    }
}

COLOPHON = False
COLOPHON_TITLE = 'About'
COLOPHON_CONTENT = 'An adaptable and enthusiastic developer with broad experience and strong graphical communication skills. Proven web, database and application developer &ndash; able to work as a team with users and other developers to create and support practical solutions.'

PLUGIN_PATH = '../pelican-plugins'
PLUGINS = ['better_figures_and_images', 'assets', 'gzip_cache', 'sitemap']

RESPONSIVE_IMAGES = True


def month_name(month_number):
    import calendar
    return calendar.month_name[month_number]


def suffix(d):
    return 'th' if 11 <= d <= 13 else {1: 'st', 2: 'nd', 3: 'rd'}.get(d % 10, 'th')


def custom_strftime(format, t):
    return t.strftime(format).replace('{S}', str(t.day) + suffix(t.day))


def archive_date_format(date):
    return custom_strftime('{S} %B, %Y', date)


JINJA_FILTERS = {
    "month_name": month_name,
    "archive_date_format": archive_date_format,
}
