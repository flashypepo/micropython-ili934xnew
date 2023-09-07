# test of printing multiple fonts to the ILI9341 on an M5Stack using H/W SP
# MIT License; Copyright (c) 2017 Jeffrey N. Magee
#
# 2023-0907 PP modified for Gravity Expansion board and Raspberry PI PICO
#              add drawing images on TFT-display,

from machine import Pin, SPI
from time import sleep
import os

#import m5stack
# Ili934x driver
from jeffmer.ili934xnew import ILI9341, color565
import jeffmer.glcdfont as glcdfont
# fonts
import jeffmer.tt14 as tt14
import jeffmer.tt24 as tt24
import jeffmer.tt32 as tt32

# SPI1 for 2.8" TFT-RGB, 240x320, ILI7943
from config import SPI1_SCK, SPI1_MOSI, SPI1_MISO, SPI1_CS
# TFT's control pins
from config import TFT_BLK1, TFT_RESET1, TFT_DC1
# or from config import GPIO02, GPIO03, GPIO12


def show_text(display, text, fonts):
    # test from jeffmers repro
    display.erase()
    display.set_pos(0,0)
    for ff in fonts:
        display.set_font(ff)
        display.print(text)


def show_images(display, path):
    display.erase()  # clean screen

    # PP: test to display an image using Jeffmers ili934xnew driver
    # driver is extended with various methods
    # get 'raw' files from path and append to array files
    files = []
    filenames = os.listdir(path)
    for file in filenames:
        if file[-3:] == "raw":
            files.append(file)
    assert len(files) == 4, "Not more then 4 images"
    # draw the images from files on TFT-display
    # TODO: generalize code - use a Dict for coordinates
    print(f"Draw image {path+files[0]}...")
    display.draw_image(path+files[0], 0, 0, 128, 128)
    sleep(2)
    print(f"Draw image {path+files[1]}...")
    display.draw_image(path+files[1], 112, 0, 128, 128)
    sleep(2)
    print(f"Draw image {path+files[2]}...")
    display.draw_image(path+files[2], 0, 129, 128, 128)
    sleep(2)
    print(f"Draw image {path+files[3]}...")
    display.draw_image(path+files[3], 112, 129, 128, 128)


def demo(dt=9):
    try:
        # setup
        
        # SPI1
        baudrate = 40_000_000  # 40 Mhz
        spi1 = SPI(1,
              baudrate=baudrate, polarity=0, phase=0,
              sck=Pin(SPI1_SCK), mosi=Pin(SPI1_MOSI), miso=Pin(SPI1_MISO))

        # TFT display
        """
        Orientation parameter 'r':
         r=0 -> 0 deg
         r=1 -> 90 deg
         r=2 -> 180 deg
         r=3 -> 270 deg
         r=4 -> mirrored + 0 deg
         r=5 -> mirrored + 90 deg
         r=6 -> mirrored + 180 deg
         r=7 -> mirrored + 270 deg
        """
        orientation = 0   # my default orientation
        display = ILI9341(
            spi1,
            cs=Pin(SPI1_CS),
            dc=Pin(TFT_DC1),
            rst=Pin(TFT_RESET1),
            #led=Pin(TFT_BLK1),
            w=320, h=240,
            r=orientation
        )

        fonts = [glcdfont,tt14,tt24,tt32]
        text = 'Now is the time for all good men to come to the aid of the party.'
        show_text(display, text, fonts)
        
        sleep(dt)
        
        path = "images/"
        show_images (display, path)
        
        # enjoy the show
        sleep(dt)
        
    except KeyboardInterrupt:
        print("User interrupt")
        
    finally:
        display.erase()
        print('Done!')



if __name__ == "__main__":
    demo(dt=9)
