import sys
import os
from waveshare_epd import epd_2in13_V3
import time
from PIL import Image,ImageDraw,ImageFont
import traceback

epd = epd_2in13_V3.EPD()
epd.init(0)
epd.Clear()
Himage = Image.open("lolz.jpg")  # 0xFF: clear the f$
epd.display(epd.getbuffer(Himage))
epd.sleep()

epd_2in13_V3.epdconfig.module_exit()




