from piece import Piece
"""Импорт из файла Piece"""

class Knight(Piece):
    """Создание класса Конь"""

    def __init__(self,color,place_at=None):
        super().__init__(color,place_at)

    @property
    def color(self):
        return self._color
    """Декоратор @property  позволяет обращаться 
    к атрибутам класса как к обычным переменным, но при этом контролировать доступ к ним. 
    Это полезно, когда необходимо выполнить какие-то 
    дополнительные действия при получении или установке значения атрибута."""


    def attack_squares(self):
        """Возвращение квадрата, ведь конь ходит и атакует с одинаковыми ходами"""
        moves = []
        """Проверка возможности хода"""
        if self.place_at.file < 6:
            if self.place_at.rank < 7:
                dest = self.game.board.squares[self.place_at + 2][self.place_at + 1],
                [self.place_at + 2][self.place_at - 1],
                [self.place_at - 2][self.place_at + 1],
                [self.place_at - 2][self.place_at - 1],
                [self.place_at + 1][self.place_at + 2],
                [self.place_at + 1][self.place_at - 2],
                [self.place_at - 1][self.place_at + 2],
                [self.place_at - 1][self.place_at - 2]
                if dest.is_empty():
                    moves.append(dest)
                elif dest.piece.color != self.color:
                    moves.append(dest)
        return moves

    def capture_free_squares(self):
        """Проверяем квадраты доступные для перемещения без захвата"""
        move1=[]
        for row in range(-2, 3):
            for col in range(-2, 3):
                if row != 0 or col != 0:
                    file = self.place_at.file + row
                    rank = self.place_at.rank + col
                    try:
                        dest = self.game.board.squares[file][rank]
                        if dest.is_empty():
                            move1.append(dest)
                    except IndexError as e:
                        print(f"Ошибка: {e}")
        return move1

    def captures(self):
        """Квадраты для захвата"""
        return [(self.place_at.file + 1, self.place_at.rank + 2)]

    def valid_moves(self):
        return self.place_at+self.captures



    