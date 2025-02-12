import unittest


class TestWhiteKingInheritedTraits(unittest.TestCase):

    def setUp(self):
        from board import Board
        self.board = Board()
        self.king = self.board.put_white_king_at('e1')

    def test_king_is_white(self):
        self.assertTrue(self.king.is_white())

    def test_king_is_not_black(self):
        self.assertFalse(self.king.is_black())

    def test_color_is_right(self):
        from color import Color
        self.assertEqual(self.king.color, Color.WHITE)

    def test_color_is_read_only(self):
        with self.assertRaises(AttributeError):
            from color import Color
            self.king.color = Color.BLACK
        self.assertTrue(self.king.is_white())

    def test_king_has_not_moved(self):
        self.assertFalse(self.king.moved)

    def test_moved_is_read_only(self):
        with self.assertRaises(AttributeError):
            self.king.moved = True
        self.assertFalse(self.king.moved)

    def test_after_move(self):
        self.king.move_to('d1')
        self.assertTrue(self.king.moved)

    def test_king_is_on_the_right_square(self):
        self.assertIs(self.king.place_at, self.board.squares.e1)

    def test_place_at_is_read_only(self):
        with self.assertRaises(AttributeError):
            self.king.place_at = self.board.squares.a1
        self.assertIs(self.king.place_at, self.board.squares.e1)

    def test_king_is_not_pawn(self):
        self.assertFalse(self.king.is_pawn())

    def test_king_is_not_bishop(self):
        self.assertFalse(self.king.is_bishop())

    def test_king_is_king(self):
        self.assertTrue(self.king.is_king())

    def test_king_is_not_knight(self):
        self.assertFalse(self.king.is_knight())

    def test_king_is_not_queen(self):
        self.assertFalse(self.king.is_queen())

    def test_king_is_not_rook(self):
        self.assertFalse(self.king.is_rook())

    def test_king_is_on_board(self):
        self.assertTrue(self.king.is_onboard())

    def test_king_is_not_off_board(self):
        self.assertFalse(self.king.is_offboard())


class TestBlackKingColor(unittest.TestCase):

    def setUp(self):
        from board import Board
        self.board = Board()
        self.king = self.board.put_black_king_at('e8')

    def test_king_is_black(self):
        self.assertTrue(self.king.is_black())

    def test_king_is_not_white(self):
        self.assertFalse(self.king.is_white())

    def test_color_is_right(self):
        from color import Color
        self.assertEqual(self.king.color, Color.BLACK)

    def test_color_is_read_only(self):
        with self.assertRaises(AttributeError):
            from color import Color
            self.king.color = Color.WHITE
        self.assertTrue(self.king.is_black())


class TestWhiteKingMoves(unittest.TestCase):

    def setUp(self):
        from board import Board
        self.board = Board()
        self.board.put_white_knight_at('b2')
        self.board.put_black_pawn_at('d4')
        self.king = self.board.put_black_king_at('c3')
        # . . . . . . . .
        # . . . . . . . .
        # . . . . . . . .
        # . . . . . . . .
        # . . . p . . . .
        # . . K . . . . .
        # . N . . . . . .
        # . . . . . . . .


    def test_valid_moves(self):
        self.assertCountEqual(self.king.valid_moves(), self.board.squares['c4,d3,d2,c2,b2,b3,b4'])

    def test_capture_free_moves(self):
        self.assertCountEqual(self.king.capture_free_moves(), self.board.squares['c4,d3,d2,c2,b3,b4'])

    def test_captures(self):
        self.assertCountEqual(self.king.captures(), [self.board.squares['b2']])


