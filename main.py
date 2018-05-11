import json
#
from Nparse import Sublink, WebPage
# #url = Sublink("http://cs467-pavo-tests.appspot.com/parse1")
#url = Sublink("http://cs467-pavo-tests.appspot.com/parse2")
# #url = Sublink("http://cs467-pavo-tests.appspot.com/parse3")
# #url = Sublink("http://cs467-pavo-tests.appspot.com/parse4")
#url = Sublink("http://cs467-pavo-tests.appspot.com/parse5")
#url = Sublink("http://cs467-pavo-tests.appspot.com/parse6")
# #url = Sublink("http://cs467-pavo-tests.appspot.com/parse7")
url = Sublink("http://cs467-pavo-tests.appspot.com/parse8")
# #url = Sublink("http://cs467-pavo-tests.appspot.com/parse9")
#
# #url = Sublink("http://cs467-pavo-tests.appspot.com/graph1")
# #url = Sublink("http://cs467-pavo-tests.appspot.com/graph2")
#url = Sublink("http://cs467-pavo-tests.appspot.com/graph3/a")
#url = Sublink("http://cs467-pavo-tests.appspot.com/graph4")
# #url = Sublink("http://cs467-pavo-tests.appspot.com/graph5")
# #url = Sublink("http://cs467-pavo-tests.appspot.com/graph6/a")
#url = Sublink("http://cs467-pavo-tests.appspot.com/graph7")
# #url = Sublink("http://cs467-pavo-tests.appspot.com/graph8/a")
# #url = Sublink("http://bl.ocks.org/rkirsling/5001347")
#
#
# newPage = WebPage(url)
# #tester = Sublink(newPage)
# arrayKeyword = {'hav66e', 'Al7so'}
# returned = newPage.GoSearch(url, 'BFS', 2, arrayKeyword)
# Title = newPage.title
# print (Title)
# for i in returned:
#     print(i)'''
# '''
# newPage = WebPage(url)
# arrayKeyword = {'hav66e', 'Als6o'}
# urls = newPage.GoSearch(url, 'BFS', 2)
# dict = {}
# dict['URLs'] = urls
# dict['start'] = url.getUrl()
# dict['cookie'] = 'temp'
# print json.dumps(dict, indent=4, sort_keys=True)'''
#
newPage = WebPage(url)
urls = newPage.GoSearch(url, 'DFS', 2)

dict = {}
dict['URLs'] = urls
dict['start'] = url.getUrl()
dict['cookie'] = 'temp'
print json.dumps(dict, indent=4, sort_keys=True)










# from google.appengine.ext.webapp import template
# from google.appengine.api import urlfetch
# import webapp2
# import json
# import logging
# from Nparse import Sublink, WebPage
#
# # Start page
# class MainHandler(webapp2.RequestHandler):
#     def get(self):
#         '''logging.getLogger().handlers[0].setLevel(logging.DEBUG)
#         url = Sublink("http://cs467-pavo-tests.appspot.com/parse6")
#         newPage = WebPage(url)
#         arrayKeyword = {'haveh', 'al88so'}
#         returned = newPage.GoSearch(url, 'DFS', 1, arrayKeyword)
#         print ('\n\n\n\n')
#         data = []
#         for i in returned:
#             #print(i)
#             logging.debug(i)
#         print ('\n\n\n\n')'''
#         logging.debug("Hello")
#
#     def post(self):
#         newPage = WebPage(url)
#         urls = newPage.GoSearch(url, 'BFS', 3)
#         dict = {}
#         dict['URLs'] = urls
#         dict['start'] = url.getUrl()
#         dict['cookie'] = 'temp'
#         print json.dumps(dict, indent=4, sort_keys=True)
#
# app = webapp2.WSGIApplication([('/', MainHandler),
#                             ('/index.html', MainHandler)],
#                             debug = True)
#
# '''

