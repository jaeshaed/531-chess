from color import Color

class Board:
    pass

class Square:

    def __init__ (self, all_squares, file_index, rank_index):
        self._all_squares = all_squares
        self.file_index = file_index
        
        if self.file_index == 0:
            self.file = "A"
        if self.file_index == 1:
            self.file = "B"
        if self.file_index == 2:
            self.file = "C"
        if self.file_index == 3:
            self.file = "D"
        if self.file_index == 4:
            self.file = "E"
        if self.file_index == 5:
            self.file = "F"
        if self.file_index == 6:
            self.file = "G"
        if self.file_index == 7:
            self.file = "H"
        self.rank = rank_index + 1
        self.piece = None


    @property
    def color(self):
        if (self.file_index + self.rank) % 2 ==0:
            return Color.WHITE
        else: 
            return Color.BLACK
        
    @property
    def down(self):
        return self._all_squares[self.file_index][self.rank_index - 1]
    
    @property
    def up(self):
        return self._all_squares[self.file_index][self.rank_index + 1]
    
    @property
    def left(self):
        return self._all_squares[self.file_index - 1][self.rank_index]
    
    @property
    def right(self):
        return self._all_squares[self.file_index + 1][self.rank_index]
    

    def is_empty(self):
        return self.piece is None

    def is_downmost(self):
        return self.rank == 0
    
    def is_topmost(self):
        return self.rank == 7

    def is_leftmost(self):
        return self.file == "A"

    def is_rightmost(self):
        return self.file == "H"
    
'''square = Square(None, 0, 0)
print(square.piece)
square.piece = "lalala"
print(square.piece)

print(square.down)
square.down = 555
print(square.down)'''







