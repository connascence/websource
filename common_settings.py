#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Thomi Richards'
SITENAME = 'connascence.io'
PATH = 'content'
TIMEZONE = 'Pacific/Auckland'
DEFAULT_LANG = 'en'

# No need for this fancy ATOM stuff...
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

DEFAULT_PAGINATION = False

THEME = 'theme'

# We never display dates on articles. This prevents pelican from complaining
# about the missing 'date' metadata from articles.
DEFAULT_DATE = 'fs'


# Order 'articles' (really connascences) by their 'strength' metadata.
ARTICLE_ORDER_BY = lambda a: int(a.metadata.get('strength', '100'))
# Order 'pages' similarly - controls order in navigation.
PAGE_ORDER_BY = lambda p: int(p.metadata.get('strength', '100'))


# Disable tag, category, author and archive pages:
DIRECT_TEMPLATES = ['index']
