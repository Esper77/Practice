for z in range(2):
    for x in range(2):
        for y in range(2):
            f = (x or y or not z) and (not x or y or not z) and (not x or not y or z)
            print(z, x, y, int(f))
