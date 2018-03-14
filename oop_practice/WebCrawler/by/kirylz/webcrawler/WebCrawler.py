__author__ = 'kiryl_zayets'

import urllib.request
import urllib.response
import urllib.robotparser
import urllib.parse
import re
import time
import unittest

class WebCrawler(object):
    linksToVisit = []
    def getAllLinks(self,url,patternForSearch = None,externalLinksPattern = None):
        if patternForSearch is None: patternForSearch="<a href="
        if externalLinksPattern is None: externalLinksPattern = "http|&#x6d;"
        patternForSkip = "http|.*:void|&#x6d;|&#[0-9]+;|ask|job_epam_by|encryptedEmailAddress|[A-Za-z]+ [A-Za-z]+|[A-Za-z]_[A-Za-z]+"
        try:
            conn = urllib.request.urlopen(url)
            html = str(conn.read())
            foundLinksInternal,foundLinksExternal = [],[]
            while True:
                # Find links by pattern, calculating start and end pos
                startPosition = html.find(patternForSearch)
                firstQuotePos = html.find('"',startPosition)
                if firstQuotePos == -1:                  #Nothing to process
                    return list(set(foundLinksInternal))
                    break
                endQuotePos = html.find('"',firstQuotePos+1)
                #Trim link caption
                itemForAppend = html[firstQuotePos+1:endQuotePos]
                if re.search(patternForSkip,itemForAppend) is None:
                    foundLinksInternal.append(itemForAppend)
                else:
                    foundLinksExternal.append(itemForAppend)
                html = html[endQuotePos:]                #Process html parsing futher
        except urllib.request.URLError:
            print("Malformed url appeared"+url)
        except ValueError:
            print("Value error")

    def composeSiteMap(self,url):
        startTime = time.time()
        patternForSkip = "http|.*:void|&#x6d;|&#[0-9]+;|skype:|ask|job_epam_by|encryptedEmailAddress|[A-Za-z]+ [A-Za-z]+|[A-Za-z]_[A-Za-z]+"
        if len(self.linksToVisit) < 1: self.linksToVisit.extend(self.getAllLinks(url))
        for linkToProcess in self.linksToVisit:
            try:
                if re.search(patternForSkip,linkToProcess) is None:
                    newbiesLinks = self.getAllLinks(url+linkToProcess)
                    if newbiesLinks is not None:
                         for newbieLink in newbiesLinks:
                            if newbieLink not in self.linksToVisit:self.linksToVisit.append(newbieLink)
            except:
                pass

        endTime = time.time()
        print(str((endTime-startTime)/60))
        return self.linksToVisit



crawler = WebCrawler()
processedLinks = crawler.composeSiteMap("http://www.epam.by")

print(str(len(processedLinks)))
for i in processedLinks:
    print(str(i))