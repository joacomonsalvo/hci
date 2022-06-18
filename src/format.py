import re


def remove(pattern, list_name):
    """
    Removes specific digit patterns
    from every string in a list
    """
    list_output = [re.sub(pattern, '', i) for i in list_name]
    return list_output


def length_tester(element: str, length: int):
    """
    Test if the string being passed as argument
    is as long as is must be. In case of x & y
    the length must be 8 and in the case of the
    color code must be 32.

    In case element is longer than the stipulated
    it will raise an IndexError. Otherwise, if the
    length is longer than the element, it will return
    the length of the element, so then it can be fixed.
    Finally, if the length and the element ar equal, True
    will be returned.
    """
    if len(element) > length:
        raise IndexError("Out of range")

    elif len(element) < length:
        element = "0" * (length - len(element)) + element
        return element

    elif len(element) == length:
        return True
