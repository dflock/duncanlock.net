"""
``Jinja Filters`` is a plugin for `Pelican <http://docs.getpelican.com/>`_,
a static site generator written in Python.

``Jinja Filters`` provides a selection of functions (called *filters*) for
templates to use when building your website. They are packaged for Pelican, but
may prove useful for other projects that make use of Jinja.
"""

import logging

from pelican import signals

from . import jinja_filters

# METADATA

__title__ = "pelican.plugins.jinja_filters"
__description__ = "Jinja Filters for Pelican"
__url__ = "https://github.com/pelican-plugins/jinja-filters"
__author__ = "William Minchin"
__email__ = "w_minchin@hotmail.com"
__license__ = "MIT License"
__copyright__ = "Copyright (c) 2016-21 William Minchin"

"""
This project uses the Semantic Versioning scheme in conjunction with PEP 0440:

    <http://semver.org/>
    <https://www.python.org/dev/peps/pep-0440>

Major versions introduce significant changes to the API, and backwards
compatibility is not guaranteed. Minor versions are for new features and other
backwards-compatible changes to the API. Patch versions are for bug fixes and
internal code changes that do not affect the API.

Version 0.x should be considered a development version with an unstable API,
and backwards compatibility is not guaranteed for minor versions.
"""
__version__ = "2.1.0"


# Package Implementation

logger = logging.getLogger(__name__)


def add_all_filters(pelican):
    """Add (register) all filters to Pelican."""
    pelican.env.filters.update({"datetime": jinja_filters.datetime})
    pelican.env.filters.update({"article_date": jinja_filters.article_date})
    pelican.env.filters.update({"breaking_spaces": jinja_filters.breaking_spaces})
    pelican.env.filters.update(
        {"datetime_from_period": jinja_filters.datetime_from_period}
    )
    pelican.env.filters.update({"merge_date_url": jinja_filters.merge_date_url})
    pelican.env.filters.update({"month_name": jinja_filters.month_name})

    pelican.env.filters.update({"suffix": jinja_filters.suffix})
    pelican.env.filters.update({"tagsort_count": jinja_filters.tagsort_count})
    pelican.env.filters.update({"tagsort_name": jinja_filters.tagsort_name})
    pelican.env.filters.update({"custom_strftime": jinja_filters.custom_strftime})
    pelican.env.filters.update(
        {"archive_date_format": jinja_filters.archive_date_format}
    )
    pelican.env.filters.update(
        {"sidebar_date_format": jinja_filters.sidebar_date_format}
    )
    pelican.env.filters.update({"typogrify_amp": jinja_filters.typogrify_amp})
    pelican.env.filters.update({"index_template": jinja_filters.index_template})

    pelican.env.filters.update({"rating": jinja_filters.rating})


def register():
    """Plugin registration."""
    signals.generator_init.connect(add_all_filters)
