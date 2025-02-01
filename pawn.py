from piece import Piece

class Pawn(Piece):
    def __init__(self, color):
        self.color = color #Цвет
        self.position = None #(x, y)
    
    def attack_squares(self):
        x, y = self.position
        return [(x - 1, y + 1), (x + 1, y + 1)]

    def set_position(self, position):
        self.position = position 

    def move(self):
        x, y = self.position
        moves = []

        if self.color == 'white':
            moves.append((x, y + 1)) #Может двигаться на одну клетку вверх(белые снизу обычно)
            if y == 1: #Если фигура в начальной позиции, а именно определяеться во Y, то она может:
                moves.append((x, y + 2)) #Сделать шаг на 2 клетки вверх
        elif self.color == 'black': #Движение вниз 
            moves.append((x, y - 1)) 
            if y == 6: #Начальная позиция у черных(сверху)
                moves.append((x, y - 2))
        return moves