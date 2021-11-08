import time
import os

from requestBot import requestBot
import schedule as sch

bot = requestBot('https://www.reddit.com/r/acturnips.json')


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def task():
    bot.displayPrices()
    print("______________________________________________________________________")
def displayUpdate():
    os.popen('sh /home/pi/ACTurnipsNewPostTracker/display.sh')

if __name__ == '__main__':
    sch.every(45).seconds.do(task)
    sch.every(1).minute.do(displayUpdate)

    while (True):
        sch.run_pending()
