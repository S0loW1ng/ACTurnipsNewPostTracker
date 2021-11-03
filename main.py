import time

from requestBot import requestBot
import schedule as sch

bot = requestBot('https://www.reddit.com/r/acturnips.json')


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def task():
    bot.displayPrices()
    print("______________________________________________________________________")


if __name__ == '__main__':


    while (True):
        task()
        time.sleep(10);
