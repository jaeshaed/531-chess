import unittest


class TestWhitePawnInheritedTraits(unittest.TestCase):

    def setUp(self):
        from board import Board
        self.board = Board()
        self.pawn = self.board.put_white_pawn_at('e2')

    def test_pawn_is_white(self):
        self.assertTrue(self.pawn.is_white())

    def test_pawn_is_not_black(self):
        self.assertFalse(self.pawn.is_black())

    def test_color_is_right(self):
        from color import Color
        self.assertEqual(self.pawn.color, Color.WHITE)

    def test_color_is_read_only(self):
        with self.assertRaises(AttributeError):
            from color import Color
            self.pawn.color = Color.BLACK
        self.assertTrue(self.pawn.is_white())

    def test_pawn_has_not_moved(self):
        self.assertFalse(self.pawn.moved)

    def test_moved_is_read_only(self):
        with self.assertRaises(AttributeError):
            self.pawn.moved = True
        self.assertFalse(self.pawn.moved)

    def test_pawn_is_on_the_right_square(self):
        self.assertIs(self.pawn.place_at, self.board.squares['e2'])

    def test_place_at_is_read_only(self):
        with self.assertRaises(AttributeError):
            self.pawn.place_at = self.board.squares['a1']
        self.assertIs(self.pawn.place_at, self.board.squares['e2'])

    def test_pawn_is_pawn(self):
        self.assertTrue(self.pawn.is_pawn())

    def test_pawn_is_not_bishop(self):
        self.assertFalse(self.pawn.is_bishop())

    def test_pawn_is_not_king(self):
        self.assertFalse(self.pawn.is_king())

    def test_pawn_is_not_knight(self):
        self.assertFalse(self.pawn.is_knight())

    def test_pawn_is_not_queen(self):
        self.assertFalse(self.pawn.is_queen())

    def test_pawn_is_not_rook(self):
        self.assertFalse(self.pawn.is_rook())

    def test_pawn_is_on_board(self):
        self.assertTrue(self.pawn.is_onboard())

    def test_pawn_is_not_off_board(self):
        self.assertFalse(self.pawn.is_offboard())


class TestBlackPawnColor(unittest.TestCase):

    def setUp(self):
        from board import Board
        self.board = Board()
        self.pawn = self.board.put_black_pawn_at('e7')

    def test_pawn_is_black(self):
        self.assertTrue(self.pawn.is_black())

    def test_pawn_is_not_white(self):
        self.assertFalse(self.pawn.is_white())

    def test_color_is_right(self):
        from color import Color
        self.assertEqual(self.pawn.color, Color.BLACK)

    def test_color_is_read_only(self):
        with self.assertRaises(AttributeError):
            from color import Color
            self.pawn.color = Color.WHITE
        self.assertTrue(self.pawn.is_black())


class TestWhitePawnAtInitialPosition(unittest.TestCase):

    def setUp(self):
        from board import Board
        self.board = Board()
        self.pawn = self.board.put_white_pawn_at('f2')

    def test_valid_moves(self):
        self.assertCountEqual(self.pawn.valid_moves(), [self.board.squares.f3, self.board.squares.f4])

    def test_capture_free_moves(self):
        self.assertCountEqual(self.pawn.capture_free_moves(), self.board.squares['f3,f4'])

    def test_attack_squares(self):
        self.assertCountEqual(self.pawn.attack_squares(), [])

    def test_move_direction_is_up(self):
        from pawn import MoveDirection
        self.assertEqual(self.pawn.move_direction, MoveDirection.UP)

    def test_move_direction_is_read_only(self):
        from pawn import MoveDirection
        with self.assertRaises(AttributeError):
            self.pawn.move_direction = MoveDirection.DOWN
        self.assertEqual(self.pawn.move_direction, MoveDirection.UP)

    def test_pawn_is_not_promoted(self):
        self.assertFalse(self.pawn.promoted)

    def test_promoted_is_read_only(self):
        with self.assertRaises(AttributeError):
            self.pawn.promoted = True
        self.assertFalse(self.pawn.promoted)

    def test_after_move(self):
        self.pawn.move_to('f4')
        self.assertTrue(self.pawn.moved)


