## Name: Michael Sterritt
## Date: 2/11/18
## CS496 - OAuth 2.0 Implementation
## Description: Program implements a OAuth 2.0 Server Side flow without using a 3rd party OAuth library. Program obtains access token for User from Google and displays information pertaining to the access token obtained.

import webapp2
import urllib
import urllib2
from webapp2 import redirect
import os
from google.appengine.ext.webapp import template

ROOT_URL = 'http://cs467-pavo-tests.appspot.com'
#ROOT_URL = 'http://localhost:8080'

GRAPH_VALUES = {'parse1': ROOT_URL + '/parse1',
                'parse2': ROOT_URL + '/parse2',
                'parse3': ROOT_URL + '/parse3',
                'parse4': ROOT_URL + '/parse4',
                'parse5': ROOT_URL + '/parse5',
                'parse6': ROOT_URL + '/parse6',
                'parse7': ROOT_URL + '/parse7',
                'parse8': ROOT_URL + '/parse8',
                'parse9': ROOT_URL + '/parse9',
                'graph1': ROOT_URL + '/graph1',
                'graph2': ROOT_URL + '/graph2',
                'graph3a': ROOT_URL + '/graph3/a',
                'graph3b': ROOT_URL + '/graph3/b',
                'graph4': ROOT_URL + '/graph4',
                'graph5': ROOT_URL + '/graph5/a',
                'graph5b': ROOT_URL + '/graph5/b',
                'graph6a': ROOT_URL + '/graph6/a',
                'graph6b': ROOT_URL + '/graph6/b',
                'graph6c': ROOT_URL + '/graph6/c',
                'graph7': ROOT_URL + '/graph7',
                'graph8a': ROOT_URL + '/graph8/a',
                'graph8b': ROOT_URL + '/graph8/b',
                'graph8c': ROOT_URL + '/graph8/c',
                'graph9': ROOT_URL + '/graph9',
                'graph10': ROOT_URL + '/graph10',
                'graph11a': ROOT_URL + '/graph11/a',
                'graph11b': ROOT_URL + '/graph11/b',
                'graph11c': ROOT_URL + '/graph11/c',
                'graph11d': ROOT_URL + '/graph11/d',
                'graph11e': ROOT_URL + '/graph11/e',
                'graph11f': ROOT_URL + '/graph11/f',
                'graph11g': ROOT_URL + '/graph11/g',
                'graph11h': ROOT_URL + '/graph11/h',
                'graph11i': ROOT_URL + '/graph11/i',
                'graph11j': ROOT_URL + '/graph11/j',
                'graph11k': ROOT_URL + '/graph11/k',
                'graph11l': ROOT_URL + '/graph11/l',
                'graph11m': ROOT_URL + '/graph11/m',
                'graph11n': ROOT_URL + '/graph11/n',
                }

## generates a random string of length n, used to randomly generate state variable

        
# [START main_page]
class MainPage(webapp2.RequestHandler):

    def get(self):
        #render page
        #template_values = {'parse1': ROOT_URL + '/parse1',
        #                   'parse2': ROOT_URL + '/parse2',
        #                   'parse3': ROOT_URL + '/parse3',
        #                   'parse4': ROOT_URL + '/parse4',
        #                   'parse5': ROOT_URL + '/parse5',
        #                   'parse6': ROOT_URL + '/parse6',
        #                   'parse7': ROOT_URL + '/parse7',
        #                   'parse8': ROOT_URL + '/parse8',
        #                   'graph1': ROOT_URL + '/graph1',
        #                   'graph2': ROOT_URL + '/graph2',
        #                   'graph3a': ROOT_URL + '/graph3/a',
        #                   'graph3b': ROOT_URL + '/graph3/b',
        #                   'graph4': ROOT_URL + '/graph4',
        #                   'graph5': ROOT_URL + '/graph5',
        #                   'graph5b': ROOT_URL + '/graph5/b',
        #                   'graph6a': ROOT_URL + '/graph6/a',
        #                   'graph6b': ROOT_URL + '/graph6/b',
        #                   'graph6c': ROOT_URL + '/graph6/c',
        #                   'graph7': ROOT_URL + '/graph7',
        #                   'graph8a': ROOT_URL + '/graph8/a',
        #                   'graph8b': ROOT_URL + '/graph8/b',
        #                   'graph8c': ROOT_URL + '/graph8/c',
        #                   'graph9': ROOT_URL + '/graph9'
        #                   }
        path = os.path.join(os.path.dirname(__file__), 'home.html')
        self.response.write(template.render(path, GRAPH_VALUES))
# [END main_page]

class Parse1Handle(webapp2.RequestHandler):

    def get(self):
        try:
            path = os.path.join(os.path.dirname(__file__), 'parse1.html')
            self.response.write(template.render(path, {}))
        except:
            self.response.write('<p>Something went wrong...</p>')

class Parse2Handle(webapp2.RequestHandler):

    def get(self):
        path = os.path.join(os.path.dirname(__file__), 'parse2.html')
        self.response.write(template.render(path, {}))

