string = '1'*95+'7'*31
while "1111" in string:
    string = string.replace('1111', '7', 1).replace('77', '1', 1)
print(string)