from urllib.request import urlopen, urlretrieve
from urllib.parse import urlencode, quote_plus
import json
from collections import deque

wikiCacheLoaded = False
        
def getAllWLinks(title, useCache = True):
    global queryResult, jsonResult, query, wikiCacheLoaded
    if useCache == True:
        if wikiCacheLoaded == False:
            readWikiCache()
            wikiCacheLoaded = True
        if title in wikiDict:
            return wikiDict[title] 
    links = []
    base = "https://en.wikipedia.org/w/api.php?action=query&prop=links&format=json&pllimit=500&titles="
    qtitle = quote_plus(title)
    plcontinue = "||"
    done = False
    while (not done):
            query = base + qtitle + "&plcontinue=" + quote_plus(plcontinue)
            queryResult = urlopen(query).read().decode('utf8')
            jsonResult = json.loads(queryResult)
            pagesDict = jsonResult["query"]["pages"]
            pageInfo = (list(pagesDict.values()))[0] # we assume just one page in pageDict
            linkInfoList = []
            if "links" in pageInfo:
                linkInfoList = pageInfo["links"]
            for linkInfo in linkInfoList:
                if linkInfo['ns'] == 0: # 'ns' field is namespace.  Ignore "special" pages like Category, etc.
                    links.append(linkInfo["title"])
            if "batchcomplete" in jsonResult:
                done = True
            else:
                plcontinue = jsonResult['continue']['plcontinue']
    if useCache == True:
        wikiDict[title] = links
    return links

# Simple, not robust code to play the Wikipedia game.  Given two Wikipedia
# page names, find path from one to the other using only regular Wikipedia page links
# between the two pages.
#
#This code uses breadth first search and "lazily" downloads
# information from Wikipedia as it searches.  It caches info downloaded from Wikipedia in
# global variable wikiDict.  If a search is taking a very long time (because the "portion" of Wikipedia
# being searched is not already in the cache) and you happen to kill it (because you have something
# else to do, e.g. :)) or if it crashes after a while due to losing a network connection, you should
# execute saveWikiCache() afterward to save to disk all the info it did succesfully download.
# Then, if you restart the search, the part that was already completed early will now be very fast
# since it won't have to retrieve the info again from Wikipedia.
#
# Be careful - if you enter toPage names that don't represent "regular" Wikipedia pages, the search
# will take a *long* time, since it will have to eventually download all of Wikipedia before realizing
# that there is no path.  For example, wikiGame("Apple", "Orange") does might never finish because
# "Orange" is not a regular Wikipedia page.  wikiGame("Apple", "Orange (fruit)") works fine, however.
#
# INITIALLY runs quite slowly (due to slow dowloading of Wiki data from the Internet) until it
# builds up a good-sized cache (a few hundred MB) stored in wikiDict (and saved on disk in
# wikidict.json)
#
def wikiGame(fromPage, toPage):
    global queue, currentPage   
    seenDict = {}
    seenDict[fromPage] = ''
    queue =deque()
    queue.append(fromPage)
    distance = 0
    queue.append(distance)
    numRemoved = 0
    while len(queue) != 0:
        currentPage = queue.popleft()
        numRemoved = numRemoved + 1
        if (numRemoved%1000 == 0):
            print("num nodes removed from queue: {}. Queue size: {}".format(numRemoved, len(queue)))
        if type(currentPage) == int:
                print("Finished considering distance {} nodes".format(distance))
                distance = distance + 1
                if len(queue) != 0:
                    queue.append(distance)
        else:
            #print("removed {} from queue (len={}). Processing neighbors".format(currentPage,len(queue))) 
            for node in getAllWLinks(currentPage):
                if node == toPage:
                        print("Found path! ", end = '')
                        print(toPage, end = " ")
                        parent = currentPage
                        while (parent != ''):
                            print(" <- ", parent, end = " ")
                            parent = seenDict[parent]                      
                        return
                elif node not in  seenDict:
                    seenDict[node] = currentPage
                    queue.append(node)
    print("No path found!")
        
def readWikiCache():
   global wikiDict
   try:
      dictInFile = open('wikidict.json')
      jsonString = dictInFile.read()
      wikiDict = json.loads(jsonString)
      dictInFile.close()
   except:
      wikiDict = {}
      
def saveWikiCache():
   print('saving wikidict.json')
   dictOutFile = open('wikidict.json', 'w')
   jsonString = json.dumps(wikiDict)
   dictOutFile.write(jsonString)
   dictOutFile.close()

# You can let this run for a long time to slowly grow your cached Wikipedia graph
# 
def growWikiCache():
    global wikiDict
    readWikiCache()
    count = 0
    for key in list(wikiDict.keys()):
        for topic in wikiDict[key]:
            getAllWLinks(topic)
            count = count + 1
            if ((count  % 200) == 0):
                saveWikiCache()
