import sys
import os
import logging
from waveshare_epd import epd2in66
import time
from PIL import Image,ImageDraw,ImageFont
import traceback
from waveshare_epd import epd2in66
import time
from PIL import Image,ImageDraw,ImageFont
import traceback

epd = epd2in66.EPD()
epd.init(0)
epd.Clear()
Himage = Image.open("lolz.jpg")  # 0xFF: clear the f$
epd.display(epd.getbuffer(Himage))
epd.sleep()

epd2in66.epdconfig.module_exit()




