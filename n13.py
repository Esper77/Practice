ip = (192<<24) + (168<< 16) + (248 << 8) + 176

q = 0

for i in range(16):
    temp_ip = ip + i
    if bin(temp_ip)[2:].count('0') == bin(temp_ip)[2:].count('1'):
        q += 1

print(q)