class Parse3Handle(webapp2.RequestHandler):
    def get(self):
        template_values = {'home': ROOT_URL}
        path = os.path.join(os.path.dirname(__file__), 'parse3.html')
        self.response.write(template.render(path, template_values))

class Parse4Handle(webapp2.RequestHandler):
    def get(self):
        template_values = {'home': ROOT_URL}
        path = os.path.join(os.path.dirname(__file__), 'parse4.html')
        self.response.write(template.render(path, template_values))

class Parse5Handle(webapp2.RequestHandler):
    def get(self):
        template_values = {'home': ROOT_URL,
                           'parse1': ROOT_URL + '/parse1',
                           'parse2': ROOT_URL + '/parse2'}
        path = os.path.join(os.path.dirname(__file__), 'parse5.html')
        self.response.write(template.render(path, template_values))

class Parse6Handle(webapp2.RequestHandler):
    def get(self):
        template_values = {'home': ROOT_URL,
                           'parse1': ROOT_URL + '/parse1',
                           'parse2': ROOT_URL + '/parse2',
                           'parse3': ROOT_URL + '/parse3'}
        path = os.path.join(os.path.dirname(__file__), 'parse6.html')
        self.response.write(template.render(path, template_values))

class Parse7Handle(webapp2.RequestHandler):
    def get(self):
        template_values = {'home': ROOT_URL}
        path = os.path.join(os.path.dirname(__file__), 'parse7.html')
        self.response.write(template.render(path, template_values))

class Parse8Handle(webapp2.RequestHandler):
    def get(self):
        template_values = {'home': ROOT_URL}
        path = os.path.join(os.path.dirname(__file__), 'parse8.html')
        self.response.write(template.render(path, template_values))

class Parse9Handle(webapp2.RequestHandler):
    def get(self):
        template_values = {'page': 'http://thispagedoesnotexist.com'}
        path = os.path.join(os.path.dirname(__file__), 'parse9.html')
        self.response.write(template.render(path, template_values))

class Graph1Handle(webapp2.RequestHandler):
    def get(self):
        path = os.path.join(os.path.dirname(__file__), 'graph1.html')
        self.response.write(template.render(path, GRAPH_VALUES))

class Graph2Handle(webapp2.RequestHandler):
    def get(self):
        path = os.path.join(os.path.dirname(__file__), 'graph2.html')
        self.response.write(template.render(path, GRAPH_VALUES))

class Graph3aHandle(webapp2.RequestHandler):
    def get(self):
        path = os.path.join(os.path.dirname(__file__), 'graph3a.html')
        self.response.write(template.render(path, GRAPH_VALUES))

class Graph3bHandle(webapp2.RequestHandler):
    def get(self):
        path = os.path.join(os.path.dirname(__file__), 'graph3b.html')
        self.response.write(template.render(path, GRAPH_VALUES))

class Graph4Handle(webapp2.RequestHandler):
    def get(self):
        path = os.path.join(os.path.dirname(__file__), 'graph4.html')
        self.response.write(template.render(path, GRAPH_VALUES))

class Graph5Handle(webapp2.RequestHandler):
    def get(self):
        path = os.path.join(os.path.dirname(__file__), 'graph5.html')
        self.response.write(template.render(path, GRAPH_VALUES))

class Graph5bHandle(webapp2.RequestHandler):
    def get(self):
        path = os.path.join(os.path.dirname(__file__), 'graph5b.html')
        self.response.write(template.render(path, GRAPH_VALUES))

class Graph6aHandle(webapp2.RequestHandler):
    def get(self):
        path = os.path.join(os.path.dirname(__file__), 'graph6a.html')
        self.response.write(template.render(path, GRAPH_VALUES))

class Graph6bHandle(webapp2.RequestHandler):
    def get(self):
        path = os.path.join(os.path.dirname(__file__), 'graph6b.html')
        self.response.write(template.render(path, GRAPH_VALUES))

class Graph6cHandle(webapp2.RequestHandler):
    def get(self):
        path = os.path.join(os.path.dirname(__file__), 'graph6c.html')
        self.response.write(template.render(path, GRAPH_VALUES))

class Graph7Handle(webapp2.RequestHandler):
    def get(self):
        path = os.path.join(os.path.dirname(__file__), 'graph7.html')
        self.response.write(template.render(path, GRAPH_VALUES))

class Graph8aHandle(webapp2.RequestHandler):
    def get(self):
        path = os.path.join(os.path.dirname(__file__), 'graph8a.html')
        self.response.write(template.render(path, GRAPH_VALUES))

class Graph8bHandle(webapp2.RequestHandler):
    def get(self):
        path = os.path.join(os.path.dirname(__file__), 'graph8b.html')
        self.response.write(template.render(path, GRAPH_VALUES))

class Graph8cHandle(webapp2.RequestHandler):
    def get(self):
        path = os.path.join(os.path.dirname(__file__), 'graph8c.html')
        self.response.write(template.render(path, GRAPH_VALUES))

class Graph9Handle(webapp2.RequestHandler):
    def get(self):
        path = os.path.join(os.path.dirname(__file__), 'graph9.html')
        self.response.write(template.render(path, GRAPH_VALUES))
        
