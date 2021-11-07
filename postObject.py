import datetime



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
        title = self.title
        title.encode('utf-8', 'ignore')
        return str(str(title)+ " " + str(self.date))
