import json
import requests as req
from operator import attrgetter
from postObject import post
from datetime import datetime as dt


class requestBot:
    postArray = []
    seenPosts = []

    def __init__(self, link):
        self.link = link
        self.postArray = []

    def requestPrices(self):
        request = req.get(url=self.link, headers={
            'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/95.0.4638.54 Safari/537.36'})
        if request.status_code == 200:
            self.postArray = []
            jsonData = json.loads(request.text)
            for i in range(0, 3):
                if jsonData["data"]["children"][2 + i]["data"]["id"] not in self.seenPosts:
                    self.postArray.append(post(jsonData["data"]["children"][2 + i]["data"]["title"],
                                               jsonData["data"]["children"][2 + i]["data"]["created_utc"],
                                               jsonData["data"]["children"][2 + i]["data"]["url"],
                                               jsonData["data"]["children"][2 + i]["data"]["id"]))
                    self.seenPosts.append(jsonData["data"]["children"][2 + i]["data"]["id"])
        else:
            print("Error: %d" % request.status_code)

    def displayPrices(self):
        print("Current Poll Time:", dt.now())
        self.requestPrices()
        self.postArray.sort(key=attrgetter('date'), reverse=True)
        for post in self.postArray:
            post.displayInfo()
