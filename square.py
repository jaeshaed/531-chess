from color import Color

class Square:
    def __init__(self, all_squares, row, col, occupant=None):
        self._all_squares = all_squares
        self._row = row
        self._col = col
        self._occupant = occupant
        self._color = Color.BLACK if (row + col) % 2 == 0 else Color.WHITE
        self._highlighted = False
        self._highlight_color = None

    @property
    def file(self):
        return self._row + 1

    @property
    def rank(self):
        return str(self._col + 1)

    @property
    def occupant(self):
        return self._occupant

    @occupant.setter
    def occupant(self, piece):
        self._occupant = piece

    @property
    def color(self):
        return self._color

    @property
    def highlighted(self):
        return self._highlighted

    @property
    def highlight_color(self):
        return self._highlight_color

    @property
    def color(self):
        return Color.WHITE
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
        return self._occupant is None

    def place_piece(self, piece):
        self._occupant = piece

    def remove_piece(self):
        self._occupant = None

    def highlight(self, color='yellow'):
        self._highlighted = True
        self._highlight_color = color

    def unhighlight(self):
        self._highlighted = False
        self._highlight_color = None

    def __str__(self):
        return str(self._occupant) if self._occupant else '.'

    def __repr__(self):
        return (f"Square(row={self._row}, col={self._col}, occupant={self._occupant}, "
                f"color={self._color}, highlighted={self._highlighted}, "
                f"highlight_color={self._highlight_color})")
