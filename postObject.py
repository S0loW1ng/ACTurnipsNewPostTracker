import datetime


class post:
    def __init__(self, title, date, url, id):
        self.title = title
        self.date = date
        self.url = url
        self.id = id

    def displayInfo(self):
        print(self.title)
        print(datetime.datetime.fromtimestamp(self.date))
        print(self.url)

    def toString(self):
        return str(self.title + " " + self.date)
