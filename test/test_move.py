"""Этот модуль проверяет правильность работы класса Move."""

import unittest

class TestCastling(unittest.TestCase):
    """Проверки рокировок."""

    def setUp(self):
        from board import Board
        from move import Move

        board = Board()
        board.put_white_rook_at('a1')
        board.put_white_rook_at('h1')
        king = board.put_white_king_at('e1')

        self.kingside_castling = Move(king.place_at, king.place_at.right.right)
        self.queenside_castling = Move(king.place_at, king.place_at.left.left)

    def test_castling(self):
        self.assertTrue(self.kingside_castling.is_castling())
        self.assertTrue(self.queenside_castling.is_castling())

    def test_kingside_castling(self):
        self.assertTrue(self.kingside_castling.is_kingside_castling())
        self.assertFalse(self.kingside_castling.is_queenside_castling())

    def test_queenside_castling(self):
        self.assertFalse(self.queenside_castling.is_kingside_castling())
        self.assertTrue(self.queenside_castling.is_queenside_castling())
