:title: How To Create Custom Error pages with Pelican and Apache
:slug: how-to-create-custom-error-pages-with-pelican-and-apache
:date: 2013-07-02 18:18:15
:tags: tutorial, pelican, apache
:category: tech

Add this to your ``.htaccess`` file:

.. code-block:: apacheconf

	# ----------------------
	# | Custom Error Pages |
	# ----------------------

	ErrorDocument 404 /pages/404.html
	ErrorDocument 403 /pages/403.html
