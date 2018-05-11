
import re
import hashlib
import urllib
import requests
from lxml import html
import urlparse
from lxml.html.clean import Cleaner
import random
'''
#This is for google app engine
from google.appengine.ext import ndb
from google.appengine.ext.webapp import template
from google.appengine.api import urlfetch
import webapp2
import json
import os
import urllib
import random
import string



class Entry(ndb.Model):
    Id = ndb.StringProperty()
    URL = ndb.StringProperty()
    Position = ndb.FloatProperty
    ParentID = ndb.JsonProperty 
    Keyword = ndb.StringProperty()
'''


dictOrP = {}
# The web page object- any page available on the world wide web,
# or used for testing purposes.
class WebPage(object):


    # Creates a new WebPage object from a link
    def __init__(self, sublink):

        # If the link is not valid, say so
        if not isinstance(sublink, Sublink) or not sublink.legal:
            raise Exception("Invalid link. Please provide a valid link")

        # Get the web page
        self.link = sublink
        global response
        try:
            response = requests.get(sublink.URL)
        except requests.exceptions.ConnectionError:
            Exception("Connection refused")
        if response: self.encoding = response.encoding
        self.Tags = response.text.encode('utf8')

        # removes tags from words in web page
        NoTags = HTMLUtils.HTML_CLEANER.clean_html(self.Tags)

        JustWords = html.fromstring(NoTags).text_content()
        JustWords = re.sub(r'/\s+/g', ' ', JustWords).strip()
        self.Text = JustWords
        self.Code = response.status_code

        # Get the links for the children
        self.children = self.FindAllURLs()

    # Find all of the URLs connected to that site
    def FindAllURLs(self):
        returned = html.fromstring(self.Tags)
        WebSite = set([urlparse.urldefrag(each)[0] for each in returned.xpath('//a[@href]/@href')])
        return [Sublink(url, self.link) for url in WebSite]

    # helper function to return all the children of a webpage
    def ReturnAllChildWebPages(self):
        return [WebPage for WebPage in self.children]

    # Source: https://stackoverflow.com/questions/5319922/python-check-if-word-is-in-a-string
    # find the keyword, ignores the case. So if the keyword is 'also' and the word
    # 'Also' is found in the text, the search will stop.
    def findWholeWord(self, w):
        return re.compile(r'\b({0})\b'.format(w), flags=re.IGNORECASE).search

    # This is the depth and breadth first search. It uses a priority queue
    # to keep track of which urls to search further on. It is constrained
    # by the keywords and the depth of the search (how many ancestors the
    # webpage  is allowed to have.
    def GoSearch(self, SublinkObject, DFSorBFS, NumLevels, keywords=None):

        #new list
        listOrURLs = [SublinkObject]

        #new set
        SetOfURLs = set()

        keywordFound = False
        NumberOfChildren = 0
        counterOfParents = 0

        #Get and set title of page
        page = urllib.urlopen(self.link.URL)
        t = html.parse(page)
        self.title = t.find(".//title").text

        if keywords is None:
            keywords = []

        if DFSorBFS != 'DFS' and DFSorBFS != 'BFS':
            return Exception("BFS or DFS not chosen correctly. ")

        parentNumber = 0

        # while there are still sublinks in the priority queue and the keyword has not been found
        while listOrURLs and not keywordFound:

            # the top of the queue can be popped if it is a depth first search
            # the bottom of the queue (as in a stack) can be popped if it is breadth first search
            if "DFS" == DFSorBFS:
                sublink = listOrURLs.pop()

            if DFSorBFS == "BFS":
                sublink = listOrURLs.pop(0)


            # this link has not been seen before
            if sublink not in SetOfURLs and sublink.legal:
                # add the sublink to the queue
                SetOfURLs.add(sublink)

                # parse sublink's page and get their children urls
            SublinkChildren = WebPage(sublink)
            if sublink.position < NumLevels and SublinkChildren.Code == 200:
                tempList = []

                for each in SublinkChildren.ReturnAllChildWebPages():
                    each.position = sublink.position + 1
                    tempList.append(each)
                    each.parentURL = sublink.URL

                    if dictOrP.get(each.parentURL) is not None:
                        each.parentNUM = dictOrP.get(each.parentURL)
                    else:
                        counterOfParents += 1
                        dictOrP[each.parentURL] = counterOfParents
                        each.parentNUM = counterOfParents

                #randomly add the children to the ListOfUrls
                while tempList:
                    addToListOfURLs = random.choice(tempList)
                    listOrURLs.append(addToListOfURLs)
                    tempList.remove(addToListOfURLs)
                    NumberOfChildren = NumberOfChildren + 1

            # check if the current page has one of the given stop words
            for word in keywords:
                keywordFound = keywordFound or self.findWholeWord(word)(self.Text)

            parentNumber = parentNumber + 1

        return SetOfURLs


# Class to represent all sublinks
class Sublink(object):

    counter = 0

    def __init__(self, address, keywords=None, ancestor=None):


        # If the parent is not a valid WebPage, say so
        if ancestor:
            if not isinstance(ancestor, Sublink):
                raise Exception("Invalid WebPage Object. ")
            # returns the full URL
            address = urlparse.urljoin(ancestor.URL, address)

        # Set the sublink's contents
        self.ancestor = ancestor

        self.parentnumber = 0
        self.parentURL = "Start Page"
        self.parentNUM = 0

        # defragment the URL
        self.URL = urlparse.urldefrag(address)[0]

        # parse the URL
        self.authority = urlparse.urlparse(address).netloc

        # validate the URL
        try:
            result = urlparse.urlparse(address)
            self.legal = all([result.scheme, result.netloc])
        except:
            self.legal = False

        # encode it properly
        encoded = self.URL
        encoded.encode('utf-8')

        # use md5 to return a hash for the given url
        self.id = hashlib.md5(address.encode('utf-8')).hexdigest()

        # set position in regards to the number of ancestors above it
        self.position = 0 if ancestor is None else ancestor.position + 1

        # Create a new Entry for only the inputed link
        '''if self.position == 0:
            newEntry = Entry()
            newEntry.Id = self.id
            newEntry.URL = self.URL
            newEntry.Position = self.position
            newEntry.ParentID = self.ancestor
            newEntry.Keyword = str(keywords).strip('[]')
            newEntry.put()'''

    # print the sublink - this is the returned object.
    def __str__(self):
        return "ancestors:%s . url: %s . parent n : %s . parentURL : %s" \
           % (self.position, self.URL, self.parentNUM, self.parentURL)

    def ReturnJSON(self):
        return {"title" : "", "found " : self.legal}



# Source: https://stackoverflow.com/questions/3073881/clean-up-html-in-python/6482979
# Removes html tags, such that only words are reviewed (such that we can find the keyword)
class HTMLUtils(object):
    HTML_CLEANER = Cleaner(**{
        'scripts': True,
        'embedded': True,
        'inline_style': True,
        'javascript': True,
        'remove_unknown_tags': True,
        'style': True,
        'comments': True,
        'meta': True
    })
