from piece import Piece

class Pawn(Piece):
    def __init__(self, color, place_at, position):
        super().__init__(color, place_at)
        self.position = position
    
    def attack_squares(self):
        x, y = self.position
        if self.color == 'white':
            return [(x - 1, y + 1), (x + 1, y + 1)]
        else:
            return [(x - 1, y - 1), (x + 1, y - 1)]

    def capture_free_squares(self):
        x, y = self.position
        captures = []

        if self.color == 'white':
            attack = [(x - 1, y + 1), (x + 1, y + 1)]
        else:
            attack = [(x - 1, y - 1), (x + 1, y - 1)]

        for dx, dy in attack:
            new_x, new_y = x + dx, y + dy
            if 0 <= new_x < 8 and 0 <= new_y < 8:
                target = board[new_x][new_y]
                if target is not None and target.color != self.color:
                    captures.append((new_x, new_y))
        return captures

    def valid_moves(self):
        x, y = self.position
        moves = []

        if self.color == 'white':
            moves.append((x, y + 1))
            if y == 1:
                moves.append((x, y + 2))
        elif self.color == 'black':
            moves.append((x, y - 1)) 
            if y == 6:
                moves.append((x, y - 2))
        return moves