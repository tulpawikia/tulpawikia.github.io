#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = 'Anonymous'
SITENAME = 'TulpaWikia'
SITEURL = 'https://tulpawikia.github.io'

PATH = 'content'
THEME_STATIC_DIR = 'tulpawikia'

TIMEZONE = 'Europe/Moscow'

DEFAULT_LANG = 'ru-ru'
DEFAULT_DATE = (2, 1, 1, 1, 1, 1)
SUMMARY_MAX_LENGTH = 500

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

TEMPLATE_PAGES = {
	'google482ecd4a72fc3785.html': 'google482ecd4a72fc3785.html',
}
DIRECT_TEMPLATES = ['index', 'categories']
TAGS_SAVE_AS = ''
TAG_SAVE_AS = ''

STATIC_PATHS = [
	'files',
	'images',
	'extra/robots.txt',
]
EXTRA_PATH_METADATA = {
	'extra/robots.txt': {'path': 'robots.txt'},
}

DEFAULT_PAGINATION = False

PATH = 'content'
ARTICLE_SAVE_AS = '{category}/{slug}.html'
ARTICLE_URL = '{category}/{slug}.html'

MARKDOWN = {
	'extensions': ['footnotes'],
	'extension_configs': {
		'markdown.extensions.codehilite': { # Needed for code syntax highlighting
			'css_class': 'highlight'
		},
		'markdown.extensions.extra': {},
		'markdown.extensions.meta': {},
		'markdown.extensions.toc': { # This is for enabling the TOC generation
			'title': 'Содержание',
		},
	},
	'output_format': 'html5',
}

SUMMARY_MAX_LENGTH = 150
SUMMARY_USE_FIRST_PARAGRAPH = True

EXTENDED_SITEMAP_PLUGIN = {
    'priorities': {
        'index': 1.0,
        'categories': 0.8,
        'articles': 0.8,
        'pages': 0.5,
        'authors': 0.1,
        'author': 0.1,
        'others': 0.1
    },
    'changefrequencies': {
        'index': 'monthly',
        'articles': 'weekly',
        'pages': 'weekly',
        'others': 'monthly',
    }
}

PLUGIN_PATHS = ["plugins"]
PLUGINS = [
	'extended_sitemap',
	'css-html-js-minify',
	'optimize_images',
	'tipue_search',
	'neighbors',
]

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True