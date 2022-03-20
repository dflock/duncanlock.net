#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from datetime import date
from os.path import expanduser

#################################
#
# Basic Settings
#
#################################

AUTHOR = "Duncan Lock"
SITENAME = "duncanlock.net"
SITESCHEME = "http"
SITEURL = SITESCHEME + "://" + "duncanlock.test"
SITE_DOMAIN = "duncanlock.net"
RELATIVE_URLS = False

SITE_TITLE = "Duncan Locks personal site"
SITE_DESCRIPTION = "Duncan Locks personal site. Includes my blog, colitis resources, SCD recipes, portfolio and CV/Resume."

TIMEZONE = "America/Vancouver"

DEFAULT_LANG = "en"

COPYRIGHT_FROM = 1998
COPYRIGHT_UNTIL = date.today().year

SUMMARY_MAX_LENGTH = 140
SUMMARY_END_MARKER = "::PELICAN_END_SUMMARY"

#################################
#
# Cache Settings
#
#################################

CACHE_CONTENT = True
CHECK_MODIFIED_METHOD = "sha1"
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
STATIC_PATHS = ["images", "extras", "files"]

# A list of extra files to copy from the source to the destination
EXTRA_PATH_METADATA = {
    "extras/.htaccess": {"path": ".htaccess"},
    "extras/robots.txt": {"path": "robots.txt"},
    "extras/favicon.ico": {"path": "favicon.ico"},
    "extras/google9b8f9c7f2338fb3e.html": {"path": "google9b8f9c7f2338fb3e.html"},
    "extras/keybase.txt": {"path": ".well-known/keybase.txt"},
}

# Do we want to wipe the /output folder every build,
# or just accumulate new stuff?
DELETE_OUTPUT_DIRECTORY = True


#################################
#
# Footer Links & Menu's
#
#################################


def load_icon(path):
    from pathlib import Path
    try:
        return Path(f"./content/images/icons/{path}").read_text()
    except:
        print(f'Failed to load icon: {path}')
        return ''

def make_icon_sheet(icon_list):
    sprite_sheet = '<svg xmlns="http://www.w3.org/2000/svg" style="display: none;">\n\n'

    for name,path in icon_list.items():
        svg = load_icon(path)
        sprite_sheet += svg.replace('<svg xmlns="http://www.w3.org/2000/svg" ', f'<symbol id="{name}" ').replace('</svg>', '</symbol>')
        sprite_sheet += "\n\n"

    sprite_sheet += '</svg>'

    from scour import scour
    scour_options = scour.sanitizeOptions(options=None)
    scour_options.remove_metadata = True
    scour_options.strip_comments = True
    scour_options.newlines = False

    sprite_sheet = scour.scourString(sprite_sheet, options = scour_options)

    with open('./content/images/icons/icon_sheet.svg', "w") as f:
        f.write(sprite_sheet)

    return sprite_sheet

def get_icons(icon_list):
    tmp = {}
    for name,path in icon_list.items():
        # tmp[name] = load_icon(path)
        tmp[name] = f'<svg><use href="#{name}" /></svg>'
        # tmp[name] = f'<noscript><img src="/images/icons/{path}" width="18px" /></noscript><svg><use href="#{name}" /></svg>'

    return tmp

def get_hash(s):
    import hashlib
    return hashlib.sha256(s.encode('utf-8')).hexdigest()[:8]

ICON_LIST = {
    "home": 'fa/solid/home-lg-alt.svg',
    "archive": 'fa/solid/archive.svg',
    "tags": 'fa/solid/tags.svg',
    "tag": 'fa/solid/tag.svg',
    "feed": 'fa/solid/rss.svg',
    "clock": 'fa/solid/clock.svg',
    "read-more": 'fa/solid/arrow-right.svg',
    "category": 'fa/solid/folder.svg',
    "category_active": 'fa/solid/folder-open.svg',
    "email": 'fa/solid/envelope.svg',
    "resume": 'fa/solid/user-tie.svg',
    "twitter": 'fa/brands/twitter.svg',
    "github": 'fa/brands/github.svg',
    "linkedin": 'fa/brands/linkedin.svg',
    "stack": 'fa/brands/stack-overflow.svg',
    "globe": 'fa/solid/globe-americas.svg',
    "enumbers": 'fa/solid/cheese-swiss.svg',
    "next": 'fa/solid/arrow-right.svg',
    "previous": 'fa/solid/arrow-left.svg',
    "dark-theme": 'fa/regular/moon-stars.svg',
    "light-theme": 'custom/bright.svg',
    # "dark-theme": 'fa/regular/lightbulb.svg',
    # "light-theme": 'fa/solid/lightbulb.svg',
}

ICON_SPRITE_SHEET = make_icon_sheet(ICON_LIST)
ICON_SPRITE_SHEET_HASH = get_hash(ICON_SPRITE_SHEET)
# make_icon_sheet(ICON_LIST)
ICONS = get_icons(ICON_LIST)

# Footer Links

