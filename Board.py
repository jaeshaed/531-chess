class Piece:
    def __init__(self, color, type):
        self.color = color
        self.type = type

class Square:
    def __inint__(self, x, y):
        self.x = x
        self.y = y
        self.piece = None

class Board:
    def __init__(self):
        self.game = None
        self.squares = [[Square(x, y) for y in range(8)] for x in range(8)]
        self.white_pieces = []
        self.black_pieces = []

    def clear(self):
        for row in self.squares:
            for square in row:
                square.piece = None
        self.white_pieces.clear()
        self.black_pieces.clear()

    



    


