from piece import Piece
"""Импорт из файла Piece"""

class Knight(Piece):
    """Создание класса Конь"""

    def __init__(self,place_at,color):
        super().__init__()
        self.color=color
        """Цвет"""
        self.place_at=place_at
        """Место атаки"""

    def attack_squares(self):
        """Функция список квадратов которые может атаковать фигура"""
        return super().attack_squares()
    