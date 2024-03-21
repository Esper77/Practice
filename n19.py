
def game(a, turn):
    global limit
    if a >= limit and (turn == 2 or turn == 4):
        return True
    if a < limit and turn == 4:
        return False
    if a > limit and turn != 4:
        return False

    if turn == 0:  # Первый неудачный ход Пети, поэтому ставим "or" между вызовом рекурсии
        return game(a + 1, turn + 1) and game(a + 2, turn + 1) and game(a + 3, turn + 1) and game(a * 2, turn + 1)
    if turn == 1:  # Второй ход Вани, как выигрывающая сторона ставим "or" всегда
        return game(a + 1, turn + 1) or game(a + 2, turn + 1) or game(a + 3, turn + 1) or game(a * 2, turn + 1)
    if turn == 2:
        return game(a + 1, turn + 1) and game(a + 2, turn + 1) and game(a + 3, turn + 1) and game(a * 2, turn + 1)
    if turn == 3:
        return game(a + 1, turn + 1) or game(a + 2, turn + 1) or game(a + 3, turn + 1) or game(a * 2, turn + 1)


limit = 38

for s in range(1, 37):  # Перебор
    if game(s, 0):
        print(s)
