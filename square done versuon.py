class Square:
    def __init__(self, row, col, occupant=None):
        self._row = row
        self._col = col
        self._occupant = occupant
        self._color = 'white' if (row + col) % 2 == 0 else 'black'
        self._highlighted = False
        self._highlight_color = None

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
