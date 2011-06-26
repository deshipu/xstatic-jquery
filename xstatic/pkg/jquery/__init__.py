"""
jQuery package (following xstatic standard)
"""

from os.path import join, dirname

from xstatic.main import XStatic

class JQuery(XStatic):
    name = 'jquery' # short, all lowercase name
    display_name = 'jQuery' # official name, upper/lowercase allowed
    version = '1.6.1' # for simplicity, use same version as bundled files

    base_dir = join(dirname(__file__), 'data')
    # base_dir = '/usr/share/javascript/jquery'

    description = "%s (xstatic packaging standard)" % display_name

    platforms = 'any'
    classifiers = []
    keywords = '%s xstatic' % name

    # this all refers to the XStatic-* package:
    author = 'xstatic developers'
    author_email = 'xstatic@example.org'
    license = '(same a %s)' % display_name
    homepage = 'http://xstatic.example.org/'

    # XXX shall we have another bunch of entries for the bundled files?
    # like upstream_author/homepage/download/...?

    locations = {
        # if value is a string, it is a base location, just append relative
        # path/filename. if value is a dict, do another lookup using the
        # relative path/filename you want.
        # your relative path/filenames should usually be without version
        # information, because either the base dir/url is exactly for this
        # version or the mapping will care for accessing this version.
        ('google', 'http'): 'http://ajax.googleapis.com/ajax/libs/jquery/%s' % version,
        ('google', 'https'): 'https://ajax.googleapis.com/ajax/libs/jquery/%s' % version,
        ('jquery', 'http'): {
            'jquery.js': 'http://code.jquery.com/jquery-%s.js' % version,
            'jquery.min.js': 'http://code.jquery.com/jquery-%s.min.js' % version,
        },
        ('microsoft', 'http'): {
            'jquery.js': 'http://ajax.aspnetcdn.com/ajax/jquery/jquery-%s.js' % version,
            'jquery.min.js': 'http://ajax.aspnetcdn.com/ajax/jquery/jquery-%s.min.js' % version,
        },
        ('microsoft', 'https'): {
            'jquery.js': 'https://ajax.aspnetcdn.com/ajax/jquery/jquery-%s.js' % version,
            'jquery.min.js': 'https://ajax.aspnetcdn.com/ajax/jquery/jquery-%s.min.js' % version,
        },
    }

