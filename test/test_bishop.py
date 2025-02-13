"""Этот модуль проверяет правильность работы класса Bishop."""

import unittest


class TestWhiteBishopInheritedTraits(unittest.TestCase):
    """Проверки основных (унаследованных от Piece) свойств и методов белого слона."""

    def setUp(self):
        from board import Board
        self.board = Board()
        self.bishop = self.board.put_white_bishop_at('a3')

    def test_bishop_is_white(self):
        self.assertTrue(self.bishop.is_white())

    def test_bishop_is_not_black(self):
        self.assertFalse(self.bishop.is_black())

    def test_color_is_right(self):
        from color import Color
        self.assertEqual(self.bishop.color, Color.WHITE)

    def test_color_is_read_only(self):
        with self.assertRaises(AttributeError):
            from color import Color
            self.bishop.color = Color.BLACK
        self.assertTrue(self.bishop.is_white())

    def test_bishop_has_not_moved(self):
        self.assertFalse(self.bishop.moved)

    def test_moved_is_read_only(self):
        with self.assertRaises(AttributeError):
            self.bishop.moved = True
        self.assertFalse(self.bishop.moved)

    def test_bishop_is_on_the_right_square(self):
        self.assertIs(self.bishop.place_at, self.board.squares['a3'])

    def test_place_at_is_read_only(self):
        with self.assertRaises(AttributeError):
            self.bishop.place_at = self.board.squares['b2']
        self.assertIs(self.bishop.place_at, self.board.squares['a3'])

    def test_bishop_is_not_pawn(self):
        self.assertFalse(self.bishop.is_pawn())

    def test_bishop_is_bishop(self):
        self.assertTrue(self.bishop.is_bishop())

    def test_bishop_is_not_king(self):
        self.assertFalse(self.bishop.is_king())

    def test_bishop_is_not_knight(self):
        self.assertFalse(self.bishop.is_knight())

    def test_bishop_is_not_queen(self):
        self.assertFalse(self.bishop.is_queen())

    def test_bishop_is_not_rook(self):
        self.assertFalse(self.bishop.is_rook())

    def test_bishop_is_on_board(self):
        self.assertTrue(self.bishop.is_onboard())

    def test_bishop_is_not_off_board(self):
        self.assertFalse(self.bishop.is_offboard())


class TestBlackBishopColor(unittest.TestCase):
    """Проверки свойства color чёрного слона."""

    def setUp(self):
        from board import Board
        self.board = Board()
        self.bishop = self.board.put_black_bishop_at('f8')

    def test_bishop_is_black(self):
        self.assertTrue(self.bishop.is_black())

    def test_bishop_is_not_white(self):
        self.assertFalse(self.bishop.is_white())

    def test_color_is_right(self):
        from color import Color
        self.assertEqual(self.bishop.color, Color.BLACK)

    def test_color_is_read_only(self):
        with self.assertRaises(AttributeError):
            from color import Color
            self.bishop.color = Color.WHITE
        self.assertTrue(self.bishop.is_black())


class TestBishopMoves(unittest.TestCase):
    """Проверки ходов слона."""

    def setUp(self):
        from board import Board
        self.board = Board()
        self.board.put_white_rook_at('a1')
        self.board.put_black_pawn_at('c7')
        self.bishop = self.board.put_white_bishop_at('e5')
        # . . . . . . . .
        # . . p . . . . .
        # . . . . . . . .
        # . . . . B . . .
        # . . . . . . . .
        # . . . . . . . .
        # . . . . . . . .
        # R . . . . . . .

    def test_valid_moves(self):
        valid_moves = self.board.squares['f6,g7,h8,f4,g3,h2,d4,c3,b2,d6,c7']
        self.assertCountEqual(self.bishop.valid_moves(), valid_moves)

    def test_capture_free_moves(self):
        capture_free_moves = self.board.squares['f6,g7,h8,f4,g3,h2,d4,c3,b2,d6']
        self.assertCountEqual(self.bishop.capture_free_moves(), capture_free_moves)

    def test_captures(self):
        self.assertCountEqual(self.bishop.captures(), [self.board.squares.c7])

    def test_attack_squares(self):
        attack_squares = self.board.squares['f6,g7,h8,f4,g3,h2,d4,c3,b2,d6,c7']
        self.assertCountEqual(self.bishop.attack_squares(), attack_squares)


if __name__ == '__main__':
    unittest.main()
