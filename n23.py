def f(n):
    if n < 46:
        return f(n*2) + f(n*2+1) + f(n+1)
    if n > 46:
        return 0
    return 1

print(f(5))