class TestBlackPawnAtInitialPosition(unittest.TestCase):

    def setUp(self):
        from board import Board
        self.board = Board()
        self.board.put_white_bishop_at('F6')
        self.board.put_white_pawn_at('H6')
        self.board.put_black_queen_at('G5')
        self.pawn = self.board.put_black_pawn_at('G7')
        # . . . . . . . .
        # . . . . . . p .
        # . . . . . B . P
        # . . . . . . q .
        # . . . . . . . .
        # . . . . . . . .
        # . . . . . . . .
        # . . . . . . . .

    def test_valid_moves(self):
        valid_moves = [self.board.squares.F6, self.board.squares.G6, self.board.squares.H6]
        self.assertCountEqual(self.pawn.valid_moves(), valid_moves)

    def test_capture_free_moves(self):
        self.assertCountEqual(self.pawn.capture_free_moves(), [self.board.squares.G6])

    def test_attack_squares(self):
        self.assertCountEqual(self.pawn.attack_squares(), self.board.squares['F6,H6'])

    def test_move_direction_is_down(self):
        from pawn import MoveDirection
        self.assertEqual(self.pawn.move_direction, MoveDirection.DOWN)

    def test_after_move(self):
        self.pawn.move_to('G5')
        self.assertTrue(self.pawn.moved)


class TestWhitePawnPromotionBasics(unittest.TestCase):

    def setUp(self):
        from board import Board
        self.board = Board()
        self.pawn = self.board.put_white_pawn_at('h7')

    def test_pawn_is_not_promoted(self):
        self.assertFalse(self.pawn.promoted)

    def test_promoted_is_read_only(self):
        with self.assertRaises(AttributeError):
            self.pawn.promoted = True
        self.assertFalse(self.pawn.promoted)

    def test_pawn_cannot_promote_until_reached_last_rank(self):
        with self.assertRaises(RuntimeError):
            from piece_type import PieceType
            self.pawn.promote_to(PieceType.QUEEN)
        self.assertFalse(self.pawn.promoted)

    def test_promotion_works_after_last_rank_is_reached(self):
        self.pawn.move_to('h8')
        self.pawn.promote_to_queen()
        self.assertTrue(self.pawn.promoted)

    def test_pawn_cannot_promote_to_pawn(self):
        self.pawn.move_to('h8')
        with self.assertRaises(ValueError):
            from piece_type import PieceType
            self.pawn.promote_to(PieceType.PAWN)
        self.assertFalse(self.pawn.promoted)

    def test_pawn_cannot_promote_to_king(self):
        self.pawn.move_to('h8')
        with self.assertRaises(ValueError):
            from piece_type import PieceType
            self.pawn.promote_to(PieceType.KING)
        self.assertFalse(self.pawn.promoted)


class TestBlackPawnPromotionBasics(unittest.TestCase):

    def setUp(self):
        from board import Board
        self.board = Board()
        self.pawn = self.board.put_black_pawn_at('a2')

    def test_pawn_cannot_promote_until_reached_last_rank(self):
        with self.assertRaises(RuntimeError):
            from piece_type import PieceType
            self.pawn.promote_to(PieceType.QUEEN)
        self.assertFalse(self.pawn.promoted)

    def test_promotion_works_after_last_rank_is_reached(self):
        self.pawn.move_to('a1')
        self.pawn.promote_to_queen()
        self.assertTrue(self.pawn.promoted)


class TestWhitePawnPromotionToBishop(unittest.TestCase):

    def setUp(self):
        from board import Board
        self.board = Board()
        self.board.put_black_rook_at('d6')
        self.pawn = self.board.put_white_pawn_at('b7')
        # . . . . . . . .
        # . P . . . . . .
        # . . . r . . . .
        # . . . . . . . .
        # . . . . . . . .
        # . . . . . . . .
        # . . . . . . . .
        # . . . . . . . .
        self.pawn.move_to('b8')
        self.pawn.promote_to_bishop()

    def test_pawn_was_promoted(self):
        self.assertTrue(self.pawn.promoted)

    def test_pawn_is_not_pawn(self):
        self.assertFalse(self.pawn.is_pawn())

    def test_pawn_is_bishop(self):
        self.assertTrue(self.pawn.is_bishop())

    def test_pawn_is_not_king(self):
        self.assertFalse(self.pawn.is_king())

    def test_pawn_is_not_knight(self):
        self.assertFalse(self.pawn.is_knight())

    def test_pawn_is_not_queen(self):
        self.assertFalse(self.pawn.is_queen())

    def test_pawn_is_not_rook(self):
        self.assertFalse(self.pawn.is_rook())

    def test_valid_moves(self):
        self.assertCountEqual(self.pawn.valid_moves(), self.board.squares['a7,c7,d6'])

    def test_capture_free_moves(self):
        self.assertCountEqual(self.pawn.capture_free_moves(), self.board.squares['a7,c7'])

    def test_attack_squares(self):
        self.assertCountEqual(self.pawn.attack_squares(), [self.board.squares.d6])


