def write_hci(arr: list):
    """
    Writes the compress image in a new file
    """
    compressed_file_name = input("Enter your hci file name: \n")
    with open(f"{compressed_file_name}.hci", "w") as fl:
        for list_items in arr:
            for list_items2 in list_items:
                fl.write(list_items2)
    return 0
