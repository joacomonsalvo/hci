from PIL import Image
from math import sqrt
import sys
#
# TODO LIST
# get image path
# finish compression format
# multiplatform
#
def get_pixel_cords_hex(path:str) -> list:
    img = Image.open(path)
    pixels = img.load()
    width, height = img.size
    data = []
    #
    for y in range(height):
        for x in range(width):
            r, g, b = pixels[x, y]
            #
            # alpha channel
            # r, g, b, a = pixels[x, y]
            data.append([x, y, "{:X}{:X}{:X}".format(r, g, b)])
    return data
#
def sqrt_data(data:list) -> list:
    data_arr = []
    for arr in range(len(data)):
        data_arr.append([int(sqrt(int(data[arr][0]))), int(sqrt(int(data[arr][1]))), '0x'.join(data[arr][2])])
    return data_arr
#
def order_data(data:list):
    sqrt_x = [bin(i[0]) for i in data]
    sqrt_y = [bin(j[1]) for j in data]
    bin_hex = [bin(hex(int(k[2], 16))) for k in data]
    return sqrt_x, sqrt_y, bin_hex
#
if __name__ == "__main__":
    data = sqrt_data(get_pixel_cords_hex("images/sample1.jpg"))
    order_data(data)