#
#
#
#
# '''
# from google.appengine.ext.webapp import template
# from google.appengine.api import urlfetch
# import webapp2
# import json
#
# ## Start page
# class MainHandler(webapp2.RequestHandler):
#     def get(self):
#         url = Sublink("http://cs467-pavo-tests.appspot.com/parse6")
#         newPage = WebPage(url)
#         arrayKeyword = {'haveh', 'also'}
#         returned = newPage.GoSearch(url, 'DFS', 2, arrayKeyword)
#         print ('\n\n\n\n')
#         for i in returned:
#             print(i)
#         print ('\n\n\n\n')
#
# app = webapp2.WSGIApplication([('/', MainHandler),
#                             ('/index.html', MainHandler)],
#                             debug = True)
#
#
#
# from Parse import Sublink, WebPage
# #url = Sublink("http://cs467-pavo-tests.appspot.com/parse1")
# #url = Sublink("http://cs467-pavo-tests.appspot.com/parse2")
# #url = Sublink("http://cs467-pavo-tests.appspot.com/parse3")
# #url = Sublink("http://cs467-pavo-tests.appspot.com/parse4")
# #url = Sublink("http://cs467-pavo-tests.appspot.com/parse5")
# #url = Sublink("http://cs467-pavo-tests.appspot.com/parse6")
# #url = Sublink("http://cs467-pavo-tests.appspot.com/parse7")
# #url = Sublink("http://cs467-pavo-tests.appspot.com/parse8")
# #url = Sublink("http://cs467-pavo-tests.appspot.com/parse9")
#
# #url = Sublink("http://cs467-pavo-tests.appspot.com/graph1")
# #url = Sublink("http://cs467-pavo-tests.appspot.com/graph2")
# #url = Sublink("http://cs467-pavo-tests.appspot.com/graph3")
# #url = Sublink("http://cs467-pavo-tests.appspot.com/graph4")
# url = Sublink("http://cs467-pavo-tests.appspot.com/graph5")
# #url = Sublink("http://cs467-pavo-tests.appspot.com/graph6/a")
# #url = Sublink("http://cs467-pavo-tests.appspot.com/graph7")
# #url = Sublink("http://cs467-pavo-tests.appspot.com/graph8/a")
# newPage = WebPage(url)
# urls = newPage.GoSearch(url, 'BFS', 3)
# dict = {}
# dict['URLs'] = urls
# dict['start'] = url.getUrl()
# dict['cookie'] = 'temp'
# print json.dumps(dict, indent=4, sort_keys=True)'''
#
# '''
# from google.appengine.ext.webapp import template
# from google.appengine.api import urlfetch
# import webapp2
# import json'''
#
#
# ## Start page
# '''class MainHandler(webapp2.RequestHandler):
#     def get(self):
#         url = Sublink("http://cs467-pavo-tests.appspot.com/parse6")
#         newPage = WebPage(url)
#         arrayKeyword = {'haveh', 'also'}
#         returned = newPage.GoSearch(url, 'DFS', 2, arrayKeyword)
#         print ('\n\n\n\n')
#         for i in returned:
#             print(i)
#         print ('\n\n\n\n')
#
#
# app = webapp2.WSGIApplication([('/', MainHandler),
#                                ('/index.html', MainHandler)],
#                               debug=True)
#
# from Parse import Sublink, WebPage'''
#
# # url = Sublink("http://cs467-pavo-tests.appspot.com/parse1")
# # url = Sublink("http://cs467-pavo-tests.appspot.com/parse2")
# # url = Sublink("http://cs467-pavo-tests.appspot.com/parse3")
# # url = Sublink("http://cs467-pavo-tests.appspot.com/parse4")
# # url = Sublink("http://cs467-pavo-tests.appspot.com/parse5")
# url = Sublink("http://cs467-pavo-tests.appspot.com/parse6")
# # url = Sublink("http://cs467-pavo-tests.appspot.com/parse7")
# # url = Sublink("http://cs467-pavo-tests.appspot.com/parse8")
# # url = Sublink("http://cs467-pavo-tests.appspot.com/parse9")
#
# # url = Sublink("http://cs467-pavo-tests.appspot.com/graph1")
# # url = Sublink("http://cs467-pavo-tests.appspot.com/graph2")
# # url = Sublink("http://cs467-pavo-tests.appspot.com/graph3")
# # url = Sublink("http://cs467-pavo-tests.appspot.com/graph4")
# #url = Sublink("http://cs467-pavo-tests.appspot.com/graph5")
# # url = Sublink("http://cs467-pavo-tests.appspot.com/graph6/a")
# # url = Sublink("http://cs467-pavo-tests.appspot.com/graph7")
# # url = Sublink("http://cs467-pavo-tests.appspot.com/graph8/a")
# newPage = WebPage(url)
# urls = newPage.GoSearch(url, 'BFS', 3)
# dict = {}
# dict['URLs'] = urls
# dict['start'] = url.getUrl()
# dict['cookie'] = 'temp'
# print json.dumps(dict, indent=4, sort_keys=True)

## Name: Michael Sterritt







'''
import webapp2
import urllib
import urllib2
import json
from webapp2 import redirect
import os
from google.appengine.ext.webapp import template
#from Parse import Sublink, Webpage

import logging
from Nparse import Sublink, WebPage



# [START main_page]
class MainPage(webapp2.RequestHandler):

    def get(self):
        self.response.write("hello world!")

    def post(self):
        data = json.loads(self.request.body)
        ## Tia's code here
        url = Sublink(data['page'])
        newPage = WebPage(url)
        urls = newPage.GoSearch(url, data['method'], data['limit'])
        #dict = {}
        #dict['URLs'] = returned
        #dict['start'] = url.getUrl()
        #dict['cookies'] = 'test'

        #newPage = WebPage(url)
        #urls = newPage.GoSearch(url, 'BFS', 3)
        dict = {}
        dict['URLs'] = urls
        dict['start'] = url.getUrl()
        dict['cookie'] = 'temp'

        self.response.write(json.dumps(dict))


# [END main_page]


app = webapp2.WSGIApplication([
    ('/', MainPage)
], debug=True)
'''

