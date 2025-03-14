from piece import Piece



class Queen(Piece):
        def __init__(self, name, color, position):
            super().__init__()
            self.name = name
            self.color = color
            self.position = position

        def __str__(self):
            return f"Queen {self.name}, {self.color}, {self.position}"

        def attack_squares(self):
            "Функция атаки"
            return super().attack_squares()
            
