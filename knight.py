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


    def move_knight(self):
        "Все возможные ходы коня"

        # offsets = [ (x+2,y+1),
        #         (x+2,y-1),
        #         (x-2,y+1),
        #         (x-2,y-1),
        #         (x+1,y+2),
        #         (x+1,y-2),
        #         (x-1,y+2),
        #         (x-1,y-2)
        #         ]

        moves = []
        """Проверка возможности хода"""
        if self.place_at.file < 6:
            if self.place_at.rank < 7:
                dest = self.game.board.squares[self.place_at + 2][self.place_at + 1],
                [self.place_at + 2][self.place_at - 1],
                [self.place_at - 2][self.place_at + 1],
                [self.place_at -2][self.place_at - 1],
                [self.place_at + 1][self.place_at + 2],
                [self.place_at + 1][self.place_at - 2],
                [self.place_at - 1][self.place_at + 2],
                [self.place_at - 1][self.place_at - 2]
                if dest.is_empty():
                    moves.append(dest)
                elif dest.piece.color != self.color:
                    moves.append(dest)
        return moves

        
    def attack_squares(self):
        """Возвращение квадрата, ведь конь ходит и атакует с одинаковыми ходами"""
        return self.move_knight()


    def capture_free_squares(self):


    