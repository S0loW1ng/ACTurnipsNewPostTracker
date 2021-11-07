import datetime
import re


class post:
    def __init__(self, title, date, url, id):
        self.title = title
        self.date = date
        self.url = url
        self.id = id

    def displayInfo(self):
        print(self.title)
        print(datetime.datetime.fromtimestamp(self.date).strftime('%c'))
        print(self.url)

    def toString(self):
        emoji_pattern = re.compile("["
                                   u"\U0001F600-\U0001F64F"  # emoticons
                                   u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                                   u"\U0001F680-\U0001F6FF"  # transport & map symbols
                                   u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                                   "]+", flags=re.UNICODE)
        title = self.title
        emoji_pattern.sub(r'', title)
        return str(str(title) + " " + str(self.date))