class TestWhiteKingCastling(unittest.TestCase):

    def setUp(self):
        from board import Board
        self.board = Board()
        self.queenside_rook = self.board.put_white_rook_at('a1')
        self.kingside_rook = self.board.put_white_rook_at('h1')
        self.king = self.board.put_white_king_at('e1')
        # . . . . . . . .
        # . . . . . . . .
        # . . . . . . . .
        # . . . . . . . .
        # . . . . . . . .
        # . . . . . . . .
        # . . . . . . . .
        # R . . . K . . R

    def test_valid_moves(self):
        self.assertCountEqual(self.king.valid_moves(), self.board.squares['c1,d1,d2,e2,f2,f1,g1'])

    def test_capture_free_moves(self):
        self.assertCountEqual(self.king.capture_free_moves(), self.board.squares['c1,d1,d2,e2,f2,f1,g1'])

    def test_captures(self):
        self.assertCountEqual(self.king.captures(), [])

    def test_cannot_castle_after_king_moves(self):
        self.king.move_to('e2')
        self.king.move_to('e1')
        self.assertCountEqual(self.king.valid_moves(), self.board.squares['d1,d2,e2,f2,f1'])

    def test_cannot_castle_after_kingside_rook_moves(self):
        self.kingside_rook.move_to('h8')
        self.kingside_rook.move_to('h1')
        self.assertCountEqual(self.king.valid_moves(), self.board.squares['c1,d1,d2,e2,f2,f1'])

    def test_cannot_castle_after_queenside_rook_moves(self):
        self.queenside_rook.move_to('a8')
        self.queenside_rook.move_to('a1')
        self.assertCountEqual(self.king.valid_moves(), self.board.squares['d1,d2,e2,f2,f1,g1'])

    def test_cannot_castle_when_there_is_piece_between_king_and_kingside_rook(self):
        self.board.put_white_queen_at('g1')
        # . . . . . . . .
        # . . . . . . . .
        # . . . . . . . .
        # . . . . . . . .
        # . . . . . . . .
        # . . . . . . . .
        # . . . . . . . .
        # R . . . K . Q R
        self.assertCountEqual(self.king.valid_moves(), self.board.squares['c1,d1,d2,e2,f2,f1'])

    def test_cannot_castle_when_there_is_piece_between_king_and_queenside_rook(self):
        self.board.put_white_queen_at('c1')
        # . . . . . . . .
        # . . . . . . . .
        # . . . . . . . .
        # . . . . . . . .
        # . . . . . . . .
        # . . . . . . . .
        # . . . . . . . .
        # R . Q . K . . R
        self.assertCountEqual(self.king.valid_moves(), self.board.squares['d1,d2,e2,f2,f1,g1'])


    def test_cannot_castle_when_king_is_under_check(self):
        self.board.put_black_bishop_at('b4')
        # . . . . . . . .
        # . . . . . . . .
        # . . . . . . . .
        # . . . . . . . .
        # . b . . . . . .
        # . . . . . . . .
        # . . . . . . . .
        # R . . . K . . R
        self.assertCountEqual(self.king.valid_moves(), self.board.squares['d1,d2,e2,f2,f1'])


    def test_cannot_castle_through_attacked_square(self):
        self.board.put_black_knight_at('e3')
        # . . . . . . . .
        # . . . . . . . .
        # . . . . . . . .
        # . . . . . . . .
        # . . . . . . . .
        # . . . . n . . .
        # . . . . . . . .
        # R . . . K . . R
        self.assertCountEqual(self.king.valid_moves(), self.board.squares['d1,d2,e2,f2,f1'])

    def test_cannot_castle_through_attacked_square_kingside(self):
        self.board.put_black_rook_at('g6')
        # . . . . . . . .
        # . . . . . . . .
        # . . . . . . r .
        # . . . . . . . .
        # . . . . . . . .
        # . . . . . . . .
        # . . . . . . . .
        # R . . . K . . R
        self.assertCountEqual(self.king.valid_moves(), self.board.squares['c1,d1,d2,e2,f2,f1'])

    def test_cannot_castle_through_attacked_square_queenside(self):
        self.board.put_black_queen_at('b2')
        # . . . . . . . .
        # . . . . . . . .
        # . . . . . . . .
        # . . . . . . . .
        # . . . . . . . .
        # . . . . . . . .
        # . q . . . . . .
        # R . . . K . . R
        self.assertCountEqual(self.king.valid_moves(), self.board.squares['d1,d2,e2,f2,f1,g1'])


