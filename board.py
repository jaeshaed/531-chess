from bishop import Bishop
from color import Color
from pawn import Pawn
from square import Square


class Squares:
    pass


class Board:

    def put_black_pawn_at(self, square):
        pass

    def put_white_pawn_at(self, square):
        pass
        #return Pawn(Color.WHITE, square)

    def put_black_bishop_at(self, square):
        return Bishop(self, Color.BLACK, square)

    def put_white_bishop_at(self, square):
        return Bishop(self, Color.WHITE, square)

    def put_black_rook_at(self, square):
        pass

    def put_white_rook_at(self, square):
        pass

    def put_black_king_at(self, square):
        pass

    def put_white_king_at(self, square):
        pass

    def put_black_knight_at(self, square):
        pass

    def put_white_knight_at(self, square):
        pass
