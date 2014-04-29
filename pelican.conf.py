#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = u"Mark Betnel"
SITENAME = u"Lab Science"
SITEURL = 'http://markbetnel.com/courses/labscience'

TIMEZONE = 'America/Los_Angeles'
GOOGLE_ANALYTICS = "UA-20141547-1"
DEFAULT_LANG='en'

DISQUS_SITENAME = 'labscience'

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

PLUGIN_PATH = '../../../pelican-plugins' 
PLUGINS = ['sitemap', 'create_calendar', 'ical', 'gallery', 'pelican-vimeo', 'pelican-youtube']


CC_LICENSE = "CC-BY"
