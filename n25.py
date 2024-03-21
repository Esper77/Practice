# 1*586?6
from utils import to_base

l = []

# for x in range(10):
#     n = f"1586{x}6"
#     if to_base(int(n), 7) == to_base(int(n), 7)[::-1]:
#         l.append(l.append((n, sum([int(i) for i in to_base(int(n), 7)]))))

for x in "02468":
    for y in "13579":
        for z in "0123456789":
            n = f"12{x}4{y}6{z}8"
            if int(n) % 92:
                l.append((n,int(n) // 92))

for unit in l:
    print(unit[0], unit[1])
