# -*- coding: utf-8 -*-
"""
Extract Table of Contents from AsciiDoc output from the htmls backend
========================

A Pelican plugin to extract table of contents (ToC) from `article.content` and
place it in its own `article.toc` variable for use in templates.
"""

from os import path
from bs4 import BeautifulSoup
from pelican import signals, readers, contents
import logging

logger = logging.getLogger(__name__)


def extract_asciidoc_toc(content):
    if isinstance(content, contents.Static):
        return

    soup = BeautifulSoup(content._content, "html.parser")
    toc = None

    toc = soup.find("nav", id="toc")

    if toc:
        toc.extract()
        content._content = soup.decode()

        # Remove: <h2 id="toc-title">Table of Contents</h2>
        toc.h2.decompose()

        # Change all ordered lists to unordered
        for l in toc("ol"):
            l.name = "ul"

        content.toc = toc.decode()

        logger.debug(f"ExtractAsciidocToc: content.toc: {content.toc}")


def register():
    signals.content_object_init.connect(extract_asciidoc_toc)