class Graph10Handle(webapp2.RequestHandler):
    def get(self):
        path = os.path.join(os.path.dirname(__file__), 'graph10.html')
        self.response.write(template.render(path, GRAPH_VALUES))

class Graph11aHandle(webapp2.RequestHandler):
    def get(self):
        path = os.path.join(os.path.dirname(__file__), 'graph11a.html')
        self.response.write(template.render(path, GRAPH_VALUES))

class Graph11bHandle(webapp2.RequestHandler):
    def get(self):
        path = os.path.join(os.path.dirname(__file__), 'graph11b.html')
        self.response.write(template.render(path, GRAPH_VALUES))

class Graph11cHandle(webapp2.RequestHandler):
    def get(self):
        path = os.path.join(os.path.dirname(__file__), 'graph11c.html')
        self.response.write(template.render(path, GRAPH_VALUES))

class Graph11dHandle(webapp2.RequestHandler):
    def get(self):
        path = os.path.join(os.path.dirname(__file__), 'graph11d.html')
        self.response.write(template.render(path, GRAPH_VALUES))

class Graph11eHandle(webapp2.RequestHandler):
    def get(self):
        path = os.path.join(os.path.dirname(__file__), 'graph11e.html')
        self.response.write(template.render(path, GRAPH_VALUES))

class Graph11fHandle(webapp2.RequestHandler):
    def get(self):
        path = os.path.join(os.path.dirname(__file__), 'graph11f.html')
        self.response.write(template.render(path, GRAPH_VALUES))

class Graph11gHandle(webapp2.RequestHandler):
    def get(self):
        path = os.path.join(os.path.dirname(__file__), 'graph11g.html')
        self.response.write(template.render(path, GRAPH_VALUES))

class Graph11hHandle(webapp2.RequestHandler):
    def get(self):
        path = os.path.join(os.path.dirname(__file__), 'graph11h.html')
        self.response.write(template.render(path, GRAPH_VALUES))

class Graph11iHandle(webapp2.RequestHandler):
    def get(self):
        path = os.path.join(os.path.dirname(__file__), 'graph11i.html')
        self.response.write(template.render(path, GRAPH_VALUES))


class Graph11jHandle(webapp2.RequestHandler):
    def get(self):
        path = os.path.join(os.path.dirname(__file__), 'graph11j.html')
        self.response.write(template.render(path, GRAPH_VALUES))

class Graph11kHandle(webapp2.RequestHandler):
    def get(self):
        path = os.path.join(os.path.dirname(__file__), 'graph11k.html')
        self.response.write(template.render(path, GRAPH_VALUES))

class Graph11lHandle(webapp2.RequestHandler):
    def get(self):
        path = os.path.join(os.path.dirname(__file__), 'graph11l.html')
        self.response.write(template.render(path, GRAPH_VALUES))

class Graph11mHandle(webapp2.RequestHandler):
    def get(self):
        path = os.path.join(os.path.dirname(__file__), 'graph11m.html')
        self.response.write(template.render(path, GRAPH_VALUES))

class Graph11nHandle(webapp2.RequestHandler):
    def get(self):
        path = os.path.join(os.path.dirname(__file__), 'graph11n.html')
        self.response.write(template.render(path, GRAPH_VALUES))

app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/parse1', Parse1Handle),
    ('/parse2', Parse2Handle),
    ('/parse3', Parse3Handle),
    ('/parse4', Parse4Handle),
    ('/parse5', Parse5Handle),
    ('/parse6', Parse6Handle),
    ('/parse7', Parse7Handle),
    ('/parse8', Parse8Handle),
    ('/parse9', Parse9Handle),
    ('/graph1', Graph1Handle),
    ('/graph2', Graph2Handle),
    ('/graph3/a', Graph3aHandle),
    ('/graph3/b', Graph3bHandle),
    ('/graph4', Graph4Handle),
    ('/graph5/a', Graph5Handle),
    ('/graph5/b', Graph5bHandle),
    ('/graph6/a', Graph6aHandle),
    ('/graph6/b', Graph6bHandle),
    ('/graph6/c', Graph6cHandle),
    ('/graph7', Graph7Handle),
    ('/graph8/a', Graph8aHandle),
    ('/graph8/b', Graph8bHandle),
    ('/graph8/c', Graph8cHandle),
    ('/graph9', Graph9Handle),
    ('/graph10', Graph10Handle),
    ('/graph11/a', Graph11aHandle),
    ('/graph11/b', Graph11bHandle),
    ('/graph11/c', Graph11cHandle),
    ('/graph11/d', Graph11dHandle),
    ('/graph11/e', Graph11eHandle),
    ('/graph11/f', Graph11fHandle),
    ('/graph11/g', Graph11gHandle),
    ('/graph11/h', Graph11hHandle),
    ('/graph11/i', Graph11iHandle),
    ('/graph11/j', Graph11jHandle),
    ('/graph11/k', Graph11kHandle),
    ('/graph11/l', Graph11lHandle),
    ('/graph11/m', Graph11mHandle),
    ('/graph11/n', Graph11nHandle)
], debug=True)
