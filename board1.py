"""Импортирование фигур"""
from pawn import Pawn
from knight import Knight
from king import King
from bishop import Bishop
from queen import Queen
from rook  import Rook
from square import Square

class Board(object):
    """Класс игровой доски"""
    def __init__(self, initial_position=True):
        self._squares = []
        for i in range(8):
            row = []
            for j in range(8):
                square = Square(i, j)
                piece = None
                if initial_position:
                    # Расстановка фигур для начальной позиции
                    if i == 0:  # Первая горизонталь (белые фигуры)
                        if j == 0 or j == 7:
                            piece = Rook('WHITE')
                        elif j == 1 or j == 6:
                            piece = Knight('WHITE')
                        elif j == 2 or j == 5:
                            piece = Bishop('WHITE')
                        elif j == 3:
                            piece = Queen('WHITE')
                        elif j == 4:
                            piece = King('WHITE')
                    elif i == 1:  # Вторая горизонталь (белые пешки)
                        piece = Pawn('WHITE')
                    elif i == 6:  # Седьмая горизонталь (черные пешки)
                        piece = Pawn('BLACK')
                    elif i == 7:  # Восьмая горизонталь (черные фигуры)
                        if j == 0 or j == 7:
                            piece = Rook('BLACK')
                        elif j == 1 or j == 6:
                            piece = Knight('BLACK')
                        elif j == 2 or j == 5:
                            piece = Bishop('BLACK')
                        elif j == 3:
                            piece = Queen('BLACK')
                        elif j == 4:
                            piece = King('BLACK')
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