class TestBlackPawnPromotionToKnight(unittest.TestCase):

    def setUp(self):
        from board import Board
        self.board = Board()
        self.board.put_black_king_at('b3')
        self.board.put_white_king_at('e2')
        self.pawn = self.board.put_black_pawn_at('c2')
        # . . . . . . . .
        # . . . . . . . .
        # . . . . . . . .
        # . . . . . . . .
        # . . . . . . . .
        # . k . . . . . .
        # . . p . K . . .
        # . . . . . . . .
        self.pawn.move_to('c1')
        self.pawn.promote_to_knight()

    def test_pawn_was_promoted(self):
        self.assertTrue(self.pawn.promoted)

    def test_pawn_is_not_pawn(self):
        self.assertFalse(self.pawn.is_pawn())

    def test_pawn_is_not_bishop(self):
        self.assertFalse(self.pawn.is_bishop())

    def test_pawn_is_not_king(self):
        self.assertFalse(self.pawn.is_king())

    def test_pawn_is_knight(self):
        self.assertTrue(self.pawn.is_knight())

    def test_pawn_is_not_queen(self):
        self.assertFalse(self.pawn.is_queen())

    def test_pawn_is_not_rook(self):
        self.assertFalse(self.pawn.is_rook())

    def test_valid_moves(self):
        self.assertCountEqual(self.pawn.valid_moves(), self.board.squares['a2,d3,e2'])

    def test_capture_free_moves(self):
        self.assertCountEqual(self.pawn.capture_free_moves(), self.board.squares['a2,d3'])

    def test_attack_squares(self):
        self.assertCountEqual(self.pawn.attack_squares(), [self.board.squares.e2])


class TestWhitePawnPromotionToQueen(unittest.TestCase):

    def setUp(self):
        from board import Board
        self.board = Board()
        self.board.put_black_bishop_at('b6')
        self.board.put_black_knight_at('h8')
        self.board.put_black_king_at('g5')
        self.board.put_white_king_at('d1')
        self.pawn = self.board.put_white_pawn_at('d7')
        # . . . . . . . n
        # . . . P . . . .
        # . b . . . . . .
        # . . . . . . k .
        # . . . . . . . .
        # . . . . . . . .
        # . . . . . . . .
        # . . . K . . . .
        self.pawn.move_to('d8')
        self.pawn.promote_to_queen()

    def test_pawn_was_promoted(self):
        self.assertTrue(self.pawn.promoted)

    def test_pawn_is_not_pawn(self):
        self.assertFalse(self.pawn.is_pawn())

    def test_pawn_is_not_bishop(self):
        self.assertFalse(self.pawn.is_bishop())

    def test_pawn_is_not_king(self):
        self.assertFalse(self.pawn.is_king())

    def test_pawn_is_not_knight(self):
        self.assertFalse(self.pawn.is_knight())

    def test_pawn_is_queen(self):
        self.assertTrue(self.pawn.is_queen())

    def test_pawn_is_not_rook(self):
        self.assertFalse(self.pawn.is_rook())

    def test_valid_moves(self):
        valid_moves = self.board.squares['a8,b8,c8,e8,f8,g8,h8,b6,c7,e7,f6,g5,d7,d6,d5,d4,d3,d2']
        self.assertCountEqual(self.pawn.valid_moves(), valid_moves)

    def test_capture_free_moves(self):
        capture_free_moves = self.board.squares['a8,b8,c8,e8,f8,g8,c7,e7,f6,d7,d6,d5,d4,d3,d2']
        self.assertCountEqual(self.pawn.capture_free_moves(), capture_free_moves)

    def test_attack_squares(self):
        self.assertCountEqual(self.pawn.attack_squares(), self.board.squares['b6,h8,g5'])



