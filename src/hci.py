from PIL import Image
from math import sqrt
from tqdm import tqdm
import argparse


def get_path() -> str:
    img_path = input("Enter image file path: \n")
    return img_path


def get_pixel_cords_hex(path: str) -> list:
    img = Image.open(path)
    pixels = img.load()
    width, height = img.size
    codes = []

    print("\n/// GETTING RGB CODE ///")

    for y in tqdm(range(height)):
        for x in range(width):
            r, g, b = pixels[x, y]
            #
            # alpha channel
            # r, g, b, a = pixels[x, y]
            codes.append([x, y, "{:X}{:X}{:X}".format(r, g, b)])
    return codes


def sqrt_data(codes: list) -> list:
    data_arr = []
    print("\n/// CALCULATING SQUARE ROOT OF EACH NUMBER ///")
    for arr in tqdm(range(len(codes))):
        sqrt_x = int(sqrt(int(codes[arr][0])))
        sqrt_y = int(sqrt(int(codes[arr][1])))
        bin_join = '0x' + codes[arr][2]
        data_arr.append([sqrt_x, sqrt_y, bin_join])
    return data_arr


def order_data(codes: list) -> list:
    print("\n/// ORDERING DATA ///")
    ordered_codes = []

    sqrt_x = [bin(x[0]) for x in tqdm(codes)]
    sqrt_y = [bin(y[1]) for y in tqdm(codes)]
    bin_hex = [bin(int(b[2], base=16)) for b in tqdm(codes)]

    for n in tqdm(range(len(codes))):
        ordered_codes.append([sqrt_x[n], sqrt_y[n], bin_hex[n]])

    return ordered_codes


def high_compressed_image(path=None) -> list:
    data = sqrt_data(get_pixel_cords_hex(path if path is not None else get_path()))
    hci = order_data(data)
    return hci


def write_dot_hci(arr: list):

    return 0


def hci_func():
    hci = high_compressed_image()
    write_dot_hci(arr=hci)

    return 0


if __name__ == "__main__":
    hci_func()
