# https://stepik.org/lesson/484592/step/1?auth=login&unit=475907
def game(a, b, turn):
    global limit
    if a + b >= limit and turn == 2:
        return True
    if a + b < limit and turn == 2:
        return False
    if a + b > limit and turn != 2:
        return False

    if turn == 0:  # Первый неудачный ход Пети, поэтому ставим "or" между вызовом рекурсии
        return game(a + 1, b, turn + 1) or game(a * 2, b, turn + 1) or game(a, b + 1, turn + 1) or game(a, b * 2,
                                                                                                        turn + 1)
    if turn == 1:  # Второй ход Вани, как выигрывающая сторона ставим "or" всегда
        return game(a + 1, b, turn + 1) or game(a * 2, b, turn + 1) or game(a, b + 1, turn + 1) or game(a, b * 2,
                                                                                                        turn + 1)


limit = 77

for s in range(1, 70):  # Перебор
    if game(7, s, 0):
        print(s)