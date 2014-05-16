#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = u"Mark Betnel"
SITENAME = u"Lab Science"
SITEURL = 'http://markbetnel.com/courses/labscience-f2014'

TIMEZONE = 'America/Los_Angeles'
GOOGLE_ANALYTICS = "UA-20141547-1"
DEFAULT_LANG='en'

DISQUS_SITENAME = 'betnelcourses'

# Blogroll
LINKS =  (
    ('PhET Sims', 'http://phet.colorado.edu'),
    ('Wolfram Alpha', 'http://www.wolframalpha.com/'),
    ('DESMOS', 'http://www.desmos.com')	
        )


DEFAULT_PAGINATION = 20 
DISPLAY_PAGES_ON_MENU = False

TAG_SAVE_AS = 'tag/{slug}.html'
TAG_URL = 'tag/{slug}.html'    

PLUGIN_PATH = '../../../pelican-plugins' 
PLUGINS = ['create_calendar', 'ical', 'gallery', 'pelican-vimeo', 'pelican-youtube']
