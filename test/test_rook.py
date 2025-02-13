"""Этот модуль проверяет правильность работы класса Rook."""

import unittest


class TestWhiteRookInheritedTraits(unittest.TestCase):
    """Проверки основных (унаследованных от Piece) свойств и методов белой ладьи."""

    def setUp(self):
        from board import Board
        self.board = Board()
        self.rook = self.board.put_white_rook_at('a1')

    def test_rook_is_white(self):
        self.assertTrue(self.rook.is_white())

    def test_rook_is_not_black(self):
        self.assertFalse(self.rook.is_black())

    def test_color_is_right(self):
        from color import Color
        self.assertEqual(self.rook.color, Color.WHITE)

    def test_color_is_read_only(self):
        with self.assertRaises(AttributeError):
            from color import Color
            self.rook.color = Color.BLACK
        self.assertTrue(self.rook.is_white())

    def test_rook_has_not_moved(self):
        self.assertFalse(self.rook.moved)

    def test_moved_is_read_only(self):
        with self.assertRaises(AttributeError):
            self.rook.moved = True
        self.assertFalse(self.rook.moved)

    def test_rook_is_on_the_right_square(self):
        self.assertIs(self.rook.place_at, self.board.squares['a1'])

    def test_place_at_is_read_only(self):
        with self.assertRaises(AttributeError):
            self.rook.place_at = self.board.squares['a8']
        self.assertIs(self.rook.place_at, self.board.squares['a1'])

    def test_rook_is_not_pawn(self):
        self.assertFalse(self.rook.is_pawn())

    def test_rook_is_not_bishop(self):
        self.assertFalse(self.rook.is_bishop())

    def test_rook_is_not_king(self):
        self.assertFalse(self.rook.is_king())

    def test_rook_is_not_knight(self):
        self.assertFalse(self.rook.is_knight())

    def test_rook_is_not_queen(self):
        self.assertFalse(self.rook.is_queen())

    def test_rook_is_rook(self):
        self.assertTrue(self.rook.is_rook())

    def test_rook_is_on_board(self):
        self.assertTrue(self.rook.is_onboard())

    def test_rook_is_not_off_board(self):
        self.assertFalse(self.rook.is_offboard())


class TestBlackRookColor(unittest.TestCase):
    """Проверки свойства color чёрной ладьи."""

    def setUp(self):
        from board import Board
        self.board = Board()
        self.rook = self.board.put_black_rook_at('h8')

    def test_rook_is_black(self):
        self.assertTrue(self.rook.is_black())

    def test_rook_is_not_white(self):
        self.assertFalse(self.rook.is_white())

    def test_color_is_right(self):
        from color import Color
        self.assertEqual(self.rook.color, Color.BLACK)

    def test_color_is_read_only(self):
        with self.assertRaises(AttributeError):
            from color import Color
            self.rook.color = Color.WHITE
        self.assertTrue(self.rook.is_black())


class TestRookMoves(unittest.TestCase):
    """Проверки ходов ладьи."""

    def setUp(self):
        from board import Board
        self.board = Board()
        self.board.put_white_rook_at('a1')
        self.board.put_black_pawn_at('c7')
        self.rook = self.board.put_white_rook_at('c1')
        # . . . . . . . .
        # . . p . . . . .
        # . . . . . . . .
        # . . . . . . . .
        # . . . . . . . .
        # . . . . . . . .
        # . . . . . . . .
        # R . R . . . . .

    def test_valid_moves(self):
        valid_moves = self.board.squares['b1,d1,e1,f1,g1,h1,c2,c3,c4,c5,c6,c7']
        self.assertCountEqual(self.rook.valid_moves(), valid_moves)

    def test_capture_free_moves(self):
        capture_free_moves = self.board.squares['b1,d1,e1,f1,g1,h1,c2,c3,c4,c5,c6']
        self.assertCountEqual(self.rook.capture_free_moves(), capture_free_moves)

    def test_captures(self):
        self.assertCountEqual(self.rook.captures(), [self.board.squares.c7])

    def test_attack_squares(self):
        attack_squares = self.board.squares['b1,d1,e1,f1,g1,h1,c2,c3,c4,c5,c6,c7']
        self.assertCountEqual(self.rook.attack_squares(), attack_squares)


if __name__ == '__main__':
    unittest.main()
