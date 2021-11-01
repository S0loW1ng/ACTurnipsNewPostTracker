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

class Display:
    font24 = ImageFont.truetype('./pic/Font.ttc', 24)
    font18 = ImageFont.truetype('./pic/Font.ttc', 18)

    Himage = Image.new('1', (epd.height, epd.width), 0xFF)  # 0xFF: clear the f$

    def __init__(self):

        logging.info("epd2in66 Demo")
        epd = epd2in66.EPD()
        logging.info("init and Clear")
        epd.init(0)
        epd.Clear()

    def display(self,array):

        draw = ImageDraw.Draw(Himage);
        draw.text((10, 0), array[0], font=font24, fill=0)
        draw.text((10, 20), array[1], font=font24, fill=0)
        draw.text((10, 100), array[2], font=font24, fill=0)
        epd.display(epd.getbuffer(Himage))
        epd.sleep()