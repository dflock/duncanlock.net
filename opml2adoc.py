import os
import sys
import urllib.request
import xml.etree.ElementTree as ET
from datetime import datetime

key = os.environ["MINIFLUX_API_KEY"]

if not key:
    print("$MINIFLUX_API_KEY not set.")
    sys.exit(-1)

url = "http://miniflux.home/v1/export"
hdr = {"X-Auth-Token": key}
request = urllib.request.Request(url, headers=hdr)
opml = ET.fromstring(urllib.request.urlopen(request).read())
updated = datetime.now().astimezone().replace(microsecond=0).isoformat(" ")

header = f"""
:title: Blogroll & Links
:slug: blogroll-links
:created: 2022-11-15 13:23:54-08:00
:date: {updated}
:meta_description: These are the feeds that I read, exported from my home Miniflux instance as an OPML file & converted to AsciiDoc.
:toc:
:toc-class: page-toc

[.lead]
These are the feeds that I read, exported from my home https://miniflux.app/[Miniflux] instance as an https://en.wikipedia.org/wiki/OPML[OPML] file & converted to AsciiDoc.

See how this page is made: link:++{{filename}}/posts/tech/automatically-publishing-a-blogroll-from-an-opml-file.adoc++[Automatically Publishing a Blogroll from an OPML File]
"""


print(header)

feed_icon = '<i class="icon"><svg><use href="#feed"></use></svg></i>'

for section in opml[1]:
    if section.attrib["text"] not in ["personal"]:
        print(f'\n## {section.attrib["text"].replace("-", " ").title()}\n')
        print("[.three-columns]")
        for link in section:
            feed_link = f'+++<a href="{link.attrib["xmlUrl"]}" title="Link to Feed">{feed_icon}</a>+++'
            print(
                f'* {link.attrib["htmlUrl"]}[{link.attrib["title"]},title="Link to Website"] {feed_link}'
            )

print("\n'''\n")
print(f"Last updated: {updated}.\n")
