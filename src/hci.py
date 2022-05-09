from PIL import Image
from math import sqrt
import argparse


def get_pixel_cords_hex(path: str) -> list:
    img = Image.open(path)
    pixels = img.load()
    width, height = img.size
    codes = []
    #
    for y in range(height):
        for x in range(width):
            r, g, b = pixels[x, y]
            #
            # alpha channel
            # r, g, b, a = pixels[x, y]
            codes.append([x, y, "{:X}{:X}{:X}".format(r, g, b)])
    return codes


def sqrt_data(codes: list) -> list:
    data_arr = []
    for arr in range(len(codes)):
        sqrt_x = int(sqrt(int(codes[arr][0])))
        sqrt_y = int(sqrt(int(codes[arr][1])))
        bin_join = '0x'.join(codes[arr][2])
        data_arr.append([sqrt_x, sqrt_y, bin_join])
    return data_arr


def order_data(codes: list) -> list:
    sqrt_x = [bin(x[0]) for x in codes]
    sqrt_y = [bin(y[1]) for y in codes]
    bin_hex = [bin(b[2]) for b in codes]
    ordered = [sqrt_x, sqrt_y, bin_hex]
    return ordered


if __name__ == "__main__":
    data = sqrt_data(get_pixel_cords_hex("images/sample1.jpg"))
    order_data(data)
