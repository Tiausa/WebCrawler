import re
import hashlib
import urllib
import urllib2

import lxml
import requests
from lxml import html
import urlparse
from lxml.html.clean import Cleaner
import random
from datetime import datetime
random.seed(datetime.now())
from BeautifulSoup import BeautifulSoup


# class Entry(ndb.Model):
#    Id = ndb.StringProperty()
#    URL = ndb.StringProperty()
#    Position = ndb.FloatProperty
#    ParentID = ndb.JsonProperty
#    Keyword = ndb.StringProperty()


# The web page object- any page available on the world wide web,
# or used for testing purposes.
class WebPage(object):

    # Creates a new WebPage object from a link
    def __init__(self, sublink):

        self.Bad = False
        self.Code = 404

        # If the link is not valid, say so
        if not isinstance(sublink, Sublink):
            raise Exception("Invalid object." + sublink.URL)
        if not sublink.legal:
            #raise Exception("Link not legal." + sublink.URL)
            #sublink.Bad = True
            self.Bad = True
            return

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

    def findDomain(self):
        parsed_uri = urlparse.urlparse(self.link.getUrl())
        domain = '{uri.scheme}://{uri.netloc}'.format(uri=parsed_uri)
        return domain

    # Find all of the URLs connected to that site
    def FindAllURLs(self):
        returned = html.fromstring(self.Tags)

        WebSite = set([urlparse.urldefrag(each)[0] for each in returned.xpath('//a[@href]/@href')])
        webpages = []
        response = 404
        for url in WebSite:
            if url and url[0] == '/':
                url = self.findDomain() + url

            # validate the URL
            try:
                response = requests.get(url)
            except:
                response = 404
            if response != 404 and response.status_code < 400:
                webpages.append(Sublink(url, self.link))
        return webpages

    # return [Sublink(url, self.link) for url in WebSite]

    # helper function to return all the children of a webpage
    def ReturnAllChildWebPages(self):
        return [WebPage for WebPage in self.children]

    # helper function to return links of children of a webpage
    def ReturnAllChildrenLinks(self):
        return [page.getUrl() for page in self.children]

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

        priorityQueue = [SublinkObject]
        InQueue = set()
        keywordFound = False
        graph = {}

        try:
            page = urllib.urlopen(SublinkObject.URL)
            t = html.parse(page)
            SublinkObject.title = t.find(".//title").text
        except:
            pass


        if keywords is None:
            keywords = []

        if DFSorBFS != 'DFS' and DFSorBFS != 'BFS':
            return Exception("BFS or DFS not chosen correctly. ")

        if DFSorBFS == "BFS":
            self.BFSearch(InQueue, NumLevels, graph, keywordFound, keywords, priorityQueue)
        else:
            PriorityQList = []
            PriorityQList.append(SublinkObject)
            self.DFSearch2(InQueue, NumLevels, graph, keywordFound, keywords, PriorityQList)

        return graph


    def BFSearch(self, InQueue, NumLevels, graph, keywordFound, keywords, priorityQueue):

        # while there are still sublinks in the priority queue and the keyword has not been found
        while priorityQueue and not keywordFound:

            sublink = priorityQueue.pop(0)
            if sublink.legal:

                # this link has not been seen before
                if sublink not in InQueue and sublink.legal:
                    # add the sublink to the queue
                    InQueue.add(sublink)

                    # parse sublink's page and get their children urls
                    SublinkChildren = WebPage(sublink)
                    if SublinkChildren.Bad is not True:

                        if sublink.position <= NumLevels and SublinkChildren.Code == 200:
                            # create a node to add to graph
                            node = {}

                            # Get the web page
                            sublink.link = sublink
                            global response
                            try:
                                response = requests.get(sublink.URL)
                            except requests.exceptions.ConnectionError:
                                Exception("Connection refused")
                            if response: sublink.encoding = response.encoding
                            sublink.Tags = response.text.encode('utf8')

                            # removes tags from words in web page
                            NoTags = HTMLUtils.HTML_CLEANER.clean_html(sublink.Tags)

                            JustWords = html.fromstring(NoTags).text_content()
                            JustWords = re.sub(r'/\s+/g', ' ', JustWords).strip()
                            sublink.Text = JustWords

                            responser = False
                            for word in keywords:
                                keywordFound = keywordFound or sublink.findWholeWord1(word)(sublink.Text)
                                if keywordFound:
                                    responser = True
                            node['found'] = responser # temporary placeholder till words are implemented

                            #node['found'] = False  # temporary placeholder till words are implemented
                            if sublink.position == NumLevels or responser == True:
                                node['edges'] = []
                            else:
                                node['edges'] = SublinkChildren.ReturnAllChildrenLinks()
                                # continue crawling children
                                counter1 = 0
                                for each in SublinkChildren.ReturnAllChildWebPages():
                                    each.position = sublink.position + 1
                                    counter1 += 1

                                    try:
                                        page = urllib.urlopen(each.URL)
                                        t = html.parse(page)
                                        each.title = t.find(".//title").text
                                    except:
                                        pass

                                    priorityQueue.append(each)

                            # add node to the graph
                            if sublink.getUrl() not in graph:
                                node['title'] = sublink.getTitle()
                                graph[sublink.getUrl()] = node

                        # check if the current page has one of the given stop words
                        for word in keywords:
                            keywordFound = keywordFound or self.findWholeWord(word)(self.Text)


    def DFSearch(self, InQueue, NumLevels, graph, keywordFound, keywords, priorityQueue):

        NumLevels += 1
        # while there are still sublinks in the priority queue and the keyword has not been found
        while priorityQueue and not keywordFound:



            KeepGoing = True
            while KeepGoing is True and len(priorityQueue) > 0:
                sublink = priorityQueue.pop()
                SublinkChildren = WebPage(sublink)
                KeepGoing = SublinkChildren.Bad


            while priorityQueue:
                priorityQueue.pop()

            # this link has not been seen before
            if sublink not in InQueue and sublink.legal:
                InQueue.add(sublink)

            # parse sublink's page and get their children urls

            if sublink.position < NumLevels and SublinkChildren.Code == 200:

                # create a node to add to graph
                node = {}

                # Get the web page
                sublink.link = sublink
                global response
                try:
                    response = requests.get(sublink.URL)
                except requests.exceptions.ConnectionError:
                    Exception("Connection refused")
                if response: sublink.encoding = response.encoding
                sublink.Tags = response.text.encode('utf8')

                # removes tags from words in web page
                NoTags = HTMLUtils.HTML_CLEANER.clean_html(sublink.Tags)

                JustWords = html.fromstring(NoTags).text_content()
                JustWords = re.sub(r'/\s+/g', ' ', JustWords).strip()
                sublink.Text = JustWords

                responser = False
                for word in keywords:
                    keywordFound = keywordFound or sublink.findWholeWord1(word)(sublink.Text)
                    if keywordFound:
                        responser = True
                node['found'] = responser  # temporary placeholder till words are implemented

                if sublink.position == NumLevels or responser == True:
                    node['edges'] = []

                else:
                    # continue crawling children
                    counter1 = 0
                    for each in SublinkChildren.ReturnAllChildWebPages():
                        each.position = sublink.position + 1
                        counter1 += 1

                        try:
                            #page = urllib.urlopen(each.URL)
                            #t = html.parse(page)
                            #each.title = t.find(".//title").text


                            source = urllib2.urlopen(each.URL)
                            BS = BeautifulSoup(source)
                            each.title =  BS.find('title').text
                        except:
                            pass

                        priorityQueue.append(each)

                    if len(priorityQueue) is 0 or responser == True:
                        node['edges'] = []

                    if len(priorityQueue) is not 0:
                        if counter1 is not 0:
                            oneToPop = random.randrange(0, counter1)
                            sublink1 = priorityQueue.pop(oneToPop)
                            while priorityQueue:
                                priorityQueue.pop()
                        else:
                            sublink1 = priorityQueue.pop()

                        priorityQueue.append(sublink1)

                        toAdd = WebPage(sublink1)
                        if sublink1.position < NumLevels and toAdd.Bad is not True:
                                node['edges'] = [sublink1.getUrl()]
                        else:
                            node['edges'] = []
                        if responser == True:
                            node['edges'] = []


                if sublink.getUrl() in graph:
                    node1 = graph[sublink.getUrl()]
                    node['edges'] += node1['edges']
                    graph[sublink.getUrl()] = node


                # add node to the graph
                if sublink.getUrl() not in graph:
                    node['title'] = sublink.getTitle()

                    graph[sublink.getUrl()] = node
                # check if the current page has one of the given stop words

    def DFSearch2(self, InQueue, NumLevels, graph, keywordFound, keywords, priorityQueue):

        NumLevels += 1
        # while there are still sublinks in the priority queue and the keyword has not been found
        while priorityQueue and not keywordFound:

            KeepGoing = True
            while KeepGoing is True and len(priorityQueue) > 0:
                sublink = priorityQueue.pop()
                SublinkChildren = WebPage(sublink)
                KeepGoing = SublinkChildren.Bad

            priorityQueue = []

            # this link has not been seen before
            if sublink not in InQueue and sublink.legal:
                InQueue.add(sublink)

            # parse sublink's page and get their children urls

            if sublink.position < NumLevels and SublinkChildren.Code == 200:

                # create a node to add to graph
                node = {}

                # Get the web page
                sublink.link = sublink
                global response
                try:
                    response = requests.get(sublink.URL)
                except requests.exceptions.ConnectionError:
                    Exception("Connection refused")
                if response: sublink.encoding = response.encoding
                sublink.Tags = response.text.encode('utf8')

                # removes tags from words in web page
                NoTags = HTMLUtils.HTML_CLEANER.clean_html(sublink.Tags)

                JustWords = html.fromstring(NoTags).text_content()
                JustWords = re.sub(r'/\s+/g', ' ', JustWords).strip()
                sublink.Text = JustWords

                responser = False
                for word in keywords:
                    keywordFound = keywordFound or sublink.findWholeWord1(word)(sublink.Text)
                    if keywordFound:
                        responser = True
                node['found'] = responser  # temporary placeholder till words are implemented

                if sublink.position == NumLevels or responser == True:
                    node['edges'] = []

                else:
                    # continue crawling children
                    #for each in SublinkChildren.ReturnAllChildWebPages():
                        #node['edges'] = each.URL
                    if len(SublinkChildren.children) is not 0:
                        #sublink2 = random.randrange(0, len(SublinkChildren.children))
                        sublink2 = random.choice(SublinkChildren.children)
                        sublink2.position = sublink.position + 1


                        try:
                            # page = urllib.urlopen(each.URL)
                            # t = html.parse(page)
                            # each.title = t.find(".//title").text

                            source = urllib2.urlopen(sublink2.URL)
                            BS = BeautifulSoup(source)
                            sublink2.title = BS.find('title').text
                        except:
                            pass

                        priorityQueue.append(sublink2)

                        toAdd = WebPage(sublink2)
                        if sublink2.position < NumLevels and toAdd.Bad is not True:
                            node['edges'] = [sublink2.getUrl()]
                        else:
                            node['edges'] = []
                        if responser == True:
                            node['edges'] = []

                if sublink.getUrl() in graph:
                    node1 = graph[sublink.getUrl()]
                    node['edges'] += node1['edges']
                    graph[sublink.getUrl()] = node

                # add node to the graph
                if sublink.getUrl() not in graph:
                    node['title'] = sublink.getTitle()

                    graph[sublink.getUrl()] = node
                # check if the current page has one of the given stop words


