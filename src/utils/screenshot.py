import math
import operator
from functools import reduce

from PIL import ImageGrab, ImageOps, Image  # pip install Pillow



# this function compares two given Images and returns the difference as an Integer
def compare(i1, i2):
    h1 = i1.histogram()
    h2 = i2.histogram()
    rms = math.sqrt(reduce(operator.add, map(lambda a, b: (a - b) ** 2, h1, h2)) / len(h1))
    return round(rms, 2)

def take_screenshot(rect):
    return ImageGrab.grab(bbox=(rect[0], rect[1], rect[2], rect[3]))

def crop_screenshot(rect, cropbox):
    raw_img = take_screenshot(rect)
    crop_img = ImageOps.crop(raw_img, cropbox)  # Crop data from it (right up corner)
    #raw_img.save("DEBUG/raw_img_debug.png")
    #crop_img.save("DEBUG/crop_img_debug.png")
    return crop_img

def crop_and_mask_screenshot(rect, cropbox, black_bg_img, mask_img):
    raw_img = take_screenshot(rect)
    crop_img = ImageOps.crop(raw_img, cropbox)  # Crop data from it (right up corner)
    #raw_img.save("DEBUG/raw_img_debug.png")
    #crop_img.save("DEBUG/crop_img_debug.png")
    if mask_img is None:
        return crop_img
    masked_img = Image.composite(crop_img, black_bg_img, mask_img)  # Mask data (timer, guild chat, xp bar)
    #masked_img.save("DEBUG/masked_final_img_debug.png")
    return masked_img

def load_image(name):
    return Image.open(name)

def create_black_image(rect_size):
    return Image.new("RGB", rect_size, (0, 0, 0))
