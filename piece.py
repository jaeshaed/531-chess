class Piece:
    """Базовый класс для шахматных фигур."""

    def __init__(self,board, color, place_at = None):
        self._color = color
        self.place_at = place_at
        self.board = board

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
