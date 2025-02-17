"""Этот модуль проверяет правильность работы класса Board."""

import unittest

from board import Board


class TestBoard(unittest.TestCase):
    """Проверки шахматной доски."""

    def test_board_is_empty(self):
        board = Board()
        for file in 'abcdefgh':
            for rank in '12345678':
                at = file + rank
                with self.subTest(square=at):
                    self.assertIsNone(board.squares[at].piece)


if __name__ == '__main__':
    unittest.main()
