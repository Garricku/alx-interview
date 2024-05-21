#!/usr/bin/python3
"""UTF-8 validation module for interview project ALX SE"""


def validUTF8(data):
    """
    Arg: data - This is the inputed dataset to be validated
    Return: True if data is a valid UTF-8 encoding,else return False.
    A character in UTF-8 can be 1 to 4 bytes long
    The data set can contain multiple characters
    The data will be represented by a list of integers
    Each integer represents 1 byte of data, therefore you
    only need to handle the 8 least significant bits of each integer.
    """
    for byte in data:
        # Convert the byte to binary representation (8 bits)
        binary_repr = format(byte, '08b')

        # Check the first octet sequence
        if binary_repr.startswith('0'):
            continue
        elif binary_repr.startswith('110'):
            num_following_bytes = 1
        elif binary_repr.startswith('1110'):
            num_following_bytes = 2
        elif binary_repr.startswith('11110'):
            num_following_bytes = 3
        else:
            return False

        # Check the following bytes
        for _ in range(num_following_bytes):
            byte = data.pop(0)
            if not (128 <= byte < 192):
                return False

    return True
