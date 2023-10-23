# -*- coding: utf-8 -*-
"""
Tipue Search
============

A Pelican plugin to serialize generated HTML to JSON
that can be used by jQuery plugin - Tipue Search.

Copyright (c) Talha Mansoor
"""

from __future__ import unicode_literals

import os.path
import json
import re
import zlib
from bs4 import BeautifulSoup
from codecs import open
try:
	from urlparse import urljoin
except ImportError:
	from urllib.parse import urljoin

from pelican import signals


class Tipue_Search_JSON_Generator(object):

	def __init__(self, context, settings, path, theme, output_path, *null):
		self.output_path = output_path
		self.context = context
		self.siteurl = settings.get('SITEURL')
		self.relative_urls = settings.get('RELATIVE_URLS')
		self.tpages = settings.get('TEMPLATE_PAGES')
		self.output_path = output_path
		self.json_nodes = []

	def create_json_node(self, page):
		if getattr(page, 'status', 'published') != 'published':
			return

		soup_title = BeautifulSoup(page.title.replace('&nbsp;', ' '), 'html.parser')
		page_title = soup_title.get_text(' ', strip=True).replace('“', '"').replace('”', '"').replace('’', "'").replace('^', '&#94;')

		soup_text = BeautifulSoup(page.content, 'html.parser')
		page_text = soup_text.get_text(' ', strip=True).replace('“', '"').replace('”', '"').replace('’', "'").replace('¶', ' ').replace('^', '&#94;')

		page_category = page.category.name if getattr(page, 'category', 'None') != 'None' else ''
		if page_category == "Hidden":
			return

		page_url = '.'
		if page.url:
			page_url = page.url if self.relative_urls else (self.siteurl + '/' + page.url)

		page_text = re.sub(r'[^ 0-9A-Za-z\u0400-\u04FF]', ' ', page_text.lower())
		page_text = ' '.join(page_text.split())
		self.json_nodes.append({
			'title': page_title,
			'category': page_category,
			'url': page_url.replace(".html", ""),
			'text': page_text
		})

	def generate_output(self, writer):
		pages = self.context['pages'] + self.context['articles']

		for article in self.context['articles']:
			pages += article.translations

		for page in pages:
			self.create_json_node(page)

		sitemap = json.dumps({'pages': self.json_nodes}, ensure_ascii=False)

		path = os.path.join(self.output_path, 'sitemap.gz')
		with open(path, 'wb') as f:
			f.write(zlib.compress(str.encode(sitemap), 9))

def get_generators(generators):
	return Tipue_Search_JSON_Generator

def register():
	signals.get_generators.connect(get_generators)
