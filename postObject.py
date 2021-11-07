import datetime
import re


class post:
    def __init__(self, title, date, url, id):
        ts = datetime.datetime.fromtimestamp(date)
        self.title = self.deEmojify(title)
        self.date = ts.strftime('%H:%M:%S')
        self.url = url
        self.id = id

    def displayInfo(self):
        print(self.title)
        print(self.date)
        print(self.url)

    def toString(self):
        return str(str(self.title )+ " " + str(self.date))

    def deEmojify(self,text):
        regrex_pattern = re.compile(pattern = "["
            u"\U0001F600-\U0001F64F"  # emoticons
            u"\U0001F300-\U0001F5FF"  # symbols & pictographs
            u"\U0001F680-\U0001F6FF"  # transport & map symbols
            u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                           "]+", flags = re.UNICODE)
        return regrex_pattern.sub(r'',text)
