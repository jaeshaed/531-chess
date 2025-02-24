"""Этот модуль проверяет правильность работы класса Board."""

import unittest

from board import Board


class TestEmptyBoard(unittest.TestCase):
    """Проверки пустой шахматной доски."""

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

    def test_getting_square_by_getattr(self):
        square = self.board.squares.e5
        self.assertEqual(square.file, 'e')
        self.assertEqual(square.rank, '5')

    def test_getting_square_by_getitem(self):
        square = self.board.squares['d4']
        self.assertEqual(square.file, 'd')
        self.assertEqual(square.rank, '4')

    def test_getting_multiple_squares(self):
        squares = self.board.squares['a3,b8,c7']
        self.assertEqual(squares[0].file, 'a')
        self.assertEqual(squares[0].rank, '3')
        self.assertEqual(squares[1].file, 'b')
        self.assertEqual(squares[1].rank, '8')
        self.assertEqual(squares[2].file, 'c')
        self.assertEqual(squares[2].rank, '7')

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

    def test_impossibility_of_putting_piece_at_offboard_square(self):
        offboard_square = self.board.squares['a1'].down.left
        with self.assertRaises((RuntimeError, ValueError)):
            self.board.put_white_pawn_at(offboard_square)


class TestBoardInInitialPosition(unittest.TestCase):
    """Проверки шахматной доски в начальной позиции для игры."""

    def setUp(self):
        self.board = Board("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1")

    def test_black_queenside_rook(self):
        self.assertTrue(self.board.squares.a8.piece.is_black())
        self.assertTrue(self.board.squares.a8.piece.is_rook())
        self.assertFalse(self.board.squares.a8.piece.moved)

    def test_black_queenside_knight(self):
        self.assertTrue(self.board.squares.b8.piece.is_black())
        self.assertTrue(self.board.squares.b8.piece.is_knight())

    def test_black_queenside_bishop(self):
        self.assertTrue(self.board.squares.c8.piece.is_black())
        self.assertTrue(self.board.squares.c8.piece.is_bishop())

    def test_black_queen(self):
        self.assertTrue(self.board.squares.d8.piece.is_black())
        self.assertTrue(self.board.squares.d8.piece.is_queen())

    def test_black_king(self):
        self.assertTrue(self.board.squares.e8.piece.is_black())
        self.assertTrue(self.board.squares.e8.piece.is_king())
        self.assertFalse(self.board.squares.e8.piece.moved)

    def test_black_kingside_bishop(self):
        self.assertTrue(self.board.squares.f8.piece.is_black())
        self.assertTrue(self.board.squares.f8.piece.is_bishop())

    def test_black_kingside_knight(self):
        self.assertTrue(self.board.squares.g8.piece.is_black())
        self.assertTrue(self.board.squares.g8.piece.is_knight())

    def test_black_kingside_rook(self):
        self.assertTrue(self.board.squares.h8.piece.is_black())
        self.assertTrue(self.board.squares.h8.piece.is_rook())
        self.assertFalse(self.board.squares.h8.piece.moved)

    def test_black_pawns(self):
        for at in 'a7', 'b7', 'c7', 'd7', 'e7', 'f7', 'g7', 'h7':
            with self.subTest(square=at):
                self.assertTrue(self.board.squares[at].piece.is_black())
                self.assertTrue(self.board.squares[at].piece.is_pawn())
                self.assertFalse(self.board.squares[at].piece.moved)

    def test_empty_squares(self):
        for rank in '6543':
            for file in 'abcdefgh':
                at = file + rank
                with self.subTest(square=at):
                    self.assertTrue(self.board.squares[at].is_empty())

    def test_white_pawns(self):
        for at in 'a2', 'b2', 'c2', 'd2', 'e2', 'f2', 'g2', 'h2':
            with self.subTest(square=at):
                self.assertTrue(self.board.squares[at].piece.is_white())
                self.assertTrue(self.board.squares[at].piece.is_pawn())
                self.assertFalse(self.board.squares[at].piece.moved)

    def test_white_queenside_rook(self):
        self.assertTrue(self.board.squares.a1.piece.is_white())
        self.assertTrue(self.board.squares.a1.piece.is_rook())
        self.assertFalse(self.board.squares.a1.piece.moved)

    def test_white_queenside_knight(self):
        self.assertTrue(self.board.squares.b1.piece.is_white())
        self.assertTrue(self.board.squares.b1.piece.is_knight())

    def test_white_queenside_bishop(self):
        self.assertTrue(self.board.squares.c1.piece.is_white())
        self.assertTrue(self.board.squares.c1.piece.is_bishop())

    def test_white_queen(self):
        self.assertTrue(self.board.squares.d1.piece.is_white())
        self.assertTrue(self.board.squares.d1.piece.is_queen())

    def test_white_king(self):
        self.assertTrue(self.board.squares.e1.piece.is_white())
        self.assertTrue(self.board.squares.e1.piece.is_king())
        self.assertFalse(self.board.squares.e1.piece.moved)

    def test_white_kingside_bishop(self):
        self.assertTrue(self.board.squares.f1.piece.is_white())
        self.assertTrue(self.board.squares.f1.piece.is_bishop())

    def test_white_kingside_knight(self):
        self.assertTrue(self.board.squares.g1.piece.is_white())
        self.assertTrue(self.board.squares.g1.piece.is_knight())

    def test_white_kingside_rook(self):
        self.assertTrue(self.board.squares.h1.piece.is_white())
        self.assertTrue(self.board.squares.h1.piece.is_rook())
        self.assertFalse(self.board.squares.h1.piece.moved)


if __name__ == '__main__':
    unittest.main()
