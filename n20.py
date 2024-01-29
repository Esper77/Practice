# https://stepik.org/lesson/484593/step/1?auth=login&unit=475908
def game(a, b, turn):
    if a + b >= 77 and turn == 3:
        return True
    if a + b < 77 and turn == 3:
        return False
    if a + b > 77 and turn != 3:
        return False

    if turn == 0:  # Первый ход Пети, как выигрывающая сторона ставим "or" всегда
        return game(a + 1, b, turn + 1) or game(a * 2, b, turn + 1) or game(a, b + 1, turn + 1) or game(a, b * 2,
                                                                                                        turn + 1)
    if turn == 1:  # Второй ход Вани, тут "независимо от хода", поэтому "and"
        return game(a + 1, b, turn + 1) and game(a * 2, b, turn + 1) and game(a, b + 1, turn + 1) and game(a, b * 2,
                                                                                                        turn + 1)
    if turn == 2:  # Второй ход Пети, как выигрывающая сторона ставим "or" всегда
        return game(a + 1, b, turn + 1) or game(a * 2, b, turn + 1) or game(a, b + 1, turn + 1) or game(a, b * 2,
                                                                                                        turn + 1)


for s in range(1, 70):  # Перебор
    if game(7, s, 0):
        print(s)