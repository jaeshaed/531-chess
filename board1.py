"""Импортирование фигур"""
from pawn import Pawn
from knight import Knight
from king import King
from bishop import Bishop
from Queen import Queen
from rook  import Rook

"""Класс игровой доски"""
class Board(object):
    """Конструктор в котором реализовано размещение фигур"""
    def __init__(self):
        self._squares = []
        for i in range(8):
            row = []
            for j in range(8):
                square = Square(i, j)
                if i == 0 or i == 7 or j == 0 or j == 7:
                    piece = None
                else:
                    if i % 2 != j % 2:
                        piece = Pawn('WHITE') if i < 6 else Pawn('BLACK')
                    elif i > 1 and i < 6 and j % 2 == 0:
                        piece = Rook('WHITE') if i < 4 else Rook('BLACK')
                    elif i > 1 and i < 6 and j % 2 == 1:
                        piece = Knight('WHITE') if i < 4 else Knight('BLACK')
                    elif i > 1 and i < 6 and j == 1:
                        piece = Bishop('WHITE') if i < 4 else Bishop('BLACK')
                    elif i > 1 and i < 6 and j == 6:
                        piece = Queen('WHITE') if i < 4 else Queen('BLACK')
                    elif i == 1:
                        piece = King('WHITE')
                    elif i == 6:
                        piece = King('BLACK')
                    else:
                        piece = None
                row.append(square)
            self._squares.append(row)

    """Возвращает в значальные координаты квадрата"""
    def get_square(self, x, y):
        return self._squares[x][y]
