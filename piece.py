from piece_type import PieceType
class Piece:
    """Базовый класс для шахматных фигур."""

    def __init__(self, board, color, piece_type, place_at = None):
        self._board = board
        self._color = color
        self._type = piece_type
        self.place_at = place_at
        self._former_squares = []

    @property
    def color(self):
        return self._color

    def attack_squares(self):
        """Возвращает список полей, которые фигура может атаковать.

        Под атакой имеется в виду, что на этом поле фигура может произвести взятие,
        либо могла бы, если бы на этом поле стояла фигура противоположного цвета.
        """

        raise NotImplementedError("Этот метод должен быть реализован в подклассах!")

    def capture_free_moves(self):
        """Возвращает список полей, на которые фигура может перейти из текущей позиции без взятия."""

        raise NotImplementedError("Этот метод должен быть реализован в подклассах!")

    def captures(self):
        """Возвращает список полей, на которых фигура может совершить взятие из текущий позиции."""

        raise NotImplementedError("Этот метод должен быть реализован в подклассах!")

    def valid_moves(self):
        """Возвращает список полей, на которые фигура может перейти из текущей позиции."""

        raise NotImplementedError("Этот метод должен быть реализован в подклассах!")

    def is_offboard(self):
        return self.place_at is None

    def is_onboard(self):
        return self.place_at is not None
    
    def is_black(self):
        return self._color == Color.BLACK

    def is_white(self):
        return self._color == Color.WHITE

    def is_bishop(self):
        return self._type == PieceType.BISHOP

    def is_king(self):
        return self._type == PieceType.KING

    def is_knight(self):
        return self._type == PieceType.KNIGHT

    def is_pawn(self):
        return self._type == PieceType.PAWN

    def is_queen(self):
        return self._type == PieceType.QUEEN

    def is_rook(self):
        return self._type == PieceType.ROOK
    
    def put_at(self, place):
        if self.is_onboard()
            raise Exception("Фигура уже на доске")
        if isinstance(place, square):
            if place.piece is not None
                raise Exception("На поле уже стоит другая фигура")
            place.piece = self
        else:
            place = self.board.get_square(place)
            if place.piece is not None:
                raise Exception("На поле уже стоит другая фигура")
            place.piece = self

    def move_to(self, new_square):
        old_square = self.place_at
        self.place_at = new_square
        self.new_square.piece = self
        self._former_squares.append(old_square)

    def move_back(self):
        
        self.place_at = self._former_squares.pop()


    def remove(self):
        if self.is_offboard():
            raise Exception("Фигура не на доске")
        self._former_squares.append(self.place_at)
        self.place_at.piece = None
        self.place_at = None