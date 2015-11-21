#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = u"Mark Betnel"
SITENAME = u"ScientificInvestigation Winter2015-16"
SITEURL = 'http://markbetnel.com/courses/si/w2015-16'

TIMEZONE = 'America/Los_Angeles'
GOOGLE_ANALYTICS = "UA-20141547-1"
DEFAULT_LANG='en'

DISQUS_SITENAME = 'betnelcourses'
COMMENTS_INTRO = "Is something unclear? Leave a comment below:"


# Blogroll
LINKS =  (
    ('PhET sims', 'http://phet.colorado.edu'),
    ('DESMOS', 'http://www.desmos.com'),
    ('NPR Science', 'http://www.npr.org/sections/science/')	
        )


DEFAULT_PAGINATION = 20 
DISPLAY_PAGES_ON_MENU = False

TAG_SAVE_AS = 'tag/{slug}.html'
TAG_URL = 'tag/{slug}.html'    

PLUGIN_PATHS = ['/home/mark/Sites/pelican-plugins']
PLUGINS = ['create_calendar', 'ical', 'gallery', 'pelican_vimeo', 'tipue_search', 'pelican_youtube', 'sitemap', 'latex']

DIRECT_TEMPLATES = (('index', 'tags', 'categories','archives', 'search', '404'))

SITEMAP = { 'format': 'xml'}

CC_LICENSE = "CC-BY"
