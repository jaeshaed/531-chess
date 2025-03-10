"""Импортирование фигур"""
from pawn import Pawn
from knight import Knight
from king import King
from bishop import Bishop
from Queen import Queen
from rook  import Rook


"""Класс игровой доски"""
class Board(object):
    """Конструктор в котором реализовано размещение фигур"""
    def __init__(self):
        self._squares = []