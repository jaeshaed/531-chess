from enum import Enum
from typing import List, Optional


class PieceColor(Enum):
    WHITE = 1
    BLACK = 2


class Square:
    def __init__(self, row: int, column: int):
        self.row = row
        self.column = column


class PieceType(Enum):
    KING = "King"


class Piece:
    def __init__(self, piece_type: PieceType, color: PieceColor, square: Square):
        self.piece_type = piece_type
        self.color = color
        self.square = square
        self.moved = False  #Для отслеживания рокировки

    def valid_moves(self, board) -> List[Square]:
        raise NotImplementedError()

    def attack_squares(self, board) -> List[Square]:
        return self.valid_moves(board)


class King(Piece):
    def __init__(self, color: PieceColor, square: Square):
        super().__init__(PieceType.KING, color, square)

    def valid_moves(self, board) -> List[Square]:
        moves = []
        current_row = self.square.row
        current_col = self.square.column

        #Все возможные направления движения короля
        directions = [
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1), (0, 1),
            (1, -1), (1, 0), (1, 1)
        ]

        for dr, dc in directions:
            new_row = current_row + dr
            new_col = current_col + dc
            if 0 <= new_row < 8 and 0 <= new_col < 8:
                target_square = Square(new_row, new_col)
                piece_on_target = board.get_piece(target_square)
                if not piece_on_target or piece_on_target.color != self.color:
                    moves.append(target_square)

        #Рокировка (упрощенная версия, без проверки на шах)
        if not self.moved:
            #Короткая рокировка (король -> ладья на том же ряду)
            rook_pos = board.get_piece(Square(current_row, 7))
            if rook_pos and not rook_pos.moved:
                if all(board.is_empty(Square(current_row, c)) for c in [5, 6]):
                    moves.append(Square(current_row, 6))

            #Длинная рокировка
            rook_pos = board.get_piece(Square(current_row, 0))
            if rook_pos and not rook_pos.moved:
                if all(board.is_empty(Square(current_row, c)) for c in [1, 2, 3]):
                    moves.append(Square(current_row, 2))

        return moves

    #Метод для проверки, находится ли король под шахом
    def is_in_check(self, board) -> bool:
        #Реализация зависит от структуры класса Board
        #Нужно проверить все вражеские фигуры и их атакующие клетки
        pass