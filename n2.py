for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                f = not(not w or z) or (not x or y) or not x
                if not f:
                    print(w, z, y, x, int(f))
