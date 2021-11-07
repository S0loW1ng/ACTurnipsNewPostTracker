import json
import os

import requests as req
from operator import attrgetter
from postObject import post
from datetime import datetime as dt
from PIL import Image, ImageDraw, ImageFont
from queue import Queue


class requestBot:
    postArray = []
    seenPosts = []


    def __init__(self, link):
        self.link = link
        self.postArray = []
        self.history = []

    def requestPrices(self):
        request = req.get(url=self.link, headers={
            'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/95.0.4638.54 Safari/537.36'})
        if request.status_code == 200:
            self.postArray = []
            jsonData = json.loads(request.text)
            for i in range(0, 3):
                    self.postArray.append(post(jsonData["data"]["children"][2 + i]["data"]["title"],
                                               jsonData["data"]["children"][2 + i]["data"]["created_utc"],
                                               jsonData["data"]["children"][2 + i]["data"]["url"],
                                               jsonData["data"]["children"][2 + i]["data"]["id"]))
                    self.seenPosts.append(jsonData["data"]["children"][2 + i]["data"]["id"])

        else:
            print("Error: %d" % request.status_code)

    def displayPrices(self):
        print("Current Poll Time:", dt.now())
        location = '/home/retr0/ACTurnipsNewPostTracker'
        file = 'lolz.bmp'
        path = os.path.join(location, file)
        self.requestPrices()
        self.postArray.sort(key=attrgetter('date'), reverse=True)
        Himage = Image.new('1', (212,104), 0xFF)  # 0xFF: clear the f$
        #/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf
        font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf",10)
        fontsmall = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf", 5)
        draw = ImageDraw.Draw(Himage)
        draw.text((10,0),str(str(dt.now().date()) + " " + str(dt.now().time())),font=font)
        draw.text((30,0),str(self.postArray[0].toString()),font=fontsmall)
        draw.text((60, 0), str(self.postArray[1].toString()), font=fontsmall)
        draw.text((90, 0), str(self.postArray[2].toString()), font=fontsmall)

        try:
            os.remove(path)
            #print("% s removed successfully" % path)
        except OSError as error:
            r = 1;
        
        Himage = Himage.save("lolz.bmp")
        for post in self.postArray:
            print(post.toString())
