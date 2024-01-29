def to_base(number, base):  # Converts number from 10-based to x-based
    alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    output = ""
    while number > 0:
        output += alphabet[number % base]
        number //= base
    return output[::-1]


def to_byte(number):  # Converts a number into 8-bit binary format
    output = to_base(number, 2)
    output = "0" * (8 - len(output)) + output
    return output


def bit_inversion(number):  # Inverts bits of binary number
    number.replace("0", "*")
    number.replace("1", "0")
    number.replace("*", "1")
    return number