# Class to represent all sublinks
class Sublink(object):

    def __init__(self, address, URL=None, keywords=None, ancestor=None):

        # If the parent is not a valid WebPage, say so
        if ancestor:
            if not isinstance(ancestor, Sublink):
                raise Exception("Invalid WebPage Object. ")
            # returns the full URL
            address = urlparse.urljoin(ancestor.URL, address)

        # Set the sublink's contents
        self.ancestor = ancestor

        #the title
        self.title = ''

        # defragment the URL
        self.URL = urlparse.urldefrag(address)[0]

        '''regex_txt = '\/.'
        regex = re.compile(regex_txt, re.IGNORECASE)
        match = regex.search(self.URL)  # From your file reading code.
        if match is not None:'''

        # if URL and URL.authority and self.URL.startswith('/'):
        #     self.URL = URL.authority + self.URL
        #     self.address = self.URL
        #     address = self.address


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

    # returns url for page
    def getUrl(self):
        return self.URL

    # returns title for page, temporary placeholder of empty string
    def getTitle(self):
        return self.title

    # print the sublink - this is the returned object.
    def __str__(self):
        return "ancestors:%s . legal:%s . id:%s . url: %s " \
               % (self.position, self.legal, self.id, self.URL)

    # Source: https://stackoverflow.com/questions/5319922/python-check-if-word-is-in-a-string
    # find the keyword, ignores the case. So if the keyword is 'also' and the word
    # 'Also' is found in the text, the search will stop.
    def findWholeWord1(self, w):
        return re.compile(r'\b({0})\b'.format(w), flags=re.IGNORECASE).search


# Source: https://stackoverflow.com/questions/3073881/clean-up-html-in-python/6482979
# Removes html tags, such that only words are reviewed (such that we can find the keyword)
# All methods are staticmethods, so that no object needs to be built.
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
