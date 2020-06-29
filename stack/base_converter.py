from stack.my_stack import Stack


def base_converter(dec_num, base):
    """
    Convert a given decimal number to the representation in the given base.
    :param dec_num: int, integer to be converted
    :param base: int, base to be converted to, should not be greater than 16.
    :return: int
    """
    if dec_num < 0:
        return -1
    if base > 16:
        return -1
    digits = "0123456789ABCDEF"
    remainder = Stack()
    while dec_num > 0:
        rem = dec_num % base
        remainder.push(rem)
        dec_num = dec_num // base

    new_num = ""
    while not remainder.is_empty():
        new_num += digits[remainder.pop()]
    return new_num


if __name__ == "__main__":
    print(base_converter(4, 2))
    print(base_converter(-1, 2))
    print(base_converter(5, 2))
    print(base_converter(16, 16))
    print(base_converter(16, 17))
