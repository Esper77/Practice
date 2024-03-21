import utils

for x in range(2, 10000):
    n = x
    if n % 2 == 0:
        n //= 2
    else:
        n -= 1
    if n % 3 == 0:
        n //= 3
    else:
        n -= 1
    if n % 7 == 0:
        n //= 7
    else:
        n -= 1

    if n == 2:
        print(x)

