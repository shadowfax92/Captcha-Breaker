#to test - run this and use 'tesseract final_output.png out' to see the conversion
from PIL import Image 
from pyocr import pyocr
import ImageEnhance
from urllib import urlretrieve
import sys 
import os
import re
import requests
import json

def get_captcha(image_path):
    im = Image.open(image_path)
    im.save('step_1_image.png')
    #crop image
    #A(12.5, 7.5) to B(70.5, 21.5).
    #im_tmp=im.crop((12,7,70,21)).save("step_2_image.png")
    imgx = Image.open('step_1_image.png')
    imgx = imgx.convert("RGBA")
    pix = imgx.load()
    for y in xrange(imgx.size[1]):
        for x in xrange(imgx.size[0]):
            if pix[x, y] != (0, 0, 0, 255):
                pix[x, y] = (255, 255, 255, 255)
    imgx.save("final_output.png", "PNG")
    #perform text recong using tesseract library
    command_tesseract='tesseract final_output.png out'
    os.system(command_tesseract)
    fh = open('out.txt','rU')
    output_tmp=fh.read().rstrip()
    #output=str(re.sub('P','f',output_tmp))
    print output_tmp

def main():
    print 'Enter the path of Captcha image: '
    captcha_image_path=sys.stdin.readline().rstrip()
    get_captcha(captcha_image_path)

if __name__ == '__main__':
        main()
