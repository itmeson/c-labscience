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
    ('SAGE', 'http://sagemath.org/'),
    ('Wolfram Alpha', 'http://www.wolframalpha.com/'),
    ('Khan Academy', 'http://www.khanacademy.org'),
    ('Math Fun Facts', 'http://www.math.hmc.edu/funfacts/'),
    ('R - Statistics', 'http://cran.r-project.org'),
    ('DESMOS', 'http://www.desmos.com')	
        )


DEFAULT_PAGINATION = 20 
DISPLAY_PAGES_ON_MENU = False

TAG_SAVE_AS = 'tag/{slug}.html'
TAG_URL = 'tag/{slug}.html'    

PLUGIN_PATH = '../../../pelican-plugins' 
PLUGINS = ['create_calendar', 'ical', 'gallery', 'pelican-vimeo', 'pelican-youtube']
