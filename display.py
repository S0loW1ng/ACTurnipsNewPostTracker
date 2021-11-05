import sys
import os
from waveshare_epd import epd2in13_V2
import time
from PIL import Image,ImageDraw,ImageFont
import traceback

epd = epd2in13_V2.EPD()
epd.init(0)
epd.Clear()
Himage = Image.open("lolz.jpg")  # 0xFF: clear the f$
epd.display(epd.getbuffer(Himage))
epd.sleep()

epd2in13_V2.epdconfig.module_exit()




