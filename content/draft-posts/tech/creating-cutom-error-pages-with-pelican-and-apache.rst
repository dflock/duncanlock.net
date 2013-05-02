:title: Creating Cutom Error pages with Pelican and Apache
:slug: creating-cutom-error-pages-with-pelican-and-apache
:date: 2013-05-01 19:24:07
:tags: tutorial, pelican, apache
:category: tech

Add this to your .htaccess file:

	# ------------------------------------------------------------------------------
	# | Custom Error Pages |
	# ------------------------------------------------------------------------------

	ErrorDocument 404 /pages/404.html
	ErrorDocument 403 /pages/403.html