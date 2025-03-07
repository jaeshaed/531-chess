from piece import Piece

class Rook(Piece):
    def __init__(self,color, place_at=None):
        super().__init__(color, place_at)

    def color(self):
        return self.color
    
    def __init__(self,color, board):
        super().__init__(color, board)
        self.moved = False

    def valid_moves(self) -> Square:
        moves = []
        current_square = self.place_at

        square = current_square.up
        while square is not None and square.is_on_board():
            if square.is_empty():
                moves.append