class TestBlackPawnPromotionToRook(unittest.TestCase):

    def setUp(self):
        from board import Board
        self.board = Board()
        self.board.put_black_king_at('f1')
        self.board.put_white_king_at('d6')
        self.board.put_white_rook_at('a1')
        self.pawn = self.board.put_black_pawn_at('e2')
        # . . . . . . . .
        # . . . . . . . .
        # . . . K . . . .
        # . . . . . . . .
        # . . . . . . . .
        # . . . . . . . .
        # . . . . p . . .
        # R . . . . k . .
        self.pawn.move_to('e1')
        self.pawn.promote_to_rook()

    def test_pawn_was_promoted(self):
        self.assertTrue(self.pawn.promoted)

    def test_pawn_is_not_pawn(self):
        self.assertFalse(self.pawn.is_pawn())

    def test_pawn_is_not_bishop(self):
        self.assertFalse(self.pawn.is_bishop())

    def test_pawn_is_not_king(self):
        self.assertFalse(self.pawn.is_king())

    def test_pawn_is_not_knight(self):
        self.assertFalse(self.pawn.is_knight())

    def test_pawn_is_not_queen(self):
        self.assertFalse(self.pawn.is_queen())

    def test_pawn_is_rook(self):
        self.assertTrue(self.pawn.is_rook())

    def test_valid_moves(self):
        self.assertCountEqual(self.pawn.valid_moves(), self.board.squares['a1,b1,c1,d1,e2,e3,e4,e5,e6,e7,e8'])

    def test_capture_free_moves(self):
        self.assertCountEqual(self.pawn.capture_free_moves(), self.board.squares['b1,c1,d1,e2,e3,e4,e5,e6,e7,e8'])

    def test_attack_squares(self):
        self.assertCountEqual(self.pawn.attack_squares(), [self.board.squares.a1])


class TestWhitePawnEnPassantCapture(unittest.TestCase):

    def setUp(self):
        from board import Board
        self.board = Board()
        self.black_pawn = self.board.put_black_pawn_at('g7')
        self.white_pawn = self.board.put_white_pawn_at('f5')
        # . . . . . . . .
        # . . . . . . p .
        # . . . . . . . .
        # . . . . . P . .
        # . . . . . . . .
        # . . . . . . . .
        # . . . . . . . .
        # . . . . . . . .
        self.black_pawn.move_to('g5')

    def test_black_pawn_has_advanced_twice(self):
        self.assertTrue(self.black_pawn.double_step)

    def test_white_pawn_has_not(self):
        self.assertFalse(self.white_pawn.double_step)

    def test_white_pawn_attack_squares(self):
        self.assertCountEqual(self.white_pawn.attack_squares(), [self.board.squares.g6])

    def test_white_pawn_valid_moves(self):
        self.assertCountEqual(self.white_pawn.valid_moves(), self.board.squares['f6,g6'])


class TestBlackPawnEnPassantCapture(unittest.TestCase):

    def setUp(self):
        from board import Board
        self.board = Board()
        self.black_pawn = self.board.put_black_pawn_at('h4')
        self.white_pawn = self.board.put_white_pawn_at('g2')
        # . . . . . . . .
        # . . . . . . . .
        # . . . . . . . .
        # . . . . . . . .
        # . . . . . . . p
        # . . . . . . . .
        # . . . . . . P .
        # . . . . . . . .
        self.white_pawn.move_to('g4')

    def test_white_pawn_has_advanced_twice(self):
        self.assertTrue(self.white_pawn.double_step)

    def test_black_pawn_has_not(self):
        self.assertFalse(self.black_pawn.double_step)

    def test_black_pawn_attack_squares(self):
        self.assertCountEqual(self.black_pawn.attack_squares(), [self.board.squares.g3])

    def test_black_pawn_valid_moves(self):
        self.assertCountEqual(self.black_pawn.valid_moves(), self.board.squares['h3,g3'])


if __name__ == '__main__':
    unittest.main()

