for x in range(int("10000000", 8), int("77777777", 8)):
    n = oct(x)[2:]
    for x in range(len(n)):
        if n.count(n[x]) == 1:
            pass