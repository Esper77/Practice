def F(n):
    if n == 0:
        return 5
    if n > 0:
        return 3*F(n-4)
    return F(n+3)
print(F(34))