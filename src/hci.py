from PIL import Image
from math import sqrt
from tqdm import tqdm
import format
import write


'''GET IMAGE DATA'''


def get_path() -> str:
    """
    Receives the image absolute path.
    :return:
    Returns image absolute path
    """
    img_path = input("Enter image file path: \n")
    return img_path


def get_pixel_cords_hex(path: str) -> list:
    """
    Returns the coordinates and the rgb code of the
    image as a list
    """
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


'''ALGORITHM FUNCTIONS'''


def sqrt_data(codes: list) -> list:
    """
    Returns the square value each value of the list that
    includes coordinates and rgb code
    """
    data_arr = []
    print("\n/// CALCULATING SQUARE ROOT OF EACH NUMBER ///")
    for arr in tqdm(range(len(codes))):
        sqrt_x = int(sqrt(int(codes[arr][0])))
        sqrt_y = int(sqrt(int(codes[arr][1])))
        bin_join = '0x' + codes[arr][2]
        data_arr.append([sqrt_x, sqrt_y, bin_join])
    return data_arr


def order_data(codes: list) -> list:
    """
    Orders the data in the main list by
    removing the extra digits and turn every
    element into their binary form.
    """
    print("\n/// ORDERING DATA ///")
    ordered_codes = []
    pattern = "0b"

    sqrt_x = [bin(x[0]) for x in tqdm(codes)]
    sqrt_x = format.remove(pattern, sqrt_x)
    sqrt_x = verify(sqrt_x, 8)

    sqrt_y = [bin(y[1]) for y in tqdm(codes)]
    sqrt_y = format.remove(pattern, sqrt_y)
    sqrt_y = verify(sqrt_y, 8)

    bin_hex = [bin(int(b[2], base=16)) for b in tqdm(codes)]
    bin_hex = format.remove(pattern, bin_hex)
    bin_hex = verify(bin_hex, 32)

    for n in tqdm(range(len(codes))):
        ordered_codes.append([sqrt_x[n], sqrt_y[n], bin_hex[n]])

    return ordered_codes


def verify(list_io: list, length) -> list:
    outcome = []

    for elem in list_io:
        format_list = format.length_tester(element=elem, length=length)
        outcome.append(format_list)

    return list_io


'''MAIN'''


def high_compressed_image(path=None) -> list:
    """
    Compress the image
    """
    data = sqrt_data(get_pixel_cords_hex(path if path is not None else get_path()))
    sub_hci = order_data(data)
    return sub_hci


def hci(path):
    hci_obj = high_compressed_image(path)
    write.write_hci(arr=hci_obj)

    return 0


if __name__ == "__main__":
    hci(path=get_path())
