# 1*586?6
from utils import to_base

l = []

for x in range(10):
    n = f"1586{x}6"
    if to_base(int(n), 7) == to_base(int(n), 7)[::-1]:
        l.append(l.append((n, sum([int(i) for i in to_base(int(n), 7)]))))

for x in range(10):
    for y in range(1000):
        n = f"1{y}586{x}6"
        if to_base(int(n), 7) == to_base(int(n), 7)[::-1]:
            l.append((n, sum([int(i) for i in to_base(int(n), 7)])))

for unit in l:
    print(unit[0], unit[1])
