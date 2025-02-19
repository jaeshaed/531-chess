"""Этот модуль проверяет правильность работы класса Board."""

import itertools
import unittest

from board import Board


class TestBoard(unittest.TestCase):
    """Проверки шахматной доски."""

    def setUp(self):
        self.board = Board()

    def test_board_is_empty(self):
        for file in 'abcdefgh':
            for rank in '12345678':
                at = file + rank
                with self.subTest(square=at):
                    self.assertIsNone(self.board.squares[at].piece)
                    self.assertTrue(self.board.squares[at].is_empty())

    def test_board_has_64_squares(self):
        self.assertEqual(len(self.board.squares), 64)

    def test_squares_are_false_when_the_board_is_empty(self):
        self.assertFalse(self.board.squares)

    def test_squares_iteration(self):
        square_coords = itertools.product('abcdefgh', '12345678')
        for square in self.board.squares:
            expected_file, expected_rank = next(square_coords)
            with self.subTest(square=expected_file+expected_rank):
                self.assertEqual(square.file, expected_file)
                self.assertEqual(square.rank, expected_rank)
        with self.assertRaises(StopIteration):
            next(square_coords)


if __name__ == '__main__':
    unittest.main()
