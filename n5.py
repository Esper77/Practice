import utils

for x in range(1, 256):
    n = utils.bit_inversion(utils.to_byte(x-1))
    if int(n, 2) == 18:
        print(x)

