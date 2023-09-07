from machine import Pin, SPI

# Ili934x driver
#from ili934xnew import ILI9341, color565
#import tt14
from jeffmer.ili934xnew import ILI9341, color565
# fonts
import jeffmer.tt14 as tt14

# SPI1 for 2.8" TFT-RGB, 240x320, ILI7943
from config import SPI1_SCK, SPI1_MOSI, SPI1_MISO, SPI1_CS
# TFT's control pins
from config import TFT_BLK1, TFT_RESET1, TFT_DC1


#spi = SPI(2, baudrate=20000000, miso=Pin(19),mosi=Pin(23), sck=Pin(18))
# PP modified for Gravity Expansion board and Raspberry PI PICO
baudrate = 40_000_000  # 40 Mhz
spi1 = SPI(1,
      baudrate=baudrate, polarity=0, phase=0,
      sck=Pin(SPI1_SCK), mosi=Pin(SPI1_MOSI), miso=Pin(SPI1_MISO))

#display = ILI9341(spi, cs=Pin(2), dc=Pin(27), rst=Pin(33), w=320, h=240, r=0)
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

from time import sleep
#text = 'F'
message = 'Now is the time for all good men to come to the aid of the party.'

def print_textblock(text):
    display.set_pos(0,0)
    display.print(text)
    display.set_pos(0,20)
    display.print(text)
    display.set_pos(40,20)
    display.print(text)


def test_rotation(text):
    display.set_font(tt14)
    prev_r = display.rotation # save current rotation
    
    for i in range(8):        # loop through r values: 0..7
        display.erase()
        display.rotation = i
        print(f"rotation = {display.rotation}")
        print_textblock(text)
        sleep(1)

    # reset rotation to original value
    display.rotation = prev_r
    display.erase()
    print_textblock(text)
    sleep(1)
    display.erase()

if __name__ == "__main__":
    print("Demo of text rotation...")
    test_rotation(message[0:3])
    print("Done!")
