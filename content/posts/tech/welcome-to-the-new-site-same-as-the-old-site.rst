:title: Welcome to the New Site; same as the Old Site.
:slug: welcome-to-the-new-site-same-as-the-old-site
:date: 2013-04-26 16:48:57
:tags: pelican, backend, frontend
:meta_description: I've been meaning to consolidate my personal websites onto this domain for a *long, long* time. My original personal website, dflock.co.uk, started in the late nineties - and has been getting a bit long in the tooth of late.

I've been meaning to consolidate my personal websites onto this domain for a *long, long* time. My original personal website, `dflock.co.uk <http://www.dflock.co.uk/>`_, started in the late nineties - and has been getting a bit long in the tooth of late.

.. figure:: {static}/images/posts/welcome-to-the-new-site-same-as-the-old-site/screenshot-13-04-26_06-54-42-pm.png
	:alt: Screenshot of the current version of the dflock.co.uk website homepage, at the time of publishing this post. It's kinda green and nineties looking.

	Static text files - the gift that keeps on giving.

	That site has been up, looking mostly like that, for ~15 years - with zero maintenance or downtime. Nice to know it's still valid CSS 1.0 :)

When I created that site originally, the options were either `Adobe PageMill <http://en.wikipedia.org/wiki/Adobe_PageMill>`_, or hand editing HTML in a text editor. I've never been a fan of :abbr:`WYSIWYG (what-you-see-is(supposedly)-what-you-get)` editors - and the early ones were... not good, so I wrote all the HTML code by hand.

That site also has some `data heavy pages <http://www.dflock.co.uk/colitis/foods/enumbers.html>`_, which are manually published from XML files using :abbr:`XSLT (Extensible Stylesheet Language Transformations)` to output HTML, processed by `Saxon <http://en.wikipedia.org/wiki/Saxon_XSLT>`_, later `XMLStarlet <http://en.wikipedia.org/wiki/XMLStarlet>`_ -- again, all written and run by hand.

As far as I can remember, I did all that on a 486sx Windows '98 PC, using the `TextPad <http://en.wikipedia.org/wiki/TextPad>`_ text editor -- which is apparently still available, unlike Adobe PageMill.

Baked, not Fried
-------------------

Since then, I've been in the trenches doing web development, amongst other things. Along came CSS, then PHP, Dynamic Sites, MySQL, JavaScript (anyone remember :abbr:`DHTML (Dynamic HTML)`?), AJAX, Web Apps, Websockets, Ruby, Python, Cloud Hosting, HTML5, etc, etc... things have got a *lot* more complex in the web development world over the last 15 years.

There are good reasons for most of these, obviously, but it unavoidably layers on a lot of complexity. Websites that were originally just a folder full of static files are now a complex cocktail of many different pieces of technology. A 'simple blog' nowadays might well combine PHP, MySQL, HTML, CSS & JavaScript -- like `WordPress <http://wordpress.com/>`_ does, for example. All of these moving parts have to work together to deliver the site -- and they all have to be bulletproof to keep it secure.

But in the end, browsers still mostly just display HTML, CSS & JavaScript - which they load from the server. How you generate that in the first place is up to you. You can bake it in advance, or fry it up on each page request. The most recent spate of widely publicised WordPress security exploits might have tipped me over the edge - I decided that I wanted to simplify.

If I was going to update my old sites, I was going to do it Old School - static files, lean & clean.

So, here we are, full circle
-------------------------------

I'm sitting writing this post in `ReStructuredText <http://docutils.sourceforge.net/rst.html>`_ - a simple, easy-to-read, what-you-see-is-what-you-get plaintext format. I'm using an amazing text editor - `SublimeText <http://www.sublimetext.com/>`_ - on a quad core, 8GB RAM, Linux box. Every time I hit CTRL+s, `Pelican <http://docs.getpelican.com/>`_ automatically pours my words into the site's templates (written in `Jinja <http://jinja.pocoo.org/>`_) and bakes it all into static files in a folder. It'll then upload it to my server if I want, or I can upload them myself.

.. figure:: {static}/images/posts/welcome-to-the-new-site-same-as-the-old-site/screenshot-13-04-28_12-48-16-pm.png
	:alt: Screenshot of the above paragraph being written in SublimeText.

	Just write, save and a website appears, as if by magic.

	Static text files - they really are the gift that keeps on giving.

That same, but different. The same, but better.

.. **Next post**: How I built this site, using Pelican - a detailed run-down of how I built this site, from install to deployment.