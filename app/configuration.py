#!/usr/bin/env python
# -*- coding: utf-8; mode: python; tab-width: 4; indent-tabs-mode: nil; -*-
# Application configuration.
# Copyright (c) 2009 happychickoo.
#
# The MIT License
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

import sys
import os

from os.path import dirname, abspath, realpath, join as path_join

DIR_PATH = abspath(dirname(realpath(__file__)))
EXTRA_LIB_PATH = [
    dirname(DIR_PATH),
    path_join(DIR_PATH, 'appengine'),
    path_join(DIR_PATH, 'gaeutilities'),
    path_join(DIR_PATH, 'jinja2'),
    path_join(DIR_PATH, 'pyporter2'),
    path_join(DIR_PATH, 'aeoid'),
]
sys.path = EXTRA_LIB_PATH + sys.path

def sanitize_url(url):
    """Ensures that the URL ends with a slash."""
    if not url.endswith('/'):
        url = url + '/'
    return url

NAKED_DOMAIN = 'themoneybees.in'
ADMIN_EMAIL = "administrator@%s" % (NAKED_DOMAIN, )
CONTACT_EMAIL = ADMIN_EMAIL
APPLICATION_ID = os.environ['APPLICATION_ID']
APPLICATION_TITLE = "The Money Bees"
MODE_DEVELOPMENT = 'development'
MODE_PRODUCTION = 'production'
SERVER_PORT = os.environ['SERVER_PORT']
SERVER_NAME = os.environ['SERVER_NAME']
SERVER_SOFTWARE = os.environ['SERVER_SOFTWARE']
TEXT_BLOG_URL = 'http://blog.themoneybees.com'

# Analytics identifiers.
GOOGLE_ANALYTICS_ID = 'UA-12340948-1'

OWNER_NAME = 'Saurabh Maheshwari'
OWNER_ADDRESS = 'Address'
OWNER_URL = '/'
OWNER_COMPANY = 'The Money Bees'
COPYRIGHT_YEARS = '2010'

if SERVER_PORT and SERVER_PORT != '80':
    # We are using the development server.
    DEPLOYMENT_MODE = MODE_DEVELOPMENT
    HOST_NAME = '%s:%s' % (SERVER_NAME, SERVER_PORT,)
    LOCAL = True
    DEBUG = True
    #MEDIA_URL = 'http://%s/s/' % (HOST_NAME, )
    MEDIA_URL = "/s/"
    TEXT_MEDIA_URL = MEDIA_URL
else:
    # We are using the production server.
    DEPLOYMENT_MODE = MODE_PRODUCTION
    HOST_NAME = SERVER_NAME
    LOCAL = False
    DEBUG = False
    TEXT_MEDIA_URL = "http://assets.%s/" % (NAKED_DOMAIN, )
    MEDIA_URL = TEXT_MEDIA_URL

if DEBUG:
    # Minification suffixes to use for CSS and JS files.
    CSS_MINIFIED = '-min'
    JS_MINIFIED = '-min'
else:
    CSS_MINIFIED = '-min'
    JS_MINIFIED = '-min'

# The URL root of the Website.
# For example:
#     http://www.example.com/
#     http://localhost:8000/
ROOT_URL = 'http://%s/' % (HOST_NAME,)

# ---------------------------------------------------------------------------
# Stuff that should be different in production.
cdn_urls = {
    'microsoft.jquery-1.3.2': "http://ajax.microsoft.com/ajax/jQuery/jquery-1.3.2.min.js",
    'google.jquery-1.3.2': "http://ajax.googleapis.com/ajax/libs/jquery/1.3.2/jquery.min.js",
    'jquery.jquery-1.4': "http://code.jquery.com/jquery-1.4a1.min.js",
    'local.jquery-1.4': "%sscript/lib/chickoojs/src/jquery/jquery-1.4a1.min.js" % (MEDIA_URL,),
    'local.jquery-1.3.2': "%sscript/lib/chickoojs/src/jquery/jquery-1.3.2.min.js" % (MEDIA_URL,),
}

if LOCAL:
    JQUERY_URL = cdn_urls.get('local.jquery-1.4')
    ANALYTICS_CODE = ""
else:
    JQUERY_URL = cdn_urls.get('jquery.jquery-1.4')
    ANALYTICS_CODE = """
<script type="text/javascript">
var _gaq = _gaq || [];
_gaq.push(['_setAccount', '%(GOOGLE_ANALYTICS_ID)s']);
_gaq.push(['_trackPageview']);
(function() {
  var doc=document, ga = doc.createElement('script');
  ga.src = ('https:' == doc.location.protocol ? 'https://ssl' :
      'http://www') + '.google-analytics.com/ga.js';
  ga.setAttribute('async', 'true');
  doc.documentElement.firstChild.appendChild(ga);
})();
</script>
""" % dict(GOOGLE_ANALYTICS_ID=GOOGLE_ANALYTICS_ID)


# The builtin variables that are available to all templates.
TEMPLATE_BUILTINS = {
    'ADMIN_EMAIL': ADMIN_EMAIL,
    'APPLICATION_TITLE': APPLICATION_TITLE,
    'APPLICATION_NAME': APPLICATION_TITLE,
    'CSS_MINIFIED': CSS_MINIFIED,
    'CONTACT_EMAIL': CONTACT_EMAIL,
    'DEBUG': DEBUG,
    'DEPLOYMENT_MODE': DEPLOYMENT_MODE,
    'GOOGLE_ANALYTICS_ID': GOOGLE_ANALYTICS_ID,
    'JS_MINIFIED': JS_MINIFIED,
    'LOCAL': LOCAL,
    'MEDIA_URL': sanitize_url(MEDIA_URL),
    'NAKED_DOMAIN': NAKED_DOMAIN,
    'ROOT_URL': sanitize_url(ROOT_URL),
    'TEMPLATE_DEBUG': DEBUG,
    'OWNER_URL': OWNER_URL,
    'OWNER_NAME': OWNER_NAME,
    'OWNER_ADDRESS': OWNER_ADDRESS,
    'OWNER_COMPANY': OWNER_COMPANY,
    'COPYRIGHT_YEARS': COPYRIGHT_YEARS,
    'JQUERY_URL': JQUERY_URL,
    'ANALYTICS_CODE': ANALYTICS_CODE,
    'TEXT_MEDIA_URL': TEXT_MEDIA_URL,
    'TEXT_BLOG_URL' : TEXT_BLOG_URL, 
}

# Directories in which to search for templates.
TEMPLATE_DIRS = (
    path_join(DIR_PATH, 'templates'),
)
