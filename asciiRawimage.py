from PIL import Image,ImageDraw,ImageFont
import random
from bisect import bisect
import os,time


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
 
im=Image.open("a.jpg")
im=im.resize((150, 100),Image.BILINEAR)
im=im.convert("L") # convert to mono

blacFactor=20

print "a"
stri =""

for y in range(0,im.size[1]):
    for x in range(0,im.size[0]):
        lum=255-im.getpixel((x,y))
        row=bisect(zonebounds,lum)
        possibles=greyscale[row]
        stri=stri+possibles[random.randint(0,len(possibles)-1)]
    stri=stri+"\n"
os.system('cls')


print stri

print len(stri)

