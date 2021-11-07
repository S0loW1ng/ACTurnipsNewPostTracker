import sys
import os
from waveshare_epd import epd2in13b_V3
import time
from PIL import Image,ImageDraw,ImageFont


epd = epd2in13b_V3.EPD()
HRYimage = Image.new('1', (epd.height, epd.width), 0)
epd.init()
epd.Clear()
time.sleep(4)
Himage = Image.open("./lolz.bmp")  # 0xFF: clear the f$
epd.display(epd.getbuffer(Himage),epd.getbuffer(HRYimage))
epd.sleep()