class TestBlackKingCastling(unittest.TestCase):

    def setUp(self):
        from board import Board
        self.board = Board()
        self.queenside_rook = self.board.put_black_rook_at('a8')
        self.kingside_rook = self.board.put_black_rook_at('h8')
        self.king = self.board.put_black_king_at('e8')
        # r . . . k . . r
        # . . . . . . . .
        # . . . . . . . .
        # . . . . . . . .
        # . . . . . . . .
        # . . . . . . . .
        # . . . . . . . .
        # . . . . . . . .

    def test_valid_moves(self):
        self.assertCountEqual(self.king.valid_moves(), self.board.squares['c8,d8,d7,e7,f7,f8,g8'])

    def test_capture_free_moves(self):
        self.assertCountEqual(self.king.capture_free_moves(), self.board.squares['c8,d8,d7,e7,f7,f8,g8'])

    def test_captures(self):
        self.assertCountEqual(self.king.captures(), [])

    def test_cannot_castle_after_king_moves(self):
        self.king.move_to('e7')
        self.king.move_to('e8')
        self.assertCountEqual(self.king.valid_moves(), self.board.squares['d8,d7,e7,f7,f8'])

    def test_cannot_castle_after_kingside_rook_moves(self):
        self.kingside_rook.move_to('h1')
        self.kingside_rook.move_to('h8')
        self.assertCountEqual(self.king.valid_moves(), self.board.squares['c8,d8,d7,e7,f7,f8'])

    def test_cannot_castle_after_queenside_rook_moves(self):
        self.queenside_rook.move_to('a1')
        self.queenside_rook.move_to('a8')
        self.assertCountEqual(self.king.valid_moves(), self.board.squares['d8,d7,e7,f7,f8,g8'])

    def test_cannot_castle_when_there_is_piece_between_king_and_kingside_rook(self):
        self.board.put_black_queen_at('g8')
        # r . . . k . q r
        # . . . . . . . .
        # . . . . . . . .
        # . . . . . . . .
        # . . . . . . . .
        # . . . . . . . .
        # . . . . . . . .
        # . . . . . . . .
        self.assertCountEqual(self.king.valid_moves(), self.board.squares['c8,d8,d7,e7,f7,f8'])

    def test_cannot_castle_when_there_is_piece_between_king_and_queenside_rook(self):
        self.board.put_black_queen_at('c8')
        # r . q . k . . r
        # . . . . . . . .
        # . . . . . . . .
        # . . . . . . . .
        # . . . . . . . .
        # . . . . . . . .
        # . . . . . . . .
        # . . . . . . . .
        self.assertCountEqual(self.king.valid_moves(), self.board.squares['d8,d7,e7,f7,f8,g8'])


    def test_cannot_castle_when_king_is_under_check(self):
        self.board.put_white_bishop_at('b5')
        # r . . . k . . r
        # . . . . . . . .
        # . . . . . . . .
        # . B . . . . . .
        # . . . . . . . .
        # . . . . . . . .
        # . . . . . . . .
        # . . . . . . . .
        self.assertCountEqual(self.king.valid_moves(), self.board.squares['d8,d7,e7,f7,f8'])


    def test_cannot_castle_through_attacked_square(self):
        self.board.put_white_bishop_at('e7')
        # r . . . k . . r
        # . . . . B . . .
        # . . . . . . . .
        # . . . . . . . .
        # . . . . . . . .
        # . . . . . . . .
        # . . . . . . . .
        # . . . . . . . .
        self.assertCountEqual(self.king.valid_moves(), self.board.squares['d8,d7,e7,f7,f8'])

    def test_cannot_castle_through_attacked_square_kingside(self):
        self.board.put_white_rook_at('g6')
        # r . . . k . . r
        # . . . . . . . .
        # . . . . . . R .
        # . . . . . . . .
        # . . . . . . . .
        # . . . . . . . .
        # . . . . . . . .
        # . . . . . . . .
        self.assertCountEqual(self.king.valid_moves(), self.board.squares['c8,d8,d7,e7,f7,f8'])

    def test_cannot_castle_through_attacked_square_queenside(self):
        self.board.put_white_queen_at('b7')
        # r . . . k . . r
        # . Q . . . . . .
        # . . . . . . . .
        # . . . . . . . .
        # . . . . . . . .
        # . . . . . . . .
        # . . . . . . . .
        # . . . . . . . .
        self.assertCountEqual(self.king.valid_moves(), self.board.squares['d8,d7,e7,f7,f8,g8'])


if __name__ == '__main__':
    unittest.main()

