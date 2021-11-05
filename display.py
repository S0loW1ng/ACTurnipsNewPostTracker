import sys
import os
from waveshare_epd import epd2in13d
import time
from PIL import Image,ImageDraw,ImageFont
import traceback

epd = epd2in13d.EPD()
epd.init()
epd.Clear(0xFF)
Himage = Image.open("lolz.jpg")  # 0xFF: clear the f$
epd.display(epd.getbuffer(Himage))
epd.sleep()





