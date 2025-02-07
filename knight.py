from piece import Piece
"""Импорт из файла Piece"""

class Knight(Piece):
    """Создание класса Конь"""

    def __init__(self,color,place_at=None):
        super().__init__(color,place_at)


    def move_knight(self,x,y,):
        "Все возможные ходы коня"

        x=None
        y=None

        """Все возможные коды"""
        return [ (x+2,y+1),
                (x+2,y-1),
                (x-2,y+1),
                (x-2,y-1),
                (x+1,y+2),
                (x+1,y-2),
                (x-1,y+2),
                (x-1,y-2)
                ]
        
    def attack_squares(self):
        """Функция список квадратов которые может атаковать фигура"""
        return super().attack_squares()
    