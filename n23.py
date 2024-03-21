def f(n, t):
    if n < t:
        return f(n+1, t) + f(n*2, t) + f(n*4, t)
    if n > t:
        return 0
    return 1


print(f(1, 17))
