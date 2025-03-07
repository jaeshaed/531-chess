"""Этот модуль проверяет правильность работы класса Queen."""

import unittest


class TestWhiteQueenInheritedTraits(unittest.TestCase):
    """Проверки основных (унаследованных от Piece) свойств и методов белого ферзя."""

    def setUp(self):
        from board import Board
        self.board = Board()
        self.queen = self.board.put_white_queen_at('d1')

    def test_queen_is_white(self):
        self.assertTrue(self.queen.is_white())

    def test_queen_is_not_black(self):
        self.assertFalse(self.queen.is_black())

    def test_color_is_right(self):
        from color import Color
        self.assertEqual(self.queen.color, Color.WHITE)

    def test_color_is_read_only(self):
        with self.assertRaises(AttributeError):
            from color import Color
            self.queen.color = Color.BLACK
        self.assertTrue(self.queen.is_white())

    def test_queen_has_not_moved(self):
        self.assertFalse(self.queen.moved)

    def test_moved_is_read_only(self):
        with self.assertRaises(AttributeError):
            self.queen.moved = True
        self.assertFalse(self.queen.moved)

    def test_queen_is_on_the_right_square(self):
        self.assertIs(self.queen.place_at, self.board.squares['d1'])

    def test_place_at_is_read_only(self):
        with self.assertRaises(AttributeError):
            self.queen.place_at = self.board.squares['d8']
        self.assertIs(self.queen.place_at, self.board.squares['d1'])

    def test_queen_is_not_pawn(self):
        self.assertFalse(self.queen.is_pawn())

    def test_queen_is_not_bishop(self):
        self.assertFalse(self.queen.is_bishop())

    def test_queen_is_not_king(self):
        self.assertFalse(self.queen.is_king())

    def test_queen_is_not_knight(self):
        self.assertFalse(self.queen.is_knight())

    def test_queen_is_queen(self):
        self.assertTrue(self.queen.is_queen())

    def test_queen_is_not_rook(self):
        self.assertFalse(self.queen.is_rook())

    def test_queen_is_on_board(self):
        self.assertTrue(self.queen.is_onboard())

    def test_queen_is_not_off_board(self):
        self.assertFalse(self.queen.is_offboard())


class TestBlackQueenColor(unittest.TestCase):
    """Проверки свойства color чёрного ферзя."""

    def setUp(self):
        from board import Board
        self.board = Board()
        self.queen = self.board.put_black_queen_at('d8')

    def test_queen_is_black(self):
        self.assertTrue(self.queen.is_black())

    def test_queen_is_not_white(self):
        self.assertFalse(self.queen.is_white())

    def test_color_is_right(self):
        from color import Color
        self.assertEqual(self.queen.color, Color.BLACK)

    def test_color_is_read_only(self):
        with self.assertRaises(AttributeError):
            from color import Color
            self.queen.color = Color.WHITE
        self.assertTrue(self.queen.is_black())


class TestQueenMoves(unittest.TestCase):
    """Проверки ходов ферзя."""

    def setUp(self):
        from board import Board
        self.board = Board()
        self.board.put_white_rook_at('a1')
        self.board.put_white_pawn_at('d2')
        self.board.put_black_pawn_at('g7')
        self.queen = self.board.put_black_queen_at('d4')
        # . . . . . . . .
        # . . . . . . p .
        # . . . . . . . .
        # . . . . . . . .
        # . . . q . . . .
        # . . . . . . . .
        # . . . P . . . .
        # R . . . . . . .

    def test_valid_moves(self):
        valid_moves = self.board.squares[
            'd5,d6,d7,d8,e5,f6,e4,f4,g4,h4,e3,f2,g1,d3,d2,c3,b2,a1,c4,b4,a4,c5,b6,a7'
        ]
        self.assertCountEqual(self.queen.valid_moves(), valid_moves)

    def test_capture_free_moves(self):
        capture_free_moves = self.board.squares[
            'd5,d6,d7,d8,e5,f6,e4,f4,g4,h4,e3,f2,g1,d3,c3,b2,c4,b4,a4,c5,b6,a7'
        ]
        self.assertCountEqual(self.queen.capture_free_moves(), capture_free_moves)

    def test_captures(self):
        self.assertCountEqual(self.queen.captures(), self.board.squares['a1,d2'])

    def test_attack_squares(self):
        attack_squares = self.board.squares[
            'd5,d6,d7,d8,e5,f6,e4,f4,g4,h4,e3,f2,g1,d3,d2,c3,b2,a1,c4,b4,a4,c5,b6,a7'
        ]
        self.assertCountEqual(self.queen.attack_squares(), attack_squares)


if __name__ == '__main__':
    unittest.main()