# (anchor-text, icon, relative URL)
SITE_LINKS = (
    ("Home", ICONS["home"], '/'),
    ("Archives", ICONS["archive"], "/blog/"),
    ("Tags", ICONS["tags"], "/tags.html"),
    ("E-Numbers", ICONS["enumbers"], "/pages/e-numbers-food-additives.html"),
)
# (anchor-text, icon-name, URL)
LINKS = (
    ("CV/Resume", ICONS["resume"], "/pages/duncan-locks-resume.html"),
    ("LinkedIn", ICONS["linkedin"], "https://www.linkedin.com/in/duncanlock/"),
    (
        "SO Careers",
        ICONS["stack"],
        "https://careers.stackoverflow.com/duncanlock",
    ),
    ("Codeistry", ICONS["globe"], "http://codeistry.com/"),
)

# Social widget
# (anchor-text, icon-name, URL)
SOCIAL = (
    ("Twitter", ICONS["twitter"], "https://twitter.com/duncanlock"),
    ("GitHub", ICONS["github"], "https://github.com/dflock"),
    (
        "Stack Overflow",
        ICONS["stack"],
        "https://stackoverflow.com/users/259698/duncan-lock",
    ),
)

# Extra Header Menu links
# (anchor-text, icon|"", URL)
HEADER_LINKS = (
    # ("about", ICONS["resume"], "/pages/about.html"),
    ("til", ICONS["tag"], "/tag/til.html"),
)

TWITTER_USERNAME = "duncanlock"
TWITTER_ACCOUNT_ID = "1512952557"
TWITTER_CARD = True

ARTICLE_TWEET_BUTTON = False
ARTICLE_GOOGLEPLUS_BUTTON = False

DEFAULT_PAGINATION = 10
DEFAULT_ORPHANS = 1

OPEN_GRAPH_METADATA = True
DUBLIN_CORE_METADATA = True

DEFAULT_PAGESCHEMA = "BlogPost"

# Switch Typogrify on, to get fancier Typography
# See here for more: https://github.com/mintchaos/typogrify
TYPOGRIFY = True
# TYPOGRIFY_IGNORE_TAGS = ['pre', 'code', 'tty']

# Which theme to use
THEME = "../blueprint"
TEMPLATE_EXTENSIONS = ['.html.j2']
# Remove the authors template
DIRECT_TEMPLATES = ['index', 'categories', 'tags', 'archives']

SHOW_THEME_SWITCHER = True

# Where should Pelican look for content?
PATH = "content"
# These are relative to PATH, above
ARTICLE_PATHS = ["posts"]
PAGE_PATHS = ["pages"]


# Use filsystem folders for categories
USE_FOLDER_AS_CATEGORY = True

INDEX_TEMPLATE_FOR_TAG = {
    "til": "minimal"
}

# What do we want article URLs to look like?
ARTICLE_URL = "blog/{date:%Y}/{date:%m}/{date:%d}/{slug}/"
ARTICLE_SAVE_AS = "blog/{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html"

# What do we want archive URLs to look like?
YEAR_ARCHIVE_SAVE_AS = "blog/{date:%Y}/index.html"
MONTH_ARCHIVE_SAVE_AS = "blog/{date:%Y}/{date:%m}/index.html"
DAY_ARCHIVE_SAVE_AS = "blog/{date:%Y}/{date:%m}/{date:%d}/index.html"

# Do something if people visit /blog
ARCHIVES_SAVE_AS = "blog/index.html"

# Don't bother generating an Author page - we've only got one author
AUTHOR_SAVE_AS = False

# Do we want all our pages displayed in the theme's header?
DISPLAY_PAGES_ON_MENU = False
# Do we want all our categories displayed in the theme's header?
DISPLAY_CATEGORIES_ON_MENU = True

# Set Colophon variables, which can be output by the theme.
COLOPHON = True
COLOPHON_TITLE = "About"
COLOPHON_CONTENT = """<a href="/pages/duncan-locks-resume.html">
An adaptable, enthusiastic writer &amp; senior software developer, with broad experience
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

#################################
#
# Setting for plugins
#
#################################

# Where to look for plugins
PLUGIN_PATHS = [expanduser("~/dev/pelican-plugins"), "./plugins"]

# Which plugins to enable
PLUGINS = [
    "jinja_filters",
    "asciidoc_reader",
    "pelican.plugins.webassets",
    "related_posts",
    "extract_toc",
    "extract_asciidoc_toc",
    "post_stats",
    "pelican.plugins.series",
    "summary",
    'drafts'
]
WEBASSETS_DEBUG = False
ASCIIDOC_OPTIONS = [
    "-a source-highlighter=rouge",
    "-a rouge-style=monokai",
    "-r asciidoctor-html5s",
    "-b html5s",
]
# ASCIIDOC_OPTIONS = ['-a source-highlighter=rouge', '-a rouge-style=monokai', '-r asciidoctor-html5s', '-b html5s', '-T ~/dev/asciidoctor-html5s']

# Settings for the related_posts plugin
RELATED_POSTS_MAX = 4
