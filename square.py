class Square:

    def __init__ (self, all_squares, file, rank):
        self._all_squares = all_squares
        self.file = file
        self.rank = rank
        self.piece = None

    def is_empty(self):
        return self.piece is None

    def is_downmost(self):
        return self.rank == 1
    
    def is_topmost(self):
        return self.rank == 8

    def is_leftmost(self):
        return self.file == "A"

    def is_rightmost(self):
        return self.file == "H"