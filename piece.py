class Piece:
    """Базовый класс для шахматных фигур."""

    def __init__(self, color, place_at = None):
        self.color = color
        self.place_at = place_at

    def attack_squares(self):
        """Возвращает список полей, на которых фигура может совершить взятие из текущий позиции."""

        raise NotImplementedError("Этот метод должен быть реализован в подклассах!")

    def capture_free_squares(self):
        """Возвращает список полей, на которые фигура может перейти из текущей позиции без взятия."""

        raise NotImplementedError("Этот метод должен быть реализован в подклассах!")

    def valid_moves(self):
        """Возвращает список полей, на которые фигура может перейти из текущей позиции."""

        raise NotImplementedError("Этот метод должен быть реализован в подклассах!")
