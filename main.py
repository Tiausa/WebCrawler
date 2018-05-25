# import json
# #
# from QParse import Sublink, WebPage
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
# #url = Sublink("http://cs467-pavo-tests.appspot.com/graph3/a")
# #url = Sublink("http://cs467-pavo-tests.appspot.com/graph4")
# #url = Sublink("http://cs467-pavo-tests.appspot.com/graph5/a")
# #url = Sublink("http://cs467-pavo-tests.appspot.com/graph6/a")
# #url = Sublink("http://cs467-pavo-tests.appspot.com/graph7")
# #url = Sublink("http://cs467-pavo-tests.appspot.com/graph8/a")
# #url = Sublink("http://cs467-pavo-tests.appspot.com/graph9")
# #url = Sublink("http://cs467-pavo-tests.appspot.com/graph10")
# #url = Sublink("http://cs467-pavo-tests.appspot.com/graph11/a")
#
#
# #url = Sublink("http://cs467-pavo-tests.appspot.com/tia1")
# #url = Sublink("http://cs467-pavo-tests.appspot.com/tia2")
# #url = Sublink("https://sterritmspyware.wordpress.com/2018/02/01/trojan-spyware-sneaks-into-your-keyboard/")
#
# #url = Sublink("https://sterritmspyware.wordpress.com/")
# url = Sublink("http://bl.ocks.org/rkirsling/5001347")
# #url = Sublink("http://www.wikipedia.com")
#
# newPage = WebPage(url)
# sentString = ''
# arrayKeyword = {sentString}
# if sentString == '':
#     urls = newPage.GoSearch(url, 'DFS', 5)
# else:
#     urls = newPage.GoSearch(url, 'DFS', 5, arrayKeyword)
# dict = {}
# dict['URLs'] = urls
# dict['start'] = url.getUrl()
# print json.dumps(dict, indent=4, sort_keys=True)




import webapp2
import urllib
import urllib2
import json
from webapp2 import redirect
import os
from google.appengine.ext.webapp import template
#from Parse import Sublink, Webpage

import logging
from QParse import Sublink, WebPage



# [START main_page]
class MainPage(webapp2.RequestHandler):

    def get(self):
        try:
            self.response.write("hello world!")
        except Exception as e:
            self.response.set_status(500)
            self.response.out.write(json.dumps(self))

    def post(self):
        try:
            data = json.loads(self.request.body)
            ## Tia's code here
            url = Sublink(data['page'])
            newPage = WebPage(url)
            sentString = data['keyword']
            if sentString == '':
                urls = newPage.GoSearch(url, data['method'], data['limit'])
            else:
                arrayKeyword = {sentString}
                urls = newPage.GoSearch(url, data['method'], data['limit'], arrayKeyword)
            dict = {}
            dict['URLs'] = urls
            dict['start'] = url.getUrl()
            dict['cookie'] = 'temp'

            self.response.write(json.dumps(dict))
        except Exception as e:
            self.response.set_status(500)
            self.response.out.write(json.dumps(self))



# [END main_page]


app = webapp2.WSGIApplication([
    ('/', MainPage)
], debug=True)



