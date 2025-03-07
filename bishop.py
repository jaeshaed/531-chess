
from piece import Piece

class Bishop(Piece):
    def __init__(self, color, place_at=None):
        super().__init__(self,color,place_at)
        moves = []
        # вправо-ввехр
        x = self.place_at.file + 1
        y = self.place_at.rank + 1
        while x < 8 and y < 8:
            dest = self.game.board.squares[x][y]
            if dest.is_empty():
                moves.append(dest)
            else:
                if dest.piece.color != self.color:
                    moves.append(dest)
                    break
                x += 1
                y += 1
        #влево-вверх

        x = self.place_at.file - 1
        y = self.place_at.rank + 1
        while x >= 0 and y < 8:
            dest = self.game.board.squares[x][y]
            if dest.is_empty():
                moves.append(dest)
            else:
                if dest.piece.color != self.color:
                    moves.append(dest)
                    break
                x -= 1
                y += 1

        # вправо-вниз
        x = self.place_at.file - 1
        y = self.place_at.rank - 1
        while x >= 0 and y >= 0:
            dest = self.game.board.squares[x][y]
            if dest.is_empty():
                moves.append(dest)
            else:
                if dest.piece.color != self.color:
                    moves.append(dest)
                    break
                x -= 1
                y -= 1

        # влево-вниз
        x = self.place_at.file + 1
        y = self.place_at.rank - 1
        while x < 8 and y >= 0:
            dest = self.game.board.squares[x][y]
            if dest.is_empty():
                moves.append(dest)
            else:
                if dest.piece.color != self.color:
                    moves.append(dest)
                    break
                x += 1
                y -= 1

        def valid_moves(self):
            return self.capture_free_moves() + self.capture()

        def captures(self):
            captures = []
            for square in self.attack_squares():
                if not square.is_empty():
                    captures.append(square)
                    return captures

        return moves



