import sys
import os
from waveshare_epd import epd_2in13bc_test
import time
from PIL import Image,ImageDraw,ImageFont
import traceback

epd = epd_2in13bc_test.EPD()
epd.init(0)
epd.Clear()
Himage = Image.open("lolz.jpg")  # 0xFF: clear the f$
epd.display(epd.getbuffer(Himage))
epd.sleep()

epd_2in13bc_test.epdconfig.module_exit()




