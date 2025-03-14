from piece import Piece
from piece_type import PieceType

class Pawn(Piece):
    def __init__(self, color, place_at, position):
        super().__init__(color, place_at)
        self.position = position
        self._promoted_to = None
    
    @property
    def promoted(self):
        return self._promoted_to is not None

    def is_pawn(self):
        return True
    
    def is_bishop(self):
        if self._promoted_to == PieceType.BISHOP:
            return True
        return False
    
    def is_rook(self):
        if self._promoted_to == PieceType.ROOK:
            return True
        return False
    
    def is_queen(self):
        if self._promoted_to == PieceType.QUEEN:
            return True
        return False
    
    def is_knight(self):
        if self._promoted_to == PieceType.KNIGHT:
            return True
        return False
    
    def promoted_to(self, piece_type):
        assert isinstance(piece_type, PieceType)
        self._promoted_to = piece_type


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
    
    def move_to(self, new_place, start_position):
        if self.color == "white":
            if new_place[1] == start_position[1] + 1 and new_place[0] == start_position[0]:
                return True
            elif start_position[1] == 1 and new_place[1] == start_position[1] + 2 and new_place[0] == start_position[0]:
                return True
            elif new_place[1] == start_position[1] + 1 and abs(new_place[0] - start_position[0]) == 1:
                return True
            return False
        else:
            if new_place[1] == start_position[1] - 1 and new_place[0] == start_position[0]:
                return True
            elif start_position[1] == 6 and new_place[1] == start_position[1] - 2 and new_place[0] == start_position[0]:
                return True
            elif new_place[1] == start_position[1] - 1 and abs(new_place[0] - start_position[0]) == 1:
                return True
            return False