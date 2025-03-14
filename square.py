from color import Color

class Square:
    def __init__(self, all_squares, file_index, rank_index, occupant=None):
        self._all_squares = all_squares
        self._file_index = file_index
        self._rank_index = rank_index
        self._occupant = occupant
        self._color = Color.BLACK if (file_index + rank_index) % 2 == 0 else Color.WHITE
        self._highlighted = False
        self._highlight_color = None

    @property
    def file(self):
        return self.rank_index + 1

    @property
    def rank(self):
        return str(self.rank_index + 1)

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
        return (f"Square(file_index={self._file_index}, rank_index={self._rank_index}, occupant={self._occupant}, "
                f"color={self._color}, highlighted={self._highlighted}, "
                f"highlight_color={self._highlight_color})")
