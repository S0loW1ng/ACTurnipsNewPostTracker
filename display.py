import sys
import os
from waveshare_epd import epd2in13b_V3
import time
from PIL import Image,ImageDraw,ImageFont


epd = epd2in13b_V3.EPD()
epd.init()
epd.Clear()
time.sleep(1)
Himage = Image.open("/home/pi/ACTurnipsNewPostTracker/lolz.bmp")  # 0xFF: clear the f$
HRYimage = Image.open("/home/pi/ACTurnipsNewPostTracker/Logo.png")
epd.display(epd.getbuffer(Himage),epd.getbuffer(HRYimage))
time.sleep(2)
epd.sleep()
print("Job done")






