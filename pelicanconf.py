#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Abdur-Rahmaan Janhangeer'
SITENAME = 'Refining the Azimuth'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Indian/Mauritius'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),)

# Social widget
SOCIAL = (('github', 'https://github.com/Abdur-RahmaanJ'),
          ('linkedIn', 'https://linkedin.com/in/appinv'),)

DEFAULT_PAGINATION = 5

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

OUTPUT_PATH = '../Abdur-rahmaanJ.github.io'

THEME = 'theme'

PLUGIN_PATHS = ['plugins/', ]

PLUGINS = ['i18n_subsites', ]

JINJA_ENVIRONMENT = {
    'extensions': ['jinja2.ext.i18n'],
}

BOOTSTRAP_THEME = 'superhero'

PYGMENTS_STYLE = 'monokai'

#:::python3     
ARTICLE_PATHS = ['articles']

STATIC_PATHS = ['img', 'pdf']

#:::python3     
PAGE_PATHS = ['pages']

ARTICLE_URL = 'articles/{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = 'articles/{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'

PAGE_URL = 'pages/{slug}/'
PAGE_SAVE_AS = 'pages/{slug}/index.html'
CATEGORY_URL = 'category/{slug}'
CATEGORY_SAVE_AS = 'category/{slug}/index.html'
TAG_URL = 'tag/{slug}'
TAG_SAVE_AS = 'tag/{slug}/index.html'

'''
git init
git remote add origin https://github.com/Abdur-rahmaanJ/Abdur-rahmaanJ.github.io
git add -A
git commit -m "initial commit"
git push --set-upstream origin master

'''

'''

    :::python3
    def do_twice(func):
    def wrapper_do_twice(*args, **kwargs):
        return func(*args, **kwargs).lower()
    return wrapper_do_twice

    @do_twice
    def say_whee(some_text):
        print(some_text)

    x = 'Whee!'
    say_whee(x)
'''