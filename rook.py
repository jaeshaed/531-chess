from piece import Piece
from square import Square
from color import Color

class Rook(Piece):

    def __init__(self,color,place_at=None):
        super().__init__(color,place_at)

    def color(self):
        return self.color

    def __init__(self,board):
        super().__init__(board)
        self.moved = False  

    def valid_moves(self) -> Square:
       
        moves = []
        current_square = self.place_at

        # Движение вверх
        square = current_square.up
        while square is not None and square.is_on_board():
            if square.is_empty():
                moves.append(square)
            else:
                if square.piece.color != self.color:
                    moves.append(square)  
                break
            square = square.up

        # Движение вниз
        square = current_square.down
        while square is not None and square.is_on_board():
            if square.is_empty():
                moves.append(square)
            else:
                if square.piece.color != self.color:
                    moves.append(square)  
                break
            square = square.down

        # Движение влево
        square = current_square.left
        while square is not None and square.is_on_board():
            if square.is_empty():
                moves.append(square)
            else:
                if square.piece.color != self.color:
                    moves.append(square)  
                break
            square = square.left

        # Движение вправо
        square = current_square.right
        while square is not None and square.is_on_board():
            if square.is_empty():
                moves.append(square)
            else:
                if square.piece.color != self.color:
                    moves.append(square) 
                break
            square = square.right

        return moves

    def move_to(self, square: Square):
        #Перемещение ладьи на указанную клетку
        if square in self.valid_moves():
            self.remove()  
            self.place_at = square  
            self.put_at(square)  
            self.moved = True  
        else:
            raise Exception






