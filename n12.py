string = '1'*2019+'3'*2119
while "11" in string:
    string = string.replace('11', '2', 1).replace('22', '3', 1).replace('33', '1', 1)
print(string)