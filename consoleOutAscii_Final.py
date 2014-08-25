'''
WebCam To Ascii art
Created by Titus Nanda kumara
2014/06/13

'''


import Console
import time

c = Console.getconsole()

c.title("ASCII Art")

c.text(10, 4, "Ready to have fun",15*16)
c.text(10, 5, "Enjoy")
time.sleep(2)

'''
This part will reduce font size to 5
Then ascii art will be visible perfectly
'''
import ctypes

LF_FACESIZE = 32
STD_OUTPUT_HANDLE = -11

class COORD(ctypes.Structure):
    _fields_ = [("X", ctypes.c_short), ("Y", ctypes.c_short)]

class CONSOLE_FONT_INFOEX(ctypes.Structure):
    _fields_ = [("cbSize", ctypes.c_ulong),
                ("nFont", ctypes.c_ulong),
                ("dwFontSize", COORD),
                ("FontFamily", ctypes.c_uint),
                ("FontWeight", ctypes.c_uint),
                ("FaceName", ctypes.c_wchar * LF_FACESIZE)]

font = CONSOLE_FONT_INFOEX()
font.cbSize = ctypes.sizeof(CONSOLE_FONT_INFOEX)
font.nFont = 12
font.dwFontSize.X = 3
font.dwFontSize.Y = 5
font.FontFamily = 54
font.FontWeight = 400
font.FaceName = "Lucida Console"

handle = ctypes.windll.kernel32.GetStdHandle(STD_OUTPUT_HANDLE)
ctypes.windll.kernel32.SetCurrentConsoleFontEx(
        handle, ctypes.c_long(False), ctypes.pointer(font))







'''
ASCII Art maker
Creates an ascii art image from an arbitrary image
Created on 7 Sep 2009
 
@author: Steven Kay
Thanks to Steven Kay :)
'''
 
from PIL import Image
import random
from bisect import bisect
import os,time
from VideoCapture import Device
 
# greyscale.. the following strings represent
# 7 tonal ranges, from lighter to darker.
# for a given pixel tonal level, choose a character
# at random from that range.

'''
This is camera initialization
'''
cam = Device()
try:
    cam.__init__(devnum=0, showVideoWindow=0)
    c.text(0, 1, "Opened device 0",15*16)
except:
    cam.__init__(devnum=1, showVideoWindow=0)
    c.text(0, 1, "Opened device 1",15*16)
cam.setResolution(640,480)

greyscale = [
            " ",
            " ",
            ".,-",
            "_ivc=!/|\\~",
            "gjez2]/(YL)t[+T7Vf",
            "mdK4ZGbNDXY5P*Q",
            "W8KMA",
            "#%$"
            ]
 
# using the bisect class to put luminosity values
# in various ranges.
# these are the luminosity cut-off points for each
# of the 7 tonal levels. At the moment, these are 7 bands
# of even width, but they could be changed to boost
# contrast or change gamma, for example.
 
zonebounds=[36,72,108,144,180,216,252]
 
# open image and resize
# experiment with aspect ratios according to font
''' 
commented because I take image from webcam
im=Image.open("a.png")
im=im.resize((50, 50),Image.BILINEAR)
im=im.convert("L") # convert to mono

'''

# now, work our way over the pixels
# build up str

blacFactor=20

while(1):
    str=""
    '''
    capture image and resize
    '''
    im = cam.getImage()
    im=im.resize((150,100),Image.BILINEAR)
    im=im.convert("L") # convert to mono
    #im = im.point(lambda x: 0 if x<blacFactor else 255, '1')
    
    #im.save("out.png")
    for y in range(0,im.size[1]):
        for x in range(0,im.size[0]):
            lum=255-im.getpixel((x,y))
            row=bisect(zonebounds,lum)
            possibles=greyscale[row]
            str=str+possibles[random.randint(0,len(possibles)-1)]
        str=str+"\n"
    #os.system('cls')
    #print str
    #c.text(0, 0, str,15*16)
    txt=str.split("\n")
    for i in range(0,len(txt)):
        c.text(0,i,txt[i],15*16)
    time.sleep(0.05)
    
