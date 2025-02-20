"""Этот модуль проверяет правильность работы класса Board."""

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
        square_coords = [
            'a1', 'b1', 'c1', 'd1', 'e1', 'f1', 'g1', 'h1',
            'a2', 'b2', 'c2', 'd2', 'e2', 'f2', 'g2', 'h2',
            'a3', 'b3', 'c3', 'd3', 'e3', 'f3', 'g3', 'h3',
            'a4', 'b4', 'c4', 'd4', 'e4', 'f4', 'g4', 'h4',
            'a5', 'b5', 'c5', 'd5', 'e5', 'f5', 'g5', 'h5',
            'a6', 'b6', 'c6', 'd6', 'e6', 'f6', 'g6', 'h6',
            'a7', 'b7', 'c7', 'd7', 'e7', 'f7', 'g7', 'h7',
            'a8', 'b8', 'c8', 'd8', 'e8', 'f8', 'g8', 'h8'
        ]
        for square, square_coords in zip(self.board.squares, square_coords, strict=True):
            with self.subTest(square=square_coords):
                expected_file, expected_rank = square_coords
                self.assertEqual(square.file, expected_file)
                self.assertEqual(square.rank, expected_rank)


if __name__ == '__main__':
    unittest.main()
