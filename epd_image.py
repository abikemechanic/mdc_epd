from PIL import Image, ImageDraw, ImageFont
import os
import sys


class EPDImage:
    font_small = ImageFont.truetype('font/Roboto_Light.ttf', 12)
    font_large = ImageFont.truetype('font/Roboto_Medium.ttf', 20)

    def __init__(self, im_width, im_height):
        self.black_image = Image.new(im_width, im_height, 255)
        self.red_image = Image.new(im_width, im_height, 255)



