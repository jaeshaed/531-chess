"""Этот модуль проверяет правильность работы класса Knights."""

import unittest


class TestWhiteKnightInheritedTraits(unittest.TestCase):
    """Проверки основных (унаследованных от Piece) свойств и методов белого коня."""

    def setUp(self):
        from board import Board
        self.board = Board()
        self.knight = self.board.put_white_knight_at('d5')

    def test_knight_is_white(self):
        self.assertTrue(self.knight.is_white())

    def test_knight_is_not_black(self):
        self.assertFalse(self.knight.is_black())

    def test_color_is_right(self):
        from color import Color
        self.assertEqual(self.knight.color, Color.WHITE)

    def test_color_is_read_only(self):
        with self.assertRaises(AttributeError):
            from color import Color
            self.knight.color = Color.BLACK
        self.assertTrue(self.knight.is_white())

    def test_knight_has_not_moved(self):
        self.assertFalse(self.knight.moved)

    def test_moved_is_read_only(self):
        with self.assertRaises(AttributeError):
            self.knight.moved = True
        self.assertFalse(self.knight.moved)

    def test_knight_is_on_the_right_square(self):
        self.assertIs(self.knight.place_at, self.board.squares['d5'])

    def test_place_at_is_read_only(self):
        with self.assertRaises(AttributeError):
            self.knight.place_at = self.board.squares['h8']
        self.assertIs(self.knight.place_at, self.board.squares['d5'])

    def test_knight_is_not_pawn(self):
        self.assertFalse(self.knight.is_pawn())

    def test_knight_is_not_bishop(self):
        self.assertFalse(self.knight.is_bishop())

    def test_knight_is_not_king(self):
        self.assertFalse(self.knight.is_king())

    def test_knight_is_knight(self):
        self.assertTrue(self.knight.is_knight())

    def test_knight_is_not_queen(self):
        self.assertFalse(self.knight.is_queen())

    def test_knight_is_not_rook(self):
        self.assertFalse(self.knight.is_rook())

    def test_knight_is_on_board(self):
        self.assertTrue(self.knight.is_onboard())

    def test_knight_is_not_off_board(self):
        self.assertFalse(self.knight.is_offboard())


class TestBlackKnightColor(unittest.TestCase):
    """Проверки свойства color чёрного коня."""

    def setUp(self):
        from board import Board
        self.board = Board()
        self.knight = self.board.put_black_knight_at('g3')

    def test_knight_is_black(self):
        self.assertTrue(self.knight.is_black())

    def test_knight_is_not_white(self):
        self.assertFalse(self.knight.is_white())

    def test_color_is_right(self):
        from color import Color
        self.assertEqual(self.knight.color, Color.BLACK)

    def test_color_is_read_only(self):
        with self.assertRaises(AttributeError):
            from color import Color
            self.knight.color = Color.WHITE
        self.assertTrue(self.knight.is_black())


class TestKnightMoves(unittest.TestCase):
    """Проверки ходов коня."""

    def setUp(self):
        from board import Board
        self.board = Board()
        self.board.put_white_knight_at('f6')
        self.board.put_black_pawn_at('g3')
        self.knight = self.board.put_black_knight_at('e4')
        # . . . . . . . .
        # . . . . . . . .
        # . . . . . N . .
        # . . . . . . . .
        # . . . . n . . .
        # . . . . . . p .
        # . . . . . . . .
        # . . . . . . . .

    def test_valid_moves(self):
        valid_moves = self.board.squares['f6,g5,f2,d2,c3,c5,d6']
        self.assertCountEqual(self.knight.valid_moves(), valid_moves)

    def test_capture_free_moves(self):
        capture_free_moves = self.board.squares['g5,f2,d2,c3,c5,d6']
        self.assertCountEqual(self.knight.capture_free_moves(), capture_free_moves)

    def test_captures(self):
        self.assertCountEqual(self.knight.captures(), [self.board.squares.f6])

    def test_attack_squares(self):
        attack_squares = self.board.squares['f6,g5,f2,d2,c3,c5,d6']
        self.assertCountEqual(self.knight.attack_squares(), attack_squares)

    def test_after_move(self):
        self.assertFalse(self.board.squares.f6.piece.moved)
        self.knight.move_to('f6')
        self.assertTrue(self.board.squares.f6.piece.moved)


class TestKnightMovesAtBoardEdge(unittest.TestCase):
    """Проверки ходов коня, стоящего у края доски."""

    def setUp(self):
        from board import Board
        self.board = Board()
        self.knight = self.board.put_white_knight_at('h7')

    def test_valid_moves(self):
        self.assertCountEqual(self.knight.valid_moves(), self.board.squares['g5,f6,f8'])

    def test_capture_free_moves(self):
        self.assertCountEqual(self.knight.capture_free_moves(), self.board.squares['g5,f6,f8'])

    def test_captures(self):
        self.assertCountEqual(self.knight.captures(), [])

    def test_attack_squares(self):
        self.assertCountEqual(self.knight.attack_squares(), self.board.squares['g5,f6,f8'])


if __name__ == '__main__':
    unittest.main()
