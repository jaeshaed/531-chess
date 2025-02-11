from color import Color
from bishop import Bishop
from square import Square

class Board:
    def __init__(self):
        self.game = None
        self.squares = [[Square(x, y) for y in range(8)] for x in range(8)]
        self.white_pieces = []
        self.black_pieces = []

    def clear(self):
        for piece in self.white_pieces:
            piece.remove()
        for piece in self.black_pieces:
            piece.remove()
   
    def put_black_bishop_at(self, place):
        bishop = Bishop(self, Color.BLACK, place)
        self.black_pieces.append(bishop)
        return bishop
    def put_black_bishop_at(self, place):
        bishop = Bishop(self, Color.WHITE, place)
        self.white_pieces.append(bishop)
        return bishop
    


    


