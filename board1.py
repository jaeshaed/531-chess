"""Импортирование фигур"""
from pawn import Pawn
from knight import Knight
from king import King
from bishop import Bishop
from queen import Queen
from rook  import Rook
from square import Square

"""Класс игровой доски"""
class Board(object):
    """Конструктор в котором реализовано размещение фигур"""
    def __init__(self, initial_position=True):
        self._squares = []
        for i in range(8):
            row = []
            for j in range(8):
                square = Square(i, j)
                if initial_position:
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
                square.piece = piece  # Присваиваем фигуру клетке
                row.append(square)
            self._squares.append(row)

    """Возвращает в значальные координаты квадрата"""
    def get_square(self, x, y):
        return self._squares[x][y]

    """Очищает квадрат по указанным координатом"""
    def clear_square(self, x, y):
        self.get_square(x, y).piece = None


    """Визуализация шахматной доски"""
    def __str__(self):
        result = ''
        for i in range(8):
            for j in range(8):
                square = self.get_square(i, j)
                piece = f"{square.piece}" if square.piece is not None else '-'
                result += f"| {piece} "
            result += '|\n'
            if i % 2 == 0:
                result += '---------------\n'
        return result


if __name__ == "__main__":
    """Создаём доску с фигурами"""
    board_with_piece = Board(initial_position=False)
    print(board_with_piece)

    """Создаём доску с пустыми клетками"""
    board = Board(initial_position=False)
    print(board)

