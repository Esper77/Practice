def game(a, b, turn):
    if a + b >= 59 and turn == 2:
        return True
    if a + b < 59 and turn == 2:
        return False
    if a + b > 59 and turn != 2:
        return False

    if turn == 0:  # Первый ход Пети, как выигрывающая сторона ставим "or" всегда
        return game(a + 2, b, turn + 1) or game(a * 2, b, turn + 1) or game(a, b + 2, turn + 1) or game(a, b * 2,
                                                                                                        turn + 1)
    if turn == 1:  # Второй ход Вани, тут "независимо от хода", поэтому "and"
        return game(a + 2, b, turn + 1) and game(a * 2, b, turn + 1) and game(a, b + 2, turn + 1) and game(a, b * 2,
                                                                                                        turn + 1)
    if turn == 2:  # Второй ход Пети, как выигрывающая сторона ставим "or" всегда
        return game(a + 2, b, turn + 1) and game(a * 2, b, turn + 1) and game(a, b + 2, turn + 1) and game(a, b * 2,
                                                                                                        turn + 1)
    if turn == 1:  # Второй ход Вани, тут "независимо от хода", поэтому "and"
        return game(a + 2, b, turn + 1) or game(a * 2, b, turn + 1) or game(a, b + 2, turn + 1) or game(a, b * 2,
                                                                                                        turn + 1)


for s in range(1, 70):  # Перебор
    if game(5, s, 0):
        print(s)