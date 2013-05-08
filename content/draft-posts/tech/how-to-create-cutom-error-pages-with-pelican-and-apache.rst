:title: How To Create Cutom Error pages with Pelican and Apache
:slug: how-to-create-cutom-error-pages-with-pelican-and-apache
:date: 2013-05-06 18:25:15
:tags: tutorial, pelican, apache
:category: tech

Add this to your ``.htaccess`` file:

.. code-block:: apacheconf

	# ----------------------
	# | Custom Error Pages |
	# ----------------------

	ErrorDocument 404 /pages/404.html
	ErrorDocument 403 /pages/403.html

