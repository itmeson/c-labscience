#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = u"Mark Betnel"
SITENAME = u"ScientificInvestigation Winter2015-16"
SITEURL = 'http://markbetnel.com/courses/si/current'

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

LANDING_PAGE_ABOUT = {'details': """<div itemscope itemtype="http://schema.org/Person"><p>This is the course page for the Winter 2015-2016 trimester of SAAS Scientific Investigation.  Please use the comment function on any page that you have questions about, use the Overview section for general course info, and the Lessons and Homework sections to find out what you need to do if you missed a day or are reviewing past material.</p></div>"""